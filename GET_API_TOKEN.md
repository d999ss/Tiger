# 🔑 Get Your Sanity API Token

## Step-by-Step Instructions

### 1. Open Sanity Token Page
**Click this link:** https://www.sanity.io/manage/personal/tokens

### 2. Create a New Token
1. Click **"Add API Token"** button
2. **Name**: `Tiger CMS Import`
3. **Permissions**: Select **"Editor"** (allows write access)
4. Click **"Add Token"**

### 3. Copy the Token
⚠️ **IMPORTANT**: Copy the token immediately - you won't see it again!

It looks like: `skAbCdEfGhIjKlMnOpQrStUvWxYz1234567890`

### 4. Run the Import

Open Terminal and run:

```bash
cd "/Users/donnysmith/Desktop/Tiger CMS"

# Set the token (paste your token after the =)
export SANITY_TOKEN="paste-your-token-here"

# Run the import
node import-content-to-sanity.js
```

### 5. Verify Import

After import completes:
1. Open: http://localhost:3333
2. You should see all your content:
   - Homepage
   - Divisions (6)
   - FAQs (4)
   - Testimonials (2)
   - Site Settings

---

## 🎯 Quick Copy-Paste Commands

```bash
# 1. Navigate to project
cd "/Users/donnysmith/Desktop/Tiger CMS"

# 2. Set your token (REPLACE WITH YOUR ACTUAL TOKEN)
export SANITY_TOKEN="your-actual-token-here"

# 3. Import content
node import-content-to-sanity.js

# 4. Open Studio to verify
open http://localhost:3333
```

---

## ✅ What Happens After Import

Once content is imported, you'll see in Sanity Studio:
- ✅ **Homepage** - Complete hero section and CTAs
- ✅ **6 Divisions** - RegenTX, Wound Care, Aesthetics, etc.
- ✅ **4 FAQs** - All your core capabilities
- ✅ **2 Testimonials** - Processing & R&D quotes
- ✅ **Site Settings** - Address, phone, footer

Then I'll connect your HTML pages to pull from Sanity!

---

**Ready?** Get your token from the link above and let's import! 🚀

