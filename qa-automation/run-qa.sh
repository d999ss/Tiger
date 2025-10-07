#!/bin/bash
# Tiger CMS Visual QA Runner
# Convenient wrapper for all QA tasks

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🐅 Tiger CMS Visual QA Automation${NC}\n"

# Check if terminator is installed
if ! command -v terminator &> /dev/null; then
    echo -e "${YELLOW}⚠️  Terminator not found. Installing...${NC}"
    curl -fsSL https://mediar.ai/install.sh | bash
    terminator setup
fi

# Check if Python dependencies are installed
if ! python3 -c "import terminator" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  Installing Python dependencies...${NC}"
    pip3 install -r requirements.txt
fi

# Parse command
case "${1:-quick}" in
    quick)
        echo -e "${GREEN}📸 Running quick screenshot...${NC}\n"
        python3 browser_qa.py
        ;;
    full)
        echo -e "${GREEN}🔍 Running full visual QA...${NC}\n"
        python3 visual_qa.py
        ;;
    node)
        echo -e "${GREEN}📸 Running Node.js version...${NC}\n"
        if [ ! -d "node_modules" ]; then
            echo -e "${YELLOW}⚠️  Installing Node.js dependencies...${NC}"
            npm install
        fi
        node quick-screenshot.js
        ;;
    help|--help|-h)
        echo "Usage: ./run-qa.sh [command]"
        echo ""
        echo "Commands:"
        echo "  quick    Quick screenshot all sites (default)"
        echo "  full     Full QA with navigation testing"
        echo "  node     Run Node.js version"
        echo "  help     Show this help message"
        echo ""
        echo "Examples:"
        echo "  ./run-qa.sh           # Quick screenshots"
        echo "  ./run-qa.sh full      # Full QA suite"
        echo "  ./run-qa.sh node      # Use Node.js version"
        ;;
    *)
        echo -e "${YELLOW}Unknown command: $1${NC}"
        echo "Run './run-qa.sh help' for usage"
        exit 1
        ;;
esac

echo -e "\n${GREEN}✅ Done!${NC}"

