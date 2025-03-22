# Python Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle directly using Python. This method is ideal for advanced users who want complete control over the installation and configuration process.

## What You'll Need

Before starting, make sure you have:

- Python 3.6 or higher installed
- pip (Python package manager)
- Internet connection
- Administrator/sudo privileges (optional, for service setup)
- At least one BlockClock device on your network

## Step 1: Download the Repository

First, get a copy of the Satoshi Shuffle code:

```bash
# Clone the repository using git
git clone https://github.com/yourusername/satoshi-shuffle.git

# Navigate into the project directory
cd satoshi-shuffle
```

Don't have git? You can also:
1. Go to https://github.com/yourusername/satoshi-shuffle
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file to a folder on your computer
5. Open your terminal/command prompt and navigate to that folder

## Step 2: Install Dependencies

Next, install the required Python packages:

```bash
# Install all dependencies
pip install -r requirements.txt
```

If you have multiple Python versions installed, you might need to use:

```bash
# On macOS/Linux
python3 -m pip install -r requirements.txt

# On Windows
py -3 -m pip install -r requirements.txt
```

This will install all the necessary libraries, including:
- Flask (web server)
- Requests (HTTP client)
- Other dependencies needed for the application

## Step 3: Configure Your Settings

Before running the application, you'll need to set up your configuration:

1. Navigate to the config directory:
   ```bash
   cd config
   ```

2. Create a new configuration file:
   ```bash
   # Copy the example config (if it exists)
   cp blockclock.conf.example blockclock.conf
   
   # Or create a new one if no example exists
   touch blockclock.conf
   ```

3. Edit the configuration file with your favorite text editor:
   ```bash
   # Using nano
   nano blockclock.conf
   
   # Or using vi
   vi blockclock.conf
   
   # Or simply open with your desktop text editor
   ```

4. Add your device information and preferences:
   ```
   # Device 1
   DEVICE_1_NAME="Living Room Clock"
   DEVICE_1_IP="192.168.1.100"
   DEVICE_1_PASSWORD=""
   
   # Device 2 (optional)
   DEVICE_2_NAME="Office Clock"
   DEVICE_2_IP="192.168.1.101"
   DEVICE_2_PASSWORD=""
   
   # Text options to display (separated by spaces)
   TEXT_OPTIONS=("BITCOIN" "HODLER" "FREEDOM" "SATOSHI" "BTFD")
   
   # Clock refresh time (in seconds): 300 (5min), 600 (10min), 900 (15min), 1800 (30min), 3600 (60min)
   CLOCK_REFRESH_TIME=300
   
   # Number of built-in screens to show between our text messages
   DISPLAYS_BETWEEN_TEXT=3
   ```

5. Return to the main directory:
   ```bash
   cd ..
   ```

## Step 4: Start the Application

Now you're ready to start the application:

### Option A: Using the Startup Script (Recommended)

The startup script handles the setup and monitoring for you:

```bash
# Make sure the script is executable (Linux/macOS)
chmod +x start_SatoshiShuffle.sh

# Run the startup script
./start_SatoshiShuffle.sh
```

### Option B: Direct Python Launch

If you prefer to run the application directly with Python:

```bash
# Start the Flask application
python webapp/blockclock_web.py
```

If you have multiple Python versions installed:

```bash
# On macOS/Linux
python3 webapp/blockclock_web.py

# On Windows
py -3 webapp/blockclock_web.py
```

## Step 5: Access the Web Interface

With the application running, open your web browser and navigate to:
```
http://localhost:5001
```

You should see the Satoshi Shuffle web interface. From here, you can:
- Start/stop the text rotation
- Send custom text on demand
- Monitor your BlockClock devices
- Access logs and status information

## Setting Up as a Service (Optional)

For a more permanent installation, you can set up Satoshi Shuffle as a service:

### On Linux (systemd)

1. Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/satoshi-shuffle.service
   ```

2. Add the following content (adjust paths as needed):
   ```
   [Unit]
   Description=Satoshi Shuffle Web App
   After=network.target

   [Service]
   User=YOUR_USERNAME
   WorkingDirectory=/path/to/satoshi-shuffle/webapp
   ExecStart=/usr/bin/python3 /path/to/satoshi-shuffle/webapp/blockclock_web.py
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable satoshi-shuffle
   sudo systemctl start satoshi-shuffle
   ```

4. Check service status:
   ```bash
   sudo systemctl status satoshi-shuffle
   ```

### On macOS (launchd)

1. Create a launchd plist file:
   ```bash
   nano ~/Library/LaunchAgents/com.satoshi-shuffle.plist
   ```

2. Add the following content (adjust paths as needed):
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.satoshi-shuffle</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/bin/python3</string>
           <string>/path/to/satoshi-shuffle/webapp/blockclock_web.py</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
       <key>KeepAlive</key>
       <true/>
       <key>StandardErrorPath</key>
       <string>/path/to/satoshi-shuffle/logs/error.log</string>
       <key>StandardOutPath</key>
       <string>/path/to/satoshi-shuffle/logs/output.log</string>
   </dict>
   </plist>
   ```

3. Load the service:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.satoshi-shuffle.plist
   ```

4. Check if it's running:
   ```bash
   launchctl list | grep satoshi-shuffle
   ```

### On Windows

1. Create a batch file (satoshi-shuffle.bat):
   ```batch
   @echo off
   cd /d C:\path\to\satoshi-shuffle
   python webapp\blockclock_web.py
   ```

2. Use Task Scheduler to create a task that runs this batch file at startup

## Troubleshooting

If you encounter issues:

- **Port conflicts**: If port 5001 is already in use, you can change it in the `webapp/blockclock_web.py` file (look for the `app.run` line)

- **Permission errors**: Make sure you have the necessary permissions for the directories

- **Dependency issues**: Ensure all dependencies are installed correctly

- **Logs**: Check the logs in the `logs/` directory for more information

## Advanced Configuration

You can modify more settings by:

- Editing the `config/blockclock.conf` file
- Modifying Python source files directly

Key files you might want to review:
- `python/blockclock.py` - Core functionality
- `webapp/routes.py` - Web interface logic
- `webapp/templates/` - HTML templates for the web interface

## Next Steps

After installation:
1. Continue to the [Configuration Guide](configuration.md) for additional setup options
2. Learn how to manage your BlockClock devices through the web interface
3. Explore the [Troubleshooting Guide](troubleshooting.md) if you encounter any issues