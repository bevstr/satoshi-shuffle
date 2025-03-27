# Configuration Guide

This guide explains how to configure Satoshi Shuffle after installation. You'll learn how to customize device settings, text options, timing, and system preferences.

## Configuration Methods

There are two ways to configure Satoshi Shuffle:

1. **Web Interface (Recommended)**: Easy-to-use settings pages with a graphical interface
2. **Configuration File**: Direct editing of the `blockclock.conf` file

## Using the Web Interface

### Accessing Settings

1. Open your web browser and navigate to `http://localhost:5001`
2. Click on the "Settings" link in the navigation bar

### Device Configuration

The **Devices** tab lets you manage your BlockClock devices:

1. **Add Device**:
   - Click the "Add Device" button
   - Enter a name for the device (e.g., "Living Room BlockClock")
   - Enter the IP address of the device (e.g., "192.168.1.100")
   - Enter the password if your device has one set
   - Click "Save Settings" when done

2. **Test Device Connectivity**:
   - After adding a device, click the "Check" button next to its IP address
   - You'll see a message indicating whether the device is reachable

3. **Remove Device**:
   - Click the trash icon next to any device you want to remove

4. **Edit Device**:
   - Simply change any field and click "Save Settings"

### Text Options Configuration

The **Text Options** tab lets you customize the text messages:

1. **Add Text Option**:
   - Click the "Add Text Option" button
   - Enter your custom text (max 7 characters)
   - Note: Only letters, numbers, and underscores are allowed

2. **Remove Text Option**:
   - Click the trash icon next to any text option you want to remove

### Timing Configuration

The **Timing** tab controls how your custom text appears:

1. **Clock Refresh Time**:
   - Select how often your BlockClock updates its display
   - Options: 5 minutes, 10 minutes, 15 minutes, 30 minutes, 60 minutes
   - **Important**: This must match the "Screen Update Rate" setting in your BlockClock's preferences

2. **Displays Between Custom Text**:
   - Set how many built-in displays (price, block height, etc.) should appear between your custom text messages
   - Higher values mean your custom text appears less frequently

3. **Resulting Frequency**:
   - The interface will show you how often your custom text will appear based on your settings
   - Example: With 5-minute refresh and 3 displays between, custom text appears every 15 minutes

### System Settings

The **System** tab controls application behavior:

1. **Log Management**:
   - Archive logs after X days: How long to keep current logs before archiving
   - Archive logs when they reach X MB: Maximum size before logs are archived
   - Delete archived logs after X days: How long to keep archived logs

2. **Theme Settings**:
   - Set the default theme (light or dark)
   - You can also toggle dark mode using the switch in the navigation bar

### Backup & Restore

The **Backup & Restore** tab helps you save and recover your settings:

1. **Create Backup**:
   - Click "Download Backup" to save a copy of all your settings
   - Store this file in a safe location

2. **Restore from Backup**:
   - Click "Choose File" and select your backup file
   - Click "Restore from Backup"
   - Confirm the restoration when prompted

## Editing the Configuration File Directly

For advanced users or headless setups, you can edit the configuration file directly:

1. **Locate the file**: The main configuration file is at `config/blockclock.conf`

2. **Edit the file** with any text editor:
   ```bash
   nano config/blockclock.conf
   ```

3. **Configuration format**:
   ```
   # Device 1
   DEVICE_1_NAME="Living Room Clock"
   DEVICE_1_IP="192.168.1.100"
   DEVICE_1_PASSWORD=""
   
   # Device 2
   DEVICE_2_NAME="Office Clock"
   DEVICE_2_IP="192.168.1.101"
   DEVICE_2_PASSWORD=""
   
   # Text options to display (separated by spaces)
   TEXT_OPTIONS=("BITCOIN" "HODLER" "FREEDOM" "SATOSHI" "BTFD")
   
   # Clock refresh time in seconds: 300 (5min), 600 (10min), 900 (15min), 1800 (30min), 3600 (60min)
   CLOCK_REFRESH_TIME=300
   
   # Number of built-in screens to show between our text messages
   DISPLAYS_BETWEEN_TEXT=3
   
   # Log settings
   LOG_ARCHIVE_DAYS=1
   LOG_ARCHIVE_SIZE=10
   LOG_DELETE_DAYS=30
   
   # Theme
   DEFAULT_THEME="dark"  # options: "light", "dark", "system"
   ```

4. **Save the file** and restart the application for changes to take effect:
   ```bash
   # If using the startup script
   ./start_SatoshiShuffle.sh
   
   # If using Docker
   docker-compose -f docker/docker-compose.yml restart
   
   # If using a service
   sudo systemctl restart satoshi-shuffle  # Linux
   launchctl unload ~/Library/LaunchAgents/com.satoshi-shuffle.plist && launchctl load ~/Library/LaunchAgents/com.satoshi-shuffle.plist  # macOS
   ```

## Configuration Tips

### Text Limitations

BlockClock devices have specific text limitations:

- Maximum 7 characters per text message
- Only letters, numbers, and underscores are supported
- Spaces are not allowed
- Custom symbols may not display correctly

### Optimizing Display Frequency

To find the best balance for your custom text:

1. **More frequent**: Set "Displays Between Custom Text" to a lower number (1-2)
2. **Less frequent**: Set it to a higher number (4-5)
3. **Best practice**: Start with 3 and adjust based on your preference

### Multi-Device Synchronization

When configuring multiple devices:

1. All devices will display the same custom text at the same time
2. Make sure all devices are reachable on your network
3. All devices should have the same "Screen Update Rate" setting in their own preferences

## Next Steps

- Review the [Troubleshooting Guide](troubleshooting.md) for help with common issues
- Explore the [Command Line Cheatsheet](../CHEATSHEET.md) for advanced operations