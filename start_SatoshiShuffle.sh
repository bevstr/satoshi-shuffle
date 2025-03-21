#!/bin/bash
# Clear terminal and print welcome banner
clear
echo "=========================================================="
echo "✅ Satoshi Shuffle Pre Lauch..."
echo "✅ Gettin' Shit Organized"
echo "=========================================================="

# Kill any existing processes using port 5001
if lsof -ti:5001 >/dev/null; then
    echo "⚠️  Terminating existing processes using port 5001 and other crap!..."
    lsof -ti:5001 | xargs kill
    sleep 1
fi

# Print startup information
echo ""
echo "=========================================================="
echo "Satoshi Shuffle lift off! 🚀"
echo "=========================================================="
echo ""
echo "📱 Access the web interface at: http://localhost:5001"
echo "📊 The app will start automatically."
echo "   You can monitor and control it from the web interface."
echo ""
echo "💡 Press Ctrl+C to stop the application when finished."
echo "=========================================================="
echo ""
echo "Log output will appear below in a jiffy:"
echo ""
echo "----------------------------------------------------------"
echo ""
sleep 2

# Path to the filter script - updated to use the correct path
FILTER_SCRIPT="./filter_output.py"

# Define a flag to track if cleanup has run
CLEANUP_DONE=0

# Define function to kill all child processes on exit
cleanup() {
    # Only run cleanup once
    if [ $CLEANUP_DONE -eq 1 ]; then
        return
    fi
    CLEANUP_DONE=1
    
    echo -e "\n\n👋 You terminated the Shuffle, where the hell are you going?.\n"
    
    # Kill all Python processes containing 'blockclock'
    pkill -f blockclock
    
    # Kill any processes using port 5001
    lsof -ti:5001 | xargs kill -9 2>/dev/null || true
    
    # Kill all child processes
    pkill -P $$ 2>/dev/null || true
    
    # After a brief delay, check if any processes are still hanging
    sleep 1
    if pgrep -f blockclock > /dev/null; then
        echo "Forcefully terminating remaining processes..."
        pkill -9 -f blockclock
    fi
}

# Set up proper trap to handle signals
trap cleanup INT TERM EXIT

# Start Flask in background and pipe through the filter
python3 webapp/blockclock_web.py 2>&1 | $FILTER_SCRIPT &
FLASK_PID=$!

# Wait for Flask to start
sleep 3

# Automatically start the rotation via curl
echo "🔄 Automatically starting Satoshi Shuffle..."
echo ""
curl -s -X POST http://localhost:5001/start > /dev/null

# Wait for the Flask process
wait $FLASK_PID