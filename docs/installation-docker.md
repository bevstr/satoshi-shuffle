# Docker Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle using Docker containers.  
**This method is best for users who want an isolated installation or are already familiar with Docker.**

---

## 📌 Before You Begin

The Docker installation method requires **Docker and Docker Compose**.  
✅ **Docker handles all dependencies inside the container**  
✅ **No need to install Python manually**  

💡 **Need more details?** Check the [Dependencies Guide](dependencies.md) for complete system requirements and installation prerequisites.

### Step 1: Install Docker

Follow the instructions for your operating system:

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

2. **Install Docker**  
   ```bash
   brew install --cask docker
   ```

3. **Start Docker Desktop**  
   Open **Docker Desktop** and wait until it's fully running.

#### **Ubuntu/Debian (Linux)**  
```bash
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER  # Add yourself to the Docker group
```

#### **Windows**  
1. Download **Docker Desktop** from [docker.com](https://www.docker.com/products/docker-desktop)  
2. Install and **restart your computer**  
3. Open **Docker Desktop** and wait for it to start  

### Step 2: Verify Docker Installation

Run these commands to ensure Docker is installed correctly:  
```bash
docker --version
docker-compose --version
```  

Both should return version numbers without errors.

---

## 🚀 Installation Steps

### Step 1: Download the Repository

To install Satoshi Shuffle, **first download the code**:

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

### Step 2: Configure Your Settings

Before building the Docker container, **set up your configuration**:

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
   nano blockclock.conf  # Linux/Mac
   notepad blockclock.conf  # Windows
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

### Step 3: Build and Start the Docker Container

Run the following command:  
```bash
docker-compose -f docker/docker-compose.yml up -d
```

**What this does:**  
✅ **Builds** the Docker image  
✅ **Starts** the container in the background  
✅ **Exposes the web interface** on port 5001  

You should see output similar to:  
```
Creating network "satoshi-network" with driver "bridge"
Building satoshi-shuffle
Successfully built 3a7c8f7e9b3e
Successfully tagged satoshi-shuffle:latest
Creating satoshi-shuffle ... done
```

---

### Step 4: Verify the Container is Running

Check if your container is running:  
```bash
docker ps | grep satoshi-shuffle
```

You should see output like:  
```
CONTAINER ID   IMAGE                COMMAND                  STATUS         PORTS                   NAMES
3a7c8f7e9b3e   satoshi-shuffle      "python webapp/block…"   Up 28 seconds  0.0.0.0:5001->5001/tcp  satoshi-shuffle
```

---

### Step 5: Access the Web Interface

Once the container is running, open your browser and go to:  
```
http://localhost:5001
```

You should now see the **Satoshi Shuffle Web Interface**, where you can:  
✅ Start/stop the text rotation  
✅ Send custom text to your BlockClock  
✅ Monitor your BlockClock devices  

---

## 🔄 Managing the Container

**Stop the container**:  
```bash
docker-compose -f docker/docker-compose.yml down
```

**Restart the container**:  
```bash
docker-compose -f docker/docker-compose.yml up -d
```

**Check logs**:  
```bash
docker logs satoshi-shuffle
```

**Access the container shell**:  
```bash
docker exec -it satoshi-shuffle /bin/bash
```

---

## 🛠 Troubleshooting

If you encounter problems:

- **Check if Docker is running**  
  ```bash
  systemctl status docker  # Linux
  ```  

- **Port conflict (5001 in use)**  
  - Edit `docker-compose.yml`  
  - Change `ports: - "5002:5001"`  
  - Restart the container  

- **Container not starting**  
  ```bash
  docker logs satoshi-shuffle
  ```

For more help, check the [Troubleshooting Guide](docs/troubleshooting.md).

---

## ✅ Next Steps  

🚀 Now that you’ve installed Satoshi Shuffle:  
- Configure your settings → **[Configuration Guide](docs/configuration.md)**  
- Learn how to manage BlockClock devices → **[Web Interface Guide](docs/web-interface.md)**  
- Need more help? → **[Troubleshooting](docs/troubleshooting.md)**  
