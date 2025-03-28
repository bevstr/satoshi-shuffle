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
2. Go to `http://localhost:5001`  
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
