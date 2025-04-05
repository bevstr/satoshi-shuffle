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