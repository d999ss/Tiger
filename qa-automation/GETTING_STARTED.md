# Getting Started with Tiger CMS Visual QA 🚀

**First time here?** This guide will walk you through your first automated visual QA test in under 10 minutes.

## What You'll Learn

By the end of this guide, you'll:
- ✅ Install and configure Terminator
- ✅ Run your first automated test
- ✅ View and interpret results
- ✅ Know where to go next

Let's get started! 🐅

---

## Step 1: Install Terminator (2 minutes)

Terminator is the automation engine that powers our visual QA system.

### macOS or Linux:

Open Terminal and run:

```bash
curl -fsSL https://mediar.ai/install.sh | bash
```

### Windows:

Open PowerShell and run:

```powershell
irm https://mediar.ai/install.ps1 | iex
```

### What This Does:
- Downloads the Terminator CLI
- Adds it to your system PATH
- Makes it ready to use

---

## Step 2: Configure Terminator (2 minutes)

Now run the setup command:

```bash
terminator setup
```

### ⚠️ Important:
**Don't touch your keyboard or mouse** for a few seconds while this runs. It's automatically installing the Chrome extension.

### What This Does:
- Installs the Terminator Chrome extension
- Checks system requirements
- Configures the environment

You should see: `✅ Setup complete!`

---

## Step 3: Install Python Dependencies (1 minute)

Navigate to the QA automation directory:

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS/qa-automation"
```

Install required Python packages:

```bash
pip3 install -r requirements.txt
```

### What This Installs:
- `terminator` - Core automation library
- `Pillow` - For image comparison (optional)
- `BeautifulSoup4` - For HTML parsing (optional)

---

## Step 4: Verify Everything Works (1 minute)

Run the verification script:

```bash
python3 test_setup.py
```

You should see output like:

```
🔍 Tiger CMS Visual QA - Setup Verification
==================================================

📦 Checking Python:
✅ Python version: 3.11.5

📚 Checking Required Modules:
✅ terminator installed

📚 Checking Optional Modules:
✅ PIL installed
✅ bs4 installed

🛠️  Checking Commands:
✅ terminator available

📄 Checking Files:
✅ browser_qa.py
✅ visual_qa.py
✅ compare_screenshots.py
✅ check_assets.py
✅ run-qa.sh
✅ requirements.txt
✅ README.md

==================================================
📊 SUMMARY
==================================================
Required checks: 4/4 passed
Optional checks: 2/2 passed

🎉 All required checks passed!

✨ You're ready to run visual QA tests!
```

**If you see errors:** Check the [Troubleshooting](#troubleshooting) section below.

---

## Step 5: Run Your First Test! (2-3 minutes)

Now for the fun part - let's take automated screenshots of all 11 Tiger websites!

Run:

```bash
./run-qa.sh quick
```

### What You'll See:

```
🐅 Tiger CMS Visual QA Automation

📸 Running quick screenshot...

🌐 Opening Chrome browser...
Chrome will open automatically

📸 Capturing: Airway Medix
✅ Saved: Airway_Medix.png

📸 Capturing: Bellafill
✅ Saved: Bellafill.png

📸 Capturing: Birth Tissue Recovery
✅ Saved: Birth_Tissue_Recovery.png

... (continues for all 11 sites)

✅ Complete! Screenshots saved to: screenshots/20251007_143022/

✅ Done!
```

**Don't close the browser** - let it do its thing! It will:
1. Open Chrome
2. Visit each Tiger website
3. Wait for the page to load
4. Take a screenshot
5. Move to the next site

This takes about 2-3 minutes total.

---

## Step 6: View Your Results (1 minute)

Open the screenshots folder:

```bash
open screenshots/
```

Or navigate in Finder to:
```
Tiger CMS/qa-automation/screenshots/[timestamp]/
```

You'll see:
- **11 PNG files** - One for each website
- **results.json** - Metadata about the test run

### Example: results.json

```json
[
  {
    "name": "Airway Medix",
    "path": "airway-medix.com/index.html",
    "screenshot": "/Users/.../screenshots/.../Airway_Medix.png",
    "status": "success",
    "timestamp": "2025-10-07T14:30:22.123Z"
  },
  ...
]
```

---

## 🎉 Congratulations!

You just ran your first automated visual QA test!

Here's what you accomplished:
- ✅ Automatically opened and controlled Chrome
- ✅ Visited all 11 Tiger websites
- ✅ Captured high-quality screenshots
- ✅ Generated a timestamped report

**Time saved:** What would have taken 30+ minutes manually took less than 3 minutes!

---

## What's Next?

### Try These Commands

#### 1. Check for Broken Images/Links

```bash
python3 check_assets.py
```

This scans all HTML files and reports:
- Missing images
- Broken CSS links
- Dead JavaScript files
- Invalid internal links

#### 2. Run Full QA with Multiple Pages

```bash
./run-qa.sh full
```

This tests not just homepages, but:
- Contact pages
- About pages
- Product pages
- Generates a beautiful HTML report

#### 3. Compare Before/After Changes

```bash
# Take screenshots (before)
python3 browser_qa.py

# Make your changes to HTML/CSS

# Take screenshots again (after)
python3 browser_qa.py

# Compare them
python3 compare_screenshots.py
```

This will show you exactly what changed!

---

## Learn More

Now that you're set up, explore these guides:

### 📖 Documentation

1. **[README.md](README.md)** - Full feature overview
2. **[EXAMPLES.md](EXAMPLES.md)** - 7 practical workflows
3. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Command cheat sheet
4. **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup troubleshooting

### 🎓 Recommended Learning Path

**Day 1** (Today):
- ✅ Complete this getting started guide
- ✅ Run `./run-qa.sh quick` 
- ✅ View your screenshots

**Day 2** (Tomorrow):
- 📖 Read [EXAMPLES.md](EXAMPLES.md) - "Daily Visual Check"
- 🔄 Set up your daily QA routine
- 📊 Try the asset checker: `python3 check_assets.py`

**Day 3** (This week):
- 🔍 Read [EXAMPLES.md](EXAMPLES.md) - "Visual Regression Testing"
- 🎨 Make a change and test before/after
- 📈 Use `compare_screenshots.py`

**Week 2**:
- 🤖 Set up automated nightly tests (cron job)
- 🛠️ Customize scripts for your workflow
- 📝 Create pre-deployment checklist

---

## Troubleshooting

### ❌ "terminator: command not found"

**Solution:**
1. Close and reopen your terminal
2. Or manually add to PATH:
   ```bash
   export PATH="$HOME/.terminator/bin:$PATH"
   ```
3. Add to `~/.zshrc` or `~/.bashrc` to make permanent

### ❌ Chrome Won't Open

**Solution:**
1. Verify Chrome is installed:
   ```bash
   open -a "Google Chrome"  # macOS
   ```
2. If not installed, download from: https://www.google.com/chrome/

### ❌ Screenshots Are Blank/Black

**Solution:**
1. Edit `browser_qa.py`
2. Find the line: `time.sleep(2.5)`
3. Change to: `time.sleep(5)`
4. Save and try again

This gives pages more time to load.

### ❌ "Module 'terminator' not found"

**Solution:**
```bash
pip3 install --force-reinstall terminator
```

### ❌ Permission Denied (macOS only)

**Solution:**
1. Open **System Preferences**
2. Go to **Security & Privacy** → **Privacy** tab
3. Select **Accessibility** from left sidebar
4. Click lock icon and enter password
5. Add **Terminal** to the list
6. Restart Terminal

### Still Having Issues?

1. Check Terminator logs:
   ```bash
   tail -f ~/.terminator/logs/terminator.log
   ```

2. Re-run setup:
   ```bash
   terminator setup
   ```

3. Check the [SETUP_GUIDE.md](SETUP_GUIDE.md) for more help

---

## Tips for Success

### 💡 Best Practices

1. **Run tests regularly** - Make it part of your routine
2. **Keep screenshots** - They're useful for comparisons
3. **Check asset reports** - Catch issues early
4. **Customize wait times** - Adjust for your needs

### ⚡ Pro Tips

- **Use `./run-qa.sh quick`** for daily checks (fastest)
- **Set up cron jobs** for automated overnight testing
- **Keep baseline screenshots** for before/after comparisons
- **Review reports** before client meetings

### 🎯 Common Workflows

**Morning Routine:**
```bash
./run-qa.sh quick
open screenshots/*/
```

**Before Deployment:**
```bash
python3 check_assets.py
python3 browser_qa.py
```

**After Making Changes:**
```bash
python3 browser_qa.py  # Before
# Make changes
python3 browser_qa.py  # After
python3 compare_screenshots.py
```

---

## Quick Command Reference

```bash
# Run quick screenshots (recommended)
./run-qa.sh quick

# Run full QA test
./run-qa.sh full

# Check for broken assets
python3 check_assets.py

# Compare screenshots
python3 compare_screenshots.py

# Verify setup
python3 test_setup.py

# Get help
./run-qa.sh help
```

---

## Support & Resources

### 📚 Documentation
- Main README: [README.md](README.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Quick Reference: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

### 🌐 External Resources
- Terminator GitHub: https://github.com/mediar-ai/terminator
- Terminator Discord: https://discord.gg/terminator
- Terminator Docs: https://github.com/mediar-ai/terminator/tree/main/docs

### 💬 Getting Help
1. Check the troubleshooting section
2. Read the SETUP_GUIDE.md
3. Check Terminator logs
4. Visit Terminator Discord

---

## What You've Learned

In this guide, you:
- ✅ Installed Terminator automation framework
- ✅ Set up the Tiger CMS visual QA system
- ✅ Ran your first automated test
- ✅ Captured screenshots of all 11 websites
- ✅ Learned where to find results
- ✅ Know what to explore next

**You're now ready to automate your visual QA workflow!** 🎉

---

## Next Steps

Choose your own adventure:

**→ I want to learn more workflows**
- Read [EXAMPLES.md](EXAMPLES.md) for 7 practical examples

**→ I want a quick command reference**
- Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for all commands

**→ I need help customizing**
- See [README.md](README.md) for customization options

**→ I'm having technical issues**
- Read [SETUP_GUIDE.md](SETUP_GUIDE.md) for troubleshooting

---

**Happy Testing! 🐅**

*Remember: Automated testing saves time, catches bugs, and makes your life easier.*

