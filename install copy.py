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

def check_docker():
    """Check if Docker and Docker Compose are installed"""
    docker_ok = check_command("docker")
    compose_ok = check_command("docker-compose") or check_command("docker compose")
    
    if not docker_ok:
        print_error("Docker is not installed")
    if not compose_ok:
        print_error("Docker Compose is not installed")
    
    return docker_ok and compose_ok

def check_docker_files():
    """Check if Docker files exist and create them if they don't"""
    print_step("Checking Docker configuration files...")
    
    # Get the project root directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check if docker directory exists
    docker_dir = os.path.join(current_dir, 'docker')
    if not os.path.exists(docker_dir):
        os.makedirs(docker_dir)
        print_success("Created Docker directory")
    
    # Check if Dockerfile exists
    dockerfile = os.path.join(docker_dir, 'Dockerfile')
    if not os.path.exists(dockerfile):
        print_step("Creating Dockerfile...")
        dockerfile_content = """FROM python:3.9-slim

WORKDIR /app

# Install required packages
RUN apt-get update && apt-get install -y \\
    curl \\
    iputils-ping \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY webapp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose the port the app runs on
EXPOSE 5001

# Create volumes for persistent data
VOLUME ["/app/logs", "/app/config"]

# Command to run the application
CMD ["python", "webapp/blockclock_web.py"]
"""
        with open(dockerfile, 'w') as f:
            f.write(dockerfile_content)
        print_success("Created Dockerfile")
    
    # Check if docker-compose.yml exists
    docker_compose = os.path.join(docker_dir, 'docker-compose.yml')
    if not os.path.exists(docker_compose):
        print_step("Creating docker-compose.yml...")
        docker_compose_content = """version: '3'

services:
  satoshi-shuffle:
    build:
      context: ..
      dockerfile: docker/Dockerfile
    container_name: satoshi-shuffle
    restart: unless-stopped
    ports:
      - "5001:5001"
    volumes:
      - ../config:/app/config
      - ../logs:/app/logs
    networks:
      - satoshi-network
    environment:
      - TZ=UTC

networks:
  satoshi-network:
    driver: bridge
"""
        with open(docker_compose, 'w') as f:
            f.write(docker_compose_content)
        print_success("Created docker-compose.yml")

    # Check if README exists
    docker_readme = os.path.join(docker_dir, 'README.md')
    if not os.path.exists(docker_readme):
        print_step("Creating Docker README...")
        docker_readme_content = """# Docker Setup Guide for Satoshi Shuffle

This guide will help you set up Satoshi Shuffle using Docker for easy deployment and maintenance.

## Prerequisites

- Docker installed on your system
- Docker Compose installed on your system

## Directory Structure

The Docker setup expects the following directory structure:

```
satoshi-shuffle/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── config/
│   └── blockclock.conf
├── logs/
└── webapp/
    └── ...
```

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/satoshi-shuffle.git
   cd satoshi-shuffle
   ```

2. Build and start the Docker container:
   ```bash
   docker-compose -f docker/docker-compose.yml up -d
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:5001
   ```

## Configuration

The application configuration is stored in the `config/blockclock.conf` file. You can edit this file directly, or use the web interface to configure your settings.

## Viewing Logs

Logs are stored in the `logs` directory. You can view them directly, or use the web interface to view the latest logs.

To view logs directly from Docker:
```bash
docker logs satoshi-shuffle
```

## Stopping the Application

To stop the Docker container:
```bash
docker-compose -f docker/docker-compose.yml down
```

## Updating the Application

To update to the latest version:

1. Pull the latest changes:
   ```bash
   git pull
   ```

2. Rebuild and restart the Docker container:
   ```bash
   docker-compose -f docker/docker-compose.yml up -d --build
   ```

## Troubleshooting

If you encounter issues:

1. Check the application logs:
   ```bash
   docker logs satoshi-shuffle
   ```

2. Ensure your BlockClock devices are reachable from the Docker container:
   ```bash
   docker exec -it satoshi-shuffle ping [BlockClock-IP]
   ```

3. Restart the container:
   ```bash
   docker-compose -f docker/docker-compose.yml restart
   ```

If issues persist, please open an issue on GitHub.
"""
        with open(docker_readme, 'w') as f:
            f.write(docker_readme_content)
        print_success("Created Docker README")

    return True

def create_service_file(use_docker):
    """Create service file for systemd (Linux) or launchd (macOS)"""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        # Create launchd plist
        plist_path = os.path.expanduser("~/Library/LaunchAgents/com.blockclock.control.plist")
        
        # Get absolute paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        python_path = sys.executable
        
        if use_docker:
            # Docker version
            plist_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.blockclock.control</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/docker-compose</string>
        <string>-f</string>
        <string>{current_dir}/docker/docker-compose.yml</string>
        <string>up</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{current_dir}</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>{current_dir}/logs/launchd.error.log</string>
    <key>StandardOutPath</key>
    <string>{current_dir}/logs/launchd.log</string>
</dict>
</plist>'''
        else:
            # Direct Python version
            plist_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.blockclock.control</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_path}</string>
        <string>{current_dir}/webapp/blockclock_web.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{current_dir}/webapp</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>{current_dir}/logs/launchd.error.log</string>
    <key>StandardOutPath</key>
    <string>{current_dir}/logs/launchd.log</string>
</dict>
</plist>'''
        
        # Write the plist file
        os.makedirs(os.path.dirname(plist_path), exist_ok=True)
        with open(plist_path, 'w') as f:
            f.write(plist_content)
        
        # Set correct permissions
        os.chmod(plist_path, 0o644)
        
        return plist_path
        
    elif system == "Linux":
        # Create systemd service
        service_name = "blockclock-control.service"
        service_path = f"/etc/systemd/system/{service_name}"
        
        # Get absolute paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        python_path = sys.executable
        
        if use_docker:
            # Docker version
            service_content = f'''[Unit]
Description=BlockClock Control Web App
After=network.target

[Service]
Type=simple
User={getpass.getuser()}
WorkingDirectory={current_dir}
ExecStart=/usr/bin/docker-compose -f {current_dir}/docker/docker-compose.yml up
ExecStop=/usr/bin/docker-compose -f {current_dir}/docker/docker-compose.yml down
Restart=on-failure

[Install]
WantedBy=multi-user.target
'''
        else:
            # Direct Python version
            service_content = f'''[Unit]
Description=BlockClock Control Web App
After=network.target

[Service]
Type=simple
User={getpass.getuser()}
WorkingDirectory={current_dir}/webapp
ExecStart={python_path} {current_dir}/webapp/blockclock_web.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
'''
        
        # Write the service file (needs sudo)
        temp_path = os.path.join(current_dir, 'blockclock-control.service')
        with open(temp_path, 'w') as f:
            f.write(service_content)
        
        print_step(f"Creating systemd service file (requires sudo password)...")
        success, output = run_command(f"sudo mv {temp_path} {service_path}")
        
        if not success:
            print_error(f"Failed to create service file: {output}")
            return None
        
        # Set permissions
        run_command(f"sudo chmod 644 {service_path}")
        
        return service_path
    else:
        print_warning("Unsupported operating system. Service installation skipped.")
        return None

def enable_service(service_path):
    """Enable and start the service"""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        print_step("Enabling and starting the service...")
        success, output = run_command(f"launchctl load -w {service_path}")
        
        if not success:
            print_error(f"Failed to enable service: {output}")
            return False
            
        print_success("Service enabled and started")
        return True
        
    elif system == "Linux":
        print_step("Enabling and starting the service (requires sudo)...")
        
        # Reload systemd
        success, output = run_command("sudo systemctl daemon-reload")
        if not success:
            print_error(f"Failed to reload systemd: {output}")
            return False
        
        # Enable the service
        service_name = os.path.basename(service_path)
        success, output = run_command(f"sudo systemctl enable {service_name}")
        if not success:
            print_error(f"Failed to enable service: {output}")
            return False
        
        # Start the service
        success, output = run_command(f"sudo systemctl start {service_name}")
        if not success:
            print_error(f"Failed to start service: {output}")
            return False
            
        print_success("Service enabled and started")
        return True
    else:
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
    webapp_requirements = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'webapp', 'requirements.txt')

    print(f"DEBUG: Installing from {webapp_requirements}")
    success, output = run_command([sys.executable, "-m", "pip", "install", "-r", webapp_requirements], timeout=60)
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

def build_docker_image():
    """Build the Docker image"""
    print_step("Building Docker image (this may take a few minutes)...")
    
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Run docker-compose build
    success, output = run_command([sys.executable, "-m", "pip", "install", "-r", webapp_requirements])

    if not success:
        print_error(f"Failed to build Docker image: {output}")
        return False
        
    print_success("Docker image built successfully")
    return True

def start_docker_container():
    """Start the Docker container"""
    print_step("Starting Docker container...")
    
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Run docker-compose up
    success, output = run_command("docker-compose -f docker/docker-compose.yml up -d", cwd=current_dir)
    
    if not success:
        print_error(f"Failed to start Docker container: {output}")
        return False
        
    print_success("Docker container started successfully")
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
    
    # Determine installation method
    use_docker = False
    
    if "--no-docker" in sys.argv:
        print_step("Installing without Docker (native Python)")
        use_docker = False
    else:
        # Check if Docker is available
        if check_docker():
            print_step("Docker is available. We recommend using Docker for easier installation.")
            use_docker = input("Use Docker for installation? (Y/n): ").strip().lower() != 'n'
        else:
            print_warning("Docker is not installed. Proceeding with native Python installation.")
            use_docker = False
    
    # Configure BlockClock
    if not configure_blockclock():
        print_error("Configuration failed")
        sys.exit(1)
    
    if use_docker:
        # Docker installation
        check_docker_files()
        if not build_docker_image():
            print_error("Docker build failed")
            sys.exit(1)
        if not start_docker_container():
            print_error("Docker container start failed")
            print_warning("You can start it manually with: docker-compose -f docker/docker-compose.yml up -d")
    else:
        # Native Python installation
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
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInstallation canceled by user")
        sys.exit(1)