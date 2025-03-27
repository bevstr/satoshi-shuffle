# Satoshi Shuffle Dependencies

## System Requirements

- Operating System: Linux (Ubuntu/Debian recommended) or macOS (limited Windows support)
- [Python 3.6 or higher](https://www.python.org/downloads/)
- Network connection to your BlockClock device(s)
- 100MB+ free disk space for application and logs

## Python Dependencies

The following Python packages are required:
- [Flask==2.3.3](https://flask.palletsprojects.com/) - Web framework
- [Flask-WTF==1.1.1](https://flask-wtf.readthedocs.io/) - Form handling for Flask
- [Requests==2.32.3](https://requests.readthedocs.io/) - HTTP library for API calls

These will be automatically installed by:
- The One-Click Script installation
- Running `pip install -r requirements.txt` in manual Python installation
- Docker installation (included in the container)

## Installation-Specific Dependencies

### One-Click Script Installation
- [Python 3.6+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)
- Administrator/sudo privileges (for service installation)

### Docker Installation
- [Docker Engine 19.03.0+](https://docs.docker.com/engine/install/)
- [Docker Compose 1.27.0+](https://docs.docker.com/compose/install/)

### Manual Python Installation
- [Python 3.6+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)
- [Git](https://git-scm.com/downloads) (optional, for cloning)
- Administrator/sudo privileges (optional, for service setup)

## BlockClock Requirements

- [Coinkite BlockClock Mini or BlockClock Micro device](https://blockclock.com/)
- Device must be on the same network as the computer running Satoshi Shuffle
- Device IP address must be known (check your router or the BlockClock settings)
- The "Screen Update Rate" setting on your BlockClock should match the refresh time setting in Satoshi Shuffle

## Browser Requirements

The web interface works best with:
- [Chrome/Chromium 80+](https://www.google.com/chrome/)
- [Firefox 75+](https://www.mozilla.org/firefox/)
- [Safari 13+](https://www.apple.com/safari/)
- [Edge 80+](https://www.microsoft.com/edge)

## Network Requirements

- Your computer must be able to reach the BlockClock devices via HTTP
- Default port 5001 must be available (or configurable to an alternative)
- No firewall blocking traffic between your computer and BlockClock devices

## Checking Your System

### Check Python Version
```bash
python --version
# or
python3 --version
```

### Check pip Installation
```bash
pip --version
# or
pip3 --version
```

### Check Docker Installation
```bash
docker --version
docker-compose --version
```

### Check Network Connectivity to BlockClock
```bash
ping 192.168.1.100  # Replace with your BlockClock's IP
```