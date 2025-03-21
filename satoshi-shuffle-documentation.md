# Satoshi Shuffle Documentation

## Project Overview
Satoshi Shuffle (also known as BlockClock Control) provides tools to control Coinkite BlockClock Mini/Micro devices by displaying custom text messages that rotate on a configurable schedule. The project has evolved from a bash script to a full web application with multiple deployment options.

## Installation Methods

### 1. Basic Python Installation
**For:** Users with some technical knowledge who want direct control  
**Overview:** This method involves the user directly installing the Python application on their system. They would:
- Clone or download the repository
- Install Python dependencies via pip
- Configure their BlockClock devices manually
- Run the application directly with Python commands

This gives users the most control and visibility into how everything works, but requires some familiarity with Python and command-line operations.

### 2. One-Click Script Installation
**For:** Semi-technical users who want a simplified setup but on their own machine  
**Overview:** Your `install.py` script automates most of the setup process:
- Handles dependency installation
- Guides users through device configuration via prompts
- Sets up service files for auto-starting on boot
- Takes care of directory creation and permissions

This provides a middle ground - simpler than manual setup but still runs directly on the user's system without containers.

### 3. Docker Installation
**For:** Users who prioritize simplicity and isolation  
**Overview:** The Docker approach containerizes the entire application:
- Users just need Docker installed on their system
- Everything runs in an isolated container
- Configuration is handled through mounted volumes
- Updates can be applied by simply pulling a new image

This is the most hands-off approach, ideal for users who just want the application to work without worrying about the technical details or potentially interfering with their system.

## Recommended GitHub Repository Structure

```
satoshi-shuffle/
├── README.md               # Main project documentation
├── LICENSE                 # Open source license (MIT is good for most projects)
├── CHEATSHEET.md           # Command-line cheat sheet for users
├── config/                 # Example configuration files
│   └── blockclock.conf     # Sample configuration
├── docker/                 # Docker implementation
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md           # Docker-specific instructions
├── install.py              # Your one-click install script
├── requirements.txt        # Python dependencies
├── webapp/                 # Web application code
│   ├── blockclock_web.py   # Main app entry point
│   ├── routes.py
│   ├── static/
│   └── templates/
├── python/                 # Core Python module
│   └── blockclock.py
├── logs/                   # Empty logs directory structure
│   └── .gitkeep            # Empty file to keep directory in git
└── screenshots/            # Screenshots for documentation
    ├── dashboard.png
    └── settings.png
```

## Project Roadmap Updates

### Documentation Tasks
- ⏳ Complete inline code documentation
- ⏳ Create comprehensive user guide
- ⏳ Create command-line cheat sheet for common operations
- ⏳ Add troubleshooting section
- ⏳ Create installation walkthrough videos

### Testing Tasks
- ⏳ Implement automated testing
- ⏳ Conduct user testing for UI improvements
- ⏳ Test installation on various platforms

### GitHub Repository Setup
- ⏳ Create repository with proper structure
- ⏳ Add contribution guidelines
- ⏳ Set up release workflow
- ⏳ Create issue templates

### Release Management
- ⏳ Create versioning strategy
- ⏳ Set up automated builds
- ⏳ Configure release notes generation

## Port Configuration

### Default Port
Satoshi Shuffle uses **port 5001** by default for its web interface. This choice was made because the commonly used port 5000 is often occupied by other services (especially on macOS where AirPlay Receiver uses port 5000).

### Troubleshooting Port Issues

If users encounter an error message like "Address already in use" when starting the application, it means port 5001 is already being used by another application on their system.

#### How to Change the Port

1. **Basic Python Installation**:
   Edit the `webapp/blockclock_web.py` file and change the port number in this line:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5001, use_reloader=True)
   ```
   For example, change `port=5001` to `port=5002` or another available port.

2. **One-Click Script Installation**:
   The script should handle port conflicts automatically by testing if port 5001 is available, and if not, moving to 5002, 5003, etc. until it finds an available port. If installation completes but the web interface isn't accessible, users should check the logs to see which port was actually used.

3. **Docker Installation**:
   Edit the `docker-compose.yml` file and change the port mapping:
   ```yaml
   ports:
     - "5001:5001"
   ```
   
   To use a different port on the host, change the first number:
   ```yaml
   ports:
     - "5002:5001"
   ```
   
   This maps port 5002 on the host to port 5001 inside the container.

### For Non-Technical Users

For users who are less comfortable with editing configuration files, we should include a simple troubleshooting note in the README:

> **Can't access the web interface?**
> 
> If you see an error message about the port being in use when starting Satoshi Shuffle, or if you can't access the web interface at http://localhost:5001, try the following:
>
> 1. Try a different port by adding the `-p` flag: `python install.py -p 5002`
> 2. Check if any other applications are using port 5001 and close them
> 3. Restart your computer to release any locked ports
> 4. If using Docker, edit the port mapping in docker-compose.yml to use a different port

## Command Line Cheat Sheet

A command line cheat sheet is essential for users who may not be familiar with terminal commands. This should be included in the documentation as a quick reference guide.

### Basic Operations Cheat Sheet

```
################################################
# 🚀 Satoshi Shuffle Command Line Cheat Sheet
# Everything you need to manage your BlockClock Control
################################################

# 🚀 STARTING THE APPLICATION
# Using the start script (recommended):
./start_SatoshiShuffle.sh

# Standard Python method (alternative):
cd /path/to/satoshi-shuffle
python webapp/blockclock_web.py

# With nohup (to keep running after terminal closes):
nohup python webapp/blockclock_web.py > /dev/null 2>&1 &

# Docker method:
cd /path/to/satoshi-shuffle
docker-compose -f docker/docker-compose.yml up -d

# ✅ CHECKING IF THE APPLICATION IS RUNNING
# Check for Python process:
ps aux | grep blockclock_web.py
pgrep -fl blockclock_web.py

# Check for Docker container:
docker ps | grep satoshi-shuffle

# Check the web server:
curl -I http://localhost:5001

# ❌ STOPPING THE APPLICATION
# Standard Python method:
pkill -f blockclock_web.py

# Docker method:
docker-compose -f docker/docker-compose.yml down

# 📝 CHECKING THE LOG FILES
# View last 20 log entries:
tail -n 20 logs/blockclock.log

# Monitor the log in real-time:
tail -f logs/blockclock.log

# 🧹 CLEAR THE LOG FILE
echo "" > logs/blockclock.log

# 🔄 RESTARTING THE APPLICATION
# Standard Python method:
pkill -f blockclock_web.py
sleep 2
python webapp/blockclock_web.py

# Docker method:
docker-compose -f docker/docker-compose.yml restart

# 🔍 DEBUGGING
# Check port usage:
lsof -i :5001

# Test if BlockClock devices are reachable:
ping -c 3 [BLOCKCLOCK-IP-ADDRESS]

# 🌐 CHECKING NETWORK CONNECTION
# Test if WiFi is still connected:
ping -c 5 8.8.8.8

# 🕒 ENABLE AUTO-START AT BOOT
# Using systemd (Linux):
sudo systemctl enable satoshi-shuffle

# Using launchd (macOS):
launchctl load -w ~/Library/LaunchAgents/com.satoshi-shuffle.plist

# Docker auto-restart:
# (Add "restart: always" to your docker-compose.yml file)
```

This cheat sheet should be:
1. Included in the README.md
2. Made available as a separate CHEATSHEET.md file
3. Potentially printed on a single page PDF for easy reference

## Automated Testing Strategies

### Types of Tests to Consider

#### 1. Unit Tests
Unit tests focus on testing individual components in isolation.

For Satoshi Shuffle, you could unit test:
- The BlockClock core Python module functions
- Configuration loading/saving
- Log rotation logic
- Rate limiting mechanisms

#### 2. Integration Tests
These test how multiple components work together.

For your project, you could test:
- Communication with BlockClock devices (potentially with mock responses)
- Web routes integration with the backend logic
- Configuration changes propagating correctly to the BlockClock control module

#### 3. UI/Frontend Tests
These verify that the user interface works correctly.

You could test:
- Form submissions
- UI updates in response to status changes
- Dark/light mode switching
- Device management UI functionality
