# Sanity CMS Setup for Tiger BioSciences

## 🚀 Quick Setup (5 minutes)

Since the CLI needs interactive mode, here's how to set it up:

### Step 1: Initialize Sanity Studio

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS"
mkdir -p studio
cd studio
npx create-sanity@latest
```

**When prompted:**
1. **Project name**: `Tiger BioSciences`
2. **Use default dataset**: `production` ✅
3. **Output path**: `.` (current directory)
4. **Package manager**: `npm` ✅
5. **Template**: Choose `Clean project`

### Step 2: Install Dependencies

```bash
npm install
```

### Step 3: Start Studio (I've pre-configured everything below)

```bash
npm run dev
```

This will open: **http://localhost:3333**

---

## 📋 Pre-Configured Schema

I've created the schema files below. After Sanity initializes, these will be automatically available!

### Content Types We're Creating:

1. **Homepage Content**
2. **Page Content** (for all pages)
3. **Division/Product** 
4. **Team Member**
5. **Testimonial**
6. **FAQ**
7. **Site Settings**

---

## 🎯 Next Steps After Setup

1. Run `npm run dev` in the studio folder
2. Open http://localhost:3333
3. Start adding content through the beautiful Sanity interface
4. I'll update your HTML pages to fetch from Sanity API

---

## 🔑 Your Sanity Project Details

After setup completes, you'll get:
- **Project ID**: (save this!)
- **Dataset**: production
- **API Endpoint**: `https://[project-id].api.sanity.io/v2024-01-01/data/query/production`

---

## 💡 Benefits You'll Get

✅ **Visual Content Editor** - Edit content without touching code
✅ **Real-time Preview** - See changes instantly  
✅ **Media Management** - Upload and manage images
✅ **Version History** - Undo any changes
✅ **Multi-user Support** - Team can edit together
✅ **Free Tier** - 3 users, 10GB bandwidth, 500k API requests/month

---

## 🚨 Important Note

Run the setup command above and tell me your **Project ID** when you get it. I'll then configure everything else automatically!


