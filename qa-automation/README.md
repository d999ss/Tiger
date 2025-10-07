# Tiger CMS Visual QA Automation 🐅

Automated visual quality assurance testing for all Tiger CMS websites using [Terminator](https://github.com/mediar-ai/terminator).

## 🎯 What This Does

- **Automated Screenshots**: Capture screenshots of all 11 Tiger websites automatically
- **Cross-page Testing**: Navigate and test multiple pages per site
- **Responsive Testing**: Test at different screen sizes (Desktop, Tablet, Mobile)
- **Navigation Verification**: Ensure links and navigation work correctly
- **Visual Regression**: Compare screenshots over time to catch visual bugs
- **HTML Reports**: Generate beautiful reports with all screenshots

## 📦 Installation

### 1. Install Terminator

**macOS/Linux:**
```bash
curl -fsSL https://mediar.ai/install.sh | bash
```

**Windows:**
```powershell
irm https://mediar.ai/install.ps1 | iex
```

### 2. Run Setup

```bash
terminator setup
```

This will:
- ✅ Install Chrome extension automatically
- ✅ Check system requirements
- ✅ Configure dependencies

### 3. Install Python SDK

```bash
pip install terminator
```

### 4. Verify Installation

Run the setup verification script:

```bash
python3 test_setup.py
```

This will check:
- ✅ Python version (3.8+)
- ✅ Terminator installation
- ✅ Required Python modules
- ✅ All script files present
- 📦 Optional modules (Pillow, BeautifulSoup)

Or quick check:

```bash
python3 -c "import terminator; print('✅ Terminator ready!')"
```

## 🚀 Quick Start

### Option 1: Quick Screenshot All Sites (Recommended)

The simplest way to capture screenshots of all sites:

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS/qa-automation"
python3 browser_qa.py
```

This will:
1. Open Chrome
2. Visit each Tiger site
3. Take a screenshot
4. Save everything to `screenshots/[timestamp]/`

**Output:**
```
screenshots/
  20251007_143022/
    Airway_Medix.png
    Bellafill.png
    Birth_Tissue_Recovery.png
    Encore_Surgical.png
    ...
    results.json
```

### Option 2: Full Visual QA Suite

For comprehensive testing with navigation checks:

```bash
python3 visual_qa.py
```

This will:
1. Test all 11 sites
2. Check multiple pages per site
3. Verify navigation works
4. Generate HTML report with all screenshots
5. Save JSON data for comparison

**Output:**
```
reports/
  20251007_143022/
    Airway_Medix_homepage_Desktop.png
    Airway_Medix_company_Desktop.png
    Bellafill_homepage_Desktop.png
    ...
    qa_report.html  ← Open this in browser!
    qa_report.json
```

## 📋 Usage Examples

### 1. Daily Visual Check

```bash
# Take quick screenshots of all sites
python3 browser_qa.py
```

### 2. Pre-deployment QA

```bash
# Full test before pushing changes
python3 visual_qa.py
```

### 3. Compare Changes

```bash
# Take screenshots before changes
python3 browser_qa.py
# Make your changes
# Take screenshots after
python3 browser_qa.py
# Compare the two screenshot folders
```

### 4. Test Specific Site

Edit `browser_qa.py` and modify the `sites` list to include only the site you want:

```python
sites = [
    ("Sientra", "sientra.com/index.html"),
]
```

## 🛠️ Customization

### Test Different Screen Sizes

In `visual_qa.py`, modify the `SCREEN_SIZES` list:

```python
SCREEN_SIZES = [
    {"name": "Desktop", "width": 1920, "height": 1080},
    {"name": "Laptop", "width": 1440, "height": 900},
    {"name": "Tablet", "width": 768, "height": 1024},
    {"name": "Mobile", "width": 375, "height": 667},
]
```

### Add More Pages to Test

In `visual_qa.py`, add pages to the `key_pages` array:

```python
{
    "name": "Sientra",
    "path": "sientra.com/index.html",
    "key_pages": [
        "index.html",
        "breast-augmentation/index.html",
        "breast-reconstruction/index.html",
        "contact-us/index.html",
        "privacy-statement/index.html"
    ]
}
```

### Change Wait Times

If pages load slowly, increase wait times:

```python
time.sleep(3)  # Wait 3 seconds for page load
```

## 📊 Output Structure

```
qa-automation/
├── browser_qa.py           # Quick screenshot script
├── visual_qa.py            # Full QA suite
├── README.md               # This file
├── screenshots/            # Quick screenshots
│   └── [timestamp]/
│       ├── Site_Name.png
│       └── results.json
└── reports/                # Full QA reports
    └── [timestamp]/
        ├── *_Desktop.png
        ├── *_Tablet.png
        ├── *_Mobile.png
        ├── qa_report.html
        └── qa_report.json
```

## 🐛 Troubleshooting

### Chrome Not Opening

Make sure Chrome is installed and accessible:
```bash
# macOS
open -a "Google Chrome"

# Windows
start chrome

# Linux
google-chrome
```

### Screenshots Are Blank

- Ensure pages have fully loaded (increase `time.sleep()` values)
- Check that file paths are correct
- Verify Chrome extension is installed: `terminator setup`

### Import Error

```bash
# Reinstall terminator
pip uninstall terminator
pip install terminator
```

### Permission Issues

On macOS, you may need to grant accessibility permissions:
1. System Preferences → Security & Privacy → Accessibility
2. Add Terminal or your Python executable

## 🎨 Advanced Use Cases

### 1. Visual Regression Testing

Compare screenshots over time:

```bash
# Baseline screenshots
python3 browser_qa.py
mv screenshots/[timestamp] screenshots/baseline

# After making changes
python3 browser_qa.py
mv screenshots/[timestamp] screenshots/current

# Use image comparison tool
# (could add ImageMagick or Pillow comparison script)
```

### 2. Automated Nightly Tests

Add to crontab for nightly visual checks:

```bash
# Run every night at 2 AM
0 2 * * * cd "/Users/donnysmith/Desktop/Tiger CMS/qa-automation" && python3 browser_qa.py
```

### 3. CI/CD Integration

Add to your deployment pipeline to catch visual regressions automatically.

## 📚 Resources

- [Terminator Documentation](https://github.com/mediar-ai/terminator)
- [Terminator Python API](https://github.com/mediar-ai/terminator/tree/main/bindings/python)
- [Tiger CMS Documentation](../QUICK_START_GUIDE.md)

## 🤝 Contributing

Found a bug or want to add a feature? Edit the scripts directly!

Common additions:
- Link checking
- Performance timing
- Console error detection
- Responsive design testing
- Accessibility audits

## 📝 License

MIT (same as Terminator)

---

**Questions?** Check the main [Tiger CMS documentation](../QUICK_START_GUIDE.md) or the [Terminator GitHub](https://github.com/mediar-ai/terminator).

