## 📘 Cheatsheet – Expand Any Section

# Satoshi Shuffle Command Line Cheatsheet

This cheatsheet provides quick reference commands for managing your Satoshi Shuffle installation. Commands are organized by task and installation type.


<details>
<summary><strong>🚀 Starting the Application</strong></summary>

## 🚀 Starting the Application

</details>

<details>
<summary><strong>Using the Start Script (Recommended)</strong></summary>

### Using the Start Script (Recommended)
```bash
# Navigate to your Satoshi Shuffle directory
cd /path/to/satoshi-shuffle

# Make script executable (first time only, on Linux/macOS)
chmod +x start_SatoshiShuffle.sh

# Run the start script
./start_SatoshiShuffle.sh
```

</details>

<details>
<summary><strong>Standard Python Method</strong></summary>

### Standard Python Method
```bash
# Navigate to your Satoshi Shuffle directory
cd /path/to/satoshi-shuffle

# Start the application
python webapp/blockclock_web.py

# Alternative for Python 3 on some systems
python3 webapp/blockclock_web.py
```

</details>

<details>
<summary><strong>Run in Background (Keep Running After Terminal Closes)</strong></summary>

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

</details>

<details>
<summary><strong>Docker Method</strong></summary>

### Docker Method
```bash
# Navigate to your Satoshi Shuffle directory
cd /path/to/satoshi-shuffle

# Start the Docker container
docker-compose -f docker/docker-compose.yml up -d
```

</details>

<details>
<summary><strong>⚙️ Installation Commands</strong></summary>

## ⚙️ Installation Commands

</details>

<details>
<summary><strong>One-Click Installation</strong></summary>

### One-Click Installation
```bash
# Run the interactive installation script
python install.py

# Install with specific options (check script help)
python install.py --no-docker

# Install and specify a different port
python install.py -p 5002
```

</details>

<details>
<summary><strong>Docker Installation</strong></summary>

### Docker Installation
```bash
# Build the Docker image
docker-compose -f docker/docker-compose.yml build

# Build without using cache (for troubleshooting)
docker-compose -f docker/docker-compose.yml build --no-cache
```

</details>

<details>
<summary><strong>Python Installation</strong></summary>

### Python Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Install with specific Python version
python3 -m pip install -r requirements.txt
```

</details>

<details>
<summary><strong>✅ Checking Application Status</strong></summary>

## ✅ Checking Application Status

</details>

<details>
<summary><strong>Process Checking</strong></summary>

### Process Checking
```bash
# Check if Python process is running
ps aux | grep blockclock_web.py

# More compact version
pgrep -fl blockclock_web.py

# Check if Docker container is running
docker ps | grep satoshi-shuffle
```

</details>

<details>
<summary><strong>Service Status</strong></summary>

### Service Status
```bash
# Linux systemd service
sudo systemctl status satoshi-shuffle

# macOS launchd service
launchctl list | grep com.satoshi-shuffle
```

</details>

<details>
<summary><strong>Web Server Check</strong></summary>

### Web Server Check
```bash
# Check if web server is responding
curl -I http://localhost:5010
```

</details>

<details>
<summary><strong>📝 Log File Operations</strong></summary>

## 📝 Log File Operations

</details>

<details>
<summary><strong>Viewing Logs</strong></summary>

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

</details>

<details>
<summary><strong>Log Management</strong></summary>

### Log Management
```bash
# Clear log file
echo "" > logs/blockclock.log

# View log archive directory
ls -la logs/archive/

# Check log file size
du -sh logs/blockclock.log
```

</details>

<details>
<summary><strong>❌ Stopping the Application</strong></summary>

## ❌ Stopping the Application

</details>

<details>
<summary><strong>Standard Method</strong></summary>

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

</details>

<details>
<summary><strong>Docker Method</strong></summary>

### Docker Method
```bash
# Stop container but keep it
docker-compose -f docker/docker-compose.yml stop

# Stop and remove container
docker-compose -f docker/docker-compose.yml down
```

</details>

<details>
<summary><strong>Service Method</strong></summary>

### Service Method
```bash
# Linux systemd
sudo systemctl stop satoshi-shuffle

# macOS launchd
launchctl unload ~/Library/LaunchAgents/com.satoshi-shuffle.plist
```

</details>

<details>
<summary><strong>🔄 Restarting the Application</strong></summary>

## 🔄 Restarting the Application

</details>

<details>
<summary><strong>Standard Method</strong></summary>

### Standard Method
```bash
# Kill and restart
pkill -f blockclock_web.py
python webapp/blockclock_web.py

# Restart in background (macOS/Linux)
pkill -f blockclock_web.py
nohup python3 webapp/blockclock_web.py > /dev/null 2>&1 &
```

</details>

<details>
<summary><strong>Docker Method</strong></summary>

### Docker Method
```bash
# Restart container
docker-compose -f docker/docker-compose.yml restart

# Full rebuild and restart
docker-compose -f docker/docker-compose.yml up -d --build
```

</details>

<details>
<summary><strong>Service Method</strong></summary>

### Service Method
```bash
# Linux systemd
sudo systemctl restart satoshi-shuffle

# macOS launchd
launchctl unload ~/Library/LaunchAgents/com.satoshi-shuffle.plist
launchctl load ~/Library/LaunchAgents/com.satoshi-shuffle.plist
```

</details>

<details>
<summary><strong>🔍 Device Connectivity</strong></summary>

## 🔍 Device Connectivity

</details>

<details>
<summary><strong>Check Device Reachability</strong></summary>

### Check Device Reachability
```bash
# Ping a BlockClock device
ping -c 3 192.168.1.100

# From Docker container
docker exec -it satoshi-shuffle ping -c 3 192.168.1.100
```

</details>

<details>
<summary><strong>Test BlockClock API</strong></summary>

### Test BlockClock API
```bash
# Test device API (displays time)
curl -v http://192.168.1.100/api/show/time

# Test device API (displays custom text)
curl -v http://192.168.1.100/api/show/text/BITCOIN
```

</details>

<details>
<summary><strong>🛠️ Updating Satoshi Shuffle</strong></summary>

## 🛠️ Updating Satoshi Shuffle

</details>

<details>
<summary><strong>Standard Method</strong></summary>

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

</details>

<details>
<summary><strong>Docker Method</strong></summary>

### Docker Method
```bash
# Get latest code
git pull

# Rebuild and restart container
docker-compose -f docker/docker-compose.yml up -d --build
```

</details>

<details>
<summary><strong>🔌 Port Management</strong></summary>

## 🔌 Port Management

</details>

<details>
<summary><strong>Check Port Usage</strong></summary>

### Check Port Usage
```bash
# Check if port 5010 is in use
lsof -i :5010

# Alternative method
netstat -tuln | grep 5010
```

</details>

<details>
<summary><strong>Change Port (Python Installation)</strong></summary>

### Change Port (Python Installation)
```bash
# Edit the web application file
nano webapp/blockclock_web.py

# Find this line and change port number:
# app.run(debug=False, host='0.0.0.0', port=5010, use_reloader=True)
```

</details>

<details>
<summary><strong>Change Port (Docker Installation)</strong></summary>

### Change Port (Docker Installation)
```bash
# Edit docker-compose file
nano docker/docker-compose.yml

# Change port mapping, e.g., from:
# "5010:5010" to "5011:5010"
```

</details>

<details>
<summary><strong>🔒 Service Management</strong></summary>

## 🔒 Service Management

</details>

<details>
<summary><strong>Setting Up Service (Linux)</strong></summary>

### Setting Up Service (Linux)
```bash
# Create systemd service file
sudo nano /etc/systemd/system/satoshi-shuffle.service

# Enable service to start at boot
sudo systemctl enable satoshi-shuffle

# Start service
sudo systemctl start satoshi-shuffle
```

</details>

<details>
<summary><strong>Setting Up Service (macOS)</strong></summary>

### Setting Up Service (macOS)
```bash
# Create launchd plist file
nano ~/Library/LaunchAgents/com.satoshi-shuffle.plist

# Load service
launchctl load -w ~/Library/LaunchAgents/com.satoshi-shuffle.plist
```

</details>

<details>
<summary><strong>💻 Screen Session (Alternative to nohup)</strong></summary>

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

</details>

<details>
<summary><strong>🔏 Docker-Specific Commands</strong></summary>

## 🔏 Docker-Specific Commands

</details>

<details>
<summary><strong>Container Management</strong></summary>

### Container Management
```bash
# Enter container shell
docker exec -it satoshi-shuffle /bin/bash

# View container details
docker inspect satoshi-shuffle

# Check container resource usage
docker stats satoshi-shuffle
```

</details>

<details>
<summary><strong>Docker Volumes</strong></summary>

### Docker Volumes
```bash
# List Docker volumes
docker volume ls

# Check volume details
docker volume inspect satoshi-shuffle_config
```

</details>

<details>
<summary><strong>📡 Network Troubleshooting</strong></summary>

## 📡 Network Troubleshooting

</details>

<details>
<summary><strong>Network Diagnostics</strong></summary>

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

</details>

<details>
<summary><strong>🧹 Cleanup Operations</strong></summary>

## 🧹 Cleanup Operations

</details>

<details>
<summary><strong>File Cleanup</strong></summary>

### File Cleanup
```bash
# Remove log files
rm logs/*.log

# Remove archived logs
rm -rf logs/archive/*
```

</details>

<details>
<summary><strong>Docker Cleanup</strong></summary>

### Docker Cleanup
```bash
# Remove container and images
docker-compose -f docker/docker-compose.yml down --rmi all

# Remove volumes too (CAUTION: Deletes all configuration!)
docker-compose -f docker/docker-compose.yml down -v

# System-wide Docker cleanup
docker system prune
```

</details>

<details>
<summary><strong>📂 Backup and Restore</strong></summary>

## 📂 Backup and Restore

</details>

<details>
<summary><strong>Configuration Backup</strong></summary>

### Configuration Backup
```bash
# Manual backup of config file
cp config/blockclock.conf config/blockclock.conf.backup

# Full directory backup
tar -czvf satoshi-shuffle-backup.tar.gz config/ logs/
```

</details>

<details>
<summary><strong>Docker Volume Backup</strong></summary>

### Docker Volume Backup
```bash
# Create a backup container and copy from volume
docker run --rm -v satoshi-shuffle_config:/backup -v $(pwd):/host alpine cp -r /backup /host/config-backup
```

</details>


---

# 📘 Satoshi Shuffle – Quick FAQ & Troubleshooting

<details><summary><strong>Troubleshooting</strong></summary>

```
# 🛠 Troubleshooting Guide

This guide provides solutions to common issues when using Satoshi Shuffle. **Follow the steps carefully based on your problem.**  


---


## 🔌 Connection Issues

### **Web Interface Not Accessible**  

**Symptoms:** Cannot access `http://localhost:5010`  

✅ **Fix Steps:**  
1. **Check if the application is running:**  
   ```bash
   ps aux | grep blockclock_web.py  # For Python installs
   docker ps | grep satoshi-shuffle  # For Docker installs
   ```

2. **Restart the application:**  
   ```bash
   sudo systemctl restart satoshi-shuffle  # Linux
   docker restart satoshi-shuffle  # Docker
   ```

3. **Check firewall settings:**  
   ```bash
   sudo ufw allow 5010  # Linux users
   ```


---


### **BlockClock Device Not Reachable**  

**Symptoms:**  
- BlockClock not displaying text  
- "Device not reachable" error  

✅ **Fix Steps:**  
1. **Verify network connection:**  
   ```bash
   ping 192.168.1.100  # Replace with your BlockClock IP
   ```

2. **Check IP Address in Configuration:**  
   ```bash
   nano config/blockclock.conf  # Ensure the correct IP is set
   ```

3. **Restart your BlockClock**  
   - Unplug the power, wait **30 seconds**, then plug it back in  

4. **Ensure your computer and BlockClock are on the same network.**  


---


## 📺 Display Issues

### **Custom Text Not Appearing**  

**Symptoms:**  
- Text rotation is running, but no custom text appears on BlockClock  

✅ **Fix Steps:**  
1. **Check if rotation is active in the Web UI**  
   - Open `http://localhost:5010`  
   - Ensure "Text Rotation" is set to **ON**  

2. **Verify Text Settings:**  
   - Custom text **must be 7 characters or less**  
   - Only **letters, numbers, and underscores** are supported  

3. **Restart the Application:**  
   ```bash
   sudo systemctl restart satoshi-shuffle  # Linux
   docker restart satoshi-shuffle  # Docker
   ```


---


## 🚀 Application Issues

### **Unexpected Crashes**  

**Symptoms:** Application stops unexpectedly or exits with errors.  

✅ **Fix Steps:**  
1. **Check logs for errors:**  
   ```bash
   tail -n 50 logs/blockclock.log  # View last 50 log lines
   tail -f logs/blockclock.log  # View live log updates
   ```

2. **Common Errors & Fixes:**  
   - `"Connection refused"` → BlockClock is offline → **Check device connectivity**  
   - `"Permission denied"` → Run as administrator:  
     ```bash
     sudo python3 webapp/blockclock_web.py
     ```

3. **Reinstall dependencies:**  
   ```bash
   pip install --upgrade -r requirements.txt
   ```


---


### **Rate Limiting Errors**  

**Symptoms:** "Rate limited" message when sending custom text  

✅ **Solution:**  
- BlockClock enforces a **70-second cooldown** between text updates  
- Wait before sending another request  


---


## 🖥 Installation Issues

### **Python Installation Problems**  

✅ **Fix Steps:**  
1. **Update pip first:**  
   ```bash
   python3 -m pip install --upgrade pip
   ```

2. **Manually install dependencies:**  
   ```bash
   pip install Flask requests
   ```


---


### **Docker Installation Problems**  

✅ **Fix Steps:**  
1. **Check if Docker is running:**  
   ```bash
   docker --version
   docker-compose --version
   ```

2. **Restart Docker:**  
   ```bash
   systemctl restart docker  # Linux
   ```

3. **Check container logs for errors:**  
   ```bash
   docker logs satoshi-shuffle
   ```


---


---

## 🔄 Restarting All Components  

If all else fails, try this **full reset sequence**:  

```bash
# Stop the application (based on installation type)

# ❌ Mac does NOT use systemctl  
# ✅ For One-Click Install & Python Users (Mac & Linux)  
pkill -f blockclock_web.py  # Stop any running process

# ✅ For Docker Users (Mac, Linux, Windows)  
docker-compose -f docker/docker-compose.yml down  # Stop Docker container

# ✅ For Linux Users who manually set up systemd (NOT for Mac)  
sudo systemctl stop satoshi-shuffle  # Stop systemd service

# Restart Your BlockClock
# (Unplug power, wait 30 seconds, then plug back in)

# Restart Satoshi Shuffle

# ✅ For One-Click Install & Python Users (Mac & Linux)  
python webapp/blockclock_web.py  # Restart manually

# ✅ For Docker Users (Mac, Linux, Windows)  
docker-compose -f docker/docker-compose.yml up -d  # Restart Docker container

# ✅ For Linux Users who manually set up systemd (NOT for Mac)  
sudo systemctl start satoshi-shuffle  # Restart systemd service
```


---


## 📡 Checking Network Connectivity  

For deeper network troubleshooting:  

1. **Check your IP address:**  
   ```bash
   ifconfig  # macOS/Linux
   ipconfig  # Windows
   ```

2. **Test connectivity to your router:**  
   ```bash
   ping 192.168.1.1  # Replace with your router’s IP
   ```

3. **Trace network path to BlockClock:**  
   ```bash
   traceroute 192.168.1.100  # macOS/Linux
   tracert 192.168.1.100  # Windows
   ```


---


## ✅ Need More Help?  

If you're still having issues:  
📌 **Check the [GitHub Issues](https://github.com/bevstr/satoshi-shuffle/issues)**  
📌 **Join the community for help**  

✅ **Now that you’ve resolved your issue, continue with:**  
- [Configuration Guide](configuration.md)  


```
</details>


<details><summary><strong>One-Click Install</strong></summary>

```
# One-Click Script Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle using the interactive installation script. **This is the recommended method for most users.**

---

## 📌 Before You Begin

The One-Click Script will handle most of the installation process for you, but **you need to install Python first**.


<details>
<summary><b>Installing Python - click to expand</b></summary>

You need Python 3.6 or higher. Follow the instructions for your operating system:

#### **MacOS**  
1. **Check if Homebrew is installed**  
   Open **Terminal** and run:  
   ```bash
   brew --version
   ```
   If you see "command not found," install Homebrew:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   In **Terminal** run:  
   ```bash
   python3 --version
   ```
   If you see no version then

2. **Install Python**  
   ```bash
   brew install python
   ```

#### **Ubuntu/Debian (Linux)**  
```bash
sudo apt update && sudo apt install python3 python3-pip
```

#### **Windows**  
1. Download Python from [python.org](https://www.python.org/downloads/)  
2. Run the installer and check **"Add Python to PATH"**  
3. Click **Install** and wait for it to finish  

### Verify Python Installation

1. Open **Terminal (Mac/Linux)** or **Command Prompt (Windows)**  
2. Run the following command to check your Python version:  
   ```bash
   python --version  # or python3 --version on some systems
   ```  
   It should return version **3.6 or higher**.
</details>
<br>

💡 **Need more details?** Check the [Dependencies Guide](dependencies.md) for complete system requirements and installation prerequisites.

---

## 🔧 What This Script Does

The One-Click Script will **automatically**:  
✅ Install required Python packages  
✅ Set up configuration files  
✅ Connect to your BlockClock devices  
✅ Create directories for logs and data  

---

## 🚀 Installation Steps

### Step 1: Download the Repository

Create a folder where you want to locate the files and now open terminal in that folder 

To install Satoshi Shuffle, **you first need to download the code**:

<details>
<summary><b>Option 1: Using Git (Recommended)</b></summary>

```bash
git clone https://github.com/bevstr/satoshi-shuffle.git
cd satoshi-shuffle
```
</details>

<details>
<summary><b>Option 2: Manual Download</b></summary>

1. Go to **[Satoshi Shuffle GitHub](https://github.com/bevstr/satoshi-shuffle)**  
2. Click the **green "Code" button** → **Download ZIP**  
3. Extract the ZIP file to a folder on your computer  
4. Open **Terminal/Command Prompt** and navigate to that folder  
</details>

---

### Step 2: Run the Installation Script

Once inside the **satoshi-shuffle** folder, run:  
```bash
python3 install.py  # Mac/Linux
py -3 install.py    # Windows
```
or 
```bash
python install.py
```

**If you have multiple Python versions installed**, use:  
```bash
python3 install.py  # Mac/Linux
py -3 install.py    # Windows
```

---

### Step 3: Follow the Interactive Prompts  

The script will ask you for:  
- **BlockClock device details** (name, IP, password)  
- **Custom text options** (Bitcoin-related phrases)  
- **Timing settings** (how often text appears)  

<details>
<summary><b>Example Configuration</b></summary>

```
Device 1:
  Name: Living Room Clock
  IP Address: 192.168.1.100
  Password: (leave blank if none)

Enter custom text options (max 7 characters each, separated by commas): BITCOIN, HODLER, BTFD

Clock refresh time options:
  1) 5 minutes
  2) 10 minutes
  3) 15 minutes
Choose an option (1-3): 2

Number of built-in screens between text (default: 3): 2
```
</details>

---

### Step 4: Running Satoshi Shuffle

<details>
<summary><b>Option 1: Start Manually</b></summary>

```bash
python webapp/blockclock_web.py
```
</details>

<details>
<summary><b>Option 2: Run in Background</b></summary>

```bash
nohup python3 webapp/blockclock_web.py > logs/webapp.log 2>&1 &
```
</details>

<details>
<summary><b>Option 3: Set Up Automatic Startup (Using Cron)</b></summary>

If you want Satoshi Shuffle to **start automatically** when you boot your system:

#### **For Linux/macOS Users:**

1. **Open your terminal** and edit your crontab:
   ```bash
   crontab -e
   ```
   
   > Note: This will open the crontab file in your default text editor.

2. **Add the following line** at the end of the file:
   ```bash
   @reboot cd /full/path/to/satoshi-shuffle && ./start_SatoshiShuffle.sh > logs/cron.log 2>&1
   ```
   
   > Replace `/full/path/to/satoshi-shuffle` with the actual full path to your installation.

3. **Save and exit** the editor:
   - For nano: Press `Ctrl+O` to save, then `Enter`, then `Ctrl+X` to exit
   - For vim: Press `Esc`, then type `:wq` and press `Enter`

4. **Verify your crontab entry** was saved:
   ```bash
   crontab -l
   ```

#### **For Windows Users:**

1. Create a shortcut to `start_SatoshiShuffle.bat` (you may need to create this batch file)
   
2. Place the shortcut in your Startup folder:
   - Press `Win+R`, type `shell:startup` and press `Enter`
   - Copy your shortcut into the folder that opens

3. **Create start_SatoshiShuffle.bat** with the following content:
   ```batch
   @echo off
   cd /d "C:\path\to\satoshi-shuffle"
   python webapp\blockclock_web.py
   ```

#### **Testing Your Automatic Startup**

To verify your autostart configuration:

1. **Restart your computer**
2. **Wait about 1-2 minutes** after login for the application to start
3. **Open your browser** and navigate to `http://localhost:5010`
4. **Check the logs** if the web interface isn't responding:
   ```bash
   cat logs/cron.log
   ```

If you encounter any issues with the cron job, check the `logs/cron.log` file for error messages.
</details>

---

## 🛠 Troubleshooting

If you run into problems:  

<details>
<summary><b>Common Troubleshooting Steps</b></summary>

- **Check logs:**  
  ```bash
  tail -f logs/blockclock.log
  ```  

- **Manually restart the application:**
  ```bash
  # Find and kill any running instances
  pkill -f blockclock_web.py
  
  # Start it again
  python webapp/blockclock_web.py
  ```

- **Verify your BlockClock is reachable:**
  ```bash
  ping 192.168.1.100  # Replace with your BlockClock's IP
  ```

For more help, check the [Troubleshooting Guide](docs/troubleshooting.md).
</details>

---

## ✅ Next Steps  

🚀 Now that you've installed Satoshi Shuffle:  
- Configure your settings → **[Configuration Guide](docs/configuration.md)**  
- Learn how to manage BlockClock devices → **[Web Interface Guide](docs/web-interface.md)**  
- Need more help? → **[Troubleshooting](docs/troubleshooting.md)**
```
</details>


<details><summary><strong>Docker Install</strong></summary>

```
# 📌 Docker Installation Guide (Updated)

This guide provides detailed instructions for installing **Satoshi Shuffle** using **Docker containers**.  
💪 **This is the recommended installation method** because it eliminates dependency issues.  
💪 **Even beginners can follow these steps to get started quickly!**

---

## 🔹 Before You Begin

To install Satoshi Shuffle via Docker, you need:  
- **Docker**  
- **Docker Compose**  

💡 If you're new to Docker, follow the **installation steps below** before proceeding.

<details>
  <summary>🔹 Click to expand Docker installation instructions</summary>

### **MacOS**
1. **Check if Homebrew is installed**  
   Open **Terminal** and run:  
   ```bash
   brew --version
   ```
   If it returns "command not found," install Homebrew:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Docker**  
   ```bash
   brew install --cask docker
   brew install docker-compose
   ```

3. **Start Docker Desktop**  
   Open **Docker Desktop** and wait for it to finish loading.

---

### **Ubuntu/Debian (Linux)**
```bash
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER  # Add yourself to the Docker group
```
Then **restart your machine** for the changes to take effect.

---

### **Windows**
1. Download **Docker Desktop** from [docker.com](https://www.docker.com/products/docker-desktop).  
2. Install and **restart your computer**.  
3. Open **Docker Desktop** and wait until it's fully running.
</details>

---

## 2️⃣ Verify Docker Installation
Run these commands to ensure Docker is installed correctly:  
```bash
docker --version
docker-compose --version
```
Both should return version numbers without errors.

---

## 🚀 Installation Steps

### 3️⃣ Download the Repository
#### To install Satoshi Shuffle, 
1. Create a folder where you want to locate the files and now open terminal in that folder 
2. **download the code by pasting below in terminal**:

#### **Option 1: Using Git (Recommended)**
```bash
git clone https://github.com/bevstr/satoshi-shuffle.git
cd satoshi-shuffle
```

#### **Option 2: Manual Download**
1. Go to **[Satoshi Shuffle GitHub](https://github.com/bevstr/satoshi-shuffle)**  
2. Click the **green "Code" button** → **Download ZIP**  
3. Extract the ZIP file to the folder on your computer  

---

### 4️⃣ Build and Start the Docker Container
Run the following command in Terminal inside the **`satoshi-shuffle`** folder:
```bash
docker-compose -f docker/docker-compose.yml up -d
```

💪 **This command will:**  
- Build the Docker image  
- Start the container in the background  
- Expose the web interface on port `5010`  

---

### 5️⃣ Configure Your Settings in the Web App
Once the container is running, open your browser and go to:  
```
http://localhost:5010
```

Here you **MUST configure the variables** before using the app. For more detailed information, refer to the [Configuration Guide](docs/configuration.md).

🛠 **In the Web App, configure your settings:**
1. **Go to the settings page** (inside the web interface).  
2. **On Devices Tab, enter your BlockClock Name and IP address.**  
3. **On Text Options Tab, add or remove Text Options.**  
4. **On Timing Tab, choose Refresh Time and Number of Natural Display Values.**  
5. **On Systems Tab, change defaults if needed.**  
6. **Save your settings.**  
7. **Return to Home Page, Click the Green Start Button.**  

That’s it! 🎉 Your BlockClock will now display your custom text.

---

## 🔄 Managing the Container
Here are some useful commands for managing your container:

### **Stop the container**  
```bash
docker-compose -f docker/docker-compose.yml down
```

### **Restart the container**  
```bash
docker-compose -f docker/docker-compose.yml up -d
```

### **Check live logs**  
```bash
docker logs -f satoshi-shuffle
```

### **Access the container shell**  
```bash
docker exec -it satoshi-shuffle /bin/bash
```
<details>
<summary><strong>🔄 How to Update the App Later</strong></summary>

If you've already installed Satoshi Shuffle and want to update it to the latest version from GitHub, just follow these steps:

1. **Open a terminal inside your container** (or SSH into it if you're running it remotely).

2. **Navigate to the `docker` folder** inside the app directory:

   ```bash
   cd docker
   ```

3. **Run the update script** to automatically pull the latest changes and rebuild the app:

   ```bash
   bash update.sh
   ```
      ```bash
   # Or if you've made it executable: ./update.sh
   ```


This script will:
- 🧠 Pull the latest code from the current Git branch
- 🔨 Rebuild the Docker container
- 🚀 Restart the app with the new changes

Once complete, open your browser and go to either:

- `http://localhost:5010` (if you're running the container on your local machine)
- or `http://<container-ip>:5010` (replace `<container-ip>` with the actual IP address of your container)

Then click **Play** to start the app. ✅

</details>



---

## 🛠 Troubleshooting
If you encounter any issues:

### **1️⃣ Check if Docker is running**  
```bash
systemctl status docker  # Linux
```

### **2️⃣ Port Conflict (Port 5010 Already in Use)**
- Open **`docker-compose.yml`**  
- Change this line:
  ```yaml
  ports:
    - "5011:5010"
  ```
- Restart the container.

### **3️⃣ Check Container Logs**
If your app isn’t working as expected, check the logs:
```bash
docker logs satoshi-shuffle
```

---

## ✅ Next Steps
🚀 Now that you’ve installed Satoshi Shuffle:  
- **Configure your settings in the web interface** (http://localhost:5010)  
- **Explore all features inside the web app**  
- **Need more help?** Check the [Troubleshooting Guide](docs/troubleshooting.md)  

---



```
</details>


<details><summary><strong>Python Install</strong></summary>

```
# Python Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle using Python.  
**This method is best for advanced users who want full control over the installation.**

---

## 📌 Before You Begin

Before installing, ensure you have:  
✅ **Python 3.6 or higher** installed  
✅ **pip (Python package manager)** installed  
✅ **Terminal (Mac/Linux) or Command Prompt (Windows)** available 

💡 **Need more details?** Check the [Dependencies Guide](dependencies.md) for complete system requirements and installation prerequisites.



### Step 1: Install Python

#### **MacOS**  
1. **Check if Homebrew is installed**  
   Open **Terminal** and run:  
   ```bash
   brew --version
   ```
   If you see "command not found," install Homebrew:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**  
   ```bash
   brew install python
   ```

#### **Ubuntu/Debian (Linux)**  
```bash
sudo apt update && sudo apt install python3 python3-pip
```

#### **Windows**  
1. Download Python from [python.org](https://www.python.org/downloads/)  
2. Run the installer and check **"Add Python to PATH"**  
3. Click **Install** and wait for it to finish  

### Step 2: Verify Python Installation

1. Open **Terminal (Mac/Linux)** or **Command Prompt (Windows)**  
2. Run the following command to check your Python version:  
   ```bash
   python --version  # or python3 --version
   ```  
   It should return version **3.6 or higher**.  

3. Check if `pip` is installed:  
   ```bash
   pip --version  # or pip3 --version
   ```  

---

## 🚀 Installation Steps

### Step 1: Download the Repository

To install Satoshi Shuffle, **you first need to download the code**:

#### **Option 1: Using Git (Recommended)**
```bash
git clone https://github.com/bevstr/satoshi-shuffle.git
cd satoshi-shuffle
```

#### **Option 2: Manual Download**
1. Go to **[Satoshi Shuffle GitHub](https://github.com/bevstr/satoshi-shuffle)**  
2. Click the **green "Code" button** → **Download ZIP**  
3. Extract the ZIP file to a folder on your computer  
4. Open **Terminal/Command Prompt** and navigate to that folder  

---

### Step 2: Install Dependencies

Run this command to install all required Python packages:  
```bash
pip install -r requirements.txt
```

**If you have multiple Python versions installed**, use:  
```bash
python3 -m pip install -r requirements.txt  # Mac/Linux
py -3 -m pip install -r requirements.txt    # Windows
```

This installs:  
✅ Flask (web server)  
✅ Requests (HTTP client)  
✅ Other dependencies needed for the application  

---

### Step 3: Configure Your Settings

Before running Satoshi Shuffle, you need to **set up your configuration file**.

1. Navigate to the `config` directory:  
   ```bash
   cd config
   ```

2. Create a new configuration file:  
   ```bash
   cp blockclock.conf.example blockclock.conf
   ```

3. Open the file for editing:  
   ```bash
   nano blockclock.conf  # For Linux/Mac users
   notepad blockclock.conf  # For Windows users
   ```

4. **Example Configuration File:**  
   ```bash
   DEVICE_1_NAME="Living Room Clock"
   DEVICE_1_IP="192.168.1.100"
   DEVICE_1_PASSWORD=""
   
   TEXT_OPTIONS=("BITCOIN" "HODLER" "BTFD")
   CLOCK_REFRESH_TIME=300
   DISPLAYS_BETWEEN_TEXT=3
   ```

5. **Save and exit** (For nano, press `CTRL+X`, then `Y`, then `Enter`).

---

### Step 4: Start the Application

#### **Option 1: Run Directly**
```bash
python webapp/blockclock_web.py
```

#### **Option 2: Run in Background**
```bash
nohup python3 webapp/blockclock_web.py > logs/webapp.log 2>&1 &
```

#### **Option 3: Set Up as a Service (Auto-Start on Boot)**
If you want Satoshi Shuffle to **start automatically** when you boot your system:  
```bash
sudo systemctl enable satoshi-shuffle
sudo systemctl start satoshi-shuffle
```

---

## 🛠 Troubleshooting

If you run into problems:  

- **Check logs:**  
  ```bash
  tail -f logs/blockclock.log
  ```  
- **Restart Satoshi Shuffle:**  
  ```bash
  pkill -f blockclock_web.py
python webapp/blockclock_web.py  # Restart manually
  ```  

For more help, check the [Troubleshooting Guide](docs/troubleshooting.md).  

---

## ✅ Next Steps  

🚀 Now that you’ve installed Satoshi Shuffle:  
- Configure your settings → **[Configuration Guide](docs/configuration.md)**  
- Learn how to manage BlockClock devices → **[Web Interface Guide](docs/web-interface.md)**  
- Need more help? → **[Troubleshooting](docs/troubleshooting.md)**  

```
</details>


<details><summary><strong>Dependencies</strong></summary>

```
# 📦 Satoshi Shuffle Dependencies

This guide provides a complete list of system requirements and software dependencies needed to run Satoshi Shuffle.

---

## 🌐 Common Requirements (All Installation Methods)

These requirements apply regardless of which installation method you choose:

✅ **Network connection** to your BlockClock device(s)  
✅ **BlockClock Mini or Micro** with:
   - Device on the same network as your computer
   - Static IP recommended for stability
   - Power and internet connectivity

<details>
<summary><b>How to find your BlockClock's IP address</b></summary>

To find your BlockClock's IP address:
- Check your router's connected devices list
- Use a network scanner app (like Fing for mobile)
- Check the BlockClock settings menu directly on the device
- Look for devices named "Coinkite" or "BlockClock" in your network

For most home networks, the IP will typically be in the form of 192.168.1.x or 10.0.0.x
</details>

---

## 🧩 Installation-Specific Dependencies

### Installation Options

<details>
<summary><b>1️⃣ Docker Installation (Recommended, Try it if you havn't its easy)</b></summary>

For Docker-based installation, you'll need:

✅ **Docker Engine** - [Docker installation guide](https://docs.docker.com/engine/install/)  
✅ **Docker Compose** - Usually included with Docker Desktop  
✅ **200MB+ free disk space** (for Docker images, volumes, and application)  
✅ **Git** (recommended for downloading the repo)  

**Note:** Using Docker eliminates the need to install Python or any Python packages directly on your system.

**Basic Docker commands you'll use:**
```bash
# Build and start container
docker-compose -f docker/docker-compose.yml up -d

# Check container status
docker ps | grep satoshi-shuffle

# View logs
docker logs satoshi-shuffle
```

**Advantages of Docker Installation:**
- Isolated environment
- Consistent across different systems
- No Python setup required
- Easy to update and maintain

[Go to Docker Installation Guide](installation-docker.md)
</details>


<details>
<summary><b>2️⃣ One-Click Script Installation </b></summary>

The One-Click Script handles most dependencies automatically but requires:

✅ **Python 3.6 or higher** - [How to install](#installing-python)  
✅ **100MB+ free disk space** for application and logs  
✅ **Basic command line knowledge**

**What the script installs for you:**
- All required Python packages (Flask, Requests, etc.)
- Directory structure setup
- Configuration file creation
- Log rotation setup

**Advantages of One-Click Installation:**
- Simplest setup process
- Guided interactive configuration
- Automatic dependency installation
- Works on most operating systems

[Go to One-Click Installation Guide](installation-one-click.md)
</details>

<details>
<summary><b>3️⃣ Standard Python Installation (For advanced users)</b></summary>

For direct Python installation, you'll need:

✅ **Python 3.6 or higher** - [How to install](#installing-python)  
✅ **pip** (Python package manager)  
✅ **100MB+ free disk space** for application and logs  
✅ **Git** (recommended for downloading the repo)  
✅ **These Python packages** (installed via requirements.txt):
   - Flask (web framework)
   - Requests (HTTP library)
   - Flask-WTF (form handling)

**Commands to install Python packages:**
```bash
# Navigate to project directory after downloading
cd satoshi-shuffle

# Install dependencies
pip install -r requirements.txt

# Or if you have multiple Python versions
python3 -m pip install -r requirements.txt
```

**Advantages of Python Installation:**
- More control over the installation
- Direct access to all components
- No containerization overhead
- Easier debugging and customization

[Go to Python Installation Guide](installation-python.md)
</details>

---

## 💻 Operating System Support

<details>
<summary><b>View operating system compatibility details</b></summary>

✅ **Linux** (Ubuntu/Debian recommended)
- Full support for all installation methods
- Systemd service integration available
- Best performance and reliability

✅ **macOS**
- Full support for all installation methods
- Launchd service integration available
- Works on both Intel and Apple Silicon

✅ **Windows**
- Limited support for One-Click and Python installations
- Docker installation recommended for Windows users
- May require additional setup steps
</details>

---

## 🌍 Network Requirements

<details>
<summary><b>View network requirements details</b></summary>

Your system must allow communication with your BlockClock:

✅ **Port 5010** must be available on your system (used by the web interface)  
✅ **Outgoing HTTP requests** must be allowed to reach your BlockClock  
✅ **No firewall blocks** between your computer and the BlockClock  

**Checking network connectivity:**
```bash
# Check if your BlockClock is reachable
ping 192.168.1.100  # Replace with your BlockClock's IP

# Check if port 5010 is available on your system
lsof -i :5010  # On macOS/Linux
netstat -ano | findstr :5010  # On Windows
```

If port 5010 is already in use, you can change the port in the configuration.
</details>

---

## <a id="installing-python"></a>📌 Installing Python

<details>
<summary><b>Python installation instructions</b></summary>

### MacOS
```bash
# Using Homebrew
brew install python

# Verify installation
python3 --version  # Should show 3.6 or higher
```

### Ubuntu/Debian
```bash
sudo apt update && sudo apt install python3 python3-pip

# Verify installation
python3 --version  # Should show 3.6 or higher
```

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer and **check "Add Python to PATH"**
3. Verify in Command Prompt: `python --version`
</details>

---

## 🔍 Verifying Dependencies

<details>
<summary><b>Commands to verify your dependencies are properly installed</b></summary>

### Check Python and pip installation
```bash
# Check Python version
python --version  # or python3 --version

# Check pip installation
pip --version  # or pip3 --version
```

### Check Docker installation
```bash
# Check Docker version
docker --version

# Check Docker Compose version
docker-compose --version
```

### Check network connectivity
```bash
# Check if your BlockClock is reachable
ping 192.168.1.100  # Replace with your BlockClock's IP
```
</details>

---

## 🛠 Need More Help?

If you encounter dependency issues:
- Check the [Troubleshooting Guide](troubleshooting.md)
- Verify missing packages with `pip list`
- Ensure your network settings allow connections to your BlockClock

Choose your installation method:
- [One-Click Installation](installation-one-click.md) (Recommended for most users)
- [Python Installation](installation-python.md) (For advanced users)
- [Docker Installation](installation-docker.md) (For those familiar with containers)
```
</details>


<details><summary><strong>Configuration</strong></summary>

```
# Configuration Guide

This guide explains how to configure Satoshi Shuffle after installation.  
You'll learn how to **set up devices, customize text options, adjust timing, and manage system preferences**.

---

## 📌 Configuration Methods

You can configure Satoshi Shuffle in two ways:  
✅ **Web Interface (Recommended)** – Easy-to-use settings page with a graphical interface  
✅ **Manual Configuration File Editing** – Advanced users can modify `blockclock.conf`  

---

## 🎛 Using the Web Interface (Recommended)

### Step 1: Open the Web Interface  

1. Open your **web browser**  
2. Go to `http://localhost:5010`  
3. Click **Settings** in the top menu  

### Step 2: Add BlockClock Devices  

1. Click the **Devices** tab  
2. Click **"Add Device"**  
3. Enter:  
   - **Device Name** (e.g., "Living Room Clock")  
   - **IP Address** (e.g., "192.168.1.100")  
   - **Password** (if applicable)  
4. Click **"Save Settings"**  

✅ **Test Device Connectivity**  
- Click the **"Check"** button next to the IP address  
- If successful, the device is connected  

### Step 3: Customize Text Options  

1. Click the **Text Options** tab  
2. Click **"Add Text Option"**  
3. Enter custom text (max **7 characters**)  
4. Click **Save**  

🛑 **Text Limitations:**  
- Only **letters, numbers, and underscores** are supported  
- Spaces and special symbols **won’t display correctly**  

### Step 4: Adjust Display Timing  

1. Click the **Timing** tab  
2. Choose how often your custom text appears:  
   - **Clock Refresh Time:** 5, 10, 15, 30, or 60 minutes as chosen in BlockClock interface  
   - **Displays Between Custom Text:** Number values you chose in BlockClock interface   
3. The app will calculate how frequently text will show  

### Step 5: System Settings & Backup  

- **Log Management:** Set how long logs are stored before deletion  
- **Theme Settings:** Choose between **light mode, dark mode, or system default**  
- **Backup Settings:** Click **Download Backup** to save settings  

---

## 📝 Editing the Configuration File Manually

For advanced users, you can **edit the configuration file manually**.

### Step 1: Locate the Configuration File  
The main config file is at:  
```bash
config/blockclock.conf
```

### Step 2: Open the File for Editing  
```bash
nano config/blockclock.conf  # Linux/Mac users
notepad config/blockclock.conf  # Windows users
```

### Step 3: Modify Configuration Settings  
```ini
# BlockClock Device Settings
DEVICE_1_NAME="Living Room Clock"
DEVICE_1_IP="192.168.1.100"
DEVICE_1_PASSWORD=""

# Custom Text Options
TEXT_OPTIONS=("BITCOIN" "HODLER" "FREEDOM")

# Clock Refresh Time (seconds): 300 (5min), 600 (10min), 900 (15min)
CLOCK_REFRESH_TIME=300

# Number of screens between custom text
DISPLAYS_BETWEEN_TEXT=3

# Log Retention Settings
LOG_ARCHIVE_DAYS=7
LOG_DELETE_DAYS=30

# Theme Options (light, dark, system)
DEFAULT_THEME="dark"
```

### Step 4: Save Changes and Restart  
```bash
pkill -f blockclock_web.py
python webapp/blockclock_web.py  # Restart manually  # Linux
docker restart satoshi-shuffle  # Docker users
```

✅ **Your new settings will now take effect!**  

---

## 🛠 Troubleshooting Configuration Issues

### **Problem: Custom text does not appear**  
✔ Ensure your **BlockClock is online and reachable**  
✔ Check **Timing Settings** → Text might be delayed based on rotation  

### **Problem: Cannot access web interface**  
✔ Restart the application  
```bash
pkill -f blockclock_web.py
python webapp/blockclock_web.py  # Restart manually  # Linux
docker restart satoshi-shuffle  # Docker users
```

For more troubleshooting, visit the [Troubleshooting Guide](troubleshooting.md).

---

## ✅ Next Steps

🚀 Now that you’ve configured Satoshi Shuffle:  
- Need more help? → **[Troubleshooting Guide](docs/troubleshooting.md)**  

```
</details>


<details><summary><strong>Full Documentation</strong></summary>

```
Version 1.0 - March 22, 2025

# Satoshi Shuffle Documentation

## Project Overview
Satoshi Shuffle provides tools to control Coinkite BlockClock Mini/Micro devices by displaying custom text messages that rotate on a configurable schedule. The project has evolved from a bash script to a full web application with multiple deployment options.

## Installation Methods

### 1. Basic Python Installation
**For:** Users with some technical knowledge who want direct control  
**Overview:** This method involves the user directly installing the Python application on their system. They would:
- Clone or download the repository
- Install Python dependencies via pip
- Configure their BlockClock devices manually
- Run the application directly with Python commands

This gives users the most control and visibility into how everything works, but requires some familiarity with Python and command-line operations.

**Detailed Guide:** See [Python Installation Guide](installation-python.md)

### 2. One-Click Script Installation
**For:** Semi-technical users who want a simplified setup but on their own machine  
**Overview:** The `install.py` script automates most of the setup process:
- Handles dependency installation
- Guides users through device configuration via prompts
- Sets up service files for auto-starting on boot
- Takes care of directory creation and permissions

This provides a middle ground - simpler than manual setup but still runs directly on the user's system without containers.

**Detailed Guide:** See [One-Click Script Installation Guide](installation-script.md)

### 3. Docker Installation
**For:** Users who prioritize simplicity and isolation  
**Overview:** The Docker approach containerizes the entire application:
- Users just need Docker installed on their system
- Everything runs in an isolated container
- Configuration is done in web app
- Updates can be applied by simply pulling a new image

This is the most hands-off approach, ideal for users who just want the application to work without worrying about the technical details or potentially interfering with their system.

**Detailed Guide:** See [Docker Installation Guide](installation-docker.md)

## Directory Structure

```
satoshi-shuffle/
├── README.md               # Main project documentation
├── LICENSE                 # MIT License
├── CHEATSHEET.md           # Command-line reference
├── config/                 # Configuration directory
│   └── blockclock.conf     # Main configuration file
├── docker/                 # Docker implementation
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md
├── docs/                   # Documentation
│   ├── configuration.md    # Configuration guide
│   ├── installation-*.md   # Installation guides
│   └── troubleshooting.md  # Troubleshooting guide
├── Images/                 # Screenshots directory
├── install.py              # One-click install script
├── logs/                   # Log directory
├── python/                 # Core Python module
│   └── blockclock.py       # Main control code
├── requirements.txt        # Python dependencies
├── start_SatoshiShuffle.sh # Startup script
└── webapp/                 # Web application code
```

## Usage and Configuration

After installation, you can configure and use Satoshi Shuffle through:

1. **Web Interface**: Access http://localhost:5010 (or configured port)
   - Control text rotation (start/stop)
   - Send one off Custom Texts to Blocckclock
   - Configure device settings
   - Customize text options
   - View logs and status

2. **Configuration File**: Edit `config/blockclock.conf` directly
   - Device IP addresses and credentials
   - Custom text options
   - Timing settings

Detailed usage instructions are available in the [Configuration Guide](configuration.md).

## Port Configuration

### Default Port
Satoshi Shuffle uses **port 5010** by default for its web interface. This choice was made because the commonly used port 5000 is often occupied by other services (especially on macOS where AirPlay Receiver uses port 5000).

### Troubleshooting Port Issues

If you encounter an error message like "Address already in use" when starting the application, it means port 5010 is already being used by another application on your system.

#### How to Change the Port

1. **Basic Python Installation**:
   Edit the `webapp/blockclock_web.py` file and change the port number:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5010, use_reloader=True)
   ```
   For example, change `port=5010` to `port=5011` or another available port.

2. **One-Click Script Installation**:
   The script handles port conflicts automatically by testing if port 5010 is available, and if not, moving to 5002, 5003, etc. until it finds an available port. If installation completes but the web interface isn't accessible, check the logs to see which port was actually used.

3. **Docker Installation**:
   Edit the `docker-compose.yml` file and change the port mapping:
   ```yaml
   ports:
     - "5010:5010"
   ```
   
   To use a different port on the host, change the first number:
   ```yaml
   ports:
     - "5011:5010"
   ```
   
   This maps port 5011 on the host to port 5010 inside the container.

## Common Issues and Troubleshooting

Common problems you might encounter:

1. **Device connectivity issues**: Ensure your BlockClock devices are on the same network
2. **Port conflicts**: See the port configuration section above
3. **Service not starting**: Check permissions and logs
4. **Custom text not appearing**: Verify configuration and check for synchronization issues

For detailed troubleshooting steps, see the [Troubleshooting Guide](troubleshooting.md).

## Command Line Operations

For quick reference to command-line operations, see the [Command Line Cheatsheet](../CHEATSHEET.md) which includes:

- Starting and stopping the application
- Checking status
- Viewing logs
- Configuration backup
- System maintenance

## Support and Contributing

If you encounter issues or have suggestions:

1. Check the [Troubleshooting Guide](troubleshooting.md) first
2. Review existing GitHub issues before creating a new one
3. When reporting issues, include:
   - Your operating system and version
   - Installation method used
   - Steps to reproduce the issue
   - Error messages and log output

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---
*This documentation is current as of March 22, 2025*
```
</details>
