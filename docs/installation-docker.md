# 📌 Docker Installation Guide (Updated)

This guide provides detailed instructions for installing **Satoshi Shuffle** using **Docker containers**.  
💪 **This is the recommended installation method** because it eliminates dependency issues.  
💪 **Even beginners can follow these steps to get started quickly!**

---

## 🔹 Before You Begin

To install Satoshi Shuffle via Docker, you need:  
- **Docker**  
- **Docker Compose**  

💡 If you're new to Docker, follow the **installation steps below** before proceeding.

<details>
  <summary>🔹 Click to expand Docker installation instructions</summary>

### **MacOS**
1. **Check if Homebrew is installed**  
   Open **Terminal** and run:  
   ```bash
   brew --version
   ```
   If it returns "command not found," install Homebrew:  
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Docker**  
   ```bash
   brew install --cask docker
   brew install docker-compose
   ```

3. **Start Docker Desktop**  
   Open **Docker Desktop** and wait for it to finish loading.

---

### **Ubuntu/Debian (Linux)**
```bash
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER  # Add yourself to the Docker group
```
Then **restart your machine** for the changes to take effect.

---

### **Windows**
1. Download **Docker Desktop** from [docker.com](https://www.docker.com/products/docker-desktop).  
2. Install and **restart your computer**.  
3. Open **Docker Desktop** and wait until it's fully running.
</details>

---

## 2️⃣ Verify Docker Installation
Run these commands to ensure Docker is installed correctly:  
```bash
docker --version
docker-compose --version
```
Both should return version numbers without errors.

---

## 🚀 Installation Steps

### 3️⃣ Download the Repository
#### To install Satoshi Shuffle, 
1. Create a folder where you want to locate the files and now open terminal in that folder 
2. **download the code by pasting below in terminal**:

#### **Option 1: Using Git (Recommended)**
```bash
git clone https://github.com/bevstr/satoshi-shuffle.git
cd satoshi-shuffle
```

#### **Option 2: Manual Download**
1. Go to **[Satoshi Shuffle GitHub](https://github.com/bevstr/satoshi-shuffle)**  
2. Click the **green "Code" button** → **Download ZIP**  
3. Extract the ZIP file to the folder on your computer  

---

### 4️⃣ Build and Start the Docker Container
Run the following command in Terminal inside the **`satoshi-shuffle`** folder:
```bash
docker-compose -f docker/docker-compose.yml up -d
```

💪 **This command will:**  
- Build the Docker image  
- Start the container in the background  
- Expose the web interface on port `5001`  

---

### 5️⃣ Configure Your Settings in the Web App
Once the container is running, open your browser and go to:  
```
http://localhost:5001
```

Here you **MUST configure the variables** before using the app. For more detailed information, refer to the [Configuration Guide](docs/configuration.md).

🛠 **In the Web App, configure your settings:**
1. **Go to the settings page** (inside the web interface).  
2. **On Devices Tab, enter your BlockClock Name and IP address.**  
3. **On Text Options Tab, add or remove Text Options.**  
4. **On Timing Tab, choose Refresh Time and Number of Natural Display Values.**  
5. **On Systems Tab, change defaults if needed.**  
6. **Save your settings.**  
7. **Return to Home Page, Click the Green Start Button.**  

That’s it! 🎉 Your BlockClock will now display your custom text.

---

## 🔄 Managing the Container
Here are some useful commands for managing your container:

### **Stop the container**  
```bash
docker-compose -f docker/docker-compose.yml down
```

### **Restart the container**  
```bash
docker-compose -f docker/docker-compose.yml up -d
```

### **Check live logs**  
```bash
docker logs -f satoshi-shuffle
```

### **Access the container shell**  
```bash
docker exec -it satoshi-shuffle /bin/bash
```

---

## 🛠 Troubleshooting
If you encounter any issues:

### **1️⃣ Check if Docker is running**  
```bash
systemctl status docker  # Linux
```

### **2️⃣ Port Conflict (Port 5001 Already in Use)**
- Open **`docker-compose.yml`**  
- Change this line:
  ```yaml
  ports:
    - "5002:5001"
  ```
- Restart the container.

### **3️⃣ Check Container Logs**
If your app isn’t working as expected, check the logs:
```bash
docker logs satoshi-shuffle
```

---

## ✅ Next Steps
🚀 Now that you’ve installed Satoshi Shuffle:  
- **Configure your settings in the web interface** (http://localhost:5001)  
- **Explore all features inside the web app**  
- **Need more help?** Check the [Troubleshooting Guide](docs/troubleshooting.md)  

---


