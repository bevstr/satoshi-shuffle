# One-Click Script Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle using the interactive installation script. **This is the recommended method for most users.**

---

## 📌 Before You Begin

The One-Click Script will handle most of the installation process for you, but **you need to install Python first**.


<details>
<summary><b>Installing Python - click to expand</b></summary>

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

### Verify Python Installation

1. Open **Terminal (Mac/Linux)** or **Command Prompt (Windows)**  
2. Run the following command to check your Python version:  
   ```bash
   python --version  # or python3 --version on some systems
   ```  
   It should return version **3.6 or higher**.
</details>
<br>

💡 **Need more details?** Check the [Dependencies Guide](dependencies.md) for complete system requirements and installation prerequisites.

---

## 🔧 What This Script Does

The One-Click Script will **automatically**:  
✅ Install required Python packages  
✅ Set up configuration files  
✅ Connect to your BlockClock devices  
✅ Create directories for logs and data  

---

## 🚀 Installation Steps

### Step 1: Download the Repository

Create a folder where you want to locate the files and now open terminal in that folder 

To install Satoshi Shuffle, **you first need to download the code**:

<details>
<summary><b>Option 1: Using Git (Recommended)</b></summary>

```bash
git clone https://github.com/bevstr/satoshi-shuffle.git
cd satoshi-shuffle
```
</details>

<details>
<summary><b>Option 2: Manual Download</b></summary>

1. Go to **[Satoshi Shuffle GitHub](https://github.com/bevstr/satoshi-shuffle)**  
2. Click the **green "Code" button** → **Download ZIP**  
3. Extract the ZIP file to a folder on your computer  
4. Open **Terminal/Command Prompt** and navigate to that folder  
</details>

---

### Step 2: Run the Installation Script

Once inside the **satoshi-shuffle** folder, run:  
```bash
python3 install.py  # Mac/Linux
py -3 install.py    # Windows
```
or 
```bash
python install.py
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

<details>
<summary><b>Example Configuration</b></summary>

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
</details>

---

### Step 4: Running Satoshi Shuffle

<details>
<summary><b>Option 1: Start Manually</b></summary>

```bash
python webapp/blockclock_web.py
```
</details>

<details>
<summary><b>Option 2: Run in Background</b></summary>

```bash
nohup python3 webapp/blockclock_web.py > logs/webapp.log 2>&1 &
```
</details>

<details>
<summary><b>Option 3: Set Up Automatic Startup (Using Cron)</b></summary>

If you want Satoshi Shuffle to **start automatically** when you boot your system:

#### **For Linux/macOS Users:**

1. **Open your terminal** and edit your crontab:
   ```bash
   crontab -e
   ```
   
   > Note: This will open the crontab file in your default text editor.

2. **Add the following line** at the end of the file:
   ```bash
   @reboot cd /full/path/to/satoshi-shuffle && ./start_SatoshiShuffle.sh > logs/cron.log 2>&1
   ```
   
   > Replace `/full/path/to/satoshi-shuffle` with the actual full path to your installation.

3. **Save and exit** the editor:
   - For nano: Press `Ctrl+O` to save, then `Enter`, then `Ctrl+X` to exit
   - For vim: Press `Esc`, then type `:wq` and press `Enter`

4. **Verify your crontab entry** was saved:
   ```bash
   crontab -l
   ```

#### **For Windows Users:**

1. Create a shortcut to `start_SatoshiShuffle.bat` (you may need to create this batch file)
   
2. Place the shortcut in your Startup folder:
   - Press `Win+R`, type `shell:startup` and press `Enter`
   - Copy your shortcut into the folder that opens

3. **Create start_SatoshiShuffle.bat** with the following content:
   ```batch
   @echo off
   cd /d "C:\path\to\satoshi-shuffle"
   python webapp\blockclock_web.py
   ```

#### **Testing Your Automatic Startup**

To verify your autostart configuration:

1. **Restart your computer**
2. **Wait about 1-2 minutes** after login for the application to start
3. **Open your browser** and navigate to `http://localhost:5010`
4. **Check the logs** if the web interface isn't responding:
   ```bash
   cat logs/cron.log
   ```

If you encounter any issues with the cron job, check the `logs/cron.log` file for error messages.
</details>

---

## 🛠 Troubleshooting

If you run into problems:  

<details>
<summary><b>Common Troubleshooting Steps</b></summary>

- **Check logs:**  
  ```bash
  tail -f logs/blockclock.log
  ```  

- **Manually restart the application:**
  ```bash
  # Find and kill any running instances
  pkill -f blockclock_web.py
  
  # Start it again
  python webapp/blockclock_web.py
  ```

- **Verify your BlockClock is reachable:**
  ```bash
  ping 192.168.1.100  # Replace with your BlockClock's IP
  ```

For more help, check the [Troubleshooting Guide](docs/troubleshooting.md).
</details>

---

## ✅ Next Steps  

🚀 Now that you've installed Satoshi Shuffle:  
- Configure your settings → **[Configuration Guide](docs/configuration.md)**  
- Learn how to manage BlockClock devices → **[Web Interface Guide](docs/web-interface.md)**  
- Need more help? → **[Troubleshooting](docs/troubleshooting.md)**