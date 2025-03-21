


BlockClock Control
A modern tool for controlling BlockClock Mini/Micro devices with custom text rotation.
Features

Multi-device support: Control multiple BlockClock devices simultaneously
Custom Text Rotation: Display your own messages on a schedule
Web Interface: Easy-to-use browser-based control panel
Multiple Installation Options: Choose between web app, Docker, or simple bash script

Installation Options
Choose the installation method that works best for you:
1. One-Click Installation (Recommended for most users)
The easiest way to get started is to use the installation script:
bashCopy# Clone the repository
git clone https://github.com/yourusername/blockclock-control.git
cd blockclock-control

# Run the installer
python install.py
The installer will guide you through configuration and setup.


2. Docker Installation (For users familiar with Docker)
If you prefer to manually set up with Docker:
bashCopy# Clone the repository
git clone https://github.com/yourusername/blockclock-control.git
cd blockclock-control

# Configure your settings
nano webapp/config/blockclock.conf

# Build and start the Docker container
docker-compose -f docker/docker-compose.yml up -d


3. Python Web App (Direct installation)
If you prefer to run the web app directly:
bashCopy# Clone the repository
git clone https://github.com/yourusername/blockclock-control.git
cd blockclock-control

# Install Python dependencies
pip install -r webapp/requirements.txt

# Configure your settings
nano webapp/config/blockclock.conf

# Run the web app
cd webapp
python blockclock_web.py
4. Bash Script (Advanced users)
For a lightweight solution, you can use the original bash script:
bashCopy# Clone the repository
git clone https://github.com/yourusername/blockclock-control.git
cd blockclock-control/bash

# Edit the configuration
nano blockclock.conf

# Make the script executable
chmod +x blockclock.sh

# Run the script
./blockclock.sh


System Requirements

Python 3.6+ (for Python and Web versions)
Docker & Docker Compose (for Docker version)
bash, curl, jq (for bash script version)
Linux or macOS (Windows not officially supported)

Configuration
You can configure your devices and text options through the web interface or by directly editing the configuration files:

Web App: Edit through http://localhost:5000/settings
Bash Script: Edit the blockclock.conf file

Support
If you encounter any issues, please create an issue on GitHub.
License
This project is licensed under the MIT License - see the LICENSE file for details.