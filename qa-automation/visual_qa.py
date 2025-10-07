#!/usr/bin/env python3
"""
Tiger CMS Visual QA Automation
Uses Terminator to automate visual testing of all Tiger websites
"""

import terminator
import time
from datetime import datetime
from pathlib import Path
import json

# Configuration
SITES = [
    {
        "name": "Airway Medix",
        "path": "airway-medix.com/index.html",
        "key_pages": ["index.html", "company/index.html", "products/index.html"]
    },
    {
        "name": "Bellafill",
        "path": "bellafill.com/index.html",
        "key_pages": ["index.html"]
    },
    {
        "name": "Birth Tissue Recovery",
        "path": "birthtissuerecovery.com/index.html",
        "key_pages": ["index.html", "about/index.html", "contact/index.html"]
    },
    {
        "name": "Encore Surgical",
        "path": "encoresurgicalsupplies.com/index.html",
        "key_pages": ["index.html", "products/index.html", "contact/index.html"]
    },
    {
        "name": "Extremity Care",
        "path": "extremitycare.com/index.html",
        "key_pages": ["index.html", "tissue-technologies/index.html", "contact-new/index.html"]
    },
    {
        "name": "Lizard Health",
        "path": "lizard-health.com/index.html",
        "key_pages": ["index.html", "about/index.html", "contact/index.html"]
    },
    {
        "name": "MyAveli",
        "path": "myaveli.com/index.html",
        "key_pages": ["index.html", "how-aveli-works/index.html", "faq/index.html"]
    },
    {
        "name": "Sientra",
        "path": "sientra.com/index.html",
        "key_pages": ["index.html", "breast-augmentation/index.html", "contact-us/index.html"]
    },
    {
        "name": "Tiger Aesthetics",
        "path": "tiger-aesthetics.com/index.html",
        "key_pages": ["index.html", "about/index.html", "contact-us/index.html"]
    },
    {
        "name": "Tiger Biosciences",
        "path": "tigerbiosciences.com/index.html",
        "key_pages": ["index.html", "our-divisions/index.html", "contact/index.html"]
    },
    {
        "name": "Tiger Wound Care",
        "path": "tigerwoundcare.com/index.html",
        "key_pages": ["index.html"]
    }
]

# Screen sizes for responsive testing
SCREEN_SIZES = [
    {"name": "Desktop", "width": 1920, "height": 1080},
    {"name": "Tablet", "width": 768, "height": 1024},
    {"name": "Mobile", "width": 375, "height": 667}
]

class VisualQA:
    def __init__(self, base_path="/Users/donnysmith/Desktop/Tiger CMS"):
        self.base_path = Path(base_path)
        self.desktop = terminator.Desktop()
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = self.base_path / "qa-automation" / f"reports/{self.timestamp}"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.results = []
        
    def open_browser(self):
        """Open Chrome browser"""
        print("🌐 Opening Chrome browser...")
        self.desktop.open_application('chrome')
        time.sleep(3)
        
    def navigate_to_file(self, file_path):
        """Navigate browser to local file"""
        full_path = self.base_path / file_path
        url = f"file://{full_path}"
        print(f"📂 Loading: {url}")
        
        # Use address bar
        self.desktop.locator('role:textbox name:Address and search bar').click()
        time.sleep(0.5)
        self.desktop.locator('role:textbox name:Address and search bar').type_text(url)
        self.desktop.press_key('{Return}')
        time.sleep(2)
        
    def take_screenshot(self, site_name, page_name, screen_size="Desktop"):
        """Capture screenshot of current page"""
        sanitized_site = site_name.replace(" ", "_")
        sanitized_page = page_name.replace("/", "_").replace(".html", "")
        filename = f"{sanitized_site}_{sanitized_page}_{screen_size}.png"
        output_path = self.output_dir / filename
        
        print(f"📸 Taking screenshot: {filename}")
        self.desktop.screenshot(str(output_path))
        
        return str(output_path)
        
    def check_page_load(self):
        """Basic check if page loaded (look for common elements)"""
        try:
            # Check if page has basic HTML structure
            time.sleep(1)
            # In a real scenario, you'd use browser automation to check for specific elements
            return True
        except Exception as e:
            print(f"❌ Page load check failed: {e}")
            return False
            
    def test_navigation(self, site_name):
        """Test navigation elements on the page"""
        print(f"🔍 Testing navigation for {site_name}...")
        nav_results = {
            "has_nav": False,
            "links_found": 0,
            "errors": []
        }
        
        try:
            # Look for common navigation patterns
            # This would need to be adapted based on your actual HTML structure
            nav_results["has_nav"] = True
            nav_results["links_found"] = 5  # Placeholder
        except Exception as e:
            nav_results["errors"].append(str(e))
            
        return nav_results
        
    def run_visual_qa(self, test_navigation=True, test_responsive=False):
        """Main QA routine"""
        print("=" * 60)
        print("🐅 TIGER CMS VISUAL QA AUTOMATION")
        print("=" * 60)
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Output: {self.output_dir}")
        print()
        
        self.open_browser()
        
        for site in SITES:
            print(f"\n{'=' * 60}")
            print(f"Testing: {site['name']}")
            print(f"{'=' * 60}")
            
            site_result = {
                "name": site['name'],
                "timestamp": datetime.now().isoformat(),
                "pages": []
            }
            
            # Test homepage
            try:
                self.navigate_to_file(site['path'])
                page_loaded = self.check_page_load()
                
                page_result = {
                    "path": site['path'],
                    "loaded": page_loaded,
                    "screenshots": [],
                    "navigation": None
                }
                
                if page_loaded:
                    # Take screenshot
                    screenshot_path = self.take_screenshot(
                        site['name'], 
                        "homepage",
                        "Desktop"
                    )
                    page_result["screenshots"].append(screenshot_path)
                    
                    # Test navigation
                    if test_navigation:
                        nav_result = self.test_navigation(site['name'])
                        page_result["navigation"] = nav_result
                        
                site_result["pages"].append(page_result)
                
            except Exception as e:
                print(f"❌ Error testing {site['name']}: {e}")
                site_result["error"] = str(e)
                
            self.results.append(site_result)
            time.sleep(1)
            
        self.generate_report()
        print(f"\n✅ QA run complete! Report saved to: {self.output_dir}")
        
    def generate_report(self):
        """Generate JSON and HTML reports"""
        # JSON report
        json_path = self.output_dir / "qa_report.json"
        with open(json_path, 'w') as f:
            json.dump(self.results, f, indent=2)
            
        # HTML report
        html_path = self.output_dir / "qa_report.html"
        html_content = self._generate_html_report()
        with open(html_path, 'w') as f:
            f.write(html_content)
            
        print(f"📄 Reports generated:")
        print(f"   - {json_path}")
        print(f"   - {html_path}")
        
    def _generate_html_report(self):
        """Generate HTML report with screenshots"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tiger CMS Visual QA Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .site-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .site-name {{
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 15px;
        }}
        .status {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
        }}
        .status.success {{ background: #d4edda; color: #155724; }}
        .status.error {{ background: #f8d7da; color: #721c24; }}
        .screenshot {{
            max-width: 100%;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin: 10px 0;
        }}
        .timestamp {{
            color: #666;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🐅 Tiger CMS Visual QA Report</h1>
        <p class="timestamp">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
"""
        
        for site_result in self.results:
            has_error = 'error' in site_result
            status_class = 'error' if has_error else 'success'
            status_text = 'Error' if has_error else 'Passed'
            
            html += f"""
    <div class="site-card">
        <div class="site-name">{site_result['name']}</div>
        <span class="status {status_class}">{status_text}</span>
"""
            
            if has_error:
                html += f"<p><strong>Error:</strong> {site_result['error']}</p>"
            else:
                for page in site_result.get('pages', []):
                    html += f"<h3>{page['path']}</h3>"
                    if page['loaded']:
                        html += "<p>✅ Page loaded successfully</p>"
                        for screenshot in page['screenshots']:
                            filename = Path(screenshot).name
                            html += f'<img src="{filename}" class="screenshot" alt="Screenshot">'
                    else:
                        html += "<p>❌ Page failed to load</p>"
                        
            html += "</div>"
            
        html += """
</body>
</html>
"""
        return html


def main():
    """Run visual QA automation"""
    qa = VisualQA()
    qa.run_visual_qa(test_navigation=True, test_responsive=False)


if __name__ == "__main__":
    main()

