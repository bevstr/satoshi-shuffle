# Docker Setup Guide for Satoshi Shuffle

This guide will help you set up Satoshi Shuffle using Docker for easy deployment and maintenance.

## Prerequisites

- Docker installed on your system
- Docker Compose installed on your system

## Directory Structure

The Docker setup expects the following directory structure:

```
satoshi-shuffle/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── config/
│   └── blockclock.conf
├── logs/
└── webapp/
    └── ...
```

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/satoshi-shuffle.git
   cd satoshi-shuffle
   ```

2. Build and start the Docker container:
   ```bash
   docker-compose -f docker/docker-compose.yml up -d
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:5001
   ```

## Configuration

The application configuration is stored in the `config/blockclock.conf` file. You can edit this file directly, or use the web interface to configure your settings.

## Viewing Logs

Logs are stored in the `logs` directory. You can view them directly, or use the web interface to view the latest logs.

To view logs directly from Docker:
```bash
docker logs satoshi-shuffle
```

## Stopping the Application

To stop the Docker container:
```bash
docker-compose -f docker/docker-compose.yml down
```

## Updating the Application

To update to the latest version:

1. Pull the latest changes:
   ```bash
   git pull
   ```

2. Rebuild and restart the Docker container:
   ```bash
   docker-compose -f docker/docker-compose.yml up -d --build
   ```

## Troubleshooting

If you encounter issues:

1. Check the application logs:
   ```bash
   docker logs satoshi-shuffle
   ```

2. Ensure your BlockClock devices are reachable from the Docker container:
   ```bash
   docker exec -it satoshi-shuffle ping [BlockClock-IP]
   ```

3. Restart the container:
   ```bash
   docker-compose -f docker/docker-compose.yml restart
   ```

If issues persist, please open an issue on GitHub.