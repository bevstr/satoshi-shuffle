# Docker Installation Guide

This guide provides detailed instructions for installing Satoshi Shuffle using Docker containers. This method is ideal for users familiar with Docker or those who want a clean, isolated installation.

## Before You Begin

The Docker installation method requires Docker and Docker Compose to be installed on your system. All other dependencies will be handled automatically inside the container.

### Step 1: Install Docker

Docker Engine and Docker Compose are required:

- **macOS**: Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop) (includes both Docker Engine and Docker Compose)
- **Ubuntu/Debian**: 
  ```bash
  # Open Terminal and run:
  sudo apt update
  sudo apt install docker.io docker-compose
  sudo usermod -aG docker $USER  # Add yourself to docker group
  # Log out and log back in for group changes to take effect
  ```
- **Other Linux**: Follow the [official Docker installation instructions](https://docs.docker.com/engine/install/)
- **Windows**: Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Step 2: Verify Docker Installation

1. Open your Terminal (macOS/Linux) or Command Prompt (Windows)
2. Run the following commands to check your Docker installation:
   ```bash
   docker --version
   docker-compose --version
   ```
3. Make sure both commands return version information without errors

### What Docker Will Handle For You

The Docker installation automatically:
- Creates an isolated environment with all required dependencies
- Sets up the Python runtime environment
- Mounts your configuration and logs directories
- Exposes the web interface on port 5001

## Installation Steps

### Step 1: Download the Repository

First, get a copy of the Satoshi Shuffle code:

```bash
# Open Terminal (macOS/Linux) or Command Prompt (Windows)

# Clone the repository using git
git clone https://github.com/bevstr/satoshi-shuffle.git

# Navigate into the project directory
cd satoshi-shuffle
```

Don't have git? You can also:
1. Go to https://github.com/bevstr/satoshi-shuffle
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file to a folder on your computer
5. Open your Terminal/Command Prompt and navigate to that folder

### Step 2: Configure Your Settings

Before building the Docker container, you'll need to set up your configuration:

1. Navigate to the config directory:
   ```bash
   cd config
   ```

2. Create a new configuration file:
   ```bash
   # Copy the example config (if it exists)
   cp blockclock.conf.example blockclock.conf
   
   # Or create a new one if no example exists
   touch blockclock.conf
   ```

3. Edit the configuration file with your favorite text editor:
   ```bash
   # Using nano
   nano blockclock.conf
   
   # Or using vi
   vi blockclock.conf
   
   # Or open with your desktop text editor
   ```

4. Add your device information and preferences:
   ```
   # Device 1
   DEVICE_1_NAME="Living Room Clock"
   DEVICE_1_IP="192.168.1.100"
   DEVICE_1_PASSWORD=""
   
   # Device 2 (optional)
   DEVICE_2_NAME="Office Clock"
   DEVICE_2_IP="192.168.1.101"
   DEVICE_2_PASSWORD=""
   
   # Text options to display (separated by spaces)
   TEXT_OPTIONS=("BITCOIN" "HODLER" "FREEDOM" "SATOSHI" "BTFD")
   
   # Clock refresh time (in seconds): 300 (5min), 600 (10min), 900 (15min), 1800 (30min), 3600 (60min)
   CLOCK_REFRESH_TIME=300
   
   # Number of built-in screens to show between our text messages
   DISPLAYS_BETWEEN_TEXT=3
   ```

5. Return to the main directory:
   ```bash
   cd ..
   ```

### Step 3: Build and Start the Docker Container

Now you'll build and start the Docker container:

```bash
# Build and start the container
docker-compose -f docker/docker-compose.yml up -d
```

This command:
- Builds the Docker image with all necessary dependencies
- Creates a container based on that image
- Starts the container in the background (-d for "detached" mode)
- Sets up volume mappings for config and logs directories

You should see output similar to:
```
Creating network "satoshi-network" with driver "bridge"
Building satoshi-shuffle
[+] Building 2.5s (10/10) FINISHED
 => [internal] loading build definition from Dockerfile
 ...
Successfully built 3a7c8f7e9b3e
Successfully tagged satoshi-shuffle:latest
Creating satoshi-shuffle ... done
```

### Step 4: Verify the Container is Running

Check that your container started successfully:

```bash
docker ps | grep satoshi-shuffle
```

You should see output showing your container is running:
```
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                    NAMES
3a7c8f7e9b3e   satoshi-shuffle      "python webapp/block…"   30 seconds ago   Up 28 seconds   0.0.0.0:5001->5001/tcp   satoshi-shuffle
```

### Step 5: Access the Web Interface

With the container running, open your web browser and navigate to:
```
http://localhost:5001
```

You should see the Satoshi Shuffle web interface. From here, you can:
- Start/stop the text rotation
- Send custom text on demand
- Monitor your BlockClock devices
- Access logs and status information

## Troubleshooting

If you encounter issues during installation or operation:

- **Docker not found**: Make sure Docker is properly installed and your user has permissions to run Docker commands

- **Port conflicts**: If port 5001 is already in use, modify the `docker-compose.yml` file to use a different port:
  ```bash
  # Edit the docker-compose.yml file
  nano docker/docker-compose.yml
  
  # Change this line in the file:
  ports:
    - "5002:5001"  # Maps port 5001 in container to port 5002 on host
  
  # Save and exit, then restart the container
  docker-compose -f docker/docker-compose.yml down
  docker-compose -f docker/docker-compose.yml up -d
  ```

- **Container not starting**: Check logs for errors:
  ```bash
  docker logs satoshi-shuffle
  ```

- **Device connectivity issues**: Ensure your BlockClock devices are on the same network and accessible from the Docker container:
  ```bash
  docker exec -it satoshi-shuffle ping 192.168.1.100
  ```

- **Permission issues with volumes**: Check that the mounted directories have the correct permissions:
  ```bash
  ls -la config/
  ls -la logs/
  ```

## Managing the Container

Common commands for managing your Docker container:

```bash
# Stop the container
docker-compose -f docker/docker-compose.yml down

# Start an existing container
docker-compose -f docker/docker-compose.yml up -d

# Restart the container
docker-compose -f docker/docker-compose.yml restart

# View logs
docker logs satoshi-shuffle

# Follow logs in real-time
docker logs -f satoshi-shuffle

# Access a shell in the container
docker exec -it satoshi-shuffle /bin/bash
```

## Updating Satoshi Shuffle

To update to a newer version:

```bash
# Pull the latest code
git pull

# Rebuild and restart the container
docker-compose -f docker/docker-compose.yml up -d --build
```

## Next Steps

After installation:
1. Continue to the [Configuration Guide](configuration.md) for additional setup options
2. Learn how to manage your BlockClock devices through the web interface

For a complete list of system requirements and dependencies, see the [Dependencies List](dependencies.md).