# Vercel Deployment Guide - Tiger BioSciences
**Public Access Configuration**  
**Last Updated:** October 7, 2025

---

## ✅ PUBLIC ACCESS CONFIRMATION

Your Tiger BioSciences site is configured for **PUBLIC ACCESS** - anyone with the URL can view it without authentication.

---

## 🚀 Deployment Steps

### 1. Initial Setup (If Not Already Done)

```bash
# Install Vercel CLI (if not installed)
npm install -g vercel

# Login to Vercel
vercel login

# Deploy from project root
cd "/Users/donnysmith/Desktop/Tiger CMS"
vercel
```

### 2. First Deployment

When prompted:
- **Set up and deploy?** → Yes
- **Which scope?** → Select your account/team
- **Link to existing project?** → No (first time) or Yes (if exists)
- **What's your project's name?** → `tiger-biosciences` (or your choice)
- **In which directory is your code located?** → `./`
- **Want to override settings?** → No

### 3. Production Deployment

```bash
# Deploy to production
vercel --prod
```

---

## 🔓 Public Access Settings

### In Vercel Dashboard

1. **Go to:** https://vercel.com/dashboard
2. **Select Project:** tiger-biosciences
3. **Settings → General**
4. **Ensure these settings:**

   ✅ **Deployment Protection:** OFF (or set to "Only Preview Deployments")
   ✅ **Password Protection:** OFF
   ✅ **Vercel Authentication:** OFF
   ✅ **Public Project:** ON

### Settings to Check:

#### ⚠️ Turn OFF These Features for Public Access:
- ❌ Password Protection
- ❌ Vercel Authentication
- ❌ Trusted IPs only
- ❌ SSO protection

#### ✅ Enable These Features:
- ✅ Automatic deployments from Git
- ✅ Production domain
- ✅ HTTPS/SSL (automatic)

---

## 🌐 Domain Configuration

### Production URL
Your site will be available at:
```
https://tiger-biosciences.vercel.app
```
or your custom domain if configured.

### Custom Domain (Optional)
1. **Go to:** Project Settings → Domains
2. **Add Domain:** tigerbiosciences.com
3. **Follow DNS instructions**
4. **Wait for SSL certificate (automatic)**

---

## 📋 Vercel Configuration Breakdown

### `vercel.json` Settings

```json
{
  "public": true,              // ✅ Makes project publicly accessible
  "version": 2,                // Vercel platform version
  "buildCommand": null,        // Static site (no build needed)
  "outputDirectory": "./",     // Root directory
  "cleanUrls": true,           // Remove .html from URLs
  "trailingSlash": false      // No trailing slashes
}
```

### Routes Configuration
- **Root route:** `/` → `index.html`
- **HTML files:** Clean URLs (no .html extension needed)
- **Assets:** Long-term caching for performance

### Security Headers
- ✅ X-Content-Type-Options
- ✅ X-Frame-Options
- ✅ X-XSS-Protection
- ✅ Cache-Control

---

## 🔍 Verification Steps

### 1. Check Public Access

After deployment, test in **Incognito/Private Browser**:

```
1. Open incognito window
2. Navigate to your Vercel URL
3. Verify site loads without login
4. Test all navigation links
5. Check mobile responsiveness
```

### 2. Verify Settings in Dashboard

**Path:** Vercel Dashboard → tiger-biosciences → Settings → General

| Setting | Status |
|---------|--------|
| Deployment Protection | ❌ OFF (or Preview Only) |
| Password Protection | ❌ OFF |
| Vercel Authentication | ❌ OFF |
| Environment Variables | Private only |
| Automatic Deployments | ✅ ON |

---

## 🔐 Privacy Considerations

### What's Public:
✅ All HTML pages  
✅ All assets (CSS, JS, images)  
✅ Navigation structure  
✅ Content and text  
✅ Site performance metrics  

### What's Private:
🔒 Build logs (if configured)  
🔒 Environment variables  
🔒 Source code (unless GitHub is public)  
🔒 Vercel dashboard settings  

---

## 🚨 Common Public Access Issues

### Issue 1: "Authentication Required" Error

**Solution:**
1. Go to Project Settings → General
2. Find "Deployment Protection"
3. Set to OFF or "Only Preview Deployments"
4. Save changes
5. Redeploy

### Issue 2: 404 Errors

**Solution:**
- Verify `vercel.json` is in root directory
- Check file names match routes
- Ensure all HTML files are committed to Git

### Issue 3: Assets Not Loading

**Solution:**
- Check asset paths in HTML (relative paths)
- Verify `/assets/` folder is deployed
- Check browser console for errors

---

## 📊 Deployment Checklist

Before going live, verify:

- [ ] `vercel.json` exists in project root
- [ ] All HTML files are present
- [ ] Assets folder is included
- [ ] No authentication enabled
- [ ] No password protection
- [ ] Custom domain configured (if applicable)
- [ ] SSL certificate active (automatic)
- [ ] Test in incognito mode
- [ ] Test on mobile device
- [ ] Check all navigation links
- [ ] Verify contact forms work
- [ ] Test mega menu functionality
- [ ] Check FAQ accordions
- [ ] Verify stats counter animation
- [ ] Test all CTAs

---

## 🔄 Continuous Deployment

### Automatic Deployments

If connected to Git (GitHub):

1. **Every push to `main`** → Production deployment
2. **Every push to other branches** → Preview deployment
3. **Every pull request** → Preview deployment

### Manual Deployment

```bash
# Deploy to preview
vercel

# Deploy to production
vercel --prod

# Promote preview to production
vercel promote [deployment-url]
```

---

## 📈 Monitoring Public Access

### Analytics (Built-in Vercel)
- Page views
- Unique visitors
- Geographic distribution
- Performance metrics

### Path:** Dashboard → Analytics

---

## 🛠️ Troubleshooting Commands

```bash
# Check deployment status
vercel ls

# View deployment logs
vercel logs [deployment-url]

# Inspect project settings
vercel inspect

# Remove deployment
vercel rm [deployment-name]

# Link project to local
vercel link
```

---

## 🌍 Environment-Specific Access

### Production
- **URL:** https://tiger-biosciences.vercel.app
- **Access:** PUBLIC - Anyone can view
- **Protection:** None
- **SSL:** Enabled (automatic)

### Preview Deployments
- **URL:** https://tiger-biosciences-[hash].vercel.app
- **Access:** PUBLIC by default (can be protected)
- **Use:** Testing before production

### Development
- **URL:** localhost:3000 (or similar)
- **Access:** Local only
- **Use:** Local development

---

## 📞 Support Resources

### Vercel Documentation
- **General:** https://vercel.com/docs
- **Deployment:** https://vercel.com/docs/deployments/overview
- **Configuration:** https://vercel.com/docs/project-configuration

### Getting Help
- **Vercel Support:** support@vercel.com
- **Community:** https://github.com/vercel/vercel/discussions
- **Status:** https://vercel-status.com

---

## ✨ Best Practices

1. **Always test in incognito** before announcing URL
2. **Use preview deployments** for testing changes
3. **Monitor analytics** to track public engagement
4. **Keep vercel.json** in version control
5. **Document custom domain setup** for team
6. **Set up monitoring** for uptime
7. **Review security headers** periodically

---

## 🎯 Quick Reference

### Deployment Commands
```bash
vercel                    # Preview deployment
vercel --prod            # Production deployment
vercel domains add       # Add custom domain
vercel env pull          # Pull environment variables
```

### Important URLs
- **Dashboard:** https://vercel.com/dashboard
- **Docs:** https://vercel.com/docs
- **Status:** https://vercel-status.com

---

## ✅ Final Confirmation

Your Tiger BioSciences site is configured for **FULL PUBLIC ACCESS**:

✅ No authentication required  
✅ No password protection  
✅ No IP restrictions  
✅ Accessible worldwide  
✅ HTTPS secured  
✅ Optimized for performance  
✅ Mobile responsive  
✅ SEO friendly  

**Anyone with the URL can view your site immediately.**

---

**Document End**

For questions, contact your Vercel administrator or refer to the official documentation.

