from flask import render_template, redirect, url_for, flash, request, jsonify
from app import app
from datetime import datetime, timedelta
import os
import sys
import json
import subprocess
import time
import importlib.util
import threading
import signal
import requests
import re
import logging
import shutil
import glob

#######################################################
# INITIALIZATION AND CONFIGURATION
#######################################################

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Add the python directory to the path
sys.path.append(os.path.join(project_root, 'python'))
from blockclock import BlockClockControl, setup_logging

# Set up the logger with the central log file path
log_file_path = os.path.join(project_root, 'logs', 'blockclock.log')
logger = setup_logging(log_file_path)

# Log that the routes module is initialized
#logger.info("🚀 Routes module initialized - logging configured to: %s", log_file_path)

# Global variables
blockclock_instance = None
rotation_thread = None
rotation_active = False
rotation_lock = threading.Lock()
monitoring_active = False
monitoring_message = ""
monitoring_start_time = 0
log_buffer = []
log_lock = threading.Lock()
blockclock_process = None
first_refresh_detected = False
last_manual_text_time = 0
RATE_LIMIT_SECONDS = 70  # Minimum time between manual text submissions (70 seconds)

#######################################################
# LOG ROTATION FUNCTIONS
#######################################################

def rotate_logs():
    """Rotate logs: archive logs older than configured days or if they exceed the size limit"""
    try:
        # Load configuration
        config = load_config()
        archive_days = config.get('log_archive_days', 1)
        archive_size_mb = config.get('log_archive_size', 10)
        delete_days = config.get('log_delete_days', 14)
        
        # Configuration using central log directories
        log_dir = os.path.join(project_root, 'logs')
        archive_dir = os.path.join(log_dir, 'archive')
        main_log = os.path.join(log_dir, 'blockclock.log')
        
        # Ensure directories exist
        os.makedirs(log_dir, exist_ok=True)
        os.makedirs(archive_dir, exist_ok=True)
        
        # Current time
        now = datetime.now()
        
        # Step 1: Archive the current log file if it's older than X days OR larger than Y MB
        if os.path.exists(main_log) and os.path.getsize(main_log) > 0:
            # Check if log file needs to be archived based on age
            log_mod_time = datetime.fromtimestamp(os.path.getmtime(main_log))
            log_age_days = (now - log_mod_time).days
            
            # Check if log file needs to be archived based on size
            log_size_mb = os.path.getsize(main_log) / (1024 * 1024)
            
            if log_age_days >= archive_days or log_size_mb >= archive_size_mb:
                # Archive the log file with timestamp
                timestamp = log_mod_time.strftime('%Y%m%d_%H%M%S')
                archive_name = f"blockclock_{timestamp}.log"
                archive_path = os.path.join(archive_dir, archive_name)
                
                logger.info(f"🗄️ Archiving log file to archive/{archive_name}")
                
                # Copy existing log to archive
                shutil.copy2(main_log, archive_path)
                
                # Clear the main log file
                with open(main_log, 'w') as f:
                    f.write(f"# Log file archived at {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"# Previous logs moved to archive/{archive_name}\n\n")
                
                if log_age_days >= archive_days:
                    logger.info(f"✅ Log archived based on age (over {archive_days} days old)")
                else:
                    logger.info(f"✅ Log archived based on size (over {archive_size_mb} MB)")
        
        # Step 2: Delete archived logs older than configured days
        cutoff_date = now - timedelta(days=delete_days)
        archived_logs = glob.glob(os.path.join(archive_dir, 'blockclock_*.log'))
        deleted_count = 0
        
        for log_file in archived_logs:
            try:
                # Extract timestamp from filename
                filename = os.path.basename(log_file)
                if '_' in filename:
                    timestamp_str = filename.split('_')[1].split('.')[0]
                    try:
                        file_date = datetime.strptime(timestamp_str, '%Y%m%d_%H%M%S')
                    except ValueError:
                        # Try alternate format if the first one fails
                        file_date = datetime.strptime(timestamp_str, '%Y%m%d')
                    
                    # Delete if older than cutoff
                    if file_date < cutoff_date:
                        os.remove(log_file)
                        deleted_count += 1
            except Exception as e:
                logger.error(f"❌ Error processing {log_file}: {str(e)}")
        
        if deleted_count > 0:
            logger.info(f"🧹 Deleted {deleted_count} archived logs older than {delete_days} days")
            
        return True
    except Exception as e:
        logger.error(f"❌ Error during log rotation: {str(e)}")
        return False

def scheduled_log_rotation():
    """Background thread for scheduled log rotation"""
    while True:
        try:
            # Check log file size every hour
            time.sleep(1 * 60 * 60)
            
            # Load configuration to get current settings
            config = load_config()
            archive_size_mb = config.get('log_archive_size', 10)
            
            # Get log file path from central location
            log_file = os.path.join(project_root, 'logs', 'blockclock.log')
            
            # If log file is larger than configured size, rotate immediately
            if os.path.exists(log_file):
                log_size_mb = os.path.getsize(log_file) / (1024 * 1024)
                if log_size_mb >= archive_size_mb:
                    logger.info(f"🔄 Log file has grown large ({int(log_size_mb)}MB), performing rotation")
                    rotate_logs()
                else:
                    # Otherwise check if 6 hours have passed since last rotation
                    if getattr(scheduled_log_rotation, 'last_rotation', 0) + 6 * 60 * 60 < time.time():
                        rotate_logs()
                        scheduled_log_rotation.last_rotation = time.time()
                    
        except Exception as e:
            logger.error(f"❌ Error in scheduled log rotation: {str(e)}")



#######################################################
# PROCESS MANAGEMENT FUNCTIONS
#######################################################

def kill_all_blockclock_processes():
    """Kill all blockclock processes using the same approach as the startup script"""
    try:
        # Use pkill -f blockclock to kill all processes with blockclock in the command line
        logger.info("🧹 Cleaning up any existing blockclock processes")
        subprocess.run(["pkill", "-f", "blockclock"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Give processes a moment to terminate
        time.sleep(1)
        
        # Check if any processes are still hanging and force kill if needed
        result = subprocess.run(["pgrep", "-f", "blockclock"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:  # Processes still exist
            logger.info("⚠️ Some processes still hanging, forcefully terminating")
            subprocess.run(["pkill", "-9", "-f", "blockclock"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        logger.info("✅ Cleanup complete")
        return True
    except Exception as e:
        logger.error(f"⚠️ Error cleaning up processes: {str(e)}")
        return False

def start_rotation():
    """Start the text rotation as a separate process"""
    global blockclock_process, rotation_active, monitoring_active, monitoring_message, monitoring_start_time, first_refresh_detected
    
    with rotation_lock:
        if rotation_active:
            return False
        
        try:
            # Add blank lines and restart message
            logger.info("")
            logger.info("==================================================")
            logger.info("🔄 FRESH RESTART - Starting Satoshi Shuffle")
            logger.info("==================================================")
            logger.info("")

            # Reset the first refresh detected flag
            first_refresh_detected = False
            
            # Path to the Python script using project root
            script_path = os.path.join(project_root, 'python', 'blockclock.py')
            
            # Config file path
            config_file = app.config['DEFAULT_CONFIG_FILE']
            
            # Start the process
            blockclock_process = subprocess.Popen(['python3', script_path, config_file])
            
            # Set flag to indicate rotation is active
            rotation_active = True
            
            # Set initial monitoring status
            monitoring_active = True
            monitoring_message = "⏳ Waiting for first refresh to synchronize..."
            monitoring_start_time = time.time()
            
            # Start monitoring logs
            monitor_logs()
            
            return True
        except Exception as e:
            logger.error(f"❌ Error starting rotation: {str(e)}")
            return False

def stop_rotation():
    """Stop the text rotation process"""
    global blockclock_process, rotation_active, monitoring_active
    
    with rotation_lock:
        # Kill all blockclock processes
        kill_all_blockclock_processes()
        
        # Reset global state
        blockclock_process = None
        rotation_active = False
        monitoring_active = False
        
        return True

#######################################################
# MONITORING FUNCTIONS
#######################################################

def update_monitoring(active=False, message=""):
    """Update monitoring status"""
    global monitoring_active, monitoring_message, monitoring_start_time
    
    monitoring_active = active
    if active:
        monitoring_message = message
        monitoring_start_time = time.time()
    
    #logger.info(f"Monitoring status updated: active={active}, message={message}")

def run_rotation():
    """Run the rotation in a separate thread"""
    global blockclock_instance, rotation_active
    
    try:
        blockclock_instance.run()
    except Exception as e:
        logger.error(f"❌ Error in rotation thread: {str(e)}")
    finally:
        with rotation_lock:
            rotation_active = False

def monitor_logs():
    """Monitor logs for refresh waiting status"""
    global rotation_active, monitoring_active, monitoring_message, monitoring_start_time
    
    # Use only the central log file location
    log_path = os.path.join(project_root, 'logs', 'blockclock.log')
    
    if not os.path.exists(log_path):
        logger.error(f"❌ Log file not found at {log_path}")
        return
    
    # Start the monitor_logs thread
    threading.Thread(target=_monitor_logs_thread, args=(log_path,), daemon=True).start()

# Find the _monitor_logs_thread function in routes.py and replace it with this version:

def _monitor_logs_thread(log_path):
    """Background thread to monitor logs"""
    global rotation_active, monitoring_active, monitoring_message
    global monitoring_start_time, first_refresh_detected
    
    last_size = 0
    last_matched_pattern = ""  # Track the last pattern we matched
    last_refresh_number = 0  # Track the last refresh number we detected
    
    # Do NOT set monitoring message here - it should be set in start_rotation()
    
    while rotation_active:
        try:
            # Check if file exists and has changed
            if os.path.exists(log_path):
                current_size = os.path.getsize(log_path)
                
                # Check log only if it has changed
                if current_size != last_size:
                    with open(log_path, 'r') as f:
                        log_content = f.read()
                        
                        # Check for first refresh detection (only if not already detected)
                        if not first_refresh_detected:
                            initial_refresh_patterns = [
                                "First refresh detected after",
                                "BlockClock refresh 1/",
                                "Display changed after"
                            ]
                            
                            for pattern in initial_refresh_patterns:
                                if pattern in log_content:
                                    first_refresh_detected = True
                                    logger.info(f"First refresh detected - text sending enabled")
                                    
                                    # Reset the monitoring start time when refresh is detected
                                    monitoring_start_time = time.time()
                                    
                                    # Update monitoring message for initial sync completion
                                    monitoring_message = " ⏳  Waiting for first Refresh  🔍"
                                    
                                    # Set as last matched pattern
                                    last_matched_pattern = pattern
                                    break
                        else:
                            # Already in sync, get only the newly added content
                            new_content = log_content[-min(5000, current_size - last_size):]
                            
                            # First check for individual refresh changes
                            refresh_match = re.search(r'BlockClock refresh (\d+)/(\d+)', new_content)
                            if refresh_match:
                                current_refresh = int(refresh_match.group(1))
                                total_refreshes = int(refresh_match.group(2))
                                
                                # Only reset if this is a new refresh number
                                if current_refresh != last_refresh_number:
                                    logger.info(f"Individual refresh detected: {current_refresh}/{total_refreshes} (timer reset)")
                                    monitoring_start_time = time.time()
                                    monitoring_message = f"🔄 Monitoring refresh {current_refresh}/{total_refreshes}"
                                    last_refresh_number = current_refresh
                            
                            # Then check for other cycle patterns
                            cycle_patterns = {
                                "Sleeping before refresh #": "🔄 Monitoring BlockClock refresh cycles",
                                "Actively monitoring for refresh #": "🔍 Actively monitoring for refresh",
                                "Final refresh complete": "✅ Refresh cycle complete",
                                "Sending new Custom Text": "📤 Sending custom text"
                            }
                            
                            for pattern, message in cycle_patterns.items():
                                # Only update if we find a pattern in new content and it's different from last match
                                if pattern in new_content and pattern != last_matched_pattern:
                                    # Reset timer and update message for this phase
                                    monitoring_start_time = time.time()
                                    monitoring_message = message
                                    logger.info(f"Monitoring phase changed: {message} (timer reset)")
                                    
                                    # If this is a new cycle starting, reset the refresh number counter
                                    if pattern == "Sleeping before refresh #":
                                        last_refresh_number = 0
                                    
                                    # Set as last matched pattern
                                    last_matched_pattern = pattern
                                    break
                    
                    last_size = current_size
            
            # Wait before checking again
            time.sleep(1)
        except Exception as e:
            logger.error(f"❌ Error monitoring logs: {str(e)}")
            time.sleep(5)  # Wait longer on error
            

#######################################################
# CONFIGURATION FUNCTIONS
#######################################################

def check_rate_limit():
    """Check if enough time has passed since the last manual text submission"""
    global last_manual_text_time
    current_time = time.time()
    time_since_last = current_time - last_manual_text_time
    
    if time_since_last < RATE_LIMIT_SECONDS:
        # Rate limit exceeded, return remaining wait time
        return False, RATE_LIMIT_SECONDS - time_since_last
    
    # Rate limit not exceeded
    return True, 0


@app.route('/backup_config')
def backup_config():
    """Generate a backup of the current configuration"""
    try:
        # Load current configuration
        config = load_config()
        
        # Add version information for compatibility checking
        backup_data = {
            'version': '1.0',
            'timestamp': datetime.now().isoformat(),
            'config': config
        }
        
        return jsonify({
            'success': True,
            'data': backup_data
        })
    except Exception as e:
        logger.error(f"❌ Error creating backup: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        })

@app.route('/restore_config', methods=['POST'])
def restore_config():
    """Restore configuration from a backup file"""
    try:
        data = request.json
        backup = data.get('backup', {})
        
        # Validate backup format
        if not backup or 'version' not in backup or 'config' not in backup:
            return jsonify({
                'success': False,
                'message': 'Invalid backup format'
            })
        
        # Check version compatibility (for future version checks)
        backup_version = backup.get('version')
        if backup_version not in ['1.0']:
            return jsonify({
                'success': False,
                'message': f'Unsupported backup version: {backup_version}'
            })
        
        # Extract configuration
        config_data = backup.get('config', {})
        
        # Validate essential configuration components
        if 'devices' not in config_data or 'text_options' not in config_data:
            return jsonify({
                'success': False,
                'message': 'Backup is missing essential configuration components'
            })
        
        # Stop rotation if active
        if rotation_active:
            stop_rotation()
            
        # Save the restored configuration
        save_config(config_data)
        
        # Log the restoration
        logger.info(f"✅ Configuration restored from backup created on {backup.get('timestamp', 'unknown date')}")
        
        return jsonify({
            'success': True,
            'message': 'Configuration restored successfully'
        })
    except Exception as e:
        logger.error(f"❌ Error restoring configuration: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        })


def load_config():
    """Load configuration from file"""
    config_file = app.config['DEFAULT_CONFIG_FILE']
    
    # Create default config if it doesn't exist
    if not os.path.exists(config_file):
        create_default_config()
    
    # Parse config file
    devices = []
    text_options = []
    clock_refresh_time = 300
    displays_between_text = 3
    
    # Default log settings
    log_archive_days = 1  # Archive logs after 1 day
    log_archive_size = 10  # Archive logs when they reach 10MB
    log_delete_days = 30  # Delete archived logs after 30 days
    
    try:
        with open(config_file, 'r') as f:
            config_content = f.read()
            
        # Parse devices
        for i in range(1, 6):  # Check for up to 5 devices
            device_name_key = f"DEVICE_{i}_NAME"
            device_ip_key = f"DEVICE_{i}_IP"
            device_password_key = f"DEVICE_{i}_PASSWORD"
            
            name_match = device_name_key + '="([^"]*)"'
            ip_match = device_ip_key + '="?([^"]*)"?'
            password_match = device_password_key + '="?([^"]*)"?'
            
            name = re.search(name_match, config_content)
            ip = re.search(ip_match, config_content)
            password = re.search(password_match, config_content)
            
            if ip and ip.group(1).strip():
                device = {
                    'id': i,
                    'name': name.group(1) if name else f"Device {i}",
                    'ip': ip.group(1),
                    'password': password.group(1) if password else ""
                }
                devices.append(device)
        
        # Parse text options
        text_match = r'TEXT_OPTIONS=\(([^)]*)\)'
        match = re.search(text_match, config_content)
        if match:
            text_part = match.group(1)
            # Extract quoted strings
            text_options = re.findall(r'"([^"]*)"', text_part)
        
        # Parse timing settings
        refresh_match = r'CLOCK_REFRESH_TIME=(\d+)'
        match = re.search(refresh_match, config_content)
        if match:
            clock_refresh_time = int(match.group(1))
        
        displays_match = r'DISPLAYS_BETWEEN_TEXT=(\d+)'
        match = re.search(displays_match, config_content)
        if match:
            displays_between_text = int(match.group(1))
            
        # Parse log settings
        log_archive_days_match = r'LOG_ARCHIVE_DAYS=(\d+)'
        match = re.search(log_archive_days_match, config_content)
        if match:
            log_archive_days = int(match.group(1))
        
        log_archive_size_match = r'LOG_ARCHIVE_SIZE=(\d+)'
        match = re.search(log_archive_size_match, config_content)
        if match:
            log_archive_size = int(match.group(1))
        
        log_delete_days_match = r'LOG_DELETE_DAYS=(\d+)'
        match = re.search(log_delete_days_match, config_content)
        if match:
            log_delete_days = int(match.group(1))
            
    except Exception as e:
        logger.error(f"❌ Error parsing config: {str(e)}")
    
    return {
        'devices': devices,
        'text_options': text_options,
        'clock_refresh_time': clock_refresh_time,
        'displays_between_text': displays_between_text,
        'log_archive_days': log_archive_days,
        'log_archive_size': log_archive_size,
        'log_delete_days': log_delete_days
    }


def create_default_config():
    """Create a default configuration file"""
    config_file = app.config['DEFAULT_CONFIG_FILE']
    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    
    with open(config_file, 'w') as f:
        f.write('''# BlockClock Text Rotation Script - Configuration File
# ==========================================================
# Edit this file to customize your BlockClock settings.

# --------- DEVICE SETTINGS ---------
# Device 1 (Primary)
DEVICE_1_NAME="BlockClock Mini"
DEVICE_1_IP="192.168.0.177"
DEVICE_1_PASSWORD=""  # Leave empty if no password set on the device

# Device 2 (Optional)
#DEVICE_2_NAME="BlockClock Micro"
#DEVICE_2_IP=""
#DEVICE_2_PASSWORD=""

# Device 3 (Optional)
#DEVICE_3_NAME="BlockClock Living Room"
#DEVICE_3_IP=""
#DEVICE_3_PASSWORD=""

# Device 4 (Optional)
#DEVICE_4_NAME="BlockClock Office"
#DEVICE_4_IP=""
#DEVICE_4_PASSWORD=""

# Device 5 (Optional)
#DEVICE_5_NAME="BlockClock Bedroom"
#DEVICE_5_IP=""
#DEVICE_5_PASSWORD=""

# --------- TEXT OPTIONS ---------
# Text options to display (separated by spaces)
TEXT_OPTIONS=("__GFY__" "_BTFD_" "_HODL_" "SATOSHI" "_NGMI_" "BITCOIN" "FIATSUX" "WENMOON" "BEVSTR")

# --------- TIMING SETTINGS ---------
# Options: 300 (5 min), 600 (10 min), 900 (15 min), 1800 (30 min), 3600 (hourly)
CLOCK_REFRESH_TIME=300

# Number of built-in screens to show between our text messages
DISPLAYS_BETWEEN_TEXT=3
''')

def save_config(config_data):
    """Save configuration to file"""
    config_file = app.config['DEFAULT_CONFIG_FILE']
    
    # Start with a template
    config_content = '''# BlockClock Text Rotation Script - Configuration File
# ==========================================================
# Edit this file to customize your BlockClock settings.

# --------- DEVICE SETTINGS ---------'''

    # Add device settings
    for i in range(1, 6):
        device = next((d for d in config_data['devices'] if d['id'] == i), None)
        
        if device:
            config_content += f'''
# Device {i}
DEVICE_{i}_NAME="{device['name']}"
DEVICE_{i}_IP="{device['ip']}"
DEVICE_{i}_PASSWORD="{device['password']}"'''
        else:
            config_content += f'''
# Device {i} (Optional)
#DEVICE_{i}_NAME="BlockClock Device {i}"
#DEVICE_{i}_IP=""
#DEVICE_{i}_PASSWORD=""'''
    
    # Add text options
    text_options_str = '" "'.join(config_data['text_options'])
    config_content += f'''

# --------- TEXT OPTIONS ---------
# Text options to display (separated by spaces)
TEXT_OPTIONS=("{text_options_str}")

# --------- TIMING SETTINGS ---------
# Options: 300 (5 min), 600 (10 min), 900 (15 min), 1800 (30 min), 3600 (hourly)
CLOCK_REFRESH_TIME={config_data['clock_refresh_time']}

# Number of built-in screens to show between our text messages
DISPLAYS_BETWEEN_TEXT={config_data['displays_between_text']}

# --------- LOG MANAGEMENT ---------
# Archive logs after this many days
LOG_ARCHIVE_DAYS={config_data.get('log_archive_days', 1)}

# Archive logs when they reach this size (MB)
LOG_ARCHIVE_SIZE={config_data.get('log_archive_size', 10)}

# Delete archived logs after this many days
LOG_DELETE_DAYS={config_data.get('log_delete_days', 30)}

# --------- DISPLAY SETTINGS ---------
# Default theme for the web interface (light, dark, or system)
DEFAULT_THEME="{config_data.get('default_theme', 'light')}"
'''
    
    # Write the config file
    with open(config_file, 'w') as f:
        f.write(config_content)

#######################################################
# ROUTE HANDLERS
#######################################################

@app.route('/')
def index():
    """Home page"""
    config = load_config()
    return render_template('index.html', 
                          config=config, 
                          rotation_active=rotation_active)

@app.route('/settings')
def settings():
    """Settings page"""
    config = load_config()
    return render_template('settings.html', config=config)

@app.route('/save_settings', methods=['POST'])
def save_settings():
    """Save settings"""
    data = request.json
    save_config(data)
    flash('Settings saved successfully!', 'success')
    return jsonify({'success': True})

@app.route('/start', methods=['POST'])
def start():
    """Start text rotation"""
    if start_rotation():
        return jsonify({'success': True, 'active': True})
    else:
        flash('Failed to start BlockClock App!', 'danger')
        return jsonify({'success': False, 'error': 'Failed to start text rotation'})

@app.route('/stop', methods=['POST'])
def stop():
    """Stop text rotation"""
    try:
        if stop_rotation():
            return jsonify({'success': True, 'active': False})
        else:
            flash('Failed to stop text rotation!', 'danger')
            return jsonify({'success': False, 'error': 'Failed to stop text rotation'})
    except Exception as e:
        logger.error(f"❌ Error in stop endpoint: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/status')
def status():
    """Get rotation status"""
    global rotation_active, blockclock_process
    
    # Check if process is still running
    if blockclock_process and blockclock_process.poll() is not None:
        # Process has exited
        rotation_active = False
    
    return jsonify({'active': rotation_active})

@app.route('/monitoring_status')
def monitoring_status():
    """Get the current monitoring status"""
    global monitoring_active, monitoring_message, monitoring_start_time
    
    now = time.time()
    elapsed_seconds = int(now - monitoring_start_time) if monitoring_start_time > 0 else 0
    minutes = elapsed_seconds // 60
    seconds = elapsed_seconds % 60
    
    # Calculate expected sleep time
    expected_time = ""
    if blockclock_instance:
        if "Sleeping before" in monitoring_message:
            # The expected sleep is clock_refresh_time - 45 seconds
            expected_seconds = blockclock_instance.clock_refresh_time - 45
            expected_minutes = expected_seconds // 60
            expected_remainder = expected_seconds % 60
            expected_time = f"{expected_minutes}:{expected_remainder:02d}"
        elif "Waiting for first refresh" in monitoring_message:
            # First refresh could take a full refresh cycle
            expected_seconds = blockclock_instance.clock_refresh_time
            expected_minutes = expected_seconds // 60
            expected_remainder = expected_seconds % 60
            expected_time = f"{expected_minutes}:{expected_remainder:02d}"
        elif "refresh #" in monitoring_message and "of" in monitoring_message:
            # Regular refresh monitoring, expect just the remaining time before next refresh
            expected_seconds = blockclock_instance.clock_refresh_time
            expected_minutes = expected_seconds // 60
            expected_remainder = expected_seconds % 60
            expected_time = f"{expected_minutes}:{expected_remainder:02d}"
    
    return jsonify({
        'active': monitoring_active,
        'message': monitoring_message,
        'elapsed': f"{minutes:02d}:{seconds:02d}",
        'expected': expected_time
    })

@app.route('/rate_limit_status')
def rate_limit_status():
    """Get the current rate limit status"""
    rate_limit_ok, wait_time = check_rate_limit()
    return jsonify({
        'can_send': rate_limit_ok,
        'wait_time': int(wait_time) if not rate_limit_ok else 0
    })

@app.route('/sync_status')
def sync_status():
    """Get synchronization status"""
    global rotation_active, first_refresh_detected
    
    return jsonify({
        'active': rotation_active,
        'sync_ready': first_refresh_detected
    })

@app.route('/logs')
def get_logs():
    """Get the recent application logs"""
    # Use the central log file location
    log_path = os.path.join(project_root, 'logs', 'blockclock.log')
    
    log_content = "No log file found. Please start the text rotation to generate logs."
    
    if os.path.exists(log_path):
        try:
            with open(log_path, 'r') as f:
                lines = f.readlines()
                # Get the last 200 lines
                recent_logs = lines[-200:] if len(lines) > 200 else lines
                log_content = ''.join(recent_logs)
        except Exception as e:
            log_content = f"Error reading log file: {str(e)}"
    
    return jsonify({
        'success': True,
        'logs': log_content
    })

@app.route('/check_device', methods=['POST'])
def check_device():
    """Check if a device is reachable"""
    data = request.json
    ip = data.get('ip', '')
    
    # Use ping to check if device is reachable
    try:
        ping_command = ["ping", "-c", "1", "-W", "2", ip]
        result = subprocess.run(ping_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        reachable = result.returncode == 0
        
        return jsonify({
            'success': True,
            'reachable': reachable,
            'message': 'Device is reachable' if reachable else 'Device is not reachable'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'reachable': False,
            'message': str(e)
        })

@app.route('/current_display')
def current_display():
    """Get the current text being displayed on BlockClocks"""
    global rotation_active, blockclock_process
    
    # If rotation is not active, return inactive status
    if not rotation_active:
        return jsonify({
            'success': True,
            'display_text': '--------',
            'display_type': 'Inactive - Start rotation to see display'
        })
    
    try:
        # Create a temporary connection directly without using BlockClockControl
        config_file = app.config['DEFAULT_CONFIG_FILE']
        
        # Get device IP from config
        device_ip = "192.168.0.177"  # Default IP
        try:
            with open(config_file, 'r') as f:
                for line in f:
                    if line.strip().startswith('DEVICE_1_IP='):
                        ip_part = line.strip().split('=', 1)[1]
                        # Remove quotes if present
                        if ip_part.startswith('"') and ip_part.endswith('"'):
                            device_ip = ip_part[1:-1]
                        else:
                            device_ip = ip_part
                        break
        except Exception as e:
            logger.error(f"❌ Error reading config file: {e}")
        
        # Get the current display directly using requests
        try:
            url = f"http://{device_ip}/api/status"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if "rendered" in data and "contents" in data["rendered"]:
                    display_text = "".join(data["rendered"]["contents"])
                    
                    # Determine display type and format display text
                    if "$" in display_text:
                        # It's a Bitcoin price
                        # Extract only the numeric part
                        price = ""
                        for char in display_text:
                            if char.isdigit():
                                price += char
                        
                        # Format the price with commas
                        if price:
                            if len(price) <= 3:
                                formatted_price = price
                            elif len(price) <= 6:
                                # Add one comma (e.g., 12,345)
                                formatted_price = f"{price[:-3]},{price[-3:]}"
                            else:
                                # Add two commas (e.g., 1,234,567)
                                formatted_price = f"{price[:-6]},{price[-6:-3]},{price[-3:]}"
                        else:
                            formatted_price = price
                        
                        display_type = "Price Display"
                        display_info = f"BTC/USD: ${formatted_price}"
                    elif display_text.strip().isdigit():
                        # It's a block height
                        display_type = "Block Height Display"
                        display_info = f"Block Height: {display_text.strip()}"
                    elif "TIME" in display_text:
                        # It's Moscow Time
                        display_type = "Moscow Time Display"
                        match = re.search(r'TIME\s+(\d+)', display_text)
                        time_only = match.group(1) if match else display_text
                        display_info = f"Moscow Time: {time_only}"
                    elif display_text.isupper() and len(display_text) <= 7:
                        # It's likely custom text
                        display_type = "Custom Text"
                        display_info = f"{display_text}"
                    else:
                        # Unknown type
                        display_type = "BlockClock Display"
                        display_info = display_text
                        
                    return jsonify({
                        'success': True,
                        'display_text': display_info,
                        'display_type': display_type
                    })
            
            # Default fallback
            return jsonify({
                'success': True,
                'display_text': 'CONNECTING',
                'display_type': 'Connecting to BlockClock...'
            })
            
        except requests.exceptions.RequestException as e:
            return jsonify({
                'success': False,
                'error': f"Connection error: {str(e)}",
                'display_text': 'ERROR',
                'display_type': 'Connection failed'
            })
        
    except Exception as e:
            error_msg = f"Error getting current display: {str(e)}"
            logger.error(f"❌ {error_msg}")
            return jsonify({
                'success': False,
                'error': error_msg,
                'display_text': 'ERROR',
                'display_type': 'Error occurred'
            })

@app.route('/send_text', methods=['POST'])
def send_text():
    """Send a custom text to devices"""
    global rotation_active, blockclock_process, first_refresh_detected, monitoring_message, monitoring_start_time, last_manual_text_time
    
    # Check if rotation is active
    if not rotation_active:
        return jsonify({
            'success': False,
            'message': 'BlockClock rotation is not running. Please start rotation first.'
        })
    
    # Check rate limit
    rate_limit_ok, wait_time = check_rate_limit()
    if not rate_limit_ok:
        # Rate limit exceeded, return error with wait time
        return jsonify({
            'success': False,
            'rate_limited': True,
            'wait_time': int(wait_time),
            'message': f'Please wait {int(wait_time)} seconds before sending another text.'
        })
    
    data = request.json
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({
            'success': False,
            'message': 'Please enter text to send'
        })
    
    try:
        # Log that we're sending a one-time text
        logger.info("")
        logger.info(f"📱 Manual one-time text requested: \"{text}\"")
        logger.info("")

        # Instead of creating a new instance, we'll call the API directly for each device
        # This avoids creating a parallel process
        config_file = app.config['DEFAULT_CONFIG_FILE']
        
        # Load devices from config
        devices = []
        with open(config_file, 'r') as f:
            config_content = f.read()
            
        # Parse devices from the config - reuse the same code pattern from load_config()
        for i in range(1, 6):  # Check for up to 5 devices
            device_name_key = f"DEVICE_{i}_NAME"
            device_ip_key = f"DEVICE_{i}_IP"
            device_password_key = f"DEVICE_{i}_PASSWORD"
            
            name_match = device_name_key + '="([^"]*)"'
            ip_match = device_ip_key + '="?([^"]*)"?'
            password_match = device_password_key + '="?([^"]*)"?'
            
            name = re.search(name_match, config_content)
            ip = re.search(ip_match, config_content)
            password = re.search(password_match, config_content)
            
            if ip and ip.group(1).strip():
                device = {
                    'name': name.group(1) if name else f"Device {i}",
                    'ip': ip.group(1),
                    'password': password.group(1) if password else ""
                }
                devices.append(device)
        
        if not devices:
            logger.error("❌ No devices configured for manual text send")
            return jsonify({
                'success': False,
                'message': 'No devices configured'
            })
        
        # Check if at least one device is reachable
        any_reachable = False
        for device in devices:
            ping_command = ["ping", "-c", "1", "-W", "2", device['ip']]
            try:
                result = subprocess.run(ping_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if result.returncode == 0:
                    any_reachable = True
                    break
            except Exception as e:
                continue
        
        if not any_reachable:
            logger.error("❌ No devices reachable for manual text send")
            return jsonify({
                'success': False,
                'message': 'No devices are reachable'
            })
        
        # Send text directly to each device without creating a new BlockClockControl instance
        for device in devices:
            name = device["name"]
            ip = device["ip"]
            password = device["password"]
            
            # Prepare API URL
            url = f"http://{ip}/api/show/text/{text}"
            
            try:
                # Make the request
                if password:
                    response = requests.get(url, auth=("", password), timeout=5)
                else:
                    response = requests.get(url, timeout=5)
                
                # Log the text send
                logger.info(f"✅ [{name}] updated with one-time text: \"{text}\"")
            except Exception as e:
                logger.error(f"❌ Error sending text to {name}: {str(e)}")
        
        # After sending text, restart the app process
        logger.info("🔄 Restarting background process to maintain synchronization")

        logger.info("")
        logger.info("==================================================")
        logger.info("🔄 RESTARTING AFTER MANUAL TEXT - Resyncing Satoshi Shuffle")
        logger.info("==================================================")
        logger.info("")
        
        # Stop all processes
        stop_rotation()
        
        # Wait a moment to ensure clean shutdown
        time.sleep(1)
        
        # Start new process with updated path
        script_path = os.path.join(project_root, 'python', 'blockclock.py')
        logger.info("▶️  Starting new background process")
        blockclock_process = subprocess.Popen(['python3', script_path, config_file])
        logger.info("✅ New process started successfully")
        
        # Reset flags
        first_refresh_detected = False
        monitoring_message = "⏳ Waiting for first refresh to synchronize..."
        monitoring_start_time = time.time()
        rotation_active = True
        
        # Update the rate limit timestamp
        last_manual_text_time = time.time()
        
        return jsonify({
            'success': True,
            'message': f'Text "{text}" sent successfully (restarting app to maintain sync)'
        })
    except Exception as e:
        logger.error(f"❌ Error in send_text: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        })