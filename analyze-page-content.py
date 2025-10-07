#!/usr/bin/env python3
"""
Analyze page content to find pages with minimum copy
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    """Extract text content from HTML"""
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip_tags = {'script', 'style', 'head', 'meta', 'link'}
        self.current_tag = None
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        
    def handle_endtag(self, tag):
        self.current_tag = None
        
    def handle_data(self, data):
        if self.current_tag not in self.skip_tags:
            text = data.strip()
            if text:
                self.text.append(text)
    
    def get_text(self):
        return ' '.join(self.text)

def extract_text_from_html(filepath):
    """Extract visible text from HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parser = TextExtractor()
        parser.feed(content)
        text = parser.get_text()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    except Exception as e:
        return ""

def analyze_pages():
    """Analyze all HTML pages"""
    
    # Get all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Exclude certain files
    exclude_files = [
        'nav-template.html',
        'universal-mega-nav.html',
        'design-comparison-dashboard.html',
        'design-comparison-dashboard-v2.html',
        'about-page.html',
        'tiger-way-page.html',
        'products-full.html'
    ]
    
    # Filter out demo/template files
    html_files = [f for f in html_files if not any(
        x in f for x in ['modern-demo', 'template', 'dashboard']
    ) and f not in exclude_files]
    
    page_data = []
    
    for filename in html_files:
        text = extract_text_from_html(filename)
        char_count = len(text)
        word_count = len(text.split())
        
        page_data.append({
            'filename': filename,
            'characters': char_count,
            'words': word_count,
            'text_preview': text[:200] if text else "[EMPTY]"
        })
    
    # Sort by character count
    page_data.sort(key=lambda x: x['characters'])
    
    print("=" * 80)
    print("📊 TIGER BIOSCIENCES - PAGE CONTENT ANALYSIS")
    print("=" * 80)
    print()
    
    # Show pages with minimum content (bottom 15)
    print("🔻 PAGES WITH MINIMUM CONTENT (Bottom 15):")
    print("-" * 80)
    for i, page in enumerate(page_data[:15], 1):
        print(f"{i:2}. {page['filename']:35} | {page['characters']:,} chars | {page['words']:,} words")
        if page['characters'] < 500:
            print(f"    Preview: {page['text_preview'][:100]}...")
        print()
    
    print("-" * 80)
    print()
    
    # Show pages with maximum content (top 10)
    print("🔺 PAGES WITH MAXIMUM CONTENT (Top 10):")
    print("-" * 80)
    for i, page in enumerate(page_data[-10:], 1):
        print(f"{i:2}. {page['filename']:35} | {page['characters']:,} chars | {page['words']:,} words")
    
    print()
    print("=" * 80)
    print(f"📈 STATISTICS:")
    print(f"   Total Pages Analyzed: {len(page_data)}")
    print(f"   Minimum Content: {page_data[0]['characters']:,} chars ({page_data[0]['filename']})")
    print(f"   Maximum Content: {page_data[-1]['characters']:,} chars ({page_data[-1]['filename']})")
    print(f"   Average Content: {sum(p['characters'] for p in page_data) // len(page_data):,} chars")
    print("=" * 80)
    
    # Find pages needing attention (< 1000 characters)
    low_content = [p for p in page_data if p['characters'] < 1000]
    if low_content:
        print()
        print(f"⚠️  {len(low_content)} PAGES NEED MORE CONTENT (< 1,000 characters):")
        print("-" * 80)
        for page in low_content:
            print(f"   • {page['filename']:35} | {page['characters']:,} chars")
    
    return page_data

if __name__ == "__main__":
    analyze_pages()

