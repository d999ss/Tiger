#!/bin/bash
# Manual Visual QA Testing Guide
# Open each Tiger CMS site in browser for manual review

BASE_PATH="/Users/donnysmith/Desktop/Tiger CMS"

echo "🐅 Tiger CMS Manual Visual QA Guide"
echo "===================================="
echo ""
echo "Opening each website in Chrome for manual review..."
echo "Press Ctrl+C to stop at any time."
echo ""

sites=(
    "airway-medix.com/index.html"
    "bellafill.com/index.html"
    "birthtissuerecovery.com/index.html"
    "encoresurgicalsupplies.com/index.html"
    "extremitycare.com/index.html"
    "lizard-health.com/index.html"
    "myaveli.com/index.html"
    "sientra.com/index.html"
    "tiger-aesthetics.com/index.html"
    "tigerbiosciences.com/index.html"
    "tigerwoundcare.com/index.html"
)

for site in "${sites[@]}"; do
    site_name=$(echo $site | cut -d'/' -f1)
    echo "📸 Opening: $site_name"
    open "file://$BASE_PATH/$site"
    echo "   ✅ Check the page visually"
    echo "   ✅ Take a screenshot manually (Cmd+Shift+4)"
    echo ""
    read -p "   Press Enter to continue to next site..." dummy
done

echo ""
echo "🎉 Manual review complete!"
echo ""
echo "To get FULL automation, install Terminator:"
echo "  curl -fsSL https://mediar.ai/install.sh | bash"
echo "  terminator setup"

