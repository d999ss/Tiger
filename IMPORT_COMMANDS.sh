#!/bin/bash

# Tiger BioSciences - Quick Import Script
# After getting your API token, paste it below and run this script

echo "🔑 Tiger BioSciences Content Import"
echo "===================================="
echo ""

# Check if token is provided
if [ -z "$1" ]; then
    echo "❌ Error: No API token provided"
    echo ""
    echo "Usage:"
    echo "  ./IMPORT_COMMANDS.sh YOUR_API_TOKEN"
    echo ""
    echo "Or run manually:"
    echo "  export SANITY_TOKEN='your-token-here'"
    echo "  node import-content-to-sanity.js"
    echo ""
    echo "📝 Get your token from:"
    echo "   https://www.sanity.io/manage/personal/tokens"
    echo ""
    exit 1
fi

# Set the token
export SANITY_TOKEN="$1"

echo "✅ Token set!"
echo "📦 Starting content import..."
echo ""

# Run the import
node import-content-to-sanity.js

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Success! Content imported to Sanity!"
    echo ""
    echo "🌐 View in Studio: http://localhost:3333"
    echo ""
    echo "Next: Tell me and I'll connect your HTML to Sanity!"
else
    echo ""
    echo "❌ Import failed. Check the error above."
fi
