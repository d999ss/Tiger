# Sanity CMS Setup - Complete Integration Guide
**Tiger BioSciences - Full CMS Control**  
**Last Updated:** October 7, 2025

---

## ✅ What's Been Implemented

### 🎨 Complete Page Builder System
- **9 Section Types** for modular page building
- **Full drag & drop** section management
- **Image uploads** throughout the system
- **Navigation management** via CMS
- **All 50+ pages** ready for CMS control

### 📦 Schema Files Created

**Content Blocks** (`studio-schemas/schemaTypes/blocks/`):
1. ✅ `heroSection.ts` - Hero sections with image/gradient backgrounds
2. ✅ `featureGrid.ts` - Feature cards (1-6 cards)
3. ✅ `statsSection.ts` - Statistics with animated counters
4. ✅ `testimonialSection.ts` - Testimonials with photos
5. ✅ `faqSection.ts` - FAQ accordions
6. ✅ `imageContentSection.ts` - Image + rich text combo
7. ✅ `ctaSection.ts` - Call-to-action sections
8. ✅ `richTextSection.ts` - Free-form rich text editor
9. ✅ `endorsedSection.ts` - Grid items

**Core Schemas:**
- ✅ `navigation.ts` - Complete mega menu management
- ✅ Updated `page.ts` - Modular sections array
- ✅ Updated `index.ts` - All schemas registered

### 🔧 JavaScript Implementation
- ✅ `sanity-client.js` - Complete renderer system
  - Renders all 9 section types
  - Image URL building
  - Navigation from CMS
  - FAQ accordion initialization
  - Stats counter animation
  - Portable text to HTML conversion

### 📄 Page Updates
- ✅ All 50 pages converted to dynamic loading
- ✅ Pages load content from Sanity on page load
- ✅ Fallback content while loading
- ✅ SEO meta tags preserved

### 🛠️ Migration Tools
- ✅ `migrate-to-sanity.js` - Populate all pages in CMS
- ✅ `update-pages-dynamic.js` - Convert pages to dynamic
- ✅ `page-content-data.json` - Source content data

---

## 🚀 Setup Instructions

### Step 1: Install Dependencies

```bash
# In main project
cd "/Users/donnysmith/Desktop/Tiger CMS"
npm install

# In Studio directory
cd studio
npm install
```

### Step 2: Get Sanity Write Token

1. Visit: **https://www.sanity.io/manage/project/0nxq33lj/api**
2. Click **"Add API Token"**
3. Name: `Tiger CMS Migration`
4. Permissions: **Editor** or **Admin**
5. **Copy the token** (save securely!)

### Step 3: Set Environment Variable

**On Mac/Linux:**
```bash
export SANITY_WRITE_TOKEN="your-token-here"
```

**On Windows (PowerShell):**
```powershell
$env:SANITY_WRITE_TOKEN="your-token-here"
```

**Permanently (add to ~/.zshrc or ~/.bashrc):**
```bash
echo 'export SANITY_WRITE_TOKEN="your-token-here"' >> ~/.zshrc
source ~/.zshrc
```

### Step 4: Run Migration

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS"
node migrate-to-sanity.js
```

**This will:**
- Create navigation document with all mega menus
- Create 50 page documents with content sections
- Upload initial content to Sanity

**Expected output:**
```
🚀 Starting migration to Sanity CMS...
✓ Created navigation
✓ contact.html
✓ products.html
... (50 pages)
✅ Migration complete!
   Created/Updated: 51 documents
```

### Step 5: Start Sanity Studio

```bash
cd studio
npm run dev
```

**Access at:** http://localhost:3333

### Step 6: Verify in Studio

1. **Open Studio** at http://localhost:3333
2. **Check "📄 Pages"** - should see all 50 pages
3. **Check "🧭 Navigation"** - should see mega menu structure
4. **Click a page** - should see sections array
5. **Try editing** - make a small change
6. **Publish** - click publish button
7. **Refresh website** - see your change!

---

## 🎨 Client Workflow

### Daily Editing Workflow

1. **Open Studio** (http://localhost:3333 or deployed URL)
2. **Navigate to content** (Pages, Navigation, etc.)
3. **Make edits** in visual editor
4. **Preview changes** (if needed)
5. **Publish** to make live
6. **Refresh website** to verify

### Managing Pages

**Edit existing page:**
- Pages → Select page → Edit → Publish

**Add section to page:**
- Open page → Scroll to "Sections" → Click "+ Add item" → Choose type → Fill fields → Publish

**Reorder sections:**
- Open page → Drag sections using ☰ handle → Publish

**Remove section:**
- Open page → Click section → Menu (...) → Remove → Publish

### Managing Images

**Upload new image:**
- Click any image field → Upload → Select file → Add alt text → Save

**Replace image:**
- Click image → Select different image from library OR upload new → Save

**Reuse image:**
- Click image → Browse library → Select existing image → Save

### Managing Navigation

**Edit mega menu:**
- Navigation → Expand mega menu → Edit columns/links → Publish

**Add new link:**
- Navigation → Find column → Click "+ Add" in links → Fill label/URL → Publish

**Change featured card:**
- Navigation → Expand mega menu → Edit Featured Card → Publish

---

## 📋 Content Management Best Practices

### SEO Optimization

**Every page should have:**
- Unique meta title (50-60 characters)
- Compelling meta description (150-160 characters)
- Relevant keywords
- Clear, descriptive H1 (hero title)
- Structured heading hierarchy (H2, H3)

**Meta Title Formula:**
```
[Page Topic] - Tiger BioSciences™
Example: "Advanced Wound Care Solutions - Tiger BioSciences™"
```

**Meta Description Formula:**
```
[What it is] [Key benefit] [Call to action]
Example: "HealPack advanced wound dressings use CAMPs technology for chronic wound management. FDA compliant and clinically proven. Contact us today."
```

### Content Structure

**Good page structure:**
1. Hero Section (clear value proposition)
2. Feature Grid (3-6 key benefits)
3. Image + Content (detailed explanation)
4. Testimonials or Stats (social proof)
5. FAQ (answer objections)
6. CTA (clear next step)

### Image Guidelines

**Hero Backgrounds:**
- Size: 2400x1200px
- Format: JPG
- File size: < 500KB (compressed)

**Content Images:**
- Size: 1200x800px
- Format: JPG or PNG
- File size: < 300KB

**Team Photos:**
- Size: 400x400px (square)
- Format: JPG
- File size: < 100KB

**Always include:**
- Descriptive alt text (accessibility + SEO)
- Relevant filename before upload

---

## 🔄 Deployment Workflows

### Content Updates (No Code Changes)

**Client makes content edit in Studio:**
1. Edit in Studio
2. Publish
3. Refresh website (2-3 seconds)
4. Changes are LIVE

**No git, no deployment, no downtime!**

### Code Updates (Developer Only)

**When changing schemas, HTML, or CSS:**
1. Make code changes locally
2. Test locally
3. Commit to git
4. Push to GitHub
5. Vercel auto-deploys

### Studio Updates

**When adding new schema fields:**
1. Edit schema files in `studio-schemas/`
2. Studio auto-reloads
3. New fields appear in Studio
4. May need to update `sanity-client.js` renderers

---

## 📊 Sanity Dashboard

### Project Dashboard

**Access:** https://www.sanity.io/manage/project/0nxq33lj

**Key Sections:**

**API:**
- View API tokens
- Configure CORS origins
- Monitor API usage

**Members:**
- Invite team members
- Assign roles
- Remove access

**Datasets:**
- production (live data)
- Can create development/staging datasets

**Settings:**
- Project name
- Billing
- Integrations

---

## 🎓 Training Checklist

### For Content Editors

- [ ] Can access Sanity Studio
- [ ] Can find and edit pages
- [ ] Can add sections to pages
- [ ] Can reorder sections (drag & drop)
- [ ] Can upload and manage images
- [ ] Can edit navigation
- [ ] Can publish changes
- [ ] Can see changes on live site

### For Administrators

- [ ] Have admin access to Sanity project
- [ ] Can invite new users
- [ ] Understand content types
- [ ] Can review version history
- [ ] Know how to restore content
- [ ] Understand deployment process

---

## 🔐 Security & Access

### API Tokens

**Read Tokens (Public):**
- Used by website to fetch content
- Safe to include in HTML/JavaScript
- Already configured in `sanity-client.js`

**Write Tokens (Private):**
- Used for migration and API writes
- **Keep secret!**
- Don't commit to git
- Don't share publicly

### CORS Configuration

Ensure these origins are allowed in Sanity dashboard:
- `http://localhost:3000`
- `http://localhost:3333` (Studio)
- `https://tigerbiosciences.com`
- `https://tiger-biosciences.vercel.app`
- `https://*.vercel.app` (preview deployments)

**Configure:** https://www.sanity.io/manage/project/0nxq33lj/api

---

## 🆘 Emergency Procedures

### Content Accidentally Deleted

1. Open the document type (Pages, etc.)
2. Find the deleted item in list (may show as deleted)
3. Click document
4. **Document menu** → **Revision History**
5. **Browse versions** → Find last good version
6. **Click "Restore"**

### Site Not Loading Content

**Quick fixes:**
1. Check Sanity API status: https://status.sanity.io
2. Check browser console for errors
3. Verify API token is valid
4. Clear browser cache
5. Check CORS settings

### Emergency Rollback

If major issues after CMS migration:
```bash
cd "/Users/donnysmith/Desktop/Tiger CMS"
git log --oneline -10
git checkout [commit-before-cms]
# Redeploy to Vercel
```

---

## 📞 Support Contacts

**Website Content Questions:**
- Your team's content manager
- Email: [content@tigerbiosciences.com]

**Technical CMS Issues:**
- Developer: [your email]
- Sanity Support: support@sanity.io

**Urgent Issues:**
- Phone: 1-888-665-5005

---

## ✨ What Your Client Can Now Do

✅ **Edit any page** - All 50+ pages through visual editor  
✅ **Upload images** - Anywhere on the site  
✅ **Update navigation** - Change menus, links, featured cards  
✅ **Add content sections** - Drag & drop page builder  
✅ **Reorder sections** - Rearrange page layout  
✅ **Manage SEO** - Meta titles, descriptions per page  
✅ **Add testimonials** - With photos and quotes  
✅ **Create FAQs** - Interactive accordion sections  
✅ **Update stats** - Animated counters  
✅ **Instant publishing** - No deployment wait time  
✅ **Version history** - Undo any change within 30 days  

**All without touching code!** 🎉

---

**Ready to migrate? Run:** `node migrate-to-sanity.js`  
**Need help? Check:** `CMS_CLIENT_GUIDE.md`

**Document End**

