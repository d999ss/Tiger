#!/usr/bin/env python3
"""
Tiger BioSciences - Comprehensive Page Generator
Generates all 52 pages with proper content, SEO, and navigation
"""

import json
import os
from pathlib import Path

# Page template with full structure
PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    
    <!-- Primary Meta Tags -->
    <title>{title}</title>
    <meta name="title" content="{title}">
    <meta name="description" content="{meta_description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Tiger BioSciences">
    <meta name="robots" content="index, follow">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://tigerbiosciences.com/{filename}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_description}">
    <meta property="og:image" content="https://tigerbiosciences.com/assets/images/og-{slug}.jpg">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://tigerbiosciences.com/{filename}">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{meta_description}">
    <meta property="twitter:image" content="https://tigerbiosciences.com/assets/images/twitter-{slug}.jpg">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    
    <!-- Performance -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://0nxq33lj.api.sanity.io">
    
    <!-- Styles -->
    <link rel="stylesheet" href="assets/css/tiger-luxury.css">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "{title}",
      "description": "{meta_description}",
      "url": "https://tigerbiosciences.com/{filename}"
    }}
    </script>
</head>
<body>

<!-- Skip to main content -->
<a href="#main-content" class="skip-to-main">Skip to main content</a>

<!-- Announcement Bar -->
<div class="announcement">
    555 E North Ln, Ste 5000, Bldg D, Conshohocken, PA 19428
    <a href="tel:+18886655005">(+1) 888 665 5005</a>
</div>

<!-- Navigation -->
{navigation}

<!-- Hero Section -->
<section class="hero hero-gradient" role="banner" aria-label="Page hero" id="main-content">
    <div class="hero-content">
        <div class="hero-badge">{badge}</div>
        <h1 class="hero-title">{hero_title}</h1>
        <p class="hero-subtitle">{hero_subtitle}</p>
        <div class="hero-buttons">
            <a href="contact.html" class="btn btn-primary">{cta_primary}</a>
            <a href="{cta_secondary_link}" class="btn btn-outline">{cta_secondary}</a>
        </div>
    </div>
</section>

<!-- Main Content -->
{main_content}

<!-- CTA Section -->
<section class="cta">
    <div class="cta-title">{cta_title}</div>
    <p class="cta-description">{cta_description}</p>
    <div class="hero-buttons">
        <a href="contact.html" class="btn btn-primary btn-cta-light">Contact Us</a>
        <a href="products.html" class="btn btn-outline btn-cta-outline">View Products</a>
    </div>
</section>

<!-- Newsletter Section -->
<section class="newsletter">
    <div class="newsletter-container">
        <h3 class="newsletter-title">Connect With Us</h3>
        <p class="newsletter-description">Ready to learn more? Get in touch with our team today.</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="tel:+18886655005" class="btn btn-primary">Call: 1-888-665-5005</a>
            <a href="contact.html" class="btn btn-outline">Contact Us</a>
        </div>
    </div>
</section>

<!-- Footer -->
{footer}

<!-- Sanity CMS Content -->
<script src="assets/js/sanity-client.js" defer></script>

</body>
</html>'''

# Navigation component (copied from index.html)
NAVIGATION = '''<nav class="navbar" id="mainNav" role="navigation" aria-label="Main navigation">
    <div class="nav-container">
        <a href="index.html" class="logo" aria-label="Tiger BioSciences Home">TIGER BIOSCIENCES™</a>
        
        <ul class="nav-menu" role="menubar">
            <!-- Our Science Mega Menu -->
            <li class="nav-item">
                <a href="#" class="nav-link">
                    Our Science
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                    </svg>
                </a>
                <div class="mega-menu">
                    <div class="mega-menu-content">
                        <div class="mega-menu-left">
                            <div class="mega-menu-section">
                                <h4>Research Areas</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="wound-care.html">Wound Care</a></li>
                                    <li><a href="tissue-reconstruction.html">Tissue Reconstruction</a></li>
                                    <li><a href="aesthetic-medicine.html">Aesthetic Medicine</a></li>
                                    <li><a href="regenerative-medicine.html">Regenerative Medicine</a></li>
                                    <li><a href="orthopedic.html">Orthopedic Applications</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Innovation</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="research-pipeline.html">Research Pipeline</a></li>
                                    <li><a href="clinical-trials.html">Clinical Trials</a></li>
                                    <li><a href="publications.html">Publications</a></li>
                                    <li><a href="camps-technology.html">CAMPs Technology</a></li>
                                    <li><a href="patents.html">Patents & IP</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Quality</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="quality-assurance.html">Quality Assurance</a></li>
                                    <li><a href="regulatory.html">Regulatory</a></li>
                                    <li><a href="manufacturing.html">Manufacturing</a></li>
                                    <li><a href="certifications.html">Certifications</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Resources</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="science.html">Science</a></li>
                                    <li><a href="training.html">Training</a></li>
                                    <li><a href="support.html">Support</a></li>
                                    <li><a href="faq.html">FAQ</a></li>
                                </ul>
                            </div>
                        </div>
                        
                        <div class="mega-menu-featured">
                            <div class="featured-badge">Featured</div>
                            <h5>Revolutionary CAMPs Technology</h5>
                            <p>Discover how our proprietary CAMPs technology is transforming healthcare.</p>
                            <a href="camps-technology.html" class="featured-link">
                                Explore CAMPs
                                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </li>
            
            <!-- Products Mega Menu -->
            <li class="nav-item">
                <a href="#" class="nav-link">
                    Products
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                    </svg>
                </a>
                <div class="mega-menu">
                    <div class="mega-menu-content">
                        <div class="mega-menu-left">
                            <div class="mega-menu-section">
                                <h4>Wound Care</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="healpack.html">HealPack</a></li>
                                    <li><a href="caregraft.html">CarGraft</a></li>
                                    <li><a href="alloply.html">AlloPly</a></li>
                                    <li><a href="wound-centers.html">Wound Centers</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Aesthetic</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="bellafill.html">Bellafill</a></li>
                                    <li><a href="aveli.html">Aveli</a></li>
                                    <li><a href="breast.html">Breast Solutions</a></li>
                                    <li><a href="plastic-surgery.html">Plastic Surgery</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Surgical</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="general-surgery.html">General Surgery</a></li>
                                    <li><a href="orthopedic.html">Orthopedic</a></li>
                                    <li><a href="podiatry.html">Podiatry</a></li>
                                    <li><a href="tissue-reconstruction.html">Tissue Reconstruction</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Specialty</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="regenerative-medicine.html">Regenerative Medicine</a></li>
                                    <li><a href="acapatch.html">AcaPatch</a></li>
                                    <li><a href="birthtissuerecovery.com">Birth Tissue Recovery</a></li>
                                </ul>
                            </div>
                        </div>
                        
                        <div class="mega-menu-featured">
                            <div class="featured-badge">New</div>
                            <h5>Advanced Wound Healing Solutions</h5>
                            <p>Our latest innovations in wound care technology.</p>
                            <a href="products.html" class="featured-link">
                                View All Products
                                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </li>
            
            <!-- Solutions Mega Menu -->
            <li class="nav-item">
                <a href="#" class="nav-link">
                    Solutions
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                    </svg>
                </a>
                <div class="mega-menu">
                    <div class="mega-menu-content">
                        <div class="mega-menu-left">
                            <div class="mega-menu-section">
                                <h4>Healthcare Systems</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="hospitals.html">Hospitals</a></li>
                                    <li><a href="wound-centers.html">Wound Centers</a></li>
                                    <li><a href="facilities.html">Facilities</a></li>
                                    <li><a href="healthcare-professionals.html">Healthcare Professionals</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Clinical Support</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="training.html">Training Programs</a></li>
                                    <li><a href="clinical-support.html">Clinical Support</a></li>
                                    <li><a href="reimbursement.html">Reimbursement</a></li>
                                    <li><a href="ordering.html">Ordering</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Research</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="investigator.html">Investigator Portal</a></li>
                                    <li><a href="clinical-trials.html">Clinical Trials</a></li>
                                    <li><a href="research-pipeline.html">Research Pipeline</a></li>
                                    <li><a href="partnerships.html">Partnerships</a></li>
                                </ul>
                            </div>
                            
                            <div class="mega-menu-section">
                                <h4>Resources</h4>
                                <ul class="mega-menu-links">
                                    <li><a href="catalog.html">Product Catalog</a></li>
                                    <li><a href="publications.html">Publications</a></li>
                                    <li><a href="news.html">News & Updates</a></li>
                                    <li><a href="support.html">Customer Support</a></li>
                                </ul>
                            </div>
                        </div>
                        
                        <div class="mega-menu-featured">
                            <div class="featured-badge">Comprehensive</div>
                            <h5>End-to-End Healthcare Solutions</h5>
                            <p>From clinical research to patient care.</p>
                            <a href="solutions.html" class="featured-link">
                                Explore Solutions
                                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </li>
            
            <!-- About -->
            <li class="nav-item">
                <a href="about.html" class="nav-link">About</a>
            </li>
            
            <!-- Contact -->
            <li class="nav-item">
                <a href="contact.html" class="nav-link">Contact</a>
            </li>
            
            <!-- CTA Button -->
            <li class="nav-item">
                <a href="contact.html" class="btn-nav">Get Started</a>
            </li>
        </ul>
    </div>
</nav>'''

# Footer component
FOOTER = '''<footer class="footer" role="contentinfo" aria-label="Site footer">
    <div class="footer-content">
        <div class="footer-brand">
            <h3>Tiger BioSciences™</h3>
            <p>Pioneering the future of healthcare through innovative biomaterial solutions.</p>
        </div>
        
        <div class="footer-section">
            <h4>Products</h4>
            <ul class="footer-links">
                <li><a href="healpack.html">HealPack</a></li>
                <li><a href="bellafill.html">Bellafill</a></li>
                <li><a href="aveli.html">Aveli</a></li>
                <li><a href="caregraft.html">CarGraft</a></li>
                <li><a href="alloply.html">AlloPly</a></li>
            </ul>
        </div>
        
        <div class="footer-section">
            <h4>Solutions</h4>
            <ul class="footer-links">
                <li><a href="wound-care.html">Wound Care</a></li>
                <li><a href="aesthetic-medicine.html">Aesthetic Medicine</a></li>
                <li><a href="tissue-reconstruction.html">Tissue Reconstruction</a></li>
                <li><a href="regenerative-medicine.html">Regenerative Medicine</a></li>
                <li><a href="orthopedic.html">Orthopedic</a></li>
            </ul>
        </div>
        
        <div class="footer-section">
            <h4>Resources</h4>
            <ul class="footer-links">
                <li><a href="science.html">Science</a></li>
                <li><a href="research-pipeline.html">Research Pipeline</a></li>
                <li><a href="publications.html">Publications</a></li>
                <li><a href="training.html">Training</a></li>
                <li><a href="support.html">Support</a></li>
            </ul>
        </div>
    </div>
    
    <div class="footer-bottom">
        <p>&copy; 2025 Copyright Tiger BioSciences. All rights reserved.</p>
        <div class="footer-legal">
            <a href="legal.html">Legal Disclaimer</a>
            <a href="privacy.html">Privacy Policy</a>
            <a href="terms.html">Terms & Conditions</a>
        </div>
    </div>
</footer>'''

def generate_main_content(page_type, data):
    """Generate main content based on page type"""
    
    if page_type == "product":
        return '''<section class="section">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Product Overview</div>
            <h2 class="section-title">Advanced Technology for Better Outcomes</h2>
            <p class="section-description">Clinically proven solutions designed for optimal patient outcomes.</p>
        </div>
        
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🔬</div>
                <h3 class="feature-title">Clinically Proven</h3>
                <p class="feature-description">Backed by rigorous clinical studies and peer-reviewed research.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">✓</div>
                <h3 class="feature-title">FDA Compliant</h3>
                <p class="feature-description">Meets all FDA regulations and quality standards.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Evidence Based</h3>
                <p class="feature-description">Demonstrated efficacy in clinical applications.</p>
            </div>
        </div>
    </div>
</section>'''
    
    elif page_type == "science":
        return '''<section class="section">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Research Excellence</div>
            <h2 class="section-title">Advancing the Science of Healing</h2>
            <p class="section-description">Our research teams combine decades of expertise with cutting-edge technology.</p>
        </div>
    </div>
</section>'''
    
    elif page_type == "solution":
        return '''<section class="section">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Comprehensive Solutions</div>
            <h2 class="section-title">Supporting Healthcare Excellence</h2>
            <p class="section-description">End-to-end support for healthcare professionals and institutions.</p>
        </div>
    </div>
</section>'''
    
    else:
        return '''<section class="section">
    <div class="section-container">
        <div class="section-header">
            <h2 class="section-title">Excellence in Healthcare</h2>
            <p class="section-description">Comprehensive information and resources.</p>
        </div>
    </div>
</section>'''

def generate_page(filename, data):
    """Generate a complete HTML page"""
    
    # Extract slug from filename
    slug = filename.replace('.html', '')
    
    # Determine page type for content generation
    product_pages = ['healpack', 'caregraft', 'alloply', 'acapatch', 'bellafill', 'aveli', 'breast']
    science_pages = ['wound-care', 'tissue-reconstruction', 'aesthetic-medicine', 'regenerative-medicine', 
                     'orthopedic', 'research-pipeline', 'clinical-trials', 'publications', 'camps-technology', 'patents']
    solution_pages = ['hospitals', 'wound-centers', 'facilities', 'healthcare-professionals', 
                      'training', 'clinical-support', 'reimbursement', 'ordering']
    
    if slug in product_pages:
        page_type = "product"
        badge = "Product"
        cta_title = "Experience the Difference"
        cta_description = "Contact us to learn more about this product and how it can benefit your patients."
    elif slug in science_pages:
        page_type = "science"
        badge = "Research"
        cta_title = "Partner With Us"
        cta_description = "Join us in advancing the future of regenerative medicine through collaboration and innovation."
    elif slug in solution_pages:
        page_type = "solution"
        badge = "Solutions"
        cta_title = "Let's Work Together"
        cta_description = "Discover how Tiger BioSciences can support your healthcare organization's success."
    else:
        page_type = "general"
        badge = "Tiger BioSciences"
        cta_title = "Get In Touch"
        cta_description = "Contact our team to learn more about Tiger BioSciences and our comprehensive solutions."
    
    # Generate main content
    main_content = generate_main_content(page_type, data)
    
    # Default values
    defaults = {
        'title': data.get('title', f'{slug.title()} - Tiger BioSciences™'),
        'meta_description': data.get('meta_description', 'Tiger BioSciences - Advanced tissue technology and CAMPs solutions.'),
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
        'cta_title': cta_title,
        'cta_description': cta_description,
        'footer': FOOTER
    }
    
    # Merge with page data
    page_data = {**defaults, **data}
    
    # Generate HTML
    html = PAGE_TEMPLATE.format(**page_data)
    
    return html

def main():
    """Main execution function"""
    print("🚀 Tiger BioSciences Page Generator")
    print("=" * 60)
    
    # Load content data
    try:
        with open('page-content-data.json', 'r') as f:
            content_data = json.load(f)
            pages = content_data.get('pages', {})
    except FileNotFoundError:
        print("❌ Error: page-content-data.json not found")
        return
    
    # Generate all pages
    generated_count = 0
    for filename, data in pages.items():
        try:
            html = generate_page(filename, data)
            
            # Write to file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            
            generated_count += 1
            print(f"✓ Generated: {filename}")
            
        except Exception as e:
            print(f"❌ Error generating {filename}: {str(e)}")
    
    print("=" * 60)
    print(f"✅ Successfully generated {generated_count} pages")
    print("\n📋 Next Steps:")
    print("1. Review generated pages")
    print("2. Verify navigation links")
    print("3. Test on localhost")
    print("4. Deploy to Vercel")

if __name__ == "__main__":
    main()

