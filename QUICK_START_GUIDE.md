# 🚀 Tiger BioSciences CMS - Quick Start Guide

## Access Your Webflow Site

### Site Information
- **Site Name:** TigerBioSciences
- **Site ID:** `68d930d0b9cebe7ec786af1d`
- **Preview URL:** https://tigerbiosciences-972d02.webflow.io
- **Workspace ID:** `636daf5936f07f053e8f85b6`

### How to Access

1. **Log into Webflow**
   - Go to: https://webflow.com/dashboard
   - Use your Webflow account credentials

2. **Open Your Site**
   - Look for "TigerBioSciences" in your workspace
   - Or use the direct preview link above

---

## 🎯 What's Already Done

### ✅ CMS Collections Populated

#### **Divisions Collection** (16 Divisions)
All divisions are organized into 4 categories:

1. **Wound Care & Pain Management** (3 divisions)
   - Tiger Wound Care ⭐
   - Extremity Care
   - Encore Surgical Dressings

2. **Soft Tissue Recon & Aesthetics** (5 divisions)
   - Tiger Aesthetics ⭐
   - Sientra
   - BioCreations Medical
   - Revelle Aesthetics
   - Suneva Medical

3. **Tissue R&D, Processing and Recovery** (4 divisions)
   - RegenTX ⭐
   - RegenTX Labs
   - Birth Tissue Recovery
   - bioCARE

4. **International** (4 divisions)
   - Tiger International ⭐
   - Lizard Health Technology
   - Airway Medix S.A.
   - Tiger Production & Services

#### **Products Collection** (21+ Products)
Including key products like:
- alloPLY™ (Dual Layer Amniotic Membrane)
- caregraFT™ (Full Thickness Placental Membrane)
- ACAPatch™ (Amnion-Chorion-Amnion)
- HealPACK™ (Wound Dressings)
- Avéli™ (Cellulite Treatment)
- Bellafill® (Dermal Filler)
- Sientra Breast Implants
- And more!

---

## 📋 Next Steps to Build Your Site

### Phase 1: Design Setup (Start Here!)

1. **Homepage Layout**
   ```
   Create a new page called "Home" and add:
   - Hero section with video background
   - "Welcome to Tiger BioSciences" section
   - Division categories (4 sections)
   - "The Tiger Way" section
   - Featured products
   - Careers call-to-action
   - Contact section
   ```

2. **Create Collection Templates**
   - Division Template (will show all division details)
   - Product Template (will show all product details)

3. **Add Navigation**
   - Main menu with dropdown for categories
   - Link to division pages
   - Products page
   - About, Careers, Contact

### Phase 2: Add Your Division Pages

You can use the CMS to dynamically generate pages, or create static pages for each division category:

- Wound Care & Pain Management Landing Page
- Soft Tissue Recon & Aesthetics Landing Page
- Tissue R&D Landing Page
- International Landing Page

### Phase 3: Style It Beautiful

Use the existing brand colors from your HTML:
- **Tiger Red:** `#991514`, `#D32F2F`
- **Tiger Orange/Gold:** `#D8930B`
- **Professional Grays and Whites**

Design elements to include:
- Wave dividers between sections
- Shaped image containers
- Floating decorative shapes
- Card-based layouts for divisions
- Product carousels

---

## 🎨 CMS Field Reference

### Division Fields
- `division-name` - Official division name
- `category` - One of 4 categories
- `division-url` - Link to division website (if external)
- `description` - Rich text description
- `key-features` - Bulleted list of features
- `hero-image` - Main division image
- `sort-order` - Order for display (1-16)

### Product Fields
- `product-name` - Official product name
- `division` - Which division owns this product
- `product-type` - Category (CAMPs, Wound Dressings, etc.)
- `description` - Rich text product description
- `technical-specs` - Technical specifications
- `applications` - Clinical applications
- `product-image` - Main product image

---

## 💡 Pro Tips

### Using CMS Collections in Webflow

1. **Collection Lists**
   - Drag a Collection List onto any page
   - Choose "Divisions" or "Products"
   - Filter by category if needed
   - Style the collection items

2. **Dynamic Content**
   - All text fields automatically pull from CMS
   - Images can be set to pull from image fields
   - Links can be dynamic

3. **Filtering**
   - Use filters to show only specific categories
   - Example: Show only "Wound Care & Pain Management" divisions

### Creating Beautiful Layouts

1. **Division Cards**
   ```
   For each division:
   - Image at top (hero-image)
   - Division name (large heading)
   - Category badge
   - Description excerpt
   - "Learn More" button
   - Link to division-url or detail page
   ```

2. **Product Showcase**
   ```
   For each product:
   - Product image
   - Product name with ™ or ® symbol
   - Product type
   - Short description
   - "View Details" button
   ```

---

## 📞 Content to Add

### Still Needed (manually add when ready):

1. **Images**
   - Division logos (upload to CMS)
   - Product photography
   - Facility photos
   - Team member photos

2. **Pages**
   - About page (company history, mission)
   - Facilities page (Conshohocken, San Antonio)
   - Careers page (job listings)
   - Science page (research, clinical trials)
   - Contact page (forms, locations)

3. **Legal**
   - Privacy Policy
   - Terms & Conditions
   - Legal Disclaimer

---

## 🔗 Important Links

### Division Websites (for reference)
- https://tigerwoundcare.com
- https://tiger-aesthetics.com
- https://sientra.com
- https://extremitycare.com
- https://lizard-health.com
- https://airway-medix.com
- And more...

### Contact Information
**Corporate:**
555 E North Ln, Ste 5000, Bldg D
Conshohocken, PA 19428
Phone: (+1) 888-665-5005
Email: info@tigerbiosciences.com

---

## 🆘 Need Help?

### Webflow Resources
- **University:** https://university.webflow.com
- **Forums:** https://forum.webflow.com
- **Support:** https://support.webflow.com

### Common Tasks

**To edit a division:**
1. Go to CMS → Divisions
2. Find the division you want to edit
3. Click to edit
4. Make changes
5. Save and publish

**To add a new product:**
1. Go to CMS → Products
2. Click "New Product"
3. Fill in all fields
4. Save and publish

**To update navigation:**
1. Go to Pages → Settings
2. Edit your navbar
3. Add links to your collection pages

---

## ✨ Quick Wins

Start with these to see immediate results:

1. **Create Homepage**
   - Add hero section with "The first of its kind" tagline
   - Add 4 division category cards
   - Add "The Tiger Way" section

2. **Create Division Category Pages**
   - One page per category showing all divisions in that category
   - Use Collection Lists filtered by category

3. **Add Navigation**
   - Main menu linking to category pages
   - "Products" page
   - "Contact" link

4. **Style It**
   - Apply Tiger Red color scheme
   - Add hover effects to cards
   - Use your existing brand fonts

---

## 📊 Success Checklist

- [ ] Homepage created with hero section
- [ ] Division category pages created (4 pages)
- [ ] Division detail template created
- [ ] Product detail template created
- [ ] Navigation menu added
- [ ] Footer with division links
- [ ] Brand colors applied
- [ ] Images uploaded
- [ ] Forms added (contact, careers)
- [ ] Mobile responsive verified
- [ ] Test on all browsers
- [ ] SEO settings configured
- [ ] Ready to publish!

---

**Your site foundation is ready! Now it's time to make it beautiful! 🎨**

Need the detailed organization document? Check out `TIGER_SITE_ORGANIZATION.md` in this folder.

---

**Questions?** Everything is set up and ready to go. Just open Webflow Designer and start building your beautiful pages!


