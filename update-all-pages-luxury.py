#!/usr/bin/env python3
"""
Script to update all HTML pages to use the unified luxury design system
"""

import os
import re
from pathlib import Path

def update_html_file(file_path):
    """Update a single HTML file to use the luxury CSS"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has the luxury CSS link
        if 'tiger-luxury.css' in content:
            print(f"✓ {file_path.name} already updated")
            return
        
        # Find the title tag and add the CSS link after it
        title_pattern = r'<title>([^<]*)</title>'
        title_match = re.search(title_pattern, content)
        
        if title_match:
            title_line = title_match.group(0)
            # Add the luxury CSS link after the title
            new_content = content.replace(
                title_line, 
                title_line + '\n    <link rel="stylesheet" href="assets/css/tiger-luxury.css">'
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Updated {file_path.name}")
        else:
            print(f"⚠ No title found in {file_path.name}")
            
    except Exception as e:
        print(f"✗ Error updating {file_path.name}: {e}")

def main():
    """Update all HTML files in the current directory"""
    current_dir = Path('.')
    html_files = list(current_dir.glob('*.html'))
    
    # Skip index.html as it's already updated
    html_files = [f for f in html_files if f.name != 'index.html']
    
    print(f"Found {len(html_files)} HTML files to update")
    print("Updating files to use unified luxury design system...\n")
    
    for html_file in html_files:
        update_html_file(html_file)
    
    print(f"\n✅ Updated {len(html_files)} files to use the unified luxury design system!")
    print("All pages now share the same world-class styling from tiger-luxury.css")

if __name__ == "__main__":
    main()
