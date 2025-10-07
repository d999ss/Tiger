#!/usr/bin/env python3
"""
Generate all missing pages for Tiger BioSciences
"""

import json

# Read the missing pages data
with open('complete-all-pages.json', 'r') as f:
    data = json.load(f)
    missing_pages = data['missing_pages']

# Read the page generation script to use its template
with open('generate-all-pages.py', 'r') as f:
    script_content = f.read()

# Merge the missing pages into page-content-data.json
try:
    with open('page-content-data.json', 'r') as f:
        existing_data = json.load(f)
except FileNotFoundError:
    existing_data = {'pages': {}}

# Add missing pages
for filename, page_data in missing_pages.items():
    existing_data['pages'][filename] = page_data

# Save updated data
with open('page-content-data.json', 'w') as f:
    json.dump(existing_data, f, indent=2)

print(f"✅ Updated page-content-data.json with {len(missing_pages)} pages")
print("\n🚀 Run: python3 generate-all-pages.py")
print("   to generate all pages including the new ones")

