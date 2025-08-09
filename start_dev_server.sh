#!/bin/bash

echo "🚀 Setting up live development server..."

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found"
else
    echo "❌ Python 3 not found. Please install Python 3 first."
    exit 1
fi

# Install watchdog if not already installed
echo "📦 Installing watchdog for file watching..."
pip3 install watchdog

# Make the Python script executable
chmod +x simple_live_server.py

# Start the live server
echo "🌐 Starting live development server..."
python3 simple_live_server.py
