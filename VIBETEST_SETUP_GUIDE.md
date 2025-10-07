# Vibetest Setup Guide for Tiger CMS

## Current Status

✅ Vibetest repository cloned to `/Users/donnysmith/Desktop/Tiger CMS/vibetest-use`  
⚠️ **Python 3.11+ Required** (Currently have Python 3.9.6)

Vibetest requires Python 3.11 or higher to run. Follow the steps below to complete the setup.

---

## Step 1: Install Python 3.11+

### Option A: Install Homebrew (Recommended)

If you don't have Homebrew installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Python 3.11:

```bash
brew install python@3.11
```

### Option B: Download from Python.org

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11+ installer for macOS
3. Run the installer

### Option C: Use pyenv (For multiple Python versions)

```bash
# Install pyenv
curl https://pyenv.run | bash

# Install Python 3.11
pyenv install 3.11.0
pyenv global 3.11.0
```

---

## Step 2: Complete Vibetest Installation

Once Python 3.11+ is installed, run these commands:

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS/vibetest-use"

# Remove old virtual environment
rm -rf .venv

# Create new virtual environment with Python 3.11+
python3.11 -m venv .venv
# OR if pyenv: python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install Vibetest
pip install -e .

# Install Playwright browser
playwright install chromium --with-deps --no-shell
```

---

## Step 3: Configure Cursor MCP Settings

### Get Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key

### Add to Cursor

1. Open Cursor Settings (⌘ + ,)
2. Click "Features" in the left sidebar
3. Find "Cursor Tab" or "AI" section
4. Look for MCP settings or click the gear icon
5. Add this configuration:

```json
{
  "mcpServers": {
    "vibetest": {
      "command": "/Users/donnysmith/Desktop/Tiger CMS/vibetest-use/.venv/bin/vibetest-mcp",
      "env": {
        "GOOGLE_API_KEY": "your_google_api_key_here"
      }
    }
  }
}
```

### Alternative: Edit MCP config file directly

Edit `~/Library/Application Support/Cursor/User/globalStorage/mcp.json`:

```json
{
  "mcpServers": {
    "vibetest": {
      "command": "/Users/donnysmith/Desktop/Tiger CMS/vibetest-use/.venv/bin/vibetest-mcp",
      "env": {
        "GOOGLE_API_KEY": "your_google_api_key_here"
      }
    }
  }
}
```

---

## Step 4: Test Vibetest

Once everything is configured, restart Cursor and try these prompts in the AI chat:

```
# Test your Tiger CMS sites
> Vibetest my website with 5 agents: file:///Users/donnysmith/Desktop/Tiger%20CMS/index.html

# Or if you have a local server running:
> Run vibetest on localhost:3000

# For thorough testing:
> Run a headless vibetest on localhost:8080 with 10 agents
```

---

## Usage Examples for Tiger CMS

### Test Main Homepage
```
Vibetest index.html with 5 agents
```

### Test Specific Site
```
Vibetest tiger-aesthetics.com with 3 agents
Vibetest sientra.com with 5 agents non-headless
```

### Test All Sites (Manual)
You can run tests on each subdomain:
- airway-medix.com
- bellafill.com
- birthtissuerecovery.com
- encoresurgicalsupplies.com
- extremitycare.com
- lizard-health.com
- myaveli.com
- sientra.com
- tiger-aesthetics.com
- tigerbiosciences.com
- tigerwoundcare.com

---

## What Vibetest Will Find

✅ **Broken Links** - Dead internal/external links  
✅ **UI Bugs** - Layout issues, missing elements  
✅ **Accessibility Issues** - Missing alt text, poor contrast  
✅ **JavaScript Errors** - Console errors, failed scripts  
✅ **Mobile Responsiveness** - Mobile/tablet display issues  
✅ **Form Validation** - Contact forms, submission issues  
✅ **Navigation Problems** - Menu issues, broken nav  

---

## Parameters You Can Specify

- **Number of agents**: `3` (default), `5 agents`, `10 agents`
  - More agents = more thorough testing
  
- **Headless mode**: `non-headless` (default) or `headless`
  - Non-headless: You can see browsers in action
  - Headless: Runs in background (faster)

- **URL formats**:
  - Live sites: `https://example.com`
  - Localhost: `localhost:3000`, `localhost:8080`
  - Local files: `file:///path/to/file.html`

---

## Troubleshooting

### "Command not found: vibetest-mcp"
Make sure you've activated the virtual environment and installed vibetest:
```bash
cd "/Users/donnysmith/Desktop/Tiger CMS/vibetest-use"
source .venv/bin/activate
pip install -e .
```

### "GOOGLE_API_KEY not set"
Add your Google API key to the MCP configuration (Step 3)

### Playwright browser issues
Reinstall the browser:
```bash
playwright install chromium --with-deps --no-shell
```

### Permission errors
Make sure the vibetest-mcp script is executable:
```bash
chmod +x .venv/bin/vibetest-mcp
```

---

## Quick Command Reference

```bash
# Activate vibetest environment
cd "/Users/donnysmith/Desktop/Tiger CMS/vibetest-use"
source .venv/bin/activate

# Update vibetest
pip install -e . --upgrade

# Reinstall browser
playwright install chromium --with-deps --no-shell

# Deactivate environment
deactivate
```

---

## Next Steps

1. ✅ Install Python 3.11+
2. ✅ Complete Vibetest installation
3. ✅ Configure Cursor MCP settings
4. ✅ Get Google API key
5. ✅ Test with Tiger CMS sites

Once completed, you can vibetest any of your Tiger CMS sites directly from Cursor!




