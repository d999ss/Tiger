# 🎯 Sanity CMS - Complete Setup Guide

## ✅ GREAT NEWS!

You already have a Sanity project: **Tiger Biosciences** (Project ID: `0nxq33lj`)

---

## 🚀 Quick Setup (Just run these commands)

### Step 1: Initialize Studio with Your Existing Project

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS"
rm -rf studio
npx create-sanity@latest
```

**When prompted, select:**
1. ✅ **Select existing project** → Choose "Tiger Biosciences (0nxq33lj)"
2. ✅ **Dataset**: `production` (or create new one)
3. ✅ **Output path**: `./studio`
4. ✅ **Template**: `Clean project`
5. ✅ **Package manager**: `npm`

### Step 2: Copy Pre-Made Schemas

After init completes, copy the schema files:

```bash
# Copy the schemas I created for you
cp -r studio-schemas/schemaTypes/* studio/schemaTypes/
```

### Step 3: Start the Studio

```bash
cd studio
npm install
npm run dev
```

**Your Studio will open at:** http://localhost:3333

---

## 📋 What's Included

I've pre-built all your content schemas:

### 📄 **Content Types**

1. **Homepage** - All homepage content (hero, sections, etc.)
2. **Page** - Generic page content for all pages
3. **Division** - Tiger divisions (RegenTX, Tiger Wound Care, etc.)
4. **Team Member** - Staff and leadership
5. **Testimonial** - Customer/partner testimonials
6. **FAQ** - Frequently asked questions
7. **Site Settings** - Global settings (contact info, social links, etc.)

---

## 🎨 Next Steps After Studio Starts

### 1. Add Initial Content

Log into http://localhost:3333 and add:

- **Site Settings** (contact info, address, phone)
- **Homepage** content
- **Divisions** (the 6 Tiger divisions)
- **FAQs** (the 4 core capability questions)
- **Testimonials** (your integrated approach quotes)

### 2. I'll Connect Your HTML

Once you have content in Sanity, I'll:
- Create API client
- Update `index.html` to fetch from Sanity
- Add dynamic content rendering
- Keep your luxury design intact

---

## 📊 Your Sanity Project Details

- **Project Name**: Tiger Biosciences  
- **Project ID**: `0nxq33lj`
- **Dataset**: `production` (or whatever you choose)
- **API Endpoint**: `https://0nxq33lj.api.sanity.io/v2024-01-01/data/query/production`

---

## 💡 What You Can Do in Sanity

✅ **Edit Content Visually** - No code needed
✅ **Upload Images** - Drag & drop media management  
✅ **Preview Changes** - See before publishing
✅ **Version History** - Undo any mistakes
✅ **Multi-user** - Your team can collaborate
✅ **Real-time** - Changes sync instantly

---

## 🚨 Important Commands

```bash
# Start Studio locally
cd studio && npm run dev

# Deploy Studio to Sanity hosting (free)
cd studio && npm run deploy

# Check for updates
cd studio && npm run upgrade
```

---

## 📞 Need Help?

After you run the setup and see the Studio, tell me and I'll:
1. Connect your HTML pages to Sanity
2. Set up automatic content fetching
3. Add image optimization
4. Create preview functionality

**Ready to go?** Just run the commands above! 🎉


