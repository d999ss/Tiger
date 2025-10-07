#!/usr/bin/env python3
"""
Browser-focused Visual QA using Terminator
Simpler approach using browser automation
"""

import terminator
import time
from datetime import datetime
from pathlib import Path
import json

class BrowserQA:
    def __init__(self, base_path="/Users/donnysmith/Desktop/Tiger CMS"):
        self.base_path = Path(base_path)
        self.desktop = terminator.Desktop()
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = self.base_path / "qa-automation" / f"screenshots/{self.timestamp}"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def screenshot_all_sites(self):
        """Quick screenshot capture of all Tiger sites"""
        sites = [
            ("Airway Medix", "airway-medix.com/index.html"),
            ("Bellafill", "bellafill.com/index.html"),
            ("Birth Tissue Recovery", "birthtissuerecovery.com/index.html"),
            ("Encore Surgical", "encoresurgicalsupplies.com/index.html"),
            ("Extremity Care", "extremitycare.com/index.html"),
            ("Lizard Health", "lizard-health.com/index.html"),
            ("MyAveli", "myaveli.com/index.html"),
            ("Sientra", "sientra.com/index.html"),
            ("Tiger Aesthetics", "tiger-aesthetics.com/index.html"),
            ("Tiger Biosciences", "tigerbiosciences.com/index.html"),
            ("Tiger Wound Care", "tigerwoundcare.com/index.html"),
        ]
        
        print("🌐 Opening browser...")
        self.desktop.open_application('chrome')
        time.sleep(3)
        
        results = []
        
        for name, path in sites:
            print(f"\n📸 Capturing: {name}")
            
            try:
                # Navigate to site
                full_path = self.base_path / path
                url = f"file://{full_path}"
                
                # Click address bar and enter URL
                self.desktop.locator('role:textbox').filter(name='Address').click()
                time.sleep(0.3)
                
                # Clear and type new URL
                self.desktop.press_key('{Ctrl}a')
                self.desktop.type_text(url)
                self.desktop.press_key('{Return}')
                time.sleep(2.5)  # Wait for page load
                
                # Take screenshot
                screenshot_name = f"{name.replace(' ', '_')}.png"
                screenshot_path = self.output_dir / screenshot_name
                self.desktop.screenshot(str(screenshot_path))
                
                print(f"✅ Saved: {screenshot_name}")
                
                results.append({
                    "name": name,
                    "path": path,
                    "screenshot": str(screenshot_path),
                    "status": "success"
                })
                
            except Exception as e:
                print(f"❌ Error with {name}: {e}")
                results.append({
                    "name": name,
                    "path": path,
                    "error": str(e),
                    "status": "error"
                })
                
        # Save results
        results_file = self.output_dir / "results.json"
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
            
        print(f"\n✅ Complete! Screenshots saved to: {self.output_dir}")
        return results


def quick_screenshot():
    """Quick screenshot utility"""
    qa = BrowserQA()
    qa.screenshot_all_sites()


if __name__ == "__main__":
    quick_screenshot()

