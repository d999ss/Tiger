#!/usr/bin/env python3
"""
Tiger BioSciences Website Content Extractor
Extracts text content from HTML files and outputs to CSV/Markdown for CMS import
"""

import os
import csv
import re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin
import json

class ContentExtractor(HTMLParser):
    """Extract meaningful content from HTML, ignoring scripts, styles, etc."""

    def __init__(self):
        super().__init__()
        self.reset_content()

    def reset_content(self):
        """Reset the content storage"""
        self.current_tag = None
        self.skip_content = False
        self.title = ""
        self.meta_description = ""
        self.headings = []  # List of (level, text) tuples
        self.paragraphs = []
        self.links = []
        self.images = []
        self.current_heading_level = None
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        """Handle opening tags"""
        self.current_tag = tag
        attrs_dict = dict(attrs)

        # Skip script, style, and navigation content
        if tag in ['script', 'style', 'nav', 'header', 'footer', 'noscript']:
            self.skip_content = True

        # Extract title
        if tag == 'title':
            self.skip_content = False

        # Extract meta description
        if tag == 'meta' and attrs_dict.get('name') == 'description':
            self.meta_description = attrs_dict.get('content', '')

        # Track headings
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.current_heading_level = int(tag[1])
            self.skip_content = False

        # Track images
        if tag == 'img':
            alt_text = attrs_dict.get('alt', '')
            src = attrs_dict.get('src', '')
            if alt_text or src:
                self.images.append({'src': src, 'alt': alt_text})

        # Track links (but don't include nav links)
        if tag == 'a' and not self.skip_content:
            href = attrs_dict.get('href', '')
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        """Handle closing tags"""
        if tag in ['script', 'style', 'nav', 'header', 'footer', 'noscript']:
            self.skip_content = False

        # Save heading
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] and self.current_heading_level:
            text = ' '.join(self.current_text).strip()
            if text:
                self.headings.append((self.current_heading_level, text))
            self.current_text = []
            self.current_heading_level = None

        # Save paragraph
        if tag == 'p':
            text = ' '.join(self.current_text).strip()
            if text and len(text) > 10:  # Ignore very short paragraphs
                self.paragraphs.append(text)
            self.current_text = []

        # Save title
        if tag == 'title':
            self.title = ' '.join(self.current_text).strip()
            self.current_text = []

        self.current_tag = None

    def handle_data(self, data):
        """Handle text data"""
        if self.skip_content:
            return

        # Clean up whitespace
        text = ' '.join(data.split())
        if text:
            self.current_text.append(text)

    def get_structured_content(self):
        """Return structured content"""
        return {
            'title': self.title,
            'meta_description': self.meta_description,
            'headings': self.headings,
            'paragraphs': self.paragraphs,
            'links': self.links,
            'images': self.images
        }


def clean_url_path(file_path, base_dir):
    """Convert file path to clean URL path"""
    rel_path = os.path.relpath(file_path, base_dir)
    # Convert index.html to / for cleaner URLs
    if rel_path.endswith('index.html'):
        rel_path = rel_path[:-10]  # Remove 'index.html'
    elif rel_path.endswith('.html'):
        rel_path = rel_path[:-5]  # Remove '.html'
    return '/' + rel_path.replace(os.sep, '/')


def extract_from_html_file(file_path, base_dir, domain):
    """Extract content from a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()

        parser = ContentExtractor()
        parser.feed(html_content)
        content = parser.get_structured_content()

        # Build URL
        url_path = clean_url_path(file_path, base_dir)
        url = f"https://{domain}{url_path}"

        return {
            'url': url,
            'file_path': file_path,
            'domain': domain,
            **content
        }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def process_website_directory(website_dir):
    """Process all HTML files in a website directory"""
    domain = os.path.basename(website_dir)
    results = []

    # Find all HTML files
    html_files = list(Path(website_dir).rglob('*.html'))

    print(f"Processing {domain}: {len(html_files)} HTML files found")

    for html_file in html_files:
        content = extract_from_html_file(str(html_file), website_dir, domain)
        if content:
            results.append(content)

    return results


def export_to_csv(all_content, output_file):
    """Export content to CSV format"""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Header
        writer.writerow([
            'Domain',
            'URL',
            'Page Title',
            'Meta Description',
            'H1 Headings',
            'H2 Headings',
            'H3 Headings',
            'Body Content',
            'Links Count',
            'Images Count',
            'File Path'
        ])

        # Content rows
        for item in all_content:
            # Group headings by level
            h1s = [h[1] for h in item['headings'] if h[0] == 1]
            h2s = [h[1] for h in item['headings'] if h[0] == 2]
            h3s = [h[1] for h in item['headings'] if h[0] == 3]

            writer.writerow([
                item['domain'],
                item['url'],
                item['title'],
                item['meta_description'],
                ' | '.join(h1s),
                ' | '.join(h2s),
                ' | '.join(h3s),
                ' '.join(item['paragraphs']),
                len(item['links']),
                len(item['images']),
                item['file_path']
            ])


def export_to_markdown(all_content, output_file):
    """Export content to Markdown format"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Tiger BioSciences Ecosystem - Content Export\n\n")
        f.write(f"Total pages extracted: {len(all_content)}\n\n")
        f.write("---\n\n")

        # Group by domain
        domains = {}
        for item in all_content:
            domain = item['domain']
            if domain not in domains:
                domains[domain] = []
            domains[domain].append(item)

        # Write content by domain
        for domain, pages in sorted(domains.items()):
            f.write(f"## {domain}\n\n")
            f.write(f"Pages: {len(pages)}\n\n")

            for page in pages:
                f.write(f"### {page['title'] or 'Untitled Page'}\n\n")
                f.write(f"**URL:** {page['url']}\n\n")

                if page['meta_description']:
                    f.write(f"**Description:** {page['meta_description']}\n\n")

                if page['headings']:
                    f.write("**Headings:**\n\n")
                    current_level = 0
                    for level, heading in page['headings']:
                        indent = "  " * (level - 1)
                        f.write(f"{indent}- H{level}: {heading}\n")
                    f.write("\n")

                if page['paragraphs']:
                    f.write("**Content:**\n\n")
                    for para in page['paragraphs'][:5]:  # Limit to first 5 paragraphs for readability
                        f.write(f"{para}\n\n")
                    if len(page['paragraphs']) > 5:
                        f.write(f"*...and {len(page['paragraphs']) - 5} more paragraphs*\n\n")

                f.write("---\n\n")


def export_to_json(all_content, output_file):
    """Export content to JSON format"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_content, f, indent=2, ensure_ascii=False)


def main():
    """Main execution function"""
    base_dir = '/Users/donnysmith/Desktop/Tiger'

    # Get all website directories
    website_dirs = [
        os.path.join(base_dir, d) for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.')
    ]

    print(f"Found {len(website_dirs)} website directories\n")

    all_content = []

    # Process each website
    for website_dir in sorted(website_dirs):
        content = process_website_directory(website_dir)
        all_content.extend(content)
        print(f"  → Extracted {len(content)} pages\n")

    print(f"\nTotal pages extracted: {len(all_content)}")
    print("\nExporting to files...")

    # Export to multiple formats
    export_to_csv(all_content, os.path.join(base_dir, 'tiger_content.csv'))
    print(f"  ✓ CSV: {base_dir}/tiger_content.csv")

    export_to_markdown(all_content, os.path.join(base_dir, 'tiger_content.md'))
    print(f"  ✓ Markdown: {base_dir}/tiger_content.md")

    export_to_json(all_content, os.path.join(base_dir, 'tiger_content.json'))
    print(f"  ✓ JSON: {base_dir}/tiger_content.json")

    print("\n✅ Content extraction complete!")


if __name__ == '__main__':
    main()
