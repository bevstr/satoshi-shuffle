# One-Click Script Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle using the interactive installation script. **This is the recommended method for most users.**

---

## 📌 Before You Begin

The One-Click Script will handle most of the installation process for you, but **you need to install Python first**.

💡 **Need more details?** Check the [Dependencies Guide](dependencies.md) for complete system requirements and installation prerequisites.



### Step 1: Install Python

You need Python 3.6 or higher. Follow the instructions for your operating system:

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
   In **Terminal** run:  
   ```bash
   python3 --version
   ```
   If you see no version then

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
   python --version  # or python3 --version on some systems
   ```  
   It should return version **3.6 or higher**.  

---

## 🔧 What This Script Does

The One-Click Script will **automatically**:  
✅ Install required Python packages  
✅ Set up configuration files  
✅ Connect to your BlockClock devices  
✅ Create directories for logs and data  
✅ Optionally set up the app as a system service  

---

## 🚀 Installation Steps

### Step 1: Download the Repository

Create a folder where you want to locate the files and now open terminal in that folder 

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

### Step 2: Run the Installation Script

Once inside the **satoshi-shuffle** folder, run:  
```bash
python install.py
```
or 
```bash
python3 install.py  # Mac/Linux
py -3 install.py    # Windows
```

**If you have multiple Python versions installed**, use:  
```bash
python3 install.py  # Mac/Linux
py -3 install.py    # Windows
```

---

### Step 3: Follow the Interactive Prompts  

The script will ask you for:  
- **BlockClock device details** (name, IP, password)  
- **Custom text options** (Bitcoin-related phrases)  
- **Timing settings** (how often text appears)  

**Example Configuration:**  
```
Device 1:
  Name: Living Room Clock
  IP Address: 192.168.1.100
  Password: (leave blank if none)

Enter custom text options (max 7 characters each, separated by commas): BITCOIN, HODLER, BTFD

Clock refresh time options:
  1) 5 minutes
  2) 10 minutes
  3) 15 minutes
Choose an option (1-3): 2

Number of built-in screens between text (default: 3): 2
```

---

### Step 4: Running Satoshi Shuffle

#### **Option 1: Start Manually**
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
  sudo systemctl restart satoshi-shuffle
  ```  

For more help, check the [Troubleshooting Guide](docs/troubleshooting.md).  

---

## ✅ Next Steps  

🚀 Now that you’ve installed Satoshi Shuffle:  
- Configure your settings → **[Configuration Guide](docs/configuration.md)**  
- Learn how to manage BlockClock devices → **[Web Interface Guide](docs/web-interface.md)**  
- Need more help? → **[Troubleshooting](docs/troubleshooting.md)**  
