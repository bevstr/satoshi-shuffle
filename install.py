#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BlockClock Control - Installation Script
=======================================
This script helps users set up the BlockClock Control system.
"""

import os
import sys
import subprocess
import shutil
import platform
import getpass
import re

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== {text} ==={Colors.ENDC}\n")

def print_step(text):
    print(f"{Colors.BLUE}➤ {text}{Colors.ENDC}")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.ENDC}")

def run_command(command, cwd=None, timeout=None):
    """Run a system command with an optional timeout and return the result"""
    try:
        result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, timeout=timeout)
        return True, result.stdout
    except subprocess.TimeoutExpired:
        return False, "Command timed out!"
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def check_command(command):
    """Check if a command is available"""
    try:
        subprocess.run(f"which {command}", shell=True, check=True, 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def check_python_version():
    """Check if Python version is 3.6+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print_error(f"Python 3.6+ is required. You have Python {version.major}.{version.minor}")
        return False
    return True

def check_pip():
    """Check if pip is installed"""
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        print_error("pip is not installed or not working properly")
        return False

def install_python_packages():
    """Ensure pip is updated and install required Python packages"""
    print_step("Ensuring pip is installed and up to date...")

    print("DEBUG: Running ensurepip")
    success, output = run_command([sys.executable, "-m", "ensurepip", "--default-pip"], timeout=60)
    print(f"DEBUG: ensurepip output: {output}")

    if not success:
        print_error(f"pip installation failed or timed out: {output}")
        return False
    else:
        print_success("pip is installed!")

    print("DEBUG: Running pip upgrade")
    success, output = run_command([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], timeout=60)
    print(f"DEBUG: pip upgrade output: {output}")

    if not success:
        print_error(f"Failed to upgrade pip: {output}")
        return False
    else:
        print_success("pip upgraded successfully!")

    # Now install dependencies
    print_step("Installing required Python packages...")
    
    # Check for requirements.txt in the root directory first
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_requirements = os.path.join(current_dir, 'requirements.txt')
    
    if os.path.exists(root_requirements):
        requirements_path = root_requirements
    else:
        # Fall back to webapp directory
        requirements_path = os.path.join(current_dir, 'webapp', 'requirements.txt')
    
    print(f"DEBUG: Installing from {requirements_path}")
    
    if not os.path.exists(requirements_path):
        print_error(f"Requirements file not found at {requirements_path}")
        print_step("Creating a basic requirements file...")
        
        # Create a basic requirements file
        with open(root_requirements, 'w') as f:
            f.write("Flask==2.3.3\nrequests==2.32.3\nFlask-WTF==1.1.1\n")
        
        requirements_path = root_requirements
    
    success, output = run_command([sys.executable, "-m", "pip", "install", "-r", requirements_path], timeout=60)
    print(f"DEBUG: Package install output: {output}")

    if not success:
        print_error(f"Failed to install packages: {output}")
        return False

    print_success("Python packages installed successfully")
    return True

def configure_blockclock():
    """Configure BlockClock devices interactively"""
    print_header("BlockClock Configuration")
    
    config = {
        'devices': [],
        'text_options': ["__GFY__", "WENMOON", "_BTFD_", "FIATSUX", "_HODL_", "SATOSHI", "_NGMI_", "BITCOIN", "BEVSTR"],
        'clock_refresh_time': 300,
        'displays_between_text': 3
    }
    
    # Ensure the config directory exists
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(current_dir, 'config')
    os.makedirs(config_dir, exist_ok=True)
    
    # Ask for device information
    print_step("Let's configure your BlockClock devices")
    print("You can add up to 5 devices. Leave the IP empty when done. Just keep pressing enter")
    print ("If you dont input a name BlockClock Device 1 will be name")

    for i in range(1, 6):
        print(f"\nDevice {i}:")
        name = input(f"  Name (default: BlockClock Device {i}): ").strip() or f"BlockClock Device {i}"
        ip = input("  IP Address: ").strip()
        
        if not ip:
            print("No IP provided, stopping device configuration.")
            break
            
        password = input("  Password (if any, leave empty for none): ").strip()
        
        config['devices'].append({
            'id': i,
            'name': name,
            'ip': ip,
            'password': password
        })
    
    # Ask for text options
    print_step("\nNow let's configure your custom text options")
    print("Default options: " + ", ".join(config['text_options']))
    
    custom_text = input("Enter custom text options (comma-separated, max 7 chars each) or press Enter to use defaults: ").strip()
    if custom_text:
        # Split by comma and trim whitespace
        custom_options = [text.strip() for text in custom_text.split(',')]
        # Filter out empty strings and limit to  characters
        custom_options = [text[:7] for text in custom_options if text]
        if custom_options:
            config['text_options'] = custom_options
    
    # Ask for timing settings
    print_step("\nNow let's configure timing settings")
    
    refresh_options = {
        "1": 300,  # 5 min
        "2": 600,  # 10 min
        "3": 900,  # 15 min
        "4": 1800, # 30 min
        "5": 3600  # 60 min
    }
    
    print("Clock refresh time options: This is the Display Preference you chose on BlockClock Interface")
    print("  1) 5 minutes (300 seconds) [default]")
    print("  2) 10 minutes (600 seconds)")
    print("  3) 15 minutes (900 seconds)")
    print("  4) 30 minutes (1800 seconds)")
    print("  5) 60 minutes (3600 seconds)")
    
    refresh_choice = input("Choose an option (1-5): ").strip()
    if refresh_choice in refresh_options:
        config['clock_refresh_time'] = refresh_options[refresh_choice]

    print("\nNumber of displays (Displayed values you chose on BlockClock)")
    displays = input(f"between when your Custom Text displays. (default: {config['displays_between_text']}): ").strip()
    if displays and displays.isdigit() and int(displays) > 0:
        config['displays_between_text'] = int(displays)
    
    # Calculate and show the frequency
    frequency = (config['clock_refresh_time'] * config['displays_between_text']) // 60
    print(f"\nWith these settings, your custom text will appear every {frequency} minutes.")
    
    # Save the configuration
    config_path = os.path.join(config_dir, 'blockclock.conf')
    
    # Generate config content
    config_content = '''# BlockClock Text Rotation Script - Configuration File
# ==========================================================
# Edit this file to customize your BlockClock settings.

# --------- DEVICE SETTINGS ---------'''

    for device in config['devices']:
        config_content += f'''
# Device {device['id']}
DEVICE_{device['id']}_NAME="{device['name']}"
DEVICE_{device['id']}_IP="{device['ip']}"
DEVICE_{device['id']}_PASSWORD="{device['password']}"'''
    
    # Fill in any remaining devices as commented out
    for i in range(len(config['devices']) + 1, 6):
        config_content += f'''
# Device {i} (Optional)
#DEVICE_{i}_NAME="BlockClock Device {i}"
#DEVICE_{i}_IP=""
#DEVICE_{i}_PASSWORD=""'''
    
    # Add text options
    text_options_str = '" "'.join(config['text_options'])
    config_content += f'''

    # --------- TEXT OPTIONS ---------
    # Text options to display (separated by spaces)
    TEXT_OPTIONS=("{text_options_str}")


# --------- TIMING SETTINGS ---------
# Options: 300 (5 min), 600 (10 min), 900 (15 min), 1800 (30 min), 3600 (hourly)
CLOCK_REFRESH_TIME={config['clock_refresh_time']}

# Number of built-in screens to show between our text messages
DISPLAYS_BETWEEN_TEXT={config['displays_between_text']}
'''

    # Write the config file
    with open(config_path, 'w') as f:
        f.write(config_content)
    
    print_success(f"Configuration saved to {config_path}")
    return True

def create_directory_structure():
    """Create the necessary directory structure for the application"""
    print_step("Creating directory structure...")
    
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create logs directory
    logs_dir = os.path.join(current_dir, 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    # Create config directory
    config_dir = os.path.join(current_dir, 'config')
    os.makedirs(config_dir, exist_ok=True)
    
    print_success("Directory structure created")
    return True

def main():
    print_header("BlockClock Control - Installation")
    
    # Create directory structure
    create_directory_structure()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check pip
    if not check_pip():
        sys.exit(1)
    
    # Configure BlockClock
    if not configure_blockclock():
        print_error("Configuration failed")
        sys.exit(1)
    
    # Python installation
    if not install_python_packages():
        print_error("Failed to install required Python packages")
        sys.exit(1)
    
    
    # 🚀 Installation Complete - Guide User to Start the App
    print_header("🚀 Installation Complete!")

    print("\n✅ Everything is set up!")
    print("\nTo start the application, run:")
    print("  ./start_SatoshiShuffle.sh")
    print("\n💡 To keep the app running even after closing the terminal, use:")
    print("  nohup ./start_SatoshiShuffle.sh &")
    print("\n📱 Once it's running, access the web interface at:")
    print("  http://localhost:5001")
    print("\nYou can use the web interface to configure your BlockClock devices,")
    print("customize text options, and control the text rotation.")

    print("\n💡 If you need to stop the app, use Ctrl+C.")
    print("\nEnjoy Satoshi Shuffle! 🚀")
    print("")
    print("")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInstallation canceled by user")
        sys.exit(1)