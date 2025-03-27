# Troubleshooting Guide\n\nCommon issues and their solutions.\n
# Troubleshooting Guide

This guide helps you solve common issues with Satoshi Shuffle. Follow the troubleshooting steps for your specific problem.

## Connection Issues

### Web Interface Not Accessible

**Symptoms**: Cannot access the web interface at `http://localhost:5001`

**Possible solutions**:

1. **Check if the application is running**:
   ```bash
   # Check for running Python process
   ps aux | grep blockclock_web.py
   
   # Check for Docker container
   docker ps | grep satoshi-shuffle
   ```

2. **Port conflict**:
   - Another application might be using port 5001
   - Try a different port by editing `webapp/blockclock_web.py`
   - Change `port=5001` to another port (e.g., `port=5002`)
   - Then access: `http://localhost:5002`

3. **Firewall issues**:
   - Check if your firewall is blocking port 5001
   - Allow the port through your firewall settings

4. **Restart the application**:
   ```bash
   # Using startup script
   ./start_SatoshiShuffle.sh
   
   # Using Docker
   docker-compose -f docker/docker-compose.yml restart
   
   # Using service (Linux)
   sudo systemctl restart satoshi-shuffle
   ```

### BlockClock Devices Not Reachable

**Symptoms**: "Device not reachable" warnings or custom text doesn't appear on your BlockClock

**Possible solutions**:

1. **Verify network connectivity**:
   ```bash
   # Ping the device directly
   ping 192.168.1.100  # Replace with your device's IP
   
   # If using Docker, ping from inside the container
   docker exec -it satoshi-shuffle ping 192.168.1.100
   ```

2. **Check IP address**:
   - Verify you're using the correct IP for your BlockClock
   - IP addresses can change if your router assigns them dynamically
   - Consider setting a static IP for your BlockClock in your router settings

3. **Network isolation**:
   - Ensure your computer and BlockClock are on the same network
   - Some networks isolate IoT devices from regular devices

4. **Restart your BlockClock**:
   - Power cycle your BlockClock device
   - Wait for it to fully boot up and connect to Wi-Fi

## Display Issues

### Custom Text Not Appearing

**Symptoms**: The application runs but your custom text doesn't show up on the BlockClock

**Possible solutions**:

1. **Check if rotation is active**:
   - In the web interface, verify that the status shows "Running"
   - If not, click the "Start Text Rotation" button

2. **Verify configuration**:
   - Make sure you have added at least one text option
   - Ensure the clock refresh time matches your BlockClock's setting
   - The first custom text may take several minutes to appear depending on your settings

3. **Check synchronization**:
   - The app needs time to synchronize with your BlockClock's refresh cycle
   - This initial sync can take up to 15 minutes
   - Watch the logs for "First refresh detected" message

4. **Manually send text**:
   - Try sending a one-time text message using the "Quick Actions" section
   - If this works but rotation doesn't, there might be a timing issue

### Text Display Issues

**Symptoms**: Text appears on the BlockClock but looks incorrect or cuts off

**Possible solutions**:

1. **Character limitations**:
   - BlockClock only supports up to 7 characters per message
   - Only use letters, numbers, and underscores
   - Avoid spaces and special characters

2. **Display formatting**:
   - Try prefixing text with underscore for left alignment (e.g., `_BTFD_`)
   - Try adding underscores on both sides for center alignment (e.g., `_HODL_`)

## Application Issues

### Unexpected Crashes

**Symptoms**: The application stops unexpectedly or displays errors

**Possible solutions**:

1. **Check logs**:
   - View the logs to identify the error:
   ```bash
   # View the last 50 lines of the log
   tail -n 50 logs/blockclock.log
   
   # If using Docker
   docker logs satoshi-shuffle | tail -n 50
   ```

2. **Common error messages**:
   - "Connection refused": BlockClock is not reachable
   - "Address already in use": Port conflict
   - "Permission denied": File permission issues

3. **Restart the application**:
   - Stop and restart using the appropriate method for your installation

4. **Clean installation**:
   - As a last resort, consider a fresh installation
   - Make sure to back up your configuration first

### Rate Limiting

**Symptoms**: "Rate limited" message when trying to send custom text

**Solution**:
- The application has a 70-second cooldown between manual text operations
- This prevents flooding your BlockClock with too many requests
- Wait for the cooldown period to end before trying again

## Installation Issues

### Python Installation Problems

**Symptoms**: Errors during Python dependency installation

**Possible solutions**:

1. **Update pip**:
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Install dependencies individually**:
   ```bash
   pip install Flask
   pip install requests
   # Continue with other dependencies
   ```

3. **Check Python version**:
   ```bash
   python --version
   ```
   - Ensure you're using Python 3.6 or higher

### Docker Installation Problems

**Symptoms**: Docker build fails or container won't start

**Possible solutions**:

1. **Check Docker logs**:
   ```bash
   docker-compose -f docker/docker-compose.yml logs
   ```

2. **Verify Docker installation**:
   ```bash
   docker --version
   docker-compose --version
   ```

3. **Build with debug output**:
   ```bash
   docker-compose -f docker/docker-compose.yml build --no-cache --progress=plain
   ```

## Service Issues

### Service Won't Start

**Symptoms**: The application won't start as a service

**Possible solutions**:

1. **Check service status**:
   ```bash
   # Linux
   sudo systemctl status satoshi-shuffle
   
   # macOS
   launchctl list | grep satoshi-shuffle
   ```

2. **Check service logs**:
   ```bash
   # Linux
   sudo journalctl -u satoshi-shuffle
   ```

3. **Verify file paths**:
   - Ensure all paths in your service file are absolute paths
   - Double-check that these paths exist

4. **Permissions**:
   - Ensure the service has permissions to access all required files
   - Check that the user running the service has appropriate access

## Advanced Troubleshooting

### Restarting All Components

If all else fails, try this full restart sequence:

```bash
# 1. Stop the application
# Using Docker
docker-compose -f docker/docker-compose.yml down

# Using service (Linux)
sudo systemctl stop satoshi-shuffle

# 2. Kill any remaining processes
pkill -f blockclock

# 3. Restart your BlockClock device
# (Physically power cycle the device)

# 4. Start Satoshi Shuffle again
# Using Docker
docker-compose -f docker/docker-compose.yml up -d

# Using service (Linux)
sudo systemctl start satoshi-shuffle
```

### Checking Network Connectivity

For more detailed network diagnostics:

```bash
# 1. Check your own IP address
ifconfig    # macOS/Linux
ipconfig    # Windows

# 2. Verify you can reach your router
ping 192.168.1.1    # Replace with your router's IP

# 3. Test connectivity to your BlockClock
ping 192.168.1.100  # Replace with your BlockClock's IP

# 4. Try trace route
traceroute 192.168.1.100  # macOS/Linux
tracert 192.168.1.100     # Windows
```

## Getting Support

If you're still experiencing issues after trying these troubleshooting steps:

1. **Check GitHub Issues**:
   - Search existing issues to see if others have encountered the same problem
   - Open a new issue if your problem is unique

2. **Provide Diagnostic Information**:
   When seeking help, please include:
   - Your installation method (Docker, Python, or Script)
   - Operating system and version
   - Error messages (from logs)
   - Steps to reproduce the issue
   - What you've already tried