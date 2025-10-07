# Tiger CMS Visual QA - Setup Guide 🚀

Complete installation and setup guide for automated visual QA testing.

## Prerequisites

- **Operating System**: macOS, Windows, or Linux
- **Browser**: Google Chrome (required for Terminator)
- **Python**: 3.8 or higher
- **Node.js**: 14 or higher (optional, for JavaScript version)

## Installation Steps

### Step 1: Install Terminator

Terminator is the automation engine that powers the visual QA system.

#### On macOS/Linux:

```bash
curl -fsSL https://mediar.ai/install.sh | bash
```

#### On Windows:

Open PowerShell and run:

```powershell
irm https://mediar.ai/install.ps1 | iex
```

### Step 2: Run Terminator Setup

This configures Terminator and installs the Chrome extension:

```bash
terminator setup
```

**Important**: Don't use your keyboard or mouse for a few seconds during setup while the Chrome extension installs automatically.

### Step 3: Install Python Dependencies

Navigate to the qa-automation directory and install requirements:

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS/qa-automation"
pip3 install -r requirements.txt
```

**Optional**: For visual comparison features, install Pillow:

```bash
pip3 install Pillow
```

### Step 4: Verify Installation

Test that everything is working:

```bash
python3 -c "import terminator; print('✅ Terminator ready!')"
```

You should see: `✅ Terminator ready!`

## Quick Test Run

Run a quick screenshot test to verify everything works:

```bash
./run-qa.sh quick
```

This will:
1. Open Chrome
2. Visit all Tiger sites
3. Take screenshots
4. Save them to `screenshots/[timestamp]/`

## Optional: Node.js Version

If you prefer using the Node.js/JavaScript version:

### Install Node.js Dependencies

```bash
npm install
```

### Run Node.js Version

```bash
npm run quick
```

## Troubleshooting

### Issue: "terminator: command not found"

**Solution**: The installation script adds Terminator to your PATH. Try:

1. Close and reopen your terminal
2. Or manually add to your PATH:

```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$HOME/.terminator/bin:$PATH"
```

### Issue: "Chrome extension not installed"

**Solution**: Run setup again:

```bash
terminator setup
```

Make sure Chrome is closed before running setup.

### Issue: Screenshots are blank or black

**Solutions**:

1. **Increase wait times**: Pages may need more time to load
   - Edit `browser_qa.py`
   - Increase `time.sleep(2.5)` to `time.sleep(5)`

2. **Check file paths**: Ensure HTML files exist
   ```bash
   ls "/Users/donnysmith/Desktop/Tiger CMS/sientra.com/index.html"
   ```

3. **Browser display**: Make sure Chrome window is visible (not minimized)

### Issue: "Permission denied" on macOS

**Solution**: Grant accessibility permissions:

1. Open **System Preferences** → **Security & Privacy** → **Privacy** tab
2. Select **Accessibility** from the left sidebar
3. Click the lock icon and enter your password
4. Add **Terminal** (or your Python executable)
5. Restart Terminal

### Issue: Python import errors

**Solution**: Reinstall terminator:

```bash
pip3 uninstall terminator
pip3 install --upgrade terminator
```

### Issue: Chrome opens but doesn't navigate

**Solution**: Verify Chrome extension is active:

1. Open Chrome manually
2. Go to `chrome://extensions/`
3. Look for "Terminator" extension
4. Ensure it's enabled

If not present, run: `terminator setup`

## Advanced Configuration

### Custom Browser Profile

If you want to use a specific Chrome profile:

Edit the script and modify the `open_application` call:

```python
# Open Chrome with specific profile
self.desktop.open_application('chrome', ['--profile-directory=Profile 1'])
```

### Headless Mode

For server environments, use headless Chrome:

```python
self.desktop.open_application('chrome', ['--headless', '--disable-gpu'])
```

### Different Browser

To use Firefox or Edge, modify the application name:

```python
# Firefox
self.desktop.open_application('firefox')

# Edge
self.desktop.open_application('msedge')
```

## Performance Tips

### Speed Up Screenshot Capture

1. **Reduce wait times** (if pages load quickly):
   ```python
   time.sleep(1.5)  # Instead of 2.5
   ```

2. **Use local server** instead of file:// URLs:
   ```bash
   # In Tiger CMS directory
   python3 -m http.server 8000
   
   # Then use http://localhost:8000/sientra.com/index.html
   ```

3. **Parallel execution** (advanced):
   - Modify script to open multiple Chrome windows
   - Process sites concurrently

## Maintenance

### Keep Terminator Updated

Check for updates regularly:

```bash
pip3 install --upgrade terminator
```

Or for the CLI:

```bash
curl -fsSL https://mediar.ai/install.sh | bash
```

### Cleanup Old Screenshots

Screenshots can accumulate over time. Clean up periodically:

```bash
# Keep only last 7 days of screenshots
find screenshots/ -type d -mtime +7 -exec rm -rf {} \;
```

Or create a cleanup script:

```bash
# cleanup.sh
#!/bin/bash
cd "/Users/donnysmith/Desktop/Tiger CMS/qa-automation/screenshots"
ls -t | tail -n +8 | xargs rm -rf
echo "✅ Cleaned up old screenshots (kept 7 most recent)"
```

## Security Considerations

### Accessibility Permissions

Terminator requires accessibility permissions to control your computer. This is normal for automation tools (similar to Selenium, Playwright, etc.).

**What Terminator can do:**
- Control mouse and keyboard
- Read UI element properties
- Take screenshots
- Open and control applications

**What Terminator cannot do:**
- Access files outside permitted directories
- Run without your explicit commands
- Operate when scripts aren't running

### Network Security

Since you're testing local HTML files, no external network requests are made (unless your HTML files load external resources).

To test in an isolated environment:
1. Disconnect from internet
2. Run QA scripts
3. They'll still work with local files

## Getting Help

### Check Logs

If something goes wrong, check Terminator logs:

```bash
# macOS/Linux
tail -f ~/.terminator/logs/terminator.log

# Windows
type %USERPROFILE%\.terminator\logs\terminator.log
```

### Resources

- **Terminator Documentation**: https://github.com/mediar-ai/terminator
- **Terminator Discord**: https://discord.gg/terminator
- **Tiger CMS Docs**: See main README files in project root

### Common Solutions

| Problem | Solution |
|---------|----------|
| Slow screenshots | Increase `time.sleep()` values |
| Missing screenshots | Check file paths are correct |
| Chrome won't open | Verify Chrome is installed and in PATH |
| Extension errors | Run `terminator setup` again |
| Permission denied | Grant accessibility permissions (macOS) |
| Import errors | Reinstall: `pip3 install --force-reinstall terminator` |

## Next Steps

Now that you're set up:

1. ✅ Run your first QA test: `./run-qa.sh quick`
2. 📖 Read the [README.md](README.md) for usage examples
3. 🔧 Customize scripts for your specific needs
4. 📊 Set up visual regression testing with comparison tool

---

**Questions?** Check the [main README](README.md) or open an issue on the Terminator GitHub.

