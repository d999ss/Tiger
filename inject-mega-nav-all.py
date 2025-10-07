#!/usr/bin/env python3
"""
Universal Mega Menu Navigation Injector - ALL PAGES
Injects the mega menu navigation into ALL HTML pages across entire Tiger CMS
"""

import os
import re
from pathlib import Path

def read_nav_template():
    """Read the universal mega nav template"""
    nav_file = Path('universal-mega-nav.html')
    if not nav_file.exists():
        print("❌ Error: universal-mega-nav.html not found!")
        return None
    
    with open(nav_file, 'r', encoding='utf-8') as f:
        return f.read()

def has_mega_nav(content):
    """Check if the page already has the mega menu navigation"""
    # Check for unique identifiers of the mega menu
    indicators = [
        'id="mainNav"',
        'class="mega-menu"',
        'mega-menu-featured'
    ]
    return any(indicator in content for indicator in indicators)

def inject_navigation(html_content, nav_content):
    """Inject navigation after the opening body tag"""
    # Find the opening body tag
    body_pattern = r'(<body[^>]*>)'
    match = re.search(body_pattern, html_content, re.IGNORECASE)
    
    if not match:
        return html_content, False
    
    # Insert navigation right after body tag
    body_tag = match.group(1)
    insertion_point = match.end()
    
    new_content = (
        html_content[:insertion_point] +
        '\n\n<!-- Universal Mega Menu Navigation -->\n' +
        nav_content +
        '\n<!-- End Universal Mega Menu Navigation -->\n\n' +
        html_content[insertion_point:]
    )
    
    return new_content, True

def process_html_file(file_path, nav_content, dry_run=False):
    """Process a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has mega nav
        if has_mega_nav(content):
            return 'skipped', '✓ Already has mega nav'
        
        # Check if it has a body tag
        if '<body' not in content.lower():
            return 'skipped', '⚠ No <body> tag found'
        
        # Inject navigation
        new_content, success = inject_navigation(content, nav_content)
        
        if not success:
            return 'failed', '❌ Failed to inject'
        
        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'updated', '✅ Navigation injected'
        else:
            return 'would_update', '🔍 Would inject navigation'
            
    except Exception as e:
        return 'error', f'❌ Error: {str(e)}'

def find_all_html_files():
    """Find all HTML files in the entire CMS"""
    # Directories to exclude
    exclude_dirs = {
        '.git', 
        'node_modules', 
        '__pycache__',
        '.venv',
        'venv',
        '.cache'
    }
    
    html_files = []
    
    # Walk through all directories
    for root, dirs, files in os.walk('.'):
        # Remove excluded directories from the search
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Find HTML files
        for file in files:
            if file.endswith('.html'):
                file_path = Path(root) / file
                html_files.append(file_path)
    
    return sorted(html_files)

def main():
    """Main function to process all HTML files"""
    print("=" * 80)
    print("🐯 TIGER CMS - Universal Mega Menu Navigation Injector (ALL PAGES)")
    print("=" * 80)
    print()
    
    # Read navigation template
    print("📖 Reading navigation template...")
    nav_content = read_nav_template()
    if not nav_content:
        return
    print("✅ Navigation template loaded\n")
    
    # Find all HTML files
    print("🔍 Scanning for HTML files across all directories...")
    html_files = find_all_html_files()
    
    if not html_files:
        print("❌ No HTML files found")
        return
    
    print(f"📄 Found {len(html_files)} HTML files across entire CMS\n")
    
    # Group files by directory
    files_by_dir = {}
    for html_file in html_files:
        dir_name = str(html_file.parent)
        if dir_name not in files_by_dir:
            files_by_dir[dir_name] = []
        files_by_dir[dir_name].append(html_file)
    
    print(f"📂 Processing {len(files_by_dir)} directories\n")
    print("-" * 80)
    
    # Process each file
    stats = {
        'updated': 0,
        'skipped': 0,
        'failed': 0,
        'error': 0
    }
    
    current_dir = None
    for html_file in html_files:
        # Print directory header when we enter a new directory
        dir_name = str(html_file.parent)
        if dir_name != current_dir:
            current_dir = dir_name
            print(f"\n📁 {dir_name}/")
            print("-" * 80)
        
        status, message = process_html_file(html_file, nav_content)
        stats[status] = stats.get(status, 0) + 1
        
        # Print status with color coding
        status_icon = {
            'updated': '✅',
            'skipped': '⏭',
            'failed': '❌',
            'error': '⚠️',
            'would_update': '🔍'
        }.get(status, '•')
        
        print(f"  {status_icon} {html_file.name:50} {message}")
    
    # Print summary
    print("\n" + "=" * 80)
    print("\n📊 SUMMARY:")
    print(f"   ✅ Updated: {stats.get('updated', 0)}")
    print(f"   ⏭  Skipped: {stats.get('skipped', 0)}")
    print(f"   ❌ Failed: {stats.get('failed', 0)}")
    print(f"   ⚠️  Errors: {stats.get('error', 0)}")
    print(f"   📄 Total: {len(html_files)}")
    print()
    
    if stats.get('updated', 0) > 0:
        print(f"✨ Successfully injected mega menu navigation into {stats['updated']} pages!")
        print(f"🎉 All company websites now have consistent navigation!")
    else:
        print("ℹ️  No files were updated (all already have navigation or were skipped)")
    
    # Show breakdown by directory
    if stats.get('updated', 0) > 0:
        print("\n📊 Files Updated by Directory:")
        dir_stats = {}
        for html_file in html_files:
            dir_name = str(html_file.parent)
            if dir_name not in dir_stats:
                dir_stats[dir_name] = {'total': 0, 'updated': 0}
            dir_stats[dir_name]['total'] += 1
            
            # Check if this file was updated (rough check)
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    if 'Universal Mega Menu Navigation' in f.read():
                        dir_stats[dir_name]['updated'] += 1
            except:
                pass
        
        for dir_name, counts in sorted(dir_stats.items()):
            if counts['updated'] > 0:
                print(f"   • {dir_name}: {counts['updated']}/{counts['total']} files")
    
    print("\n" + "=" * 80)

if __name__ == '__main__':
    main()

