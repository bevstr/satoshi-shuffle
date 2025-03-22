# Satoshi Shuffle Command Line Cheatsheet

This cheatsheet provides quick reference commands for managing your Satoshi Shuffle installation. Commands are organized by task and installation type.

## 🚀 Starting the Application

### Using the Start Script (Recommended)
```bash
# Navigate to your Satoshi Shuffle directory
cd /path/to/satoshi-shuffle

# Make script executable (first time only, on Linux/macOS)
chmod +x start_SatoshiShuffle.sh

# Run the start script
./start_SatoshiShuffle.sh
```

### Standard Python Method
```bash
# Navigate to your Satoshi Shuffle directory
cd /path/to/satoshi-shuffle

# Start the application
python webapp/blockclock_web.py

# Alternative for Python 3 on some systems
python3 webapp/blockclock_web.py
```

### Run in Background (Keep Running After Terminal Closes)
```bash
# On macOS/Linux - Keep running after terminal closes
nohup python3 webapp/blockclock_web.py > /dev/null 2>&1 &

# Explanation:
# nohup - Prevents the process from stopping when terminal closes
# > /dev/null - Discards standard output
# 2>&1 - Redirects error messages to standard output
# & - Runs the process in background

# Send output to log file instead of discarding
nohup python3 webapp/blockclock_web.py > logs/webapp.log 2>&1 &

# On Windows
start /b python webapp\blockclock_web.py > nul 2>&1

# Check if background process is running
ps aux | grep blockclock_web.py

# Stop background process
pkill -f blockclock_web.py
```

### Docker Method
```bash
# Navigate to your Satoshi Shuffle directory
cd /path/to/satoshi-shuffle

# Start the Docker container
docker-compose -f docker/docker-compose.yml up -d
```

## ⚙️ Installation Commands

### One-Click Installation
```bash
# Run the interactive installation script
python install.py

# Install with specific options (check script help)
python install.py --no-docker

# Install and specify a different port
python install.py -p 5002
```

### Docker Installation
```bash
# Build the Docker image
docker-compose -f docker/docker-compose.yml build

# Build without using cache (for troubleshooting)
docker-compose -f docker/docker-compose.yml build --no-cache
```

### Python Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Install with specific Python version
python3 -m pip install -r requirements.txt
```

## ✅ Checking Application Status

### Process Checking
```bash
# Check if Python process is running
ps aux | grep blockclock_web.py

# More compact version
pgrep -fl blockclock_web.py

# Check if Docker container is running
docker ps | grep satoshi-shuffle
```

### Service Status
```bash
# Linux systemd service
sudo systemctl status satoshi-shuffle

# macOS launchd service
launchctl list | grep com.satoshi-shuffle
```

### Web Server Check
```bash
# Check if web server is responding
curl -I http://localhost:5001
```

## 📝 Log File Operations

### Viewing Logs
```bash
# View last 20 log entries
tail -n 20 logs/blockclock.log

# Follow log in real-time (Ctrl+C to exit)
tail -f logs/blockclock.log

# Search logs for specific text
grep "error" logs/blockclock.log

# View Docker container logs
docker logs satoshi-shuffle

# Follow Docker logs in real-time
docker logs -f satoshi-shuffle
```

### Log Management
```bash
# Clear log file
echo "" > logs/blockclock.log

# View log archive directory
ls -la logs/archive/

# Check log file size
du -sh logs/blockclock.log
```

## ❌ Stopping the Application

### Standard Method
```bash
# Kill Python process
pkill -f blockclock_web.py

# More forceful termination if needed
pkill -9 -f blockclock_web.py

# Find the process ID and kill it specifically
ps aux | grep blockclock_web.py
kill [PID]  # Replace [PID] with the actual process ID
```

### Docker Method
```bash
# Stop container but keep it
docker-compose -f docker/docker-compose.yml stop

# Stop and remove container
docker-compose -f docker/docker-compose.yml down
```

### Service Method
```bash
# Linux systemd
sudo systemctl stop satoshi-shuffle

# macOS launchd
launchctl unload ~/Library/LaunchAgents/com.satoshi-shuffle.plist
```

## 🔄 Restarting the Application

### Standard Method
```bash
# Kill and restart
pkill -f blockclock_web.py
python webapp/blockclock_web.py

# Restart in background (macOS/Linux)
pkill -f blockclock_web.py
nohup python3 webapp/blockclock_web.py > /dev/null 2>&1 &
```

### Docker Method
```bash
# Restart container
docker-compose -f docker/docker-compose.yml restart

# Full rebuild and restart
docker-compose -f docker/docker-compose.yml up -d --build
```

### Service Method
```bash
# Linux systemd
sudo systemctl restart satoshi-shuffle

# macOS launchd
launchctl unload ~/Library/LaunchAgents/com.satoshi-shuffle.plist
launchctl load ~/Library/LaunchAgents/com.satoshi-shuffle.plist
```

## 🔍 Device Connectivity

### Check Device Reachability
```bash
# Ping a BlockClock device
ping -c 3 192.168.1.100

# From Docker container
docker exec -it satoshi-shuffle ping -c 3 192.168.1.100
```

### Test BlockClock API
```bash
# Test device API (displays time)
curl -v http://192.168.1.100/api/show/time

# Test device API (displays custom text)
curl -v http://192.168.1.100/api/show/text/BITCOIN
```

## 🛠️ Updating Satoshi Shuffle

### Standard Method
```bash
# Get latest code
git pull

# Restart application
./start_SatoshiShuffle.sh

# Or restart in background
pkill -f blockclock_web.py
nohup python3 webapp/blockclock_web.py > /dev/null 2>&1 &
```

### Docker Method
```bash
# Get latest code
git pull

# Rebuild and restart container
docker-compose -f docker/docker-compose.yml up -d --build
```

## 🔌 Port Management

### Check Port Usage
```bash
# Check if port 5001 is in use
lsof -i :5001

# Alternative method
netstat -tuln | grep 5001
```

### Change Port (Python Installation)
```bash
# Edit the web application file
nano webapp/blockclock_web.py

# Find this line and change port number:
# app.run(debug=False, host='0.0.0.0', port=5001, use_reloader=True)
```

### Change Port (Docker Installation)
```bash
# Edit docker-compose file
nano docker/docker-compose.yml

# Change port mapping, e.g., from:
# "5001:5001" to "5002:5001"
```

## 🔒 Service Management

### Setting Up Service (Linux)
```bash
# Create systemd service file
sudo nano /etc/systemd/system/satoshi-shuffle.service

# Enable service to start at boot
sudo systemctl enable satoshi-shuffle

# Start service
sudo systemctl start satoshi-shuffle
```

### Setting Up Service (macOS)
```bash
# Create launchd plist file
nano ~/Library/LaunchAgents/com.satoshi-shuffle.plist

# Load service
launchctl load -w ~/Library/LaunchAgents/com.satoshi-shuffle.plist
```

## 💻 Screen Session (Alternative to nohup)

Using `screen` is another way to keep applications running after closing your terminal:

```bash
# Install screen (if not already installed)
# Ubuntu/Debian
sudo apt install screen
# macOS
brew install screen

# Start a new screen session
screen -S satoshi-shuffle

# Now run your application
python3 webapp/blockclock_web.py

# Detach from screen session (keeps running in background)
# Press Ctrl+A, then D

# List running screen sessions
screen -ls

# Reattach to a running session
screen -r satoshi-shuffle

# Kill a screen session (when attached)
# Press Ctrl+A, then type :quit and press Enter
```

## 🔏 Docker-Specific Commands

### Container Management
```bash
# Enter container shell
docker exec -it satoshi-shuffle /bin/bash

# View container details
docker inspect satoshi-shuffle

# Check container resource usage
docker stats satoshi-shuffle
```

### Docker Volumes
```bash
# List Docker volumes
docker volume ls

# Check volume details
docker volume inspect satoshi-shuffle_config
```

## 📡 Network Troubleshooting

### Network Diagnostics
```bash
# Check your IP address
ifconfig    # macOS/Linux
ipconfig    # Windows

# Check network route to device
traceroute 192.168.1.100    # macOS/Linux
tracert 192.168.1.100       # Windows

# Check local network devices (if arp is available)
arp -a
```

## 🧹 Cleanup Operations

### File Cleanup
```bash
# Remove log files
rm logs/*.log

# Remove archived logs
rm -rf logs/archive/*
```

### Docker Cleanup
```bash
# Remove container and images
docker-compose -f docker/docker-compose.yml down --rmi all

# Remove volumes too (CAUTION: Deletes all configuration!)
docker-compose -f docker/docker-compose.yml down -v

# System-wide Docker cleanup
docker system prune
```

## 📂 Backup and Restore

### Configuration Backup
```bash
# Manual backup of config file
cp config/blockclock.conf config/blockclock.conf.backup

# Full directory backup
tar -czvf satoshi-shuffle-backup.tar.gz config/ logs/
```

### Docker Volume Backup
```bash
# Create a backup container and copy from volume
docker run --rm -v satoshi-shuffle_config:/backup -v $(pwd):/host alpine cp -r /backup /host/config-backup
```