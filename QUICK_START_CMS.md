# Quick Start - Tiger BioSciences CMS
**Get Your CMS Running in 5 Minutes**

---

## 🚀 Quick Setup (5 Steps)

### 1. Get Your Sanity Write Token

Visit: https://www.sanity.io/manage/project/0nxq33lj/api

- Click **"Add API Token"**
- Name: `Migration Token`
- Permissions: **Editor**
- **Copy the token**

### 2. Set Environment Variable

```bash
export SANITY_WRITE_TOKEN="paste-your-token-here"
```

### 3. Install Dependencies

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS"
npm install
cd studio
npm install
cd ..
```

### 4. Run Migration

```bash
node migrate-to-sanity.js
```

**Expected:** Creates 51 documents (1 navigation + 50 pages)

### 5. Start Sanity Studio

```bash
cd studio
npm run dev
```

**Access:** http://localhost:3333

---

## ✅ Verify It Works

1. Open http://localhost:3333
2. Click **"📄 Pages"**
3. Click any page (e.g., "About")
4. See sections array with content
5. Make a small edit
6. Click **"Publish"**
7. Open that page on your website
8. Refresh browser
9. See your change!

---

## 🎯 What You Can Now Do

- ✅ Edit all 50+ pages
- ✅ Upload & manage images
- ✅ Update navigation/menus
- ✅ Add/remove page sections
- ✅ Reorder sections (drag & drop)
- ✅ Instant publishing

**No coding required!**

---

## 📚 Full Documentation

See these guides for complete information:

- **`CMS_CLIENT_GUIDE.md`** - Complete client editing guide
- **`SANITY_SETUP_COMPLETE.md`** - Technical implementation details
- **`NAVIGATION_SITEMAP.md`** - Navigation structure

---

## 🆘 Troubleshooting

**"Module not found" error:**
```bash
npm install
cd studio && npm install
```

**"Token not set" error:**
```bash
export SANITY_WRITE_TOKEN="your-token"
```

**Studio won't start:**
```bash
cd studio
rm -rf node_modules
npm install
npm run dev
```

**Content not loading on website:**
- Check browser console for errors
- Verify Sanity API is accessible
- Check CORS settings in Sanity dashboard

---

## 🎉 You're All Set!

**Studio:** http://localhost:3333  
**Website:** Open any .html file  
**Guide:** Read `CMS_CLIENT_GUIDE.md`

**Questions?** Check the full documentation or contact support.

