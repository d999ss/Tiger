#!/usr/bin/env python3
"""
Generate all pages with expanded content (800-1,500+ words each)
"""

import json
import sys

# Import the expanded content templates
sys.path.insert(0, '.')
from expanded_content_templates import CONTENT_GENERATORS

# Read navigation and footer from generate-all-pages.py
exec(open('generate-all-pages.py').read(), globals())

def generate_expanded_page(filename, data):
    """Generate page with expanded content"""
    
    slug = filename.replace('.html', '')
    
    # Determine page type and get appropriate content
    product_pages = ['healpack', 'caregraft', 'alloply', 'acapatch', 'bellafill', 'aveli', 'breast',
                     'general-surgery', 'plastic-surgery', 'podiatry']
    
    science_pages = ['wound-care', 'tissue-reconstruction', 'aesthetic-medicine', 'regenerative-medicine',
                     'orthopedic', 'research-pipeline', 'clinical-trials', 'publications', 'camps-technology',
                     'patents', 'quality-assurance', 'regulatory', 'manufacturing', 'certifications']
    
    solution_pages = ['hospitals', 'wound-centers', 'facilities', 'healthcare-professionals',
                      'training', 'clinical-support', 'reimbursement', 'ordering', 'support',
                      'investigator', 'partnerships', 'catalog', 'solutions']
    
    # Get content based on page type
    if slug in product_pages:
        page_type = "product"
        main_content = CONTENT_GENERATORS['product'](
            data.get('hero_title', slug.title()),
            data.get('hero_subtitle', 'Advanced solutions for optimal outcomes.')
        )
        badge = data.get('badge', 'Product')
    elif slug in science_pages:
        page_type = "science"
        main_content = CONTENT_GENERATORS['science'](
            data.get('hero_title', slug.title()),
            data.get('hero_subtitle', 'Scientific excellence in regenerative medicine.')
        )
        badge = data.get('badge', 'Research')
    elif slug in solution_pages:
        page_type = "solution"
        main_content = CONTENT_GENERATORS['solution'](
            data.get('hero_title', slug.title()),
            data.get('hero_subtitle', 'Comprehensive healthcare solutions.')
        )
        badge = data.get('badge', 'Solutions')
    else:
        # Default content for other pages
        main_content = f'''<section class="section">
    <div class="section-container">
        <div class="section-header">
            <h2 class="section-title">{data.get('hero_title', slug.title())}</h2>
            <p class="section-description">{data.get('hero_subtitle', 'Information and resources.')}</p>
        </div>
    </div>
</section>'''
        badge = data.get('badge', 'Tiger BioSciences')
    
    # Build page data
    page_data = {
        'title': data.get('title', f'{slug.title()} - Tiger BioSciences™'),
        'meta_description': data.get('meta_description', 'Tiger BioSciences - Advanced tissue technology solutions.'),
        'keywords': f'Tiger BioSciences, {slug}, CAMPs, tissue technology, regenerative medicine',
        'filename': filename,
        'slug': slug,
        'navigation': NAVIGATION,
        'badge': badge,
        'hero_title': data.get('hero_title', slug.replace('-', ' ').title()),
        'hero_subtitle': data.get('hero_subtitle', 'Advanced solutions for better patient outcomes.'),
        'cta_primary': 'Contact Us',
        'cta_secondary': 'Learn More',
        'cta_secondary_link': 'about.html',
        'main_content': main_content,
        'cta_title': 'Get In Touch',
        'cta_description': 'Contact our team to learn more about how Tiger BioSciences can support your needs.',
        'footer': FOOTER
    }
    
    # Generate HTML
    html = PAGE_TEMPLATE.format(**page_data)
    return html

def main():
    """Generate all pages with expanded content"""
    print("🚀 Generating ALL pages with expanded content (800-1,500+ words)")
    print("=" * 70)
    
    # Load page data
    with open('page-content-data.json', 'r') as f:
        content_data = json.load(f)
        pages = content_data.get('pages', {})
    
    generated_count = 0
    word_counts = []
    
    for filename, data in pages.items():
        try:
            html = generate_expanded_page(filename, data)
            
            # Write file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            
            # Estimate word count
            text = html.replace('<', ' <').replace('>', '> ')
            words = len([w for w in text.split() if w and not w.startswith('<')])
            word_counts.append(words)
            
            generated_count += 1
            print(f"✓ {filename:40} ~{words:,} words")
            
        except Exception as e:
            print(f"❌ Error generating {filename}: {str(e)}")
    
    print("=" * 70)
    print(f"✅ Generated {generated_count} pages")
    print(f"📊 Average content: ~{sum(word_counts)//len(word_counts):,} words per page")
    print(f"📈 Total content: ~{sum(word_counts):,} words across all pages")

if __name__ == "__main__":
    main()
