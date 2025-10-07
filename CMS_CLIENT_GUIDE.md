# Tiger BioSciences CMS - Client User Guide
**Complete Guide to Managing Your Website Content**  
**Last Updated:** October 7, 2025

---

## 🎯 Overview

Your Tiger BioSciences website is now **fully CMS-managed** through Sanity Studio. You can edit:
- ✅ All 50+ pages
- ✅ Navigation and mega menus
- ✅ All images and media
- ✅ Text content on every section
- ✅ Add/remove/reorder page sections
- ✅ SEO settings for all pages

**No coding required!** All updates happen through an intuitive visual interface.

---

## 🚀 Getting Started

### Step 1: Access Sanity Studio

**Option A: Local Access (Recommended for initial setup)**
```bash
cd "/Users/donnysmith/Desktop/Tiger CMS/studio"
npm run dev
```
Then visit: **http://localhost:3333**

**Option B: Remote Access (After deployment)**
Visit: **https://tigerbiosciences.sanity.studio** (if deployed)

### Step 2: Login
- Use your Sanity account credentials
- If you don't have an account, create one at https://www.sanity.io

---

## 📚 Studio Interface Overview

When you open Sanity Studio, you'll see:

```
┌─────────────────────────────────────────┐
│  Tiger BioSciences CMS                  │
├─────────────────────────────────────────┤
│  🏠 Homepage                             │
│  🧭 Navigation                           │
│  ⚙️  Site Settings                       │
│  ─────────────────────────────           │
│  📄 Pages (50+ pages)                    │
│  👥 Team Members                         │
│  💬 Testimonials                         │
│  ❓ FAQs                                  │
│  🏢 Divisions                             │
└─────────────────────────────────────────┘
```

---

## 📝 Editing Pages

### How to Edit a Page

1. **Click "📄 Pages"** in the sidebar
2. **Search or scroll** to find your page (e.g., "About", "Products")
3. **Click the page** to open the editor
4. **Make your changes** in the form fields
5. **Click "Publish"** in the bottom right

### Page Structure

Each page has:

#### **1. Basic Information**
- **Title** - Page title (appears in browser tab)
- **Slug** - URL identifier (e.g., "about" for about.html)
- **Badge** - Small label above hero title
- **Subtitle** - Hero subtitle text

#### **2. Page Sections** (Drag & Drop!)
You can add, remove, and reorder these section types:

**🎨 Hero Section**
- Title, subtitle, badge
- Background image OR gradient
- CTA buttons (up to 2)

**📦 Feature Grid**
- Section title and description
- 1-6 feature cards with icons, titles, descriptions
- Background color (white or light gray)

**📊 Stats Section**
- 2-4 statistics with numbers and labels
- Animated counters option
- Dark or light background

**💬 Testimonial Section**
- Section title
- 1-4 testimonials with quotes
- Author name, title, organization
- Author photo OR initials

**❓ FAQ Section**
- Section title
- 1-10 FAQ items
- Accordion functionality (auto-collapsing)

**🖼️ Image + Content Section**
- Title and rich text content
- Upload image OR use DNA visual
- Image position (left or right)
- CTA button

**📢 CTA Section**
- Title and description
- Up to 2 CTA buttons
- Background style (gradient or dark)

**📝 Rich Text Section**
- Free-form content editor
- Headings, paragraphs, lists
- Bold, italic, links
- Image uploads
- Background color option

**🎯 Endorsed Section**
- Grid of items (2-6)
- Each with title and description
- Perfect for benefits, values, etc.

---

## 🧭 Editing Navigation

### How to Update the Mega Menu

1. **Click "🧭 Navigation"** in sidebar
2. You'll see the complete navigation structure
3. **Edit mega menus:**
   - Update menu titles ("Our Science", "Products", "Solutions")
   - Edit column headings
   - Add/remove/reorder links
   - Update featured cards
4. **Edit direct links** (About, Contact)
5. **Update CTA button**
6. **Click "Publish"**

### Navigation Structure

```
Logo Text
├── Mega Menu 1: Our Science
│   ├── Column 1: Research Areas (5 links)
│   ├── Column 2: Innovation (5 links)
│   ├── Column 3: Quality (4 links)
│   ├── Column 4: Resources (4 links)
│   └── Featured Card (badge, title, description, CTA)
├── Mega Menu 2: Products
│   ├── 4 columns with links
│   └── Featured Card
├── Mega Menu 3: Solutions
│   ├── 4 columns with links
│   └── Featured Card
├── Direct Link: About
├── Direct Link: Contact
└── CTA Button: Get Started
```

**Important:** Changes to navigation appear on ALL pages instantly!

---

## 🖼️ Managing Images

### How to Upload Images

1. **In any section with an image field**, click the image area
2. **Click "Upload"** or drag and drop your image
3. **Add alt text** (required for accessibility)
4. **Adjust hotspot** (optional - sets focal point for cropping)
5. **Save/Publish**

### Image Guidelines

**Recommended Sizes:**
- Hero backgrounds: 2400x1200px
- Content images: 1200x800px
- Team photos: 400x400px (square)
- Testimonial photos: 200x200px (square)

**Formats:**
- JPG for photos
- PNG for graphics with transparency
- WebP for best performance (auto-converted)

**File Sizes:**
- Keep under 2MB per image
- Sanity auto-optimizes on delivery

### Using the DNA Visual

Many sections offer a toggle: **"Use DNA Visual Instead of Image"**
- Toggle ON: Shows animated DNA graphic (no upload needed)
- Toggle OFF: Upload your own image

---

## ✏️ Content Best Practices

### Writing for SEO

**Meta Titles (50-60 characters)**
```
✓ Good: "HealPack Wound Dressings - Tiger BioSciences™"
✗ Bad: "Product"
```

**Meta Descriptions (150-160 characters)**
```
✓ Good: "HealPack advanced wound dressings use CAMPs technology for chronic wound management and accelerated healing. FDA compliant and clinically proven."
✗ Bad: "Our product for wounds."
```

### Writing Hero Sections

**Titles:** Clear, compelling, 3-10 words
```
✓ "Revolutionary CAMPs Technology"
✓ "Advanced Wound Care Solutions"
✗ "Welcome to our page about products"
```

**Subtitles:** 20-40 words, explain value proposition
```
✓ "Clinically proven CAMPs technology for faster healing and better patient outcomes in chronic and complex wound management."
```

### Writing Feature Descriptions

**Each feature:** 50-100 words
- Start with benefit
- Add supporting details
- Use specific language
- Avoid jargon when possible

---

## 🔄 Publishing Workflow

### Making Changes

1. **Edit content** in Sanity Studio
2. **Preview** (if available)
3. **Click "Publish"**
4. **Wait 2-3 seconds**
5. **Refresh website** to see changes

**Changes are INSTANT** - no deployment needed!

### Scheduling Posts (Optional)

- Set "Publish At" date/time
- Content goes live automatically
- Perfect for news, announcements

---

## 🎨 Page Builder Tips

### Adding a New Section

1. In any page, scroll to **"Page Sections"**
2. Click **"+ Add item"**
3. **Choose section type** from menu
4. **Fill in the fields**
5. **Publish**

### Reordering Sections

1. **Hover** over section
2. **Click and drag** the handle (☰)
3. **Drop** in new position
4. **Publish**

### Removing a Section

1. **Click** the section
2. **Click "..."** menu
3. **Select "Remove"**
4. **Publish**

### Duplicating a Section

1. **Click** the section
2. **Click "..."** menu  
3. **Select "Duplicate"**
4. **Edit** the duplicate
5. **Publish**

---

## 📄 Managing All 50+ Pages

### Page Categories

**Core Pages (5):**
- Homepage (special - different schema)
- About, Contact, Products, Science

**Our Science Section (16 pages):**
- Wound Care, Tissue Reconstruction, Aesthetic Medicine, etc.
- Research Pipeline, Clinical Trials, Publications, etc.
- Quality Assurance, Regulatory, Manufacturing, etc.

**Products Section (15 pages):**
- HealPack, CarGraft, AlloPly, AcaPatch
- Bellafill, Aveli, Breast Solutions
- General Surgery, Orthopedic, Podiatry

**Solutions Section (16 pages):**
- Hospitals, Wound Centers, Facilities
- Training, Clinical Support, Reimbursement
- Investigator Portal, Partnerships

**Additional Pages (8):**
- Careers, Investors, Grants
- Legal, Privacy, Terms
- Tiger Way, Vertical Integration

### Finding Pages Quickly

Use the **search box** in Pages list:
- Type page name: "wound care"
- Type URL slug: "healpack"
- Type content keywords

---

## 🏠 Editing Homepage (Special)

The homepage has its own editor (not in Pages list):

1. **Click "🏠 Homepage"** in sidebar
2. Edit these sections:
   - Hero badge, title, subtitle
   - CTA buttons
   - Integration section (4 items)
   - Divisions section
3. **Publish**

**Note:** Homepage structure is fixed, but content is fully editable.

---

## 👥 Managing Team Members

1. **Click "👥 Team Members"**
2. **Click "+"** to add new team member
3. Fill in:
   - Name, role, bio
   - Photo upload
   - Credentials, LinkedIn
4. **Publish**

Team members can be displayed on About page or dedicated team page.

---

## 💬 Managing Testimonials

1. **Click "💬 Testimonials"**
2. **Click "+"** to add new testimonial
3. Fill in:
   - Quote text
   - Author name, title, organization
   - Author photo OR initials for avatar
   - Featured toggle (show on homepage)
4. **Publish**

Use testimonials in any page by adding a Testimonial Section.

---

## ❓ Managing FAQs

1. **Click "❓ FAQs"**
2. **Click "+"** to add new FAQ
3. Fill in:
   - Question
   - Answer
   - Category
   - Order number
   - Featured toggle
4. **Publish**

FAQs can be:
- Added individually to any page
- Used in FAQ section blocks
- Filtered by category

---

## ⚙️ Site Settings

### Global Site Settings

1. **Click "⚙️ Site Settings"**
2. Edit:
   - Site name and tagline
   - Contact information (address, phone, email)
   - Footer text
   - Social media links
3. **Publish**

These appear across all pages automatically.

---

## 🖼️ Media Library

### Accessing Your Media

1. **Click any image field** to see "Image library"
2. **View all uploaded images**
3. **Search by filename** or browse
4. **Reuse images** across multiple pages

### Organizing Media

- Use clear, descriptive filenames
- Always add alt text
- Delete unused images periodically
- Optimize before upload when possible

---

## 🔍 Common Tasks

### Update a Product Page

1. Go to **Pages** → Find product (e.g., "HealPack")
2. Update **hero title/subtitle**
3. Edit **feature grid** - add/remove/edit features
4. Update **FAQ section** - edit questions/answers
5. Change **images** in Image + Content sections
6. **Publish**

### Add a News Item

1. Create **News page** in Pages
2. Add sections:
   - Hero Section (title, date, author)
   - Rich Text Section (article content)
   - Image + Content Section (photos)
3. **Publish**
4. Add link to **news.html** page

### Update Navigation Links

1. **Navigation** → Expand mega menu
2. Find the column and link
3. **Edit URL or label**
4. **Publish**
5. **Refresh** any page to see change

### Change Homepage Stats

1. **Homepage** → Scroll to sections
2. Find **stats items** (currently: 15 years, 50+ products, etc.)
3. **Edit numbers and labels**
4. **Publish**

### Add New Testimonial

1. **Testimonials** → **Create new**
2. Fill in quote, author info
3. Upload author photo (or use initials)
4. Toggle **"Featured"** to show on homepage
5. **Publish**

---

## 🚨 Important Notes

### Changes Go Live Immediately
- **No deployment needed**
- Changes appear in 2-3 seconds
- May need to **refresh browser** to see updates

### Draft vs Published
- **Drafts** - Not visible on website
- **Published** - Live on website immediately
- Always click **"Publish"** to make changes live

### Deleting Content
- **Be careful** - deletion is permanent
- **Unpublish** instead if unsure
- Can restore from version history (30 days)

### Version History
- Every publish creates a version
- **View history** in document menu
- **Restore** previous versions if needed

---

## 🎓 Training Resources

### Video Tutorials (Sanity)
- Introduction to Sanity Studio: https://www.sanity.io/docs/sanity-studio
- Content Editing Basics: https://www.sanity.io/docs/editing-content
- Image Management: https://www.sanity.io/docs/image-type

### Support

**Technical Issues:**
- Email: support@tigerbiosciences.com
- Developer: [Your contact]

**Sanity Platform:**
- Help docs: https://www.sanity.io/help
- Community: https://slack.sanity.io

---

## 🔐 User Management

### Adding Team Members to CMS

1. Go to **https://www.sanity.io/manage/project/0nxq33lj**
2. **Project Settings** → **Members**
3. **Invite member** via email
4. **Assign role:**
   - **Administrator** - Full access
   - **Editor** - Can edit content
   - **Viewer** - Read-only access

### Roles Explained

**Administrator:**
- Edit all content
- Manage users
- Change project settings
- Deploy Studio

**Editor:**
- Edit all content
- Publish changes
- Upload media
- Cannot manage users

**Viewer:**
- View content
- Cannot make changes

---

## 📊 Content Types Reference

### Section Types You Can Add

| Section Type | Best For | Fields |
|--------------|----------|--------|
| Hero Section | Page top, main message | Title, subtitle, background, CTAs |
| Feature Grid | Benefits, features | 1-6 cards with icons, titles, descriptions |
| Stats Section | Numbers, achievements | 2-4 stats with labels |
| Testimonial Section | Social proof | 1-4 testimonials with photos |
| FAQ Section | Common questions | 1-10 Q&A items with accordion |
| Image + Content | Detailed explanation | Rich text + image, layout control |
| CTA Section | Action prompt | Title, description, 2 buttons |
| Rich Text Section | Long-form content | Full editor with images, formatting |
| Endorsed Section | Grid items | 2-6 items with titles, descriptions |

---

## 💡 Pro Tips

### Content Tips

1. **Use sections strategically**
   - Hero → Feature Grid → Image+Content → CTA
   - Tells a story, guides user journey

2. **Optimize images before upload**
   - Compress to reasonable file sizes
   - Crop to desired dimensions
   - Name files descriptively

3. **Write for your audience**
   - Healthcare professionals need detail
   - General audience needs clarity
   - Balance technical accuracy with readability

4. **SEO best practices**
   - Include keywords naturally in titles
   - Write compelling meta descriptions
   - Use descriptive alt text for images

### Performance Tips

1. **Don't overload pages**
   - 5-8 sections per page is ideal
   - Too many sections = slow loading

2. **Optimize images**
   - Sanity auto-optimizes, but start small
   - Use WebP when possible

3. **Test on mobile**
   - Preview pages on phone/tablet
   - Ensure readability and usability

---

## 🔧 Troubleshooting

### Content Not Showing on Website

**Check:**
1. Did you click "Publish"? (not just save)
2. Did you refresh the browser?
3. Is there a JavaScript error? (check browser console)
4. Try clearing browser cache

### Image Not Loading

**Check:**
1. Is alt text filled in?
2. Is image actually uploaded?
3. Is file size reasonable (<2MB)?
4. Try re-uploading

### Navigation Links Not Working

**Check:**
1. Is URL correct? (e.g., "about.html" not "/about")
2. Did you publish navigation changes?
3. Refresh browser

### Can't Find a Page

**Check:**
1. Use search box in Pages list
2. Check slug matches filename
3. May be in different content type

---

## 📞 Getting Help

### Before Contacting Support

1. Check this guide
2. Check Sanity documentation
3. Try in different browser
4. Clear cache and try again

### Contact Information

**Website Issues:**
- Email: support@tigerbiosciences.com
- Phone: 1-888-665-5005

**CMS Technical:**
- Developer: [Your email]
- Sanity Support: https://www.sanity.io/help

---

## 🎯 Quick Reference Card

### Most Common Tasks

| Task | Steps |
|------|-------|
| Edit page content | Pages → Select page → Edit → Publish |
| Add new section | Open page → Sections → Add item → Choose type → Fill → Publish |
| Upload image | Click image field → Upload → Add alt text → Save |
| Update navigation | Navigation → Edit links → Publish |
| Add FAQ | FAQs → Create → Fill question/answer → Publish |
| Change homepage | Homepage → Edit sections → Publish |

### Keyboard Shortcuts (in Studio)

- **Cmd/Ctrl + S** - Save (but doesn't publish!)
- **Cmd/Ctrl + P** - Publish
- **Cmd/Ctrl + K** - Quick search
- **Esc** - Close panel

---

## 🚀 Going Live Checklist

Before announcing your updated site:

- [ ] All pages reviewed and published
- [ ] Navigation tested on all pages
- [ ] All images have alt text
- [ ] Meta descriptions on all pages
- [ ] Test on mobile device
- [ ] Test all links work
- [ ] FAQ accordions work
- [ ] Stats counters animate
- [ ] Contact forms work
- [ ] Review on different browsers

---

## 📈 Ongoing Maintenance

### Weekly Tasks
- Review and update news/blog content
- Check for outdated information
- Update stats/numbers if changed
- Review testimonials

### Monthly Tasks
- Add new team members
- Update product information
- Refresh images/photos
- Review SEO performance

### Quarterly Tasks
- Content audit all pages
- Update copyright year
- Review navigation structure
- Optimize underperforming pages

---

## ✅ Success!

You now have complete control over your website content through an intuitive CMS interface. No coding required - just point, click, and publish!

**Questions?** Refer to this guide or contact support.

**Happy editing!** 🎉

---

**Document Version:** 1.0  
**Last Updated:** October 7, 2025

