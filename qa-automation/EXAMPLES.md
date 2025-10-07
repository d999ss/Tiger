# Tiger CMS Visual QA - Usage Examples 📚

Practical examples for common visual QA workflows.

## Table of Contents

1. [Quick Screenshot All Sites](#1-quick-screenshot-all-sites)
2. [Full QA with Navigation Testing](#2-full-qa-with-navigation-testing)
3. [Visual Regression Testing](#3-visual-regression-testing)
4. [Check for Broken Assets](#4-check-for-broken-assets)
5. [Test Specific Sites Only](#5-test-specific-sites-only)
6. [Automated Nightly Testing](#6-automated-nightly-testing)
7. [Pre-Deployment Checklist](#7-pre-deployment-checklist)

---

## 1. Quick Screenshot All Sites

**Use Case**: Daily visual check of all 11 Tiger sites

### Command:

```bash
./run-qa.sh quick
```

Or directly:

```bash
python3 browser_qa.py
```

### What It Does:

- Opens Chrome
- Visits each Tiger site homepage
- Takes full-page screenshot
- Saves to `screenshots/[timestamp]/`
- Generates `results.json` with status

### Output:

```
screenshots/
  20251007_143022/
    Airway_Medix.png
    Sientra.png
    Tiger_Aesthetics.png
    ...
    results.json
```

### When to Use:

- ✅ Before client meetings
- ✅ After making design changes
- ✅ As part of morning routine
- ✅ Before deployment

---

## 2. Full QA with Navigation Testing

**Use Case**: Comprehensive testing with navigation verification

### Command:

```bash
./run-qa.sh full
```

Or:

```bash
python3 visual_qa.py
```

### What It Does:

- Tests all sites
- Checks multiple pages per site
- Verifies navigation elements
- Tests at different screen sizes (optional)
- Generates HTML report with all screenshots

### Output:

```
reports/
  20251007_143022/
    Sientra_homepage_Desktop.png
    Sientra_contact_Desktop.png
    qa_report.html  ← Open in browser
    qa_report.json
```

### Customization:

Edit `visual_qa.py` to add more pages:

```python
{
    "name": "Sientra",
    "path": "sientra.com/index.html",
    "key_pages": [
        "index.html",
        "breast-augmentation/index.html",
        "breast-reconstruction/index.html",
        "contact-us/index.html",
        "privacy-statement/index.html"  # Add more pages
    ]
}
```

### When to Use:

- ✅ Weekly comprehensive check
- ✅ Before major releases
- ✅ After structural changes
- ✅ For detailed QA reports

---

## 3. Visual Regression Testing

**Use Case**: Detect visual changes between versions

### Workflow:

#### Step 1: Capture Baseline

```bash
python3 browser_qa.py
# Screenshots saved to screenshots/20251007_100000/
```

#### Step 2: Make Your Changes

Edit HTML, CSS, or content files.

#### Step 3: Capture New Screenshots

```bash
python3 browser_qa.py
# Screenshots saved to screenshots/20251007_140000/
```

#### Step 4: Compare

```bash
python3 compare_screenshots.py
```

Interactive mode will ask:

```
📁 Available screenshot runs:

  [0] 20251007_140000 (11 sites)
  [1] 20251007_100000 (11 sites)

Enter baseline run number [0]: 1
Enter current run number [1]: 0
```

### Output:

```
📊 Comparing:
   Baseline: 20251007_100000
   Current:  20251007_140000

✅ SAME Airway Medix: 0.23% difference
✅ SAME Bellafill: 0.15% difference
🔴 CHANGED Sientra: 12.45% difference
✅ SAME Tiger Aesthetics: 0.31% difference
...

📈 Summary:
   Changed: 1
   Unchanged: 10
   Total: 11
```

### When to Use:

- ✅ Before/after comparisons
- ✅ Catch unintended visual changes
- ✅ Verify design consistency
- ✅ QA after bulk changes

---

## 4. Check for Broken Assets

**Use Case**: Find missing images, CSS, and JavaScript files

### Command:

```bash
python3 check_assets.py
```

### Requirements:

```bash
pip install beautifulsoup4 lxml
```

### What It Checks:

- ✅ Missing images (`<img>` tags)
- ✅ Missing CSS files (`<link rel="stylesheet">`)
- ✅ Missing JavaScript (`<script src="">`)
- ✅ Broken internal links (`<a href="">`)

### Output:

```
🔍 Checking assets for all Tiger CMS sites...

Checking: Airway Medix
  ✅ No issues found

Checking: Sientra
  ⚠️  Found 3 issue(s):
     - 2 missing images
     - 1 missing CSS files

Checking: Tiger Aesthetics
  ✅ No issues found

📄 Full report saved: qa-automation/asset_check_report.json

📊 Summary:
   Sites checked: 11
   ✅ OK: 9
   ⚠️  With issues: 2
```

### JSON Report:

```json
{
  "site": "Sientra",
  "issues": {
    "missing_images": [
      {
        "src": "images/hero-banner.jpg",
        "alt": "Hero Banner",
        "expected_path": "/Users/.../sientra.com/images/hero-banner.jpg"
      }
    ],
    "missing_css": [...],
    "missing_js": [...],
    "missing_links": [...]
  },
  "total_issues": 3
}
```

### When to Use:

- ✅ After moving files
- ✅ Before deployment
- ✅ After bulk updates
- ✅ Regular maintenance

---

## 5. Test Specific Sites Only

**Use Case**: Quick test of one or two sites during active development

### Method 1: Edit the Python Script

Edit `browser_qa.py`:

```python
sites = [
    ("Sientra", "sientra.com/index.html"),
    ("Tiger Aesthetics", "tiger-aesthetics.com/index.html"),
]
```

Run:

```bash
python3 browser_qa.py
```

### Method 2: Create Custom Script

Create `test_single.py`:

```python
import terminator
import time
from pathlib import Path

desktop = terminator.Desktop()
base_path = "/Users/donnysmith/Desktop/Tiger CMS"

# Open browser
desktop.open_application('chrome')
time.sleep(3)

# Navigate to site
site_path = Path(base_path) / "sientra.com/index.html"
url = f"file://{site_path}"

desktop.locator('role:textbox name:Address').click()
desktop.type_text(url)
desktop.press_key('{Return}')
time.sleep(2)

# Take screenshot
desktop.screenshot('sientra_test.png')
print("✅ Screenshot saved: sientra_test.png")
```

Run:

```bash
python3 test_single.py
```

### When to Use:

- ✅ Active development on one site
- ✅ Quick iteration testing
- ✅ Debugging specific issues

---

## 6. Automated Nightly Testing

**Use Case**: Run QA automatically every night

### Option 1: Cron Job (macOS/Linux)

Edit crontab:

```bash
crontab -e
```

Add:

```bash
# Run QA every night at 2 AM
0 2 * * * cd "/Users/donnysmith/Desktop/Tiger CMS/qa-automation" && python3 browser_qa.py >> ~/qa_cron.log 2>&1
```

### Option 2: LaunchAgent (macOS)

Create `~/Library/LaunchAgents/com.tiger.qa.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.tiger.qa</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/Users/donnysmith/Desktop/Tiger CMS/qa-automation/browser_qa.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
```

Load:

```bash
launchctl load ~/Library/LaunchAgents/com.tiger.qa.plist
```

### Option 3: Task Scheduler (Windows)

Create `run_qa.bat`:

```batch
@echo off
cd "C:\Users\YourName\Desktop\Tiger CMS\qa-automation"
python browser_qa.py
```

Schedule in Task Scheduler:
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Daily at 2:00 AM
4. Action: Start a program → `run_qa.bat`

### When to Use:

- ✅ Continuous monitoring
- ✅ Catch issues early
- ✅ No manual intervention needed

---

## 7. Pre-Deployment Checklist

**Use Case**: Comprehensive check before pushing changes live

### Full Workflow:

```bash
#!/bin/bash
# pre-deploy.sh

echo "🐅 Tiger CMS Pre-Deployment Checklist"
echo "======================================"

# 1. Check for broken assets
echo -e "\n1️⃣ Checking for broken assets..."
python3 check_assets.py

# 2. Capture baseline (if not already done)
echo -e "\n2️⃣ Capturing current state..."
python3 browser_qa.py

# 3. Run full QA
echo -e "\n3️⃣ Running comprehensive QA..."
python3 visual_qa.py

# 4. Open reports
echo -e "\n4️⃣ Opening reports for review..."
open reports/*/qa_report.html
open asset_check_report.json

echo -e "\n✅ Pre-deployment checks complete!"
echo "Review the reports before deploying."
```

Make executable:

```bash
chmod +x pre-deploy.sh
```

Run:

```bash
./pre-deploy.sh
```

### Checklist:

- [ ] No broken assets
- [ ] All sites screenshot successfully
- [ ] Navigation works on all pages
- [ ] Visual regression check passes
- [ ] Reports reviewed and approved

---

## Advanced Patterns

### Custom Assertions

Add custom checks to `browser_qa.py`:

```python
def check_title(desktop, expected_title):
    """Check if page title matches expected"""
    # Implementation depends on browser automation capabilities
    pass

def check_responsive(desktop, site_name):
    """Test at multiple screen sizes"""
    sizes = [(1920, 1080), (768, 1024), (375, 667)]
    for width, height in sizes:
        # Resize window
        # Take screenshot
        pass
```

### Performance Timing

Track page load times:

```python
import time

start = time.time()
# Navigate to page
load_time = time.time() - start

if load_time > 3:
    print(f"⚠️  Slow load time: {load_time:.2f}s")
```

### Email Notifications

Send results via email:

```python
import smtplib
from email.mime.text import MIMEText

def send_report(results):
    msg = MIMEText(f"QA Results: {results}")
    msg['Subject'] = 'Tiger CMS QA Report'
    msg['From'] = 'qa@tiger.com'
    msg['To'] = 'team@tiger.com'
    
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)
```

---

## Tips & Tricks

### Speed Up Testing

- Use local web server instead of file:// URLs
- Reduce wait times for fast-loading pages
- Test only changed sites during development

### Better Screenshots

- Maximize browser window for consistent sizing
- Wait for animations to complete
- Scroll to capture full page (requires additional code)

### Debugging

- Add `print()` statements to track progress
- Increase `time.sleep()` values if actions fail
- Check Terminator logs: `~/.terminator/logs/`

---

## Next Steps

- Integrate with CI/CD pipeline
- Add Slack/Discord notifications
- Create custom reports with branding
- Implement A/B testing comparisons

**Questions?** Check the [README](README.md) or [Setup Guide](SETUP_GUIDE.md).

