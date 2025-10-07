#!/usr/bin/env python3
"""
Setup Verification Script
Tests that all dependencies and tools are properly installed
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check Python version is 3.8+"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version:", f"{version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} found, need 3.8+")
        return False

def check_module(module_name):
    """Check if a Python module is installed"""
    try:
        __import__(module_name)
        print(f"✅ {module_name} installed")
        return True
    except ImportError:
        print(f"❌ {module_name} not installed")
        return False

def check_command(command):
    """Check if a command is available"""
    try:
        subprocess.run([command, '--version'], 
                      capture_output=True, 
                      check=True,
                      timeout=5)
        print(f"✅ {command} available")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        print(f"❌ {command} not found")
        return False

def check_files():
    """Check if required files exist"""
    base_path = Path(__file__).parent
    files = [
        'browser_qa.py',
        'visual_qa.py',
        'compare_screenshots.py',
        'check_assets.py',
        'run-qa.sh',
        'requirements.txt',
        'README.md'
    ]
    
    all_exist = True
    for file in files:
        path = base_path / file
        if path.exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all checks"""
    print("🔍 Tiger CMS Visual QA - Setup Verification")
    print("=" * 50)
    
    checks = []
    
    # Python version
    print("\n📦 Checking Python:")
    checks.append(check_python_version())
    
    # Required modules
    print("\n📚 Checking Required Modules:")
    checks.append(check_module('terminator'))
    
    # Optional modules
    print("\n📚 Checking Optional Modules:")
    optional_checks = []
    optional_checks.append(check_module('PIL'))  # Pillow
    optional_checks.append(check_module('bs4'))  # BeautifulSoup
    
    # Commands
    print("\n🛠️  Checking Commands:")
    checks.append(check_command('terminator'))
    
    # Files
    print("\n📄 Checking Files:")
    checks.append(check_files())
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)
    
    required_passed = sum(checks)
    required_total = len(checks)
    optional_passed = sum(optional_checks)
    optional_total = len(optional_checks)
    
    print(f"Required checks: {required_passed}/{required_total} passed")
    print(f"Optional checks: {optional_passed}/{optional_total} passed")
    
    if all(checks):
        print("\n🎉 All required checks passed!")
        print("\n✨ You're ready to run visual QA tests!")
        print("\nNext steps:")
        print("  1. Run: ./run-qa.sh quick")
        print("  2. Check: screenshots/*/")
        print("  3. Read: EXAMPLES.md for more workflows")
        return 0
    else:
        print("\n⚠️  Some required checks failed!")
        print("\n🔧 To fix:")
        print("  1. Install Terminator: curl -fsSL https://mediar.ai/install.sh | bash")
        print("  2. Run setup: terminator setup")
        print("  3. Install deps: pip3 install -r requirements.txt")
        print("  4. Run this script again: python3 test_setup.py")
        return 1
    
if __name__ == "__main__":
    sys.exit(main())

