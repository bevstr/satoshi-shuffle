#!/bin/bash

# 🚀 Auto-update script for Satoshi Shuffle Docker container
# Use this to pull latest changes from the active Git branch and rebuild your container

echo "📦 Pulling latest code from GitHub..."
git pull

echo "🔨 Rebuilding and restarting Docker container..."
docker-compose down
docker-compose up --build -d

echo ""
echo "✅ Update complete! Your app is running with the latest changes."
echo "✅ Goto web app in browser and click play. 🚀 "
echo ""