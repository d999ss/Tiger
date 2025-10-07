#!/bin/bash

# Vibetest Complete Setup Script
# Run this after installing Python 3.11+

set -e

echo "🐯 Tiger CMS - Vibetest Setup"
echo "=============================="
echo ""

# Check Python version - try python3.11 first, then python3
echo "Checking Python version..."

if command -v python3.11 &> /dev/null; then
    PYTHON_CMD="python3.11"
    PYTHON_VERSION=$(python3.11 --version 2>&1 | awk '{print $2}')
    echo "✅ Found python3.11: $PYTHON_VERSION"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ "$MAJOR" -lt 3 ] || { [ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 11 ]; }; then
        echo "❌ Python 3.11+ required. Current python3 version: $PYTHON_VERSION"
        echo ""
        echo "Please install Python 3.11+ first:"
        echo "  Option 1: Download from python.org (installer should be open)"
        echo "  Option 2: brew install python@3.11"
        echo "  Option 3: Use pyenv"
        exit 1
    fi
    echo "✅ Python $PYTHON_VERSION detected"
else
    echo "❌ Python not found"
    echo ""
    echo "Please install Python 3.11+ first:"
    echo "  Option 1: Download from python.org"
    echo "  Option 2: brew install python@3.11"
    exit 1
fi

echo ""

# Navigate to vibetest directory
cd "$(dirname "$0")"
echo "📁 Working directory: $(pwd)"
echo ""

# Remove old venv if exists
if [ -d ".venv" ]; then
    echo "🗑️  Removing old virtual environment..."
    rm -rf .venv
fi

# Create new venv
echo "🔧 Creating virtual environment..."
$PYTHON_CMD -m venv .venv

# Activate venv
echo "⚡ Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip setuptools wheel -q

# Install vibetest
echo "🚀 Installing Vibetest..."
pip install -e . -q

# Install playwright
echo "🎭 Installing Playwright browser..."
playwright install chromium --with-deps --no-shell

echo ""
echo "✨ Setup Complete! ✨"
echo ""
echo "Next steps:"
echo "1. Get Google API key: https://makersuite.google.com/app/apikey"
echo "2. Add to Cursor MCP settings:"
echo ""
echo '{
  "mcpServers": {
    "vibetest": {
      "command": "'"$(pwd)/.venv/bin/vibetest-mcp"'",
      "env": {
        "GOOGLE_API_KEY": "your_google_api_key_here"
      }
    }
  }
}'
echo ""
echo "3. Restart Cursor"
echo "4. Test with: 'Vibetest my website with 5 agents: localhost:3000'"
echo ""
echo "📖 See VIBETEST_SETUP_GUIDE.md for more info"

