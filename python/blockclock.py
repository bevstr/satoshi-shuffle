#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BlockClock Text Rotation Script
================================================
This script rotates text on BlockClock devices at regular intervals,
in sync with the built-in refresh cycle of the device.
"""

import os
import sys
import time
import random
import logging
import requests
import json
import subprocess
import re
from datetime import datetime

# Sentinel to prevent multiple executions
_BLOCKCLOCK_LOADED = False

# Set up logging
def setup_logging(log_file=None):
    """Configure logging to file and console"""
    # Use the central logs directory at the project root level
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")
    
    # Use absolute path if relative path provided
    if log_file and not os.path.isabs(log_file):
        # Convert to absolute path
        log_file = os.path.abspath(log_file)
    
    # Create log directory if using default path
    if log_file is None:
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.abspath(f"{log_dir}/blockclock.log")
    
    # Create the directory for the log file if it doesn't exist
    log_file_dir = os.path.dirname(log_file)
    os.makedirs(log_file_dir, exist_ok=True)
    
    # Print debug info
    #print(f"Setting up logging to file: {log_file}")
    
    # Get the root logger and clean any existing handlers
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Set up file handler with immediate flushing
    try:
        file_handler = logging.FileHandler(log_file, mode='a')
        file_formatter = logging.Formatter("[%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        
        # Force immediate flushing after each log entry
        original_emit = file_handler.emit
        def new_emit(record):
            result = original_emit(record)
            file_handler.flush()
            return result
        file_handler.emit = new_emit
        
        #print(f"File handler added for: {log_file}")
    except Exception as e:
        print(f"Error setting up file handler: {str(e)}")
    
    # Set up console handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("[%(asctime)s] %(message)s", "%Y-%m-%d %H:%M:%S")
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    
    # Log a test message to verify it's working
    #logger.info(f"🔍 Logging initialized, writing to: {log_file}")
    
    return logger
    
# Main class for BlockClock control
class BlockClockControl:
    """Main class for controlling BlockClock devices"""
    
    def __init__(self, config_file=None, should_continue_callback=None):
        """Initialize with default settings or from config file"""
        self.logger = setup_logging()
        
        # Default settings
        self.devices = [
            {
                "name": "BlockClock Mini",
                "ip": "192.168.x.xxx",
                "password": "",
            }
        ]
        
        self.text_options = ["__GFY__" "WENMOON" "_BTFD_" "FIATSUX" "_HODL_" "SATOSHI" "_NGMI_" "BITCOIN"]
        self.clock_refresh_time = 300  # in seconds
        self.displays_between_text = 3
        
        # Default callback always returns True if none provided
        self.should_continue = should_continue_callback or (lambda: True)
        
        # Load configuration from file if provided
        if config_file and os.path.exists(config_file):
            self.load_config(config_file)
        
        self.logger.info("🚀 Starting BlockClock Custom Text Rotation Script")
        self.logger.info(f"📊 Custom Text will Display every {self.displays_between_text * self.clock_refresh_time // 60} minutes")
        
        # List configured devices
        self.logger.info("ℹ️  Current configuration:")
        for i, device in enumerate(self.devices):
            self.logger.info(f"   - Device {i+1}: {device['name']} ({device['ip']})")
        self.logger.info(f"   - Refresh time: {self.clock_refresh_time // 60} mins ({self.clock_refresh_time} seconds)")
        self.logger.info(f"   - Displays between Custom Text: {self.displays_between_text}")
        
    def load_config(self, config_file):
        """Load configuration from file"""

        #self.logger.info("\n")
        self.logger.info(f"ℹ️  Loading your configuration")
            
        # Dictionary to store settings
        config = {}
        
        try:
            with open(config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    # Skip comments and empty lines
                    if not line or line.startswith('#'):
                        continue
                    
                    # Parse key-value pairs
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # Remove quotes if present
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                        
                        config[key] = value
            
            # Process device information
            devices = []
            for i in range(1, 6):  # Check for up to 5 devices
                device_ip_key = f"DEVICE_{i}_IP"
                if device_ip_key in config and config[device_ip_key]:
                    device = {
                        "name": config.get(f"DEVICE_{i}_NAME", f"Device {i}"),
                        "ip": config[device_ip_key],
                        "password": config.get(f"DEVICE_{i}_PASSWORD", "")
                    }
                    devices.append(device)
            
            if devices:
                self.devices = devices
            
            # Process text options
            text_options_key = "TEXT_OPTIONS"
            if text_options_key in config:
                # Parse text options array format: ("option1" "option2" "option3")
                text_value = config[text_options_key]
                if text_value.startswith('(') and text_value.endswith(')'):
                    # Remove parentheses and split by spaces
                    text_value = text_value[1:-1]
                    # Extract quoted strings
                    options = re.findall(r'"([^"]*)"', text_value)
                    if options:
                        self.text_options = options
            
            # Process timing settings
            if "CLOCK_REFRESH_TIME" in config:
                try:
                    self.clock_refresh_time = int(config["CLOCK_REFRESH_TIME"])
                except ValueError:
                    self.logger.warning("⚠️ Invalid CLOCK_REFRESH_TIME in config, using default")
            
            if "DISPLAYS_BETWEEN_TEXT" in config:
                try:
                    self.displays_between_text = int(config["DISPLAYS_BETWEEN_TEXT"])
                except ValueError:
                    self.logger.warning("⚠️ Invalid DISPLAYS_BETWEEN_TEXT in config, using default")
            
            self.logger.info("✅ Configuration loaded successfully")
            
        except Exception as e:
            self.logger.error(f"❌ Error loading configuration: {str(e)}")
            self.logger.info("ℹ️  Using default settings")

    def check_devices(self):
        """Check if devices are reachable"""
        reachable_devices = []
        unreachable_names = []
        any_reachable = False
        any_unreachable = False
        
        for device in self.devices:
            name = device["name"]
            ip = device["ip"]
            
            self.logger.info(f"🔍 Checking connection to {name} at {ip}...")
            
            # Use ping to check if device is reachable
            ping_command = ["ping", "-c", "1", "-W", "2", ip]
            try:
                result = subprocess.run(ping_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if result.returncode == 0:
                    self.logger.info(f"✅ {name} is reachable")

                    reachable_devices.append(device)
                    any_reachable = True
                else:
                    self.logger.info(f"❌ {name} is not reachable at {ip}")
                    unreachable_names.append(name)
                    any_unreachable = True
            except Exception as e:
                self.logger.error(f"❌ Error checking {name}: {str(e)}")
                unreachable_names.append(name)
                any_unreachable = True
        
        # If no devices are reachable, we can't continue
        if not any_reachable:
            self.logger.error("❌ No devices are reachable. Please check network settings and try again.")
            return False
        
        # If some devices are unreachable, warn but continue
        if any_unreachable:
            for name in unreachable_names:
                self.logger.warning(f"⚠️ {name} is not reachable. Possible causes:")
                self.logger.warning(f"   - Device powered off")
                self.logger.warning(f"   - Incorrect IP address")
                self.logger.warning(f"   - Network connectivity issues")
            
            # List the devices we're continuing with
            if len(reachable_devices) == 1:
                self.logger.info(f"ℹ️  Continuing with {reachable_devices[0]['name']} only")
            else:
                devices_list = ", ".join([d["name"] for d in reachable_devices])
                self.logger.info(f"ℹ️  Continuing with these devices: {devices_list}")
        
        # Update self.devices with only reachable devices
        self.devices = reachable_devices
        return True

    def get_display(self, device=None):
        """Get current display from a device"""
        # Use the first device if none specified
        if device is None and self.devices:
            device = self.devices[0]
        elif not device and not self.devices:
            return "ERROR"
        
        ip = device["ip"]
        password = device["password"]
        
        # Prepare API URL
        url = f"http://{ip}/api/status"
        
        try:
            # Make the request
            if password:
                response = requests.get(url, auth=("", password), timeout=5)
            else:
                response = requests.get(url, timeout=5)
            
            # Check if request was successful
            if response.status_code == 200:
                data = response.json()
                # Extract displayed text from response
                if "rendered" in data and "contents" in data["rendered"]:
                    return "".join(data["rendered"]["contents"])
            
            return "ERROR"
        except Exception as e:
            self.logger.error(f"❌ Error getting display: {str(e)}")
            return "ERROR"

    def clean_display_text(self, text):
        """Clean display text for logging"""
        if not text or text == "ERROR":
            return text
        
        # Remove /BTC, /, and USD from text
        text = text.replace("/BTC", "")
        text = text.replace("/", "")
        text = text.replace("USD", "")
        
        return text

    def get_display_info(self, display_text):
        """Get display type and extra info"""
        clean_text = self.clean_display_text(display_text)
        
        # Check if it's a block height (starts with space and then only numbers)
        if display_text.strip() and display_text.strip().isdigit():
            return f"Block Height: {clean_text}"
        
        # Check if it's a Bitcoin price (has $ sign)
        elif "$" in display_text:
            # Extract ONLY the numeric part of the price (no $ sign)
            price = ""
            for char in clean_text:
                if char.isdigit():
                    price += char
            
            # Format with commas
            if not price:
                formatted_price = price
            elif len(price) <= 3:
                # No commas needed
                formatted_price = price
            elif len(price) <= 6:
                # One comma (e.g., 12,345)
                thousands = price[:-3]
                remainder = price[-3:]
                formatted_price = f"{thousands},{remainder}"
            else:
                # Two commas (e.g., 1,234,567)
                millions = price[:-6]
                thousands = price[-6:-3]
                remainder = price[-3:]
                formatted_price = f"{millions},{thousands},{remainder}"
            
            # Output with a single $ sign
            return f"Bitcoin Price: ${formatted_price}"
        
        # Check for TIME in the display
        elif "TIME" in display_text:
            # Extract just the time part (the numbers after "TIME")
            match = re.search(r'TIME\s+(\d+)', clean_text)
            if match:
                time_only = match.group(1)
                return f"Moscow Time: {time_only}"
            else:
                return f"Moscow Time: {clean_text}"
        else:
            return clean_text

    def send_text(self, text):
        """Send text to all configured devices"""
        for device in self.devices:
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
                
                self.logger.info(f"✅ [{name}] updated with: \"{text}\"")
            except Exception as e:
                self.logger.error(f"❌ Error sending text to {name}: {str(e)}")
        
        if len(self.devices) > 1:
            self.logger.info("")
            self.logger.info("✨ Custom Text displayed on all available devices")
            self.logger.info("")  # Empty line
        else:
            self.logger.info("✨ Custom Text displayed on device")

    def wait_for_refresh(self, start_display, ignore_text=None, timeout=None, message="Waiting for refresh"):
        """Wait for display to change, ignoring specified text"""
        if timeout is None:
            timeout = self.clock_refresh_time + 300  # Default timeout
        
        # Start monitoring for changes
        start_time = time.time()
        self.logger.info(f"🔍 Started Monitoring!")

            # Get current display immediately to check if it has already changed
        current_display = self.get_display()

        
        # If it's the initial waiting phase, set up for progress indicators
        is_initial_wait = "first refresh" in message.lower()
        if is_initial_wait:
            # Log the start of waiting
            self.logger.info(f"⏳ Waiting for first refresh...")
        
        # Get current display immediately to check if it has already changed
            #current_display = self.get_display()
        
        # If display has already changed at the start of monitoring
        if (current_display != start_display and
            current_display != ignore_text and
            current_display and
            current_display != "ERROR"):
            
            # A short artificial delay to avoid showing "0 seconds"
            elapsed_time = max(1, int(time.time() - start_time))
            display_info = self.get_display_info(current_display)
            
            # Special handling for first refresh
            if is_initial_wait:
                self.logger.info("")
                #self.logger.info(f"✅ First refresh detected after {elapsed_time} seconds - Displaying: \"{display_info}\"")
                self.logger.info(f"✅ First refresh detected after {elapsed_time} seconds")
                self.logger.info(f"Current Display: \"{display_info}\"")

            else:
                self.logger.info(f"✅ Display changed after {elapsed_time} seconds - Displaying: \"{display_info}\"")
                self.logger.info("")  # Empty line
            return True
        
        # Monitor for changes
        next_update_time = start_time + 10  # First update after 10 seconds
        progress_indicators = [
            "⏳ Still waiting... (elapsed: {elapsed_time})",
            "⏳ Still waiting... (elapsed: {elapsed_time})",
            "⏳ Still bloody waiting... (elapsed: {elapsed_time})",
            "⏳ Hang in there... (elapsed: {elapsed_time})",
            "⏳ Patience is a Virtue... (elapsed: {elapsed_time})",
            "⏳ It will happen, trust me... (elapsed: {elapsed_time})",
            "⏳ Won't be long now... (elapsed: {elapsed_time})"


        ]
        indicator_index = 0
        
        while True:
            elapsed = time.time() - start_time
            if elapsed >= timeout:
                self.logger.warning(f"⚠️ Timeout waiting for display change after {timeout} seconds")
                return False
            
            # Show progress updates
            if is_initial_wait and time.time() >= next_update_time:
                # Format elapsed time
                elapsed_mins = int(elapsed) // 60
                elapsed_secs = int(elapsed) % 60
                elapsed_time_str = f"{elapsed_mins:02d}:{elapsed_secs:02d}"
                
                # Print progress message
                progress_msg = progress_indicators[indicator_index].format(elapsed_time=elapsed_time_str)
                self.logger.info(progress_msg)
                
                # Cycle through indicators
                indicator_index = (indicator_index + 1) % len(progress_indicators)
                
                # Set next update time
                next_update_time = time.time() + 30  # Update every 30 seconds
            
            current_display = self.get_display()
            
            # Check if display has changed
            if (current_display != start_display and
                current_display != ignore_text and
                current_display and
                current_display != "ERROR"):
                
                display_info = self.get_display_info(current_display)
                elapsed_time = int(time.time() - start_time)
                
                # Special handling for first refresh
                if is_initial_wait:
                    #self.logger.info(f"✅ First refresh detected after {elapsed_time} seconds - Displaying: \"{display_info}\"")
                    self.logger.info("")
                    self.logger.info(f"✅ First refresh detected after {elapsed_time} seconds")
                    self.logger.info(f"Current Display: \"{display_info}\"")
                    self.logger.info("")

                else:
                    self.logger.info(f"✅ Display changed after {elapsed_time} seconds - Displaying: \"{display_info}\"")
                    self.logger.info("")  # Empty line
                return True
            
            # Simple sleep without console updates
            time.sleep(1)



    def countdown(self, seconds):
        """Display a countdown timer with periodic updates"""
        start_time = time.time()
        end_time = start_time + seconds
        
        # Calculate total segments to show
        total_segments = 10  # We'll divide the countdown into 10 segments
        segment_time = seconds / total_segments
        
        # Log the start of countdown
        self.logger.info(f"Countdown started: sleep time: {seconds//60:02d}:{seconds%60:02d}")
        
        # Track segments for progress updates
        for segment in range(1, total_segments + 1):
            # Wait until this segment should be complete
            segment_end_time = start_time + (segment * segment_time)
            while time.time() < segment_end_time and time.time() < end_time:
                time.sleep(1)
            
            # Skip printing updates if we've reached the end already
            if time.time() >= end_time:
                break
                
            # Calculate percentage and remaining time
            elapsed = time.time() - start_time
            remaining = end_time - time.time()
            percent = int((elapsed / seconds) * 100)
            
            # Format remaining time
            mins_remaining = int(remaining) // 60
            secs_remaining = int(remaining) % 60
            
            # Create progress bar
            progress_chars = "▮" * segment + "▯" * (total_segments - segment)
            
            # Instead of using print (which might get filtered), use logger
            self.logger.info(f"Countdown progress: [{progress_chars}] {percent}% ({mins_remaining:02d}:{secs_remaining:02d} remaining)")
        
        # Wait for any remaining time
        remaining_time = end_time - time.time()
        if remaining_time > 0:
            time.sleep(remaining_time)
        
        # Log completion
        elapsed = int(time.time() - start_time)
        self.logger.info(f"Countdown completed after {elapsed//60:02d}:{elapsed%60:02d}")


    def run(self):
        """Main execution loop"""
        initial_display = self.get_display()
        if initial_display == "ERROR":
            self.logger.error("❌ Error connecting to BlockClock. Check IP address and connection.")
            return
        
        clean_initial = self.clean_display_text(initial_display)
        display_info = self.get_display_info(initial_display)
        
        if not clean_initial or clean_initial == "null":
            display_info = "(unknown)"
        
        #self.logger.info(f"⏳ Waiting for first refresh to synchronize... Displaying: \"{display_info}\"")
        self.logger.info(f"⏳ Waiting for first refresh to synchronize...")
        self.logger.info(f"⏳ Current Display: \"{display_info}\"")

        self.wait_for_refresh(initial_display, None, self.clock_refresh_time + 300, "Waiting for first refresh")
        
        self.logger.info("⏳ Waiting 6 seconds for animation to complete...")
        time.sleep(6)
        
        random_text = random.choice(self.text_options)
        self.send_text(random_text)
        self.logger.info("🔄 Starting monitoring cycle")
        
        current_display = self.get_display()
        clean_current = self.clean_display_text(current_display)
        self.logger.info(f"⏳ Current display after sending custom text: \"{clean_current}\"")
        
        cycle_count = 0
        last_custom_text = random_text
        
        while self.should_continue():
            cycle_count += 1
            self.logger.info("")  # Empty line
            self.logger.info(f"🔄 Beginning rotation cycle #{cycle_count}")
            
            if cycle_count % 5 == 0:
                self.logger.info("🔄 Performing periodic device check (every 5 cycles)")
                if not self.check_devices():
                    self.logger.error("❌ No devices are reachable. Please check network settings.")
                    self.logger.error("🛑 Exiting script.")
                    return
            
            for i in range(1, self.displays_between_text + 1):
                wait_time = self.clock_refresh_time - 45
                self.logger.info(f"⏳ Sleeping before refresh #{i} of {self.displays_between_text}...")
                self.countdown(wait_time)
                self.logger.info("")  # Empty line
                self.wait_for_refresh(
                    current_display, 
                    last_custom_text,
                    self.clock_refresh_time + 300, 
                    f"Actively monitoring for refresh #{i}"
                )
                
                current_display = self.get_display()
                clean_current = self.clean_display_text(current_display)
                display_info = self.get_display_info(current_display)
                self.logger.info(f"🔄 BlockClock refresh {i}/{self.displays_between_text} - Displaying: \"{display_info}\"")
                time.sleep(0.5)


            wait_time = self.clock_refresh_time - 45
            self.logger.info("⏳ Sleeping before final refresh check...")
            self.countdown(wait_time)
            
            self.wait_for_refresh(
                current_display, 
                last_custom_text,
                self.clock_refresh_time + 300, 
                "Actively monitoring for final refresh"
            )
            
            current_display = self.get_display()
            clean_current = self.clean_display_text(current_display)
            display_info = self.get_display_info(current_display)
            self.logger.info(f"✅ Final refresh complete - Displaying: \"{display_info}\"")
            
            self.logger.info("⏳ Waiting 6 seconds for animation to complete...")
            time.sleep(6)
            
            self.logger.info("🎯 Full cycle complete!")
            random_text = random.choice(self.text_options)
            self.logger.info(f"📤 Sending new Custom Text: \"{random_text}\"")
            self.send_text(random_text)
            
            last_custom_text = random_text
            
            current_display = self.get_display()
            clean_current = self.clean_display_text(current_display)
            self.logger.info(f"⏳ Current display after sending custom text: \"Custom Text: {clean_current}\"")
            self.logger.info("")  # Empty line
            self.logger.info("----------------------------------------")

# This code only runs when the script is executed directly
if __name__ == "__main__":
    # Set the sentinel to true - we're running as the main script
    _BLOCKCLOCK_LOADED = True
    
    # Get config file path from command line or use default
    config_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "blockclock.conf")
    
    # Create and run the BlockClock control
    blockclock = BlockClockControl(config_file)
    
    # Check if devices are reachable
    if not blockclock.check_devices():
        blockclock.logger.error("❌ No devices are reachable. Please check network settings.")
        blockclock.logger.error("🛑 Exiting script.")
        sys.exit(1)
    
    # Start the main loop
    try:
        # Check if run method exists
        if hasattr(blockclock, 'run'):
            blockclock.run()
        else:
            # If run method doesn't exist, print diagnostic info
            print("ERROR: The 'run' method was not found in the BlockClockControl class.")
            print("Available methods:", dir(blockclock))
            sys.exit(1)
    except KeyboardInterrupt:
        blockclock.logger.info("\n\n👋 Script terminated by you, bye for now see you soon.\n")
    except Exception as e:
        blockclock.logger.error(f"❌ Error: {str(e)}")
        raise