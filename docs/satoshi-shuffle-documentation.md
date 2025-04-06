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

1. **Web Interface**: Access http://localhost:5001 (or configured port)
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
Satoshi Shuffle uses **port 5001** by default for its web interface. This choice was made because the commonly used port 5000 is often occupied by other services (especially on macOS where AirPlay Receiver uses port 5000).

### Troubleshooting Port Issues

If you encounter an error message like "Address already in use" when starting the application, it means port 5001 is already being used by another application on your system.

#### How to Change the Port

1. **Basic Python Installation**:
   Edit the `webapp/blockclock_web.py` file and change the port number:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5001, use_reloader=True)
   ```
   For example, change `port=5001` to `port=5002` or another available port.

2. **One-Click Script Installation**:
   The script handles port conflicts automatically by testing if port 5001 is available, and if not, moving to 5002, 5003, etc. until it finds an available port. If installation completes but the web interface isn't accessible, check the logs to see which port was actually used.

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