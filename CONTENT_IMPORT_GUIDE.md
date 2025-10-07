# 📦 Content Import Guide for Sanity CMS

## ✅ Your Content is Ready!

I've extracted all content from your HTML pages and prepared it for Sanity.

**File Created:** `sanity-content-export.json`

---

## 🎯 Two Ways to Import

### Option 1: Automatic Import (Recommended)

1. **Get a Sanity API Token:**
   - Go to: https://www.sanity.io/manage/personal/tokens
   - Create a new token with "Editor" permissions
   - Copy the token

2. **Run the import script:**
   ```bash
   cd "/Users/donnysmith/Desktop/Tiger CMS"
   export SANITY_TOKEN="your-token-here"
   node import-content-to-sanity.js
   ```

### Option 2: Manual Entry

Open Sanity Studio (http://localhost:3333) and manually add the content from `sanity-content-export.json`.

---

## 📋 Content Extracted

### ✅ **Homepage Content**
- Hero Badge: "The First of Its Kind"
- Hero Title: "Tiger BioSciences"
- Hero Subtitle: Complete description
- CTA Buttons: "Let's Get Together" + "Our Story"
- Integration Section: The Tiger Way (4 items)

### ✅ **6 Divisions**
1. RegenTX Division - Tissue Science Redefined
2. Tiger Wound Care - Advanced CAMP Solutions
3. Tiger Aesthetics - Shaping the Future  
4. Tiger International - Global Access
5. Production & Services - Medical Device Engineering
6. Vertical Integration - Complete Quality Control

### ✅ **4 FAQs**
1. What are CAMPs?
2. What makes vertical integration important?
3. How do you ensure product quality?
4. How can I access products?

### ✅ **2 Testimonials**
1. Tissue Processing testimonial
2. Research & Development testimonial

### ✅ **Site Settings**
- Address: 555 E North Ln, Ste 5000, Bldg D, Conshohocken, PA 19428
- Phone: (+1) 888 665 5005
- Footer text

---

## 🚀 After Import

Once content is in Sanity, I'll:
1. ✅ Update your HTML to fetch from Sanity API
2. ✅ Add dynamic content rendering
3. ✅ Keep your luxury design 100% intact
4. ✅ Enable real-time content updates

---

## 💡 Quick Start

```bash
# Start Sanity Studio
cd studio && npm run dev

# View at
http://localhost:3333

# Import content (if you have token)
export SANITY_TOKEN="your-token"
node import-content-to-sanity.js
```

---

**Ready?** Get your API token and run the import! 🎉

