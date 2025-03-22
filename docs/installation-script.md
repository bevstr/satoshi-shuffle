# One-Click Script Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle using the interactive installation script. This is the recommended method for most users.

## Before You Begin

The One-Click Script will handle most of the installation process for you, but you'll need to have Python installed on your computer first.

### Step 1: Install Python

The only prerequisite you need to install manually is Python 3.6 or higher:

- **macOS**: Install using [Homebrew](https://brew.sh) with `brew install python` or download from [python.org](https://www.python.org/downloads/)
- **Ubuntu/Debian**: Open Terminal and run `sudo apt update && sudo apt install python3 python3-pip`
- **Windows**: Download and install from [python.org](https://www.python.org/downloads/)

### Step 2: Verify Python Installation

1. Open your Terminal (macOS/Linux) or Command Prompt (Windows)
2. Run the following command to check your Python version:
   ```bash
   python --version  # or python3 --version on some systems
   ```
3. Make sure it shows version 3.6 or higher

### What the Script Will Do For You

The One-Click Script will automatically:
- Install all required Python packages
- Set up your configuration file
- Configure connection to your BlockClock devices
- Create directories for logs and data
- Optionally set up as a system service

## Installation Steps

### Step 1: Download the Repository

First, get a copy of the Satoshi Shuffle code:

```bash
# Clone the repository using git
git clone https://github.com/bevstr/satoshi-shuffle.git

# Navigate into the project directory
cd satoshi-shuffle
```

Don't have git? You can also:
1. Go to https://github.com/bevstr/satoshi-shuffle
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file to a folder on your computer
5. Open your Terminal/Command Prompt and navigate to that folder

### Step 2: Run the Installation Script

The installation script will guide you through the setup process:

```bash
# Run the script with Python
python install.py
```

If you have multiple Python versions installed, you might need to use:

```bash
# On macOS/Linux
python3 install.py

# On Windows
py -3 install.py
```

### Step 3: Follow the Interactive Prompts

The script will ask you several questions:

1. **Installation Method** - Confirm you want to proceed with the interactive installation
2. **BlockClock Devices** - Enter information about your devices:
   - Device name (for your reference)
   - IP address of the device
   - Password (if your device has one set)
3. **Custom Text Options** - Enter the text messages you want displayed
4. **Timing Settings** - Configure how often your custom text appears:
   - Clock refresh time (how often the BlockClock updates its display)
   - Number of displays between custom text

Example configuration session:
```
=== BlockClock Configuration ===

Let's configure your BlockClock devices
You can add up to 5 devices. Leave the IP empty when done.

Device 1:
  Name (default: BlockClock Device 1): Living Room Clock
  IP Address: 192.168.1.100
  Password (if any, leave empty for none): 

Device 2:
  Name (default: BlockClock Device 2): Office Clock
  IP Address: 192.168.1.101
  Password (if any, leave empty for none): 

Device 3:
  Name (default: BlockClock Device 3): 
  IP Address: 

Now let's configure your custom text options
Default options: __GFY__, _BTFD_, __HODL_, SATOSHI, KIRSTY, BEVO_21
Enter custom text options (comma-separated, max 8 chars each) or press Enter to use defaults: BITCOIN,HODLER,TICK-TOCK

Clock refresh time options:
  1) 5 minutes (300 seconds) [default]
  2) 10 minutes (600 seconds)
  3) 15 minutes (900 seconds)
  4) 30 minutes (1800 seconds)
  5) 60 minutes (3600 seconds)
Choose an option (1-5): 2

Number of displays between text (default: 3): 2

With these settings, your custom text will appear every 20 minutes.
```

### Step 4: Service Installation

The script will offer to set up Satoshi Shuffle as a system service so it can:
- Start automatically when your computer boots
- Run in the background without requiring a terminal window

This requires administrator privileges:
- On Linux: The script will ask for your sudo password
- On macOS: The script will create a LaunchAgent for your user

If you decline service installation, you'll need to manually start the application each time.

### Step 5: Access the Web Interface

Once installation is complete, the script will provide a URL to access the web interface:

```
Installation Complete

BlockClock Control should now be running!
Open your web browser and navigate to: http://localhost:5001

You can use the web interface to configure your BlockClock devices,
customize text options, and control the text rotation.
```

Open your web browser and go to this address to continue setup.

## Troubleshooting

If you encounter issues during installation:

- **Python not found**: Make sure Python 3.6+ is installed and in your PATH
- **Permission errors**: Run the script with administrator privileges
- **Port conflicts**: If port 5001 is already in use, the script will try alternative ports
- **Device not found**: Ensure your BlockClock device is on the same network and powered on

For more help, see the [Troubleshooting Guide](troubleshooting.md).

## Next Steps

After installation:
1. Continue to the [Configuration Guide](configuration.md) for additional setup options
2. Learn how to manage your BlockClock devices through the web interface

## Manual Startup (If Not Using Service)

If you didn't set up the service or need to start the application manually:

```bash
# Navigate to your Satoshi Shuffle directory
cd path/to/satoshi-shuffle

# Start the application with the helper script
./start_SatoshiShuffle.sh

# Or directly with Python
python webapp/blockclock_web.py
```

For a complete list of system requirements and dependencies, see the [Dependencies List](dependencies.md).