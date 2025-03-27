# 📦 Satoshi Shuffle Dependencies

This guide provides a complete list of system and software requirements needed to run Satoshi Shuffle.

---

## 🖥 System Requirements

✅ **Operating System**: Linux (Ubuntu/Debian recommended) or macOS (Windows limited support)  
✅ **100MB+ free disk space** for application and logs  
✅ **Network connection** to your BlockClock device(s)  

---

## 🛠 Required Software

| Dependency | Version | Installation Command |
|------------|---------|----------------------|
| Python     | 3.6+    | `sudo apt install python3` or `brew install python` |
| Pip        | Latest  | `sudo apt install python3-pip` or `brew install pip` |
| Git        | Latest  | `sudo apt install git` or `brew install git` |
| Docker     | Latest  | `sudo apt install docker.io` or `brew install --cask docker` |

✅ **All dependencies are automatically handled by the installation script.**  

---

## 📦 Python Package Dependencies  

The following Python libraries are required:  

- **Flask** - Web framework  
- **Requests** - HTTP library  
- **Flask-WTF** - Form handling for Flask  

### Installing Dependencies Manually  

If needed, install all Python dependencies with:  
```bash
pip install -r requirements.txt
```

**Or install them individually:**  
```bash
pip install Flask requests Flask-WTF
```

---

## 🖥 BlockClock Requirements

✅ **Coinkite BlockClock Mini or Micro**  
✅ **Device must be on the same WiFi/network as your computer**  
✅ **Static IP recommended** for better stability  

To find your BlockClock’s IP:  
- Check your router settings  
- Use a network scanner app  
- Check the BlockClock settings menu  

---

## 🌍 Network Requirements  

Your system must allow **outgoing HTTP requests** to communicate with your BlockClock.  

- Default **port 5001** must be open  
- No firewall should block requests  

### Checking Your Connection  

Run these commands to verify network connectivity:  

**Check Python version:**  
```bash
python --version  # or python3 --version
```

**Check pip installation:**  
```bash
pip --version  # or pip3 --version
```

**Check Docker installation:**  
```bash
docker --version
docker-compose --version
```

**Check if your system can reach the BlockClock:**  
```bash
ping 192.168.1.100  # Replace with your BlockClock's IP
```

---

## 🛠 Need More Help?  

If you encounter dependency issues:  
📌 **Check the [Troubleshooting Guide](troubleshooting.md)**  
📌 **Verify missing packages with**:  
```bash
pip list  # List all installed Python packages
```

✅ **Continue with [One-Click Installation](installation-one-click.md)**  
- [Installation Guide](installation-one-click.md)  
- [Configuration Guide](configuration.md)  
