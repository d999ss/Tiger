#!/bin/bash

# Create all menu pages with consistent template
cd "/Users/donnysmith/Desktop/Tiger CMS"

# Function to create a page
create_page() {
    local filename="$1"
    local title="$2"
    local heading="$3"
    local description="$4"
    
    cat > "$filename" << 'PAGEEND'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TITLE_PLACEHOLDER - Tiger BioSciences™</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        @font-face {
            font-family: 'LT Superior Mono';
            src: url('LTSuperiorMono.otf') format('opentype');
            font-weight: 500;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            color: #1a1a1a;
            background: #fff;
            line-height: 1.6;
        }
        .mono { font-family: 'LT Superior Mono', monospace; font-weight: 500; }
        :root {
            --red-primary: #991514;
            --red-dark: #7f1d1d;
            --red-light: #fef2f2;
            --neutral-50: #fafafa;
            --neutral-100: #f5f5f5;
            --neutral-200: #e5e5e5;
            --neutral-700: #404040;
            --neutral-800: #262626;
            --neutral-900: #171717;
        }
        
        .announcement {
            background: var(--red-primary);
            color: #fff;
            text-align: center;
            padding: 0.875rem 1.5rem;
            font-size: 0.8125rem;
        }
        .announcement a { color: #fff; text-decoration: underline; margin-left: 0.75rem; }
        
        .navbar {
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(20px);
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid var(--neutral-200);
        }
        .nav-container {
            max-width: 90rem;
            margin: 0 auto;
            padding: 1.75rem 3rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo {
            font-size: 1.125rem;
            font-weight: 600;
            color: var(--red-primary);
            text-decoration: none;
        }
        .nav-menu {
            display: flex;
            gap: 2.5rem;
            list-style: none;
        }
        .nav-link {
            font-size: 0.9375rem;
            color: var(--neutral-800);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }
        .nav-link:hover { color: var(--red-primary); }
        .btn-nav {
            padding: 0.625rem 1.5rem;
            background: var(--red-primary);
            color: #fff;
            border-radius: 624.9375rem;
            text-decoration: none;
            font-size: 0.875rem;
            font-weight: 500;
            transition: all 0.2s;
        }
        .btn-nav:hover { background: var(--red-dark); }
        
        .page-hero {
            background: linear-gradient(135deg, var(--red-dark), var(--red-primary));
            color: #fff;
            padding: 8rem 3rem 5rem;
            text-align: center;
        }
        .hero-badge {
            display: inline-block;
            padding: 0.5rem 1.25rem;
            background: rgba(255,255,255,0.2);
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 624.9375rem;
            font-size: 0.6875rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 1.5rem;
        }
        .page-hero h1 {
            font-size: 4rem;
            font-weight: 600;
            line-height: 1.2;
            margin-bottom: 1.5rem;
        }
        .page-hero p {
            font-size: 1.25rem;
            opacity: 0.95;
            max-width: 48rem;
            margin: 0 auto;
        }
        
        .content {
            max-width: 56rem;
            margin: 0 auto;
            padding: 6rem 3rem;
        }
        .content h2 {
            font-size: 2.5rem;
            font-weight: 600;
            color: var(--red-primary);
            margin: 3rem 0 1.5rem;
        }
        .content p {
            font-size: 1.125rem;
            line-height: 1.8;
            color: var(--neutral-700);
            margin-bottom: 1.5rem;
        }
        .content ul {
            margin: 1.5rem 0 1.5rem 2rem;
        }
        .content li {
            font-size: 1.125rem;
            line-height: 1.8;
            color: var(--neutral-700);
            margin-bottom: 0.75rem;
        }
        
        .cta-section {
            background: var(--neutral-50);
            padding: 5rem 3rem;
            text-align: center;
        }
        .cta-section h3 {
            font-size: 2rem;
            font-weight: 600;
            color: var(--neutral-900);
            margin-bottom: 1.5rem;
        }
        .cta-section p {
            font-size: 1.125rem;
            color: var(--neutral-700);
            margin-bottom: 2rem;
        }
        .btn {
            display: inline-block;
            padding: 1rem 2.5rem;
            background: var(--red-primary);
            color: #fff;
            border-radius: 624.9375rem;
            text-decoration: none;
            font-size: 0.9375rem;
            font-weight: 500;
            transition: all 0.3s;
        }
        .btn:hover {
            background: var(--red-dark);
            transform: translateY(-2px);
        }
        
        .footer {
            background: var(--neutral-900);
            color: #fff;
            padding: 5rem 3rem 3rem;
        }
        .footer-content {
            max-width: 90rem;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 4rem;
            margin-bottom: 3rem;
        }
        .footer-brand h3 {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--red-primary);
        }
        .footer-brand p {
            font-size: 0.9375rem;
            line-height: 1.7;
            opacity: 0.7;
        }
        .footer-section h4 {
            font-size: 0.875rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 1.5rem;
            opacity: 0.6;
        }
        .footer-links {
            list-style: none;
        }
        .footer-links li {
            margin-bottom: 0.875rem;
        }
        .footer-links a {
            color: #fff;
            text-decoration: none;
            font-size: 0.9375rem;
            opacity: 0.8;
            transition: opacity 0.2s;
        }
        .footer-links a:hover { opacity: 1; }
        .footer-bottom {
            padding-top: 3rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            justify-content: space-between;
            font-size: 0.875rem;
            opacity: 0.6;
        }
        .footer-legal {
            display: flex;
            gap: 2rem;
        }
        .footer-legal a {
            color: #fff;
            text-decoration: none;
            opacity: 0.6;
        }
        
        @media (max-width: 768px) {
            .nav-menu { display: none; }
            .page-hero h1 { font-size: 2.5rem; }
            .content { padding: 4rem 1.5rem; }
            .footer-content { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

<div class="announcement">
    Now Live: Tiger BioSciences Comprehensive Solutions
    <a href="index-perfect.html#solutions">Explore</a>
</div>

<nav class="navbar">
    <div class="nav-container">
        <a href="index-perfect.html" class="logo">TIGER BIOSCIENCES™</a>
        <ul class="nav-menu">
            <li><a href="about.html" class="nav-link">Our Story</a></li>
            <li><a href="products.html" class="nav-link">Products</a></li>
            <li><a href="science.html" class="nav-link">Science</a></li>
            <li><a href="contact.html" class="nav-link">Contact</a></li>
            <li><a href="faq.html" class="nav-link">FAQ</a></li>
        </ul>
        <a href="contact.html" class="btn-nav">Get In Touch</a>
    </div>
</nav>

<div class="page-hero">
    <div class="hero-badge mono">TIGER BIOSCIENCES™</div>
    <h1>HEADING_PLACEHOLDER</h1>
    <p>DESCRIPTION_PLACEHOLDER</p>
</div>

<div class="content">
    <h2>Overview</h2>
    <p>CONTENT_PLACEHOLDER</p>
    
    <h2>Key Features</h2>
    <ul>
        <li>Advanced technology and proven results</li>
        <li>Supported by clinical evidence and peer-reviewed research</li>
        <li>Designed for optimal patient outcomes</li>
        <li>Backed by our vertically integrated quality system</li>
    </ul>
</div>

<div class="cta-section">
    <h3>Learn More</h3>
    <p>Contact our team to discover how this solution can benefit your practice.</p>
    <a href="contact.html" class="btn">Contact Us</a>
</div>

<footer class="footer">
    <div class="footer-content">
        <div class="footer-brand">
            <h3>TIGER BIOSCIENCES™</h3>
            <p>The world's first fully vertically integrated tissue company.</p>
        </div>
        <div class="footer-section">
            <h4 class="mono">Main Pages</h4>
            <ul class="footer-links">
                <li><a href="index-perfect.html">Homepage</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="products.html">Products</a></li>
                <li><a href="careers.html">Careers</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4 class="mono">Company</h4>
            <ul class="footer-links">
                <li><a href="tiger-way.html">The Tiger Way</a></li>
                <li><a href="facilities.html">Facilities</a></li>
                <li><a href="faq.html">FAQ</a></li>
                <li><a href="privacy.html">Privacy</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4 class="mono">Contact</h4>
            <ul class="footer-links">
                <li><a href="contact.html">Contact Us</a></li>
                <li><a href="legal.html">Legal</a></li>
                <li><a href="terms.html">Terms</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© Tiger BioSciences™ 2025, All Rights Reserved</p>
        <div class="footer-legal">
            <a href="legal.html">Legal</a>
            <a href="terms.html">Terms</a>
            <a href="privacy.html">Privacy</a>
        </div>
    </div>
</footer>

</body>
</html>
PAGEEND

    # Replace placeholders
    sed -i '' "s/TITLE_PLACEHOLDER/$title/g" "$filename"
    sed -i '' "s/HEADING_PLACEHOLDER/$heading/g" "$filename"
    sed -i '' "s/DESCRIPTION_PLACEHOLDER/$description/g" "$filename"
    sed -i '' "s/CONTENT_PLACEHOLDER/Tiger BioSciences is committed to advancing $heading through innovative research, clinical excellence, and our unique vertically integrated approach. Our solutions are designed to meet the highest standards of quality and efficacy./g" "$filename"
    
    echo "Created: $filename"
}

# Create all Our Science pages
create_page "wound-care.html" "Wound Care" "Wound Care Solutions" "Advanced tissue technologies for chronic and acute wound management"
create_page "tissue-reconstruction.html" "Tissue Reconstruction" "Tissue Reconstruction" "Innovative solutions for soft tissue repair and reconstruction"
create_page "aesthetic-medicine.html" "Aesthetic Medicine" "Aesthetic Medicine" "Premium aesthetic solutions for cosmetic and reconstructive procedures"
create_page "regenerative-medicine.html" "Regenerative Medicine" "Regenerative Medicine" "Cutting-edge regenerative therapies for tissue healing and repair"
create_page "orthopedic.html" "Orthopedic Applications" "Orthopedic Applications" "Specialized tissue solutions for orthopedic soft tissue repair"
create_page "clinical-trials.html" "Clinical Trials" "Clinical Trials" "Ongoing research and clinical studies advancing regenerative medicine"
create_page "publications.html" "Publications" "Scientific Publications" "Peer-reviewed research and clinical evidence supporting our technologies"
create_page "camps-technology.html" "CAMPs Technology" "CAMPs Technology Platform" "Cellular, Acellular, and Matrix-like Products revolutionizing tissue repair"
create_page "patents.html" "Patents & IP" "Patents & Intellectual Property" "Proprietary technologies protecting our innovative solutions"
create_page "vertical-integration.html" "Vertical Integration" "Vertical Integration" "Complete control from tissue recovery to distribution"
create_page "quality-assurance.html" "Quality Assurance" "Quality Assurance" "AATB-accredited facilities meeting the highest quality standards"
create_page "regulatory.html" "Regulatory Affairs" "Regulatory Affairs" "Compliance with FDA regulations and industry standards"
create_page "partnerships.html" "Academic Partnerships" "Academic Partnerships" "Collaborations with leading research institutions"
create_page "grants.html" "Research Grants" "Research Grants" "Funding opportunities for innovative tissue research"
create_page "investigator.html" "Investigator Portal" "Investigator Portal" "Resources and support for clinical investigators"

# Create all Products pages
create_page "alloply.html" "alloPLY™" "alloPLY™" "Dual layer amniotic membrane with 2-year shelf stability"
create_page "caregraft.html" "caregraFT™" "caregraFT™" "Full thickness placental tissue with 5-year shelf stability"
create_page "acapatch.html" "ACAPatch™" "ACAPatch™" "ACA configuration with maximum ECM content"
create_page "healpack.html" "HealPACK™" "HealPACK™" "Comprehensive wound dressing portfolio"
create_page "aveli.html" "Avéli™" "Avéli™" "FDA-cleared minimally invasive cellulite treatment"
create_page "bellafill.html" "Bellafill®" "Bellafill®" "FDA-approved dermal filler with 5-year efficacy"
create_page "breast.html" "Breast Products" "Breast Products" "FDA-approved breast implants and tissue expanders"
create_page "podiatry.html" "Podiatry Solutions" "Podiatry Solutions" "Specialized tissue technologies for podiatric applications"
create_page "plastic-surgery.html" "Plastic Surgery" "Plastic Surgery Solutions" "Advanced products for reconstructive and cosmetic procedures"
create_page "general-surgery.html" "General Surgery" "General Surgery" "Tissue solutions for surgical wound management"
create_page "wound-centers.html" "Wound Care Centers" "Wound Care Centers" "Comprehensive solutions for wound care facilities"
create_page "catalog.html" "Product Catalog" "Product Catalog" "Complete catalog of Tiger BioSciences products"
create_page "ordering.html" "Ordering Information" "Ordering Information" "How to order Tiger BioSciences products"
create_page "training.html" "Product Training" "Product Training" "Educational resources and training programs"
create_page "reimbursement.html" "Reimbursement Support" "Reimbursement Support" "Insurance coverage and reimbursement assistance"

echo ""
echo "✅ All pages created successfully!"
echo "Total pages created: 30"
PAGEEND

chmod +x create-all-menu-pages.sh
./create-all-menu-pages.sh

