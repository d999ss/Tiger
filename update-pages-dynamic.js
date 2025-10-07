#!/usr/bin/env node
/**
 * Update all HTML pages to use dynamic content from Sanity
 */

const fs = require('fs');
const path = require('path');

// Page template with dynamic content loading
const PAGE_TEMPLATE = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    
    <!-- Primary Meta Tags -->
    <title>{{TITLE}}</title>
    <meta name="title" content="{{TITLE}}">
    <meta name="description" content="{{META_DESCRIPTION}}">
    <meta name="keywords" content="{{KEYWORDS}}">
    <meta name="author" content="Tiger BioSciences">
    <meta name="robots" content="index, follow">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://tigerbiosciences.com/{{FILENAME}}">
    <meta property="og:title" content="{{TITLE}}">
    <meta property="og:description" content="{{META_DESCRIPTION}}">
    <meta property="og:image" content="https://tigerbiosciences.com/assets/images/og-{{SLUG}}.jpg">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://tigerbiosciences.com/{{FILENAME}}">
    <meta property="twitter:title" content="{{TITLE}}">
    <meta property="twitter:description" content="{{META_DESCRIPTION}}">
    
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
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "{{TITLE}}",
      "description": "{{META_DESCRIPTION}}",
      "url": "https://tigerbiosciences.com/{{FILENAME}}"
    }
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

<!-- Navigation (Loaded from Sanity) -->
<nav class="navbar" id="mainNav" role="navigation" aria-label="Main navigation">
    <div class="nav-container">
        <a href="index.html" class="logo" aria-label="Tiger BioSciences Home">TIGER BIOSCIENCES™</a>
        
        <ul class="nav-menu" role="menubar">
            <!-- Navigation loaded dynamically from Sanity -->
        </ul>
    </div>
</nav>

<!-- Dynamic Content Area (Loaded from Sanity CMS) -->
<div id="dynamic-content" aria-live="polite">
    <!-- Page content sections will be loaded here from Sanity -->
    <div style="min-height: 50vh; display: flex; align-items: center; justify-content: center; padding: 4rem;">
        <div style="text-align: center;">
            <div style="font-size: 2rem; color: var(--neutral-600); margin-bottom: 1rem;">Loading content...</div>
            <div style="color: var(--neutral-500);">Fetching from Sanity CMS</div>
        </div>
    </div>
</div>

<!-- Footer -->
<footer class="footer" role="contentinfo" aria-label="Site footer">
    <div class="footer-content">
        <div class="footer-brand">
            <h3>Tiger BioSciences™</h3>
            <p>Pioneering the future of healthcare through innovative biomaterial solutions that enhance patient outcomes and improve quality of life.</p>
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
</footer>

<!-- Sanity CMS Client -->
<script src="assets/js/sanity-client.js"></script>

</body>
</html>`;

/**
 * Update a page to use dynamic content
 */
function updatePage(filename, data) {
  const slug = filename.replace('.html', '');
  
  let html = PAGE_TEMPLATE
    .replace(/{{FILENAME}}/g, filename)
    .replace(/{{SLUG}}/g, slug)
    .replace(/{{TITLE}}/g, data.title || `${slug} - Tiger BioSciences™`)
    .replace(/{{META_DESCRIPTION}}/g, data.meta_description || 'Tiger BioSciences - Advanced tissue technology')
    .replace(/{{KEYWORDS}}/g, `Tiger BioSciences, ${slug}, CAMPs, tissue technology`);
  
  return html;
}

/**
 * Main execution
 */
async function main() {
  console.log('🔄 Updating all pages to use dynamic Sanity content...');
  console.log('='.repeat(60));
  
  // Load page data
  const pageData = JSON.parse(fs.readFileSync('./page-content-data.json', 'utf8'));
  
  let updated = 0;
  
  for (const [filename, data] of Object.entries(pageData.pages)) {
    try {
      const html = updatePage(filename, data);
      fs.writeFileSync(filename, html, 'utf8');
      console.log(`✓ ${filename}`);
      updated++;
    } catch (error) {
      console.error(`❌ Error updating ${filename}:`, error.message);
    }
  }
  
  console.log('='.repeat(60));
  console.log(`✅ Updated ${updated} pages to use Sanity CMS`);
  console.log('\n📋 All pages now load content dynamically from Sanity!');
}

main();

