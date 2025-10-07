# Tiger BioSciences - Complete Content Strategy
**Content Filling Guide**  
**Last Updated:** October 7, 2025

---

## 🎯 Content Overview

### Total Pages: 52 HTML Pages
- **Primary Pages:** 5 pages (Home, About, Contact, Products, Solutions)
- **Our Science Mega Menu:** 16 pages
- **Products Mega Menu:** 15 pages
- **Solutions Mega Menu:** 16 pages

---

## 🔑 Sanity CMS Configuration

### API Settings
```json
{
  "projectId": "0nxq33lj",
  "dataset": "production",
  "apiVersion": "2024-01-01",
  "useCdn": true
}
```

### API Endpoint
```
https://0nxq33lj.api.sanity.io/2024-01-01/data/query/production
```

### Token Setup
- **Public Token:** Already configured (read-only)
- **Write Token:** Required for Studio access
- **CORS:** Configure allowed origins in Sanity dashboard

---

## 📄 Page Content Priority

### Phase 1: Core Pages (PRIORITY 1)
1. ✅ `index.html` - Homepage (COMPLETE)
2. ⏳ `about.html` - Company story, mission, values
3. ⏳ `contact.html` - Contact forms, locations, support
4. ⏳ `products.html` - Product overview/catalog
5. ⏳ `science.html` - Research & science overview

### Phase 2: Our Science Section (PRIORITY 2)
**Research Areas:**
1. `wound-care.html` - Wound care solutions
2. `tissue-reconstruction.html` - Tissue reconstruction tech
3. `aesthetic-medicine.html` - Aesthetic applications
4. `regenerative-medicine.html` - Regenerative solutions
5. `orthopedic.html` - Orthopedic applications

**Innovation:**
6. `research-pipeline.html` - Current research projects
7. `clinical-trials.html` - Ongoing clinical trials
8. `publications.html` - Scientific publications
9. `camps-technology.html` - CAMPs technology deep dive
10. `patents.html` - Patent portfolio

**Quality:**
11. `quality-assurance.html` - QA processes
12. `regulatory.html` - Regulatory compliance
13. `manufacturing.html` - Manufacturing facilities
14. `certifications.html` - Certifications & standards

**Resources:**
15. `training.html` - Training programs
16. `faq.html` - Frequently asked questions

### Phase 3: Products Section (PRIORITY 3)
**Wound Care:**
1. `healpack.html` - HealPack product
2. `cargraft.html` - CarGraft product (typo: should be caregraft)
3. `alloply.html` - AlloPly product
4. `wound-centers.html` - Wound center solutions

**Aesthetic:**
5. `bellafill.html` - Bellafill dermal filler
6. `aveli.html` - Aveli cellulite treatment
7. `breast.html` - Breast reconstruction solutions
8. `plastic-surgery.html` - Plastic surgery products

**Surgical:**
9. `general-surgery.html` - General surgery products
10. `orthopedic.html` - Orthopedic solutions (duplicate)
11. `podiatry.html` - Podiatry solutions
12. `tissue-reconstruction.html` - Tissue solutions (duplicate)

**Specialty:**
13. `regenerative-medicine.html` - Regenerative products (duplicate)
14. `acapatch.html` - AcaPatch product
15. Birth Tissue Recovery (external)

### Phase 4: Solutions Section (PRIORITY 4)
**Healthcare Systems:**
1. `hospitals.html` - Hospital solutions
2. `wound-centers.html` - Wound center programs (duplicate)
3. `facilities.html` - Facility partnerships
4. `healthcare-professionals.html` - HCP resources

**Clinical Support:**
5. `training.html` - Training programs (duplicate)
6. `clinical-support.html` - Clinical support services
7. `reimbursement.html` - Reimbursement assistance
8. `ordering.html` - Ordering process

**Research:**
9. `investigator.html` - Investigator portal
10. `clinical-trials.html` - Clinical trial info (duplicate)
11. `research-pipeline.html` - Research programs (duplicate)
12. `partnerships.html` - Partnership opportunities

**Resources:**
13. `catalog.html` - Product catalog
14. `publications.html` - Publications library (duplicate)
15. `news.html` - News & updates
16. `support.html` - Customer support

### Phase 5: Secondary Pages
1. `careers.html` - Career opportunities
2. `investors.html` - Investor relations
3. `legal.html` - Legal information
4. `privacy.html` - Privacy policy
5. `terms.html` - Terms & conditions
6. `grants.html` - Grant programs
7. `tiger-way.html` - The Tiger Way philosophy
8. `vertical-integration.html` - Vertical integration story

---

## 📝 Content Templates

### Standard Page Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Page Title] - Tiger BioSciences™</title>
    <meta name="description" content="[150-160 character description]">
    <meta name="keywords" content="[relevant, keywords, separated, by, commas]">
    <link rel="stylesheet" href="assets/css/tiger-luxury.css">
</head>
<body>
    <!-- Navigation (Universal Mega Menu) -->
    <!-- Hero Section -->
    <!-- Main Content -->
    <!-- CTA Section -->
    <!-- Footer -->
</body>
</html>
```

### Content Sections Per Page
1. **Hero Banner** - Title, subtitle, CTA
2. **Overview Section** - Main content introduction
3. **Features/Benefits** - 3-6 key features
4. **Detailed Content** - In-depth information
5. **CTA Section** - Call to action
6. **Related Content** - Links to related pages

---

## 🎨 Content Guidelines

### Tone & Voice
- **Professional:** Medical/scientific credibility
- **Approachable:** Human-centered care
- **Innovative:** Leading-edge technology
- **Trustworthy:** Quality and safety focused

### Key Messaging
1. **Vertical Integration:** Complete control, superior quality
2. **CAMPs Technology:** Proprietary innovation
3. **Patient Outcomes:** Better healing, better lives
4. **Clinical Excellence:** Evidence-based solutions
5. **Global Leadership:** Worldwide trusted partner

### SEO Requirements
- **Title Tag:** 50-60 characters
- **Meta Description:** 150-160 characters
- **H1 Tag:** One per page, keyword-rich
- **H2-H3 Tags:** Hierarchical structure
- **Alt Text:** All images described
- **Internal Links:** 3-5 relevant links per page

---

## 🔗 Sanity Content Types

### Content Models Needed
1. **Pages**
   - title, slug, hero, content blocks, SEO

2. **Products**
   - name, description, features, applications, downloads

3. **Publications**
   - title, authors, journal, date, abstract, PDF

4. **Team Members**
   - name, role, bio, photo, credentials

5. **Testimonials**
   - quote, author, role, organization, avatar

6. **FAQs**
   - question, answer, category, order

7. **News/Blog Posts**
   - title, date, excerpt, content, featured image

8. **Locations**
   - name, address, phone, services, hours

---

## 📊 Content Metrics

### Per Page Requirements
- **Word Count:** 800-1,500 words minimum
- **Images:** 3-5 relevant images
- **Internal Links:** 5-8 links
- **External Links:** 2-3 authoritative sources
- **CTA:** 2-3 call-to-action elements
- **Contact Points:** Phone, email, or form

### Quality Checklist
- [ ] Unique content (no duplicate pages)
- [ ] Keyword optimized
- [ ] Mobile responsive
- [ ] Fast loading (<3 seconds)
- [ ] Accessible (WCAG 2.1 AA)
- [ ] Schema markup
- [ ] Social meta tags
- [ ] Analytics tracking

---

## 🚀 Implementation Strategy

### Week 1: Core Pages
- Day 1-2: About, Contact pages
- Day 3-4: Products, Science overview pages
- Day 5: QA and optimization

### Week 2: Our Science Section
- Day 1-2: Research areas (5 pages)
- Day 3: Innovation pages (5 pages)
- Day 4: Quality pages (4 pages)
- Day 5: Resources pages (2 pages)

### Week 3: Products Section
- Day 1-2: Wound care products (4 pages)
- Day 3: Aesthetic products (4 pages)
- Day 4: Surgical products (4 pages)
- Day 5: Specialty products (3 pages)

### Week 4: Solutions Section
- Day 1: Healthcare systems (4 pages)
- Day 2: Clinical support (4 pages)
- Day 3: Research programs (4 pages)
- Day 4: Resources (4 pages)
- Day 5: Secondary pages & QA

---

## 📋 Content Sources

### Internal Resources
- Existing company materials
- Product specifications
- Clinical data
- Team bios
- Company history

### External Research
- Industry publications
- Competitor analysis
- Medical journals
- FDA databases
- Patent filings

### Content Creation Tools
- Sanity Studio for CMS
- Figma for designs
- Canva for graphics
- Grammarly for editing
- SEMrush for SEO

---

## ✅ Completion Checklist

### Technical Setup
- [x] Sanity CMS configured
- [x] API endpoints working
- [x] sanity-client.js functional
- [ ] Write token configured
- [ ] CORS settings updated
- [ ] CDN caching enabled

### Content Creation
- [x] Homepage complete
- [ ] Core pages (4 pages)
- [ ] Science section (16 pages)
- [ ] Products section (15 pages)
- [ ] Solutions section (16 pages)
- [ ] Secondary pages (8 pages)

### SEO & Optimization
- [ ] All meta tags complete
- [ ] Schema markup added
- [ ] Sitemap.xml updated
- [ ] robots.txt configured
- [ ] Open Graph tags
- [ ] Twitter cards
- [ ] Analytics tracking

### Quality Assurance
- [ ] Content proofread
- [ ] Links tested
- [ ] Forms functional
- [ ] Mobile tested
- [ ] Accessibility audit
- [ ] Performance audit
- [ ] Cross-browser tested

---

**Document End**

Next Step: Begin filling out priority pages starting with About and Contact.

