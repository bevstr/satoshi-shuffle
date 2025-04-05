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

