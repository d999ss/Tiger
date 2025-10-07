#!/usr/bin/env python3
"""
Asset Checker for Tiger CMS
Verifies that images, CSS, and JavaScript files are present and accessible
"""

import os
from pathlib import Path
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False
    print("⚠️  BeautifulSoup not installed. Install with: pip install beautifulsoup4 lxml")


SITES = [
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


class AssetChecker:
    def __init__(self, base_path="/Users/donnysmith/Desktop/Tiger CMS"):
        self.base_path = Path(base_path)
        
    def check_file_exists(self, file_path, base_dir):
        """Check if a file exists relative to the base directory"""
        # Handle absolute URLs (external resources)
        if file_path.startswith(('http://', 'https://', '//')):
            return True, "external"
            
        # Remove query strings and fragments
        file_path = file_path.split('?')[0].split('#')[0]
        
        # Handle root-relative paths
        if file_path.startswith('/'):
            file_path = file_path[1:]
            check_path = base_dir / file_path
        else:
            check_path = base_dir / file_path
            
        exists = check_path.exists()
        return exists, str(check_path) if not exists else None
        
    def check_html_file(self, html_path):
        """Check all assets referenced in an HTML file"""
        if not BS4_AVAILABLE:
            return {"error": "BeautifulSoup not available"}
            
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'lxml')
        except Exception as e:
            return {"error": f"Failed to parse HTML: {e}"}
            
        base_dir = html_path.parent
        issues = {
            "missing_images": [],
            "missing_css": [],
            "missing_js": [],
            "missing_links": []
        }
        
        # Check images
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                exists, path = self.check_file_exists(src, base_dir)
                if not exists and path != "external":
                    issues["missing_images"].append({
                        "src": src,
                        "alt": img.get('alt', 'No alt text'),
                        "expected_path": path
                    })
                    
        # Check CSS
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href:
                exists, path = self.check_file_exists(href, base_dir)
                if not exists and path != "external":
                    issues["missing_css"].append({
                        "href": href,
                        "expected_path": path
                    })
                    
        # Check JavaScript
        for script in soup.find_all('script', src=True):
            src = script.get('src')
            if src:
                exists, path = self.check_file_exists(src, base_dir)
                if not exists and path != "external":
                    issues["missing_js"].append({
                        "src": src,
                        "expected_path": path
                    })
                    
        # Check internal links
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            # Only check relative HTML links
            if href and not href.startswith(('http://', 'https://', '#', 'mailto:', 'tel:')):
                if href.endswith('.html') or '/' in href:
                    exists, path = self.check_file_exists(href, base_dir)
                    if not exists and path != "external":
                        issues["missing_links"].append({
                            "href": href,
                            "text": link.get_text(strip=True)[:50],
                            "expected_path": path
                        })
                        
        return issues
        
    def check_all_sites(self):
        """Check assets for all Tiger sites"""
        print("🔍 Checking assets for all Tiger CMS sites...\n")
        
        all_results = []
        
        for site_name, site_path in SITES:
            print(f"Checking: {site_name}")
            
            html_path = self.base_path / site_path
            
            if not html_path.exists():
                print(f"  ❌ HTML file not found: {html_path}\n")
                all_results.append({
                    "site": site_name,
                    "path": site_path,
                    "error": "HTML file not found"
                })
                continue
                
            issues = self.check_html_file(html_path)
            
            if "error" in issues:
                print(f"  ❌ {issues['error']}\n")
                all_results.append({
                    "site": site_name,
                    "path": site_path,
                    "error": issues["error"]
                })
                continue
                
            # Count issues
            total_issues = sum(len(v) for v in issues.values())
            
            if total_issues == 0:
                print(f"  ✅ No issues found")
            else:
                print(f"  ⚠️  Found {total_issues} issue(s):")
                if issues["missing_images"]:
                    print(f"     - {len(issues['missing_images'])} missing images")
                if issues["missing_css"]:
                    print(f"     - {len(issues['missing_css'])} missing CSS files")
                if issues["missing_js"]:
                    print(f"     - {len(issues['missing_js'])} missing JS files")
                if issues["missing_links"]:
                    print(f"     - {len(issues['missing_links'])} broken internal links")
                    
            print()
            
            all_results.append({
                "site": site_name,
                "path": site_path,
                "issues": issues,
                "total_issues": total_issues
            })
            
        # Save report
        report_path = self.base_path / "qa-automation" / "asset_check_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w') as f:
            json.dump(all_results, f, indent=2)
            
        print(f"📄 Full report saved: {report_path}")
        
        # Summary
        total_sites = len(all_results)
        sites_with_issues = sum(1 for r in all_results if r.get('total_issues', 0) > 0)
        sites_ok = total_sites - sites_with_issues
        
        print(f"\n📊 Summary:")
        print(f"   Sites checked: {total_sites}")
        print(f"   ✅ OK: {sites_ok}")
        print(f"   ⚠️  With issues: {sites_with_issues}")
        
        return all_results


def main():
    if not BS4_AVAILABLE:
        print("\n❌ BeautifulSoup is required for asset checking")
        print("Install with: pip install beautifulsoup4 lxml")
        return
        
    checker = AssetChecker()
    checker.check_all_sites()


if __name__ == "__main__":
    main()

