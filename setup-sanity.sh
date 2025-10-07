#!/bin/bash

# Tiger BioSciences - Sanity CMS Setup Script
# This script will help you set up Sanity CMS

echo "🚀 Tiger BioSciences - Sanity CMS Setup"
echo "========================================"
echo ""
echo "This will set up Sanity CMS for your Tiger BioSciences website."
echo ""
echo "👉 I'll guide you through the interactive setup..."
echo ""

# Navigate to project root
cd "/Users/donnysmith/Desktop/Tiger CMS"

# Clean up any existing studio folder
if [ -d "studio" ]; then
    echo "📁 Cleaning up existing studio folder..."
    rm -rf studio
fi

echo ""
echo "📦 Starting Sanity initialization..."
echo ""
echo "WHEN PROMPTED:"
echo "  1. Select: Tiger Biosciences (0nxq33lj)"
echo "  2. Dataset: production"
echo "  3. Output path: ./studio"
echo "  4. Template: Clean project"
echo ""

# Run Sanity init
npx create-sanity@latest

# Check if studio was created
if [ ! -d "studio" ]; then
    echo ""
    echo "❌ Studio folder not created. Please run manually:"
    echo "   npx create-sanity@latest"
    exit 1
fi

echo ""
echo "✅ Sanity Studio initialized!"
echo ""
echo "📋 Now copying pre-made schemas..."

# Copy schemas
if [ -d "studio-schemas/schemaTypes" ]; then
    cp -r studio-schemas/schemaTypes/* studio/schemaTypes/ 2>/dev/null
    echo "✅ Schemas copied successfully!"
else
    echo "⚠️  Schema files not found in studio-schemas/"
    echo "   You'll need to manually copy them after setup."
fi

echo ""
echo "📦 Installing dependencies..."
cd studio
npm install

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎉 Your Sanity Studio is ready!"
echo ""
echo "To start the Studio, run:"
echo "  cd studio"
echo "  npm run dev"
echo ""
echo "Your Studio will open at: http://localhost:3333"
echo ""

