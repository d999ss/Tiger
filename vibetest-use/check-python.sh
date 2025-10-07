#!/bin/bash

# Quick Python verification script

echo "🔍 Checking Python Installation..."
echo ""

if command -v python3.11 &> /dev/null; then
    echo "✅ python3.11 found!"
    python3.11 --version
    echo "   Location: $(which python3.11)"
    echo ""
    echo "🎉 Ready to run setup!"
    echo ""
    echo "Run this command to complete Vibetest installation:"
    echo "  cd \"/Users/donnysmith/Desktop/Tiger CMS/vibetest-use\""
    echo "  ./complete-setup.sh"
    exit 0
elif command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ "$MAJOR" -ge 3 ] && [ "$MINOR" -ge 11 ]; then
        echo "✅ python3 found with version $PYTHON_VERSION"
        echo "   Location: $(which python3)"
        echo ""
        echo "🎉 Ready to run setup!"
        echo ""
        echo "Run this command to complete Vibetest installation:"
        echo "  cd \"/Users/donnysmith/Desktop/Tiger CMS/vibetest-use\""
        echo "  ./complete-setup.sh"
        exit 0
    else
        echo "⚠️  python3 found but version is too old: $PYTHON_VERSION"
        echo "   Need Python 3.11 or higher"
        echo ""
        echo "The Python 3.11 installer might still be running."
        echo "Please complete the installation and try again."
        exit 1
    fi
else
    echo "❌ Python not found"
    echo ""
    echo "The Python installer might still be running."
    echo "Please complete the installation and try again."
    echo ""
    echo "If you closed the installer, you can reopen it:"
    echo "  open /tmp/python3.11.pkg"
    exit 1
fi




