# 🐯 Vibetest Quick Start - Tiger CMS

## 🚦 Current Status
- ✅ Vibetest repository cloned
- ⚠️ **Needs Python 3.11+** (you have 3.9.6)

---

## 📝 Quick Setup (3 commands)

```bash
# 1. Install Python 3.11+ (choose one):
brew install python@3.11
# OR download from: https://www.python.org/downloads/

# 2. Run automated setup:
cd "/Users/donnysmith/Desktop/Tiger CMS/vibetest-use"
./complete-setup.sh

# 3. Get API key and configure Cursor
# Get key: https://makersuite.google.com/app/apikey
# Add to Cursor MCP settings (see below)
```

---

## ⚙️ Cursor MCP Configuration

**Path:** Cursor Settings → Features → MCP

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

## 🎯 Test Your Tiger CMS Sites

### Test Local Files
```
Vibetest index.html with 5 agents
Vibetest about.html with 3 agents
```

### Test With Local Server
```bash
# First, start a local server in another terminal:
cd "/Users/donnysmith/Desktop/Tiger CMS"
python3 -m http.server 8000

# Then in Cursor:
Vibetest localhost:8000 with 5 agents
Vibetest localhost:8000/tiger-aesthetics.com with 3 agents
```

### Test All Sites Systematically
```
Vibetest localhost:8000/airway-medix.com with 5 agents non-headless
Vibetest localhost:8000/bellafill.com with 5 agents
Vibetest localhost:8000/birthtissuerecovery.com with 5 agents
Vibetest localhost:8000/encoresurgicalsupplies.com with 5 agents
Vibetest localhost:8000/extremitycare.com with 5 agents
Vibetest localhost:8000/lizard-health.com with 5 agents
Vibetest localhost:8000/myaveli.com with 5 agents
Vibetest localhost:8000/sientra.com with 5 agents
Vibetest localhost:8000/tiger-aesthetics.com with 5 agents
Vibetest localhost:8000/tigerbiosciences.com with 5 agents
Vibetest localhost:8000/tigerwoundcare.com with 5 agents
```

---

## 🔍 What Gets Tested

| Category | What Vibetest Finds |
|----------|---------------------|
| 🔗 **Links** | Broken internal/external links, 404s |
| 🎨 **UI** | Layout breaks, missing images, CSS issues |
| ♿ **Accessibility** | Missing alt text, poor contrast, ARIA issues |
| 📱 **Responsive** | Mobile/tablet display problems |
| ⚡ **Performance** | Slow loading, large files |
| 📝 **Forms** | Contact forms, validation issues |
| 🧭 **Navigation** | Menu problems, broken paths |
| 🐛 **JavaScript** | Console errors, failed scripts |

---

## 🎛️ Testing Options

### Number of Agents
- `3 agents` - Quick test (default)
- `5 agents` - Balanced (recommended)
- `10 agents` - Thorough test

**More agents = more coverage but slower**

### Display Mode
- `non-headless` - See browsers in action (default)
- `headless` - Runs in background (faster)

### Example Combinations
```
# Quick test with visible browsers
Vibetest localhost:8000 with 3 agents non-headless

# Thorough test in background
Vibetest localhost:8000 with 10 agents headless

# Balanced test
Vibetest localhost:8000/index.html with 5 agents
```

---

## 🛠️ Troubleshooting

### "Python 3.11+ required"
```bash
brew install python@3.11
# Then run ./complete-setup.sh again
```

### "vibetest-mcp not found"
```bash
cd "/Users/donnysmith/Desktop/Tiger CMS/vibetest-use"
source .venv/bin/activate
pip install -e .
```

### "GOOGLE_API_KEY not set"
1. Get key: https://makersuite.google.com/app/apikey
2. Add to Cursor MCP settings (see above)
3. Restart Cursor

### Playwright issues
```bash
cd "/Users/donnysmith/Desktop/Tiger CMS/vibetest-use"
source .venv/bin/activate
playwright install chromium --with-deps --no-shell
```

---

## 📚 Full Documentation

See `VIBETEST_SETUP_GUIDE.md` for detailed instructions.

---

## 🎬 Ready to Go?

1. ✅ Install Python 3.11+
2. ✅ Run `./complete-setup.sh`
3. ✅ Get Google API key
4. ✅ Configure Cursor MCP
5. ✅ Restart Cursor
6. ✅ Start testing!

```
Vibetest my Tiger CMS with 5 agents! 🐯
```





