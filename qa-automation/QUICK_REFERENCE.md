# Tiger CMS Visual QA - Quick Reference Card 🚀

One-page reference for common commands and workflows.

## Installation (One-Time Setup)

```bash
# Install Terminator
curl -fsSL https://mediar.ai/install.sh | bash
terminator setup

# Install Python dependencies
cd "/Users/donnysmith/Desktop/Tiger CMS/qa-automation"
pip3 install -r requirements.txt
```

---

## Common Commands

| Task | Command |
|------|---------|
| **Quick screenshots** | `./run-qa.sh quick` |
| **Full QA test** | `./run-qa.sh full` |
| **Node.js version** | `./run-qa.sh node` |
| **Check broken assets** | `python3 check_assets.py` |
| **Compare screenshots** | `python3 compare_screenshots.py` |

---

## Quick Workflows

### 📸 Daily Visual Check

```bash
./run-qa.sh quick
open screenshots/*/
```

### 🔍 Pre-Deployment QA

```bash
python3 check_assets.py           # Check for broken links/images
python3 browser_qa.py              # Take screenshots
open screenshots/*/qa_report.html # Review
```

### 🔄 Visual Regression Testing

```bash
python3 browser_qa.py              # Before changes
# Make your changes
python3 browser_qa.py              # After changes
python3 compare_screenshots.py     # Compare
```

---

## File Structure

```
qa-automation/
├── run-qa.sh              # Main runner script
├── browser_qa.py          # Quick screenshot tool
├── visual_qa.py           # Full QA suite
├── compare_screenshots.py # Visual comparison
├── check_assets.py        # Asset checker
├── screenshots/           # Screenshot output
│   └── [timestamp]/
└── reports/               # Full QA reports
    └── [timestamp]/
```

---

## Customization Quick Tips

### Test Only Specific Sites

Edit `browser_qa.py`, line ~15:

```python
sites = [
    ("Sientra", "sientra.com/index.html"),
    # Comment out others
]
```

### Adjust Wait Times

If pages load slowly, increase sleep:

```python
time.sleep(5)  # Instead of 2.5
```

### Add More Pages to Test

Edit `visual_qa.py`, `SITES` array:

```python
"key_pages": [
    "index.html",
    "about/index.html",  # Add pages here
]
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Command not found | Restart terminal or add to PATH |
| Chrome won't open | Verify Chrome installed |
| Blank screenshots | Increase `time.sleep()` values |
| Import errors | `pip3 install --force-reinstall terminator` |
| Permission denied (macOS) | Grant accessibility permissions |

---

## Output Files

### Screenshots

```
screenshots/YYYYMMDD_HHMMSS/
├── Site_Name.png          # Individual screenshots
└── results.json           # Metadata
```

### Full Reports

```
reports/YYYYMMDD_HHMMSS/
├── Site_Page_Desktop.png  # Screenshots by page/size
├── qa_report.html         # Visual HTML report
└── qa_report.json         # Data export
```

### Asset Checks

```
qa-automation/
└── asset_check_report.json  # Broken asset report
```

---

## Key Scripts

### browser_qa.py
- **Purpose**: Quick screenshots of all sites
- **Time**: ~2-3 minutes
- **Use**: Daily checks

### visual_qa.py
- **Purpose**: Comprehensive multi-page testing
- **Time**: ~5-10 minutes
- **Use**: Weekly/pre-deployment

### compare_screenshots.py
- **Purpose**: Visual regression detection
- **Time**: ~1 minute
- **Use**: After making changes

### check_assets.py
- **Purpose**: Find broken images/links
- **Time**: ~1 minute
- **Use**: Maintenance/debugging

---

## Advanced

### Automated Nightly Testing

```bash
# Add to crontab
crontab -e

# Run at 2 AM daily
0 2 * * * cd "/Users/.../qa-automation" && python3 browser_qa.py
```

### Pre-Deployment Script

```bash
#!/bin/bash
python3 check_assets.py
python3 browser_qa.py
python3 visual_qa.py
open reports/*/qa_report.html
```

---

## Documentation

- **Setup**: [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)
- **Full README**: [README.md](README.md)
- **Terminator Docs**: https://github.com/mediar-ai/terminator

---

## Support

**Issues?** Check:
1. Terminator logs: `~/.terminator/logs/`
2. Run: `terminator setup`
3. Reinstall: `pip3 install --force-reinstall terminator`

**Questions?** See detailed docs or Discord: https://discord.gg/terminator

---

**🐅 Tiger CMS Visual QA** - Automated testing made easy!

