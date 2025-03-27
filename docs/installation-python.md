# Python Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle using Python.  
**This method is best for advanced users who want full control over the installation.**

---

## 📌 Before You Begin

Before installing, ensure you have:  
✅ **Python 3.6 or higher** installed  
✅ **pip (Python package manager)** installed  
✅ **Terminal (Mac/Linux) or Command Prompt (Windows)** available 

💡 **Need more details?** Check the [Dependencies Guide](dependencies.md) for complete system requirements and installation prerequisites.



### Step 1: Install Python

#### **MacOS**  
1. **Check if Homebrew is installed**  
   Open **Terminal** and run:  
   ```bash
   brew --version
   ```
   If you see "command not found," install Homebrew:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**  
   ```bash
   brew install python
   ```

#### **Ubuntu/Debian (Linux)**  
```bash
sudo apt update && sudo apt install python3 python3-pip
```

#### **Windows**  
1. Download Python from [python.org](https://www.python.org/downloads/)  
2. Run the installer and check **"Add Python to PATH"**  
3. Click **Install** and wait for it to finish  

### Step 2: Verify Python Installation

1. Open **Terminal (Mac/Linux)** or **Command Prompt (Windows)**  
2. Run the following command to check your Python version:  
   ```bash
   python --version  # or python3 --version
   ```  
   It should return version **3.6 or higher**.  

3. Check if `pip` is installed:  
   ```bash
   pip --version  # or pip3 --version
   ```  

---

## 🚀 Installation Steps

### Step 1: Download the Repository

To install Satoshi Shuffle, **you first need to download the code**:

#### **Option 1: Using Git (Recommended)**
```bash
git clone https://github.com/bevstr/satoshi-shuffle.git
cd satoshi-shuffle
```

#### **Option 2: Manual Download**
1. Go to **[Satoshi Shuffle GitHub](https://github.com/bevstr/satoshi-shuffle)**  
2. Click the **green "Code" button** → **Download ZIP**  
3. Extract the ZIP file to a folder on your computer  
4. Open **Terminal/Command Prompt** and navigate to that folder  

---

### Step 2: Install Dependencies

Run this command to install all required Python packages:  
```bash
pip install -r requirements.txt
```

**If you have multiple Python versions installed**, use:  
```bash
python3 -m pip install -r requirements.txt  # Mac/Linux
py -3 -m pip install -r requirements.txt    # Windows
```

This installs:  
✅ Flask (web server)  
✅ Requests (HTTP client)  
✅ Other dependencies needed for the application  

---

### Step 3: Configure Your Settings

Before running Satoshi Shuffle, you need to **set up your configuration file**.

1. Navigate to the `config` directory:  
   ```bash
   cd config
   ```

2. Create a new configuration file:  
   ```bash
   cp blockclock.conf.example blockclock.conf
   ```

3. Open the file for editing:  
   ```bash
   nano blockclock.conf  # For Linux/Mac users
   notepad blockclock.conf  # For Windows users
   ```

4. **Example Configuration File:**  
   ```bash
   DEVICE_1_NAME="Living Room Clock"
   DEVICE_1_IP="192.168.1.100"
   DEVICE_1_PASSWORD=""
   
   TEXT_OPTIONS=("BITCOIN" "HODLER" "BTFD")
   CLOCK_REFRESH_TIME=300
   DISPLAYS_BETWEEN_TEXT=3
   ```

5. **Save and exit** (For nano, press `CTRL+X`, then `Y`, then `Enter`).

---

### Step 4: Start the Application

#### **Option 1: Run Directly**
```bash
python webapp/blockclock_web.py
```

#### **Option 2: Run in Background**
```bash
nohup python3 webapp/blockclock_web.py > logs/webapp.log 2>&1 &
```

#### **Option 3: Set Up as a Service (Auto-Start on Boot)**
If you want Satoshi Shuffle to **start automatically** when you boot your system:  
```bash
sudo systemctl enable satoshi-shuffle
sudo systemctl start satoshi-shuffle
```

---

## 🛠 Troubleshooting

If you run into problems:  

- **Check logs:**  
  ```bash
  tail -f logs/blockclock.log
  ```  
- **Restart Satoshi Shuffle:**  
  ```bash
  pkill -f blockclock_web.py
python webapp/blockclock_web.py  # Restart manually
  ```  

For more help, check the [Troubleshooting Guide](docs/troubleshooting.md).  

---

## ✅ Next Steps  

🚀 Now that you’ve installed Satoshi Shuffle:  
- Configure your settings → **[Configuration Guide](docs/configuration.md)**  
- Learn how to manage BlockClock devices → **[Web Interface Guide](docs/web-interface.md)**  
- Need more help? → **[Troubleshooting](docs/troubleshooting.md)**  
