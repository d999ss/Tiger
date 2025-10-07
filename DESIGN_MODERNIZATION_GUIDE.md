# Tiger CMS Design Modernization Guide
## Inspired by for:human™ Webflow Template

> Learn how to transform your Tiger CMS websites with modern, human-centered design principles from the award-winning [for:human template](https://for-human-template.webflow.io/).

---

## 🎨 Core Design Principles from for:human™

### 1. **Minimalist & Clean**
- Generous white space
- Focused content hierarchy
- Clear visual breathing room
- "Less is more" philosophy

### 2. **Human-Centered**
- Warm, approachable typography
- Authentic imagery (not stock photos)
- Story-driven content
- Emotional connection focus

### 3. **Modern & Responsive**
- Mobile-first design
- Smooth animations
- Interactive elements
- Fast-loading pages

### 4. **Professional Polish**
- Consistent spacing system
- Cohesive color palette
- High-quality visuals
- Attention to micro-details

---

## 🔍 Key Design Elements to Adopt

### Typography

**for:human uses:**
- Large, bold headlines (60-120px)
- Clean sans-serif fonts
- Generous line-height (1.4-1.6)
- Limited font weights (2-3 max)

**Apply to Tiger CMS:**
```css
/* Modern Typography System */
:root {
  --font-primary: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-heading: "Inter", "SF Pro Display", sans-serif;
  
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px */
  --text-lg: 1.125rem;   /* 18px */
  --text-xl: 1.25rem;    /* 20px */
  --text-2xl: 1.5rem;    /* 24px */
  --text-3xl: 1.875rem;  /* 30px */
  --text-4xl: 2.25rem;   /* 36px */
  --text-5xl: 3rem;      /* 48px */
  --text-6xl: 3.75rem;   /* 60px */
  --text-7xl: 4.5rem;    /* 72px */
}

body {
  font-family: var(--font-primary);
  font-size: var(--text-base);
  line-height: 1.6;
  color: #1a1a1a;
}

h1 {
  font-family: var(--font-heading);
  font-size: var(--text-6xl);
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -0.02em;
  margin-bottom: 1.5rem;
}

h2 {
  font-size: var(--text-4xl);
  font-weight: 600;
  line-height: 1.2;
  margin-bottom: 1.25rem;
}

h3 {
  font-size: var(--text-2xl);
  font-weight: 500;
  line-height: 1.3;
}

p {
  font-size: var(--text-lg);
  line-height: 1.7;
  color: #4a5568;
}
```

### Color Palette

**for:human uses:**
- Neutral base (blacks, grays, whites)
- One accent color (subtle, not overwhelming)
- High contrast for accessibility
- Muted, sophisticated tones

**Tiger CMS Modern Palette:**
```css
:root {
  /* Neutrals - Primary */
  --color-black: #0a0a0a;
  --color-gray-900: #1a1a1a;
  --color-gray-800: #2d3748;
  --color-gray-700: #4a5568;
  --color-gray-600: #718096;
  --color-gray-500: #a0aec0;
  --color-gray-400: #cbd5e0;
  --color-gray-300: #e2e8f0;
  --color-gray-200: #edf2f7;
  --color-gray-100: #f7fafc;
  --color-white: #ffffff;
  
  /* Accent - Choose one per brand */
  --color-accent-primary: #2563eb;   /* Medical blue */
  --color-accent-hover: #1d4ed8;
  --color-accent-light: #dbeafe;
  
  /* Semantic Colors */
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-error: #ef4444;
  
  /* Background */
  --bg-primary: var(--color-white);
  --bg-secondary: var(--color-gray-100);
  --bg-tertiary: var(--color-gray-200);
  
  /* Text */
  --text-primary: var(--color-gray-900);
  --text-secondary: var(--color-gray-700);
  --text-tertiary: var(--color-gray-600);
}
```

### Spacing System

**for:human uses:**
- Consistent 8px base unit
- Generous padding (80-120px sections)
- Wide containers (1200-1400px max)

**Apply to Tiger CMS:**
```css
:root {
  /* Spacing Scale (8px base) */
  --space-1: 0.5rem;   /* 8px */
  --space-2: 1rem;     /* 16px */
  --space-3: 1.5rem;   /* 24px */
  --space-4: 2rem;     /* 32px */
  --space-5: 2.5rem;   /* 40px */
  --space-6: 3rem;     /* 48px */
  --space-8: 4rem;     /* 64px */
  --space-10: 5rem;    /* 80px */
  --space-12: 6rem;    /* 96px */
  --space-16: 8rem;    /* 128px */
  --space-20: 10rem;   /* 160px */
  
  /* Container */
  --container-sm: 640px;
  --container-md: 768px;
  --container-lg: 1024px;
  --container-xl: 1280px;
  --container-2xl: 1400px;
}

.container {
  max-width: var(--container-xl);
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-4);
  padding-right: var(--space-4);
}

section {
  padding-top: var(--space-16);
  padding-bottom: var(--space-16);
}

@media (max-width: 768px) {
  section {
    padding-top: var(--space-10);
    padding-bottom: var(--space-10);
  }
}
```

---

## 🏗️ Layout Patterns from for:human

### 1. Hero Section

**for:human style:**
- Full viewport height
- Centered content
- Large headline + subtext
- Single clear CTA
- Minimal background

**Tiger CMS Implementation:**
```html
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-label">Medical Innovation</p>
      <h1 class="hero-title">Elevate Your Practice with Advanced Solutions</h1>
      <p class="hero-description">
        Cutting-edge medical technology designed for better patient outcomes
      </p>
      <div class="hero-actions">
        <a href="#" class="btn btn-primary">Learn More</a>
        <a href="#" class="btn btn-secondary">View Products</a>
      </div>
    </div>
  </div>
</section>

<style>
.hero {
  min-height: 90vh;
  display: flex;
  align-items: center;
  background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
}

.hero-content {
  max-width: 800px;
  text-align: center;
  margin: 0 auto;
}

.hero-label {
  font-size: var(--text-sm);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-accent-primary);
  font-weight: 600;
  margin-bottom: var(--space-2);
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: var(--space-4);
  letter-spacing: -0.02em;
}

.hero-description {
  font-size: var(--text-xl);
  line-height: 1.6;
  color: var(--text-secondary);
  margin-bottom: var(--space-6);
}

.hero-actions {
  display: flex;
  gap: var(--space-3);
  justify-content: center;
  flex-wrap: wrap;
}
</style>
```

### 2. Feature Grid

**for:human style:**
- 2-3 column grid
- Icon/image + title + description
- Equal height cards
- Subtle hover effects

```html
<section class="features">
  <div class="container">
    <div class="section-header">
      <h2>Why Choose Our Solutions</h2>
      <p>Industry-leading technology backed by clinical excellence</p>
    </div>
    
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon">
          <svg><!-- icon --></svg>
        </div>
        <h3>Clinically Proven</h3>
        <p>Backed by extensive clinical trials and peer-reviewed research</p>
      </div>
      
      <div class="feature-card">
        <div class="feature-icon">
          <svg><!-- icon --></svg>
        </div>
        <h3>Patient-Centered</h3>
        <p>Designed with patient comfort and outcomes as the priority</p>
      </div>
      
      <div class="feature-card">
        <div class="feature-icon">
          <svg><!-- icon --></svg>
        </div>
        <h3>Comprehensive Support</h3>
        <p>24/7 technical support and training resources</p>
      </div>
    </div>
  </div>
</section>

<style>
.features {
  padding: var(--space-16) 0;
  background: var(--bg-primary);
}

.section-header {
  text-align: center;
  max-width: 700px;
  margin: 0 auto var(--space-12);
}

.section-header h2 {
  margin-bottom: var(--space-3);
}

.section-header p {
  font-size: var(--text-xl);
  color: var(--text-secondary);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-6);
}

.feature-card {
  padding: var(--space-6);
  border-radius: 12px;
  background: var(--bg-secondary);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.08);
}

.feature-icon {
  width: 48px;
  height: 48px;
  margin-bottom: var(--space-4);
  color: var(--color-accent-primary);
}

.feature-card h3 {
  margin-bottom: var(--space-2);
  font-size: var(--text-2xl);
}

.feature-card p {
  color: var(--text-secondary);
  line-height: 1.7;
}
</style>
```

### 3. Content Sections

**for:human style:**
- Image + text side-by-side
- Alternating layouts
- Large, high-quality images
- Ample white space

```html
<section class="content-section">
  <div class="container">
    <div class="content-grid">
      <div class="content-image">
        <img src="medical-device.jpg" alt="Advanced medical device">
      </div>
      <div class="content-text">
        <h2>Precision Engineering for Medical Excellence</h2>
        <p>
          Our devices combine cutting-edge technology with intuitive design,
          ensuring optimal performance in critical moments.
        </p>
        <ul class="feature-list">
          <li>FDA-approved and clinically validated</li>
          <li>Intuitive user interface</li>
          <li>Real-time monitoring capabilities</li>
          <li>Seamless integration with existing systems</li>
        </ul>
        <a href="#" class="btn btn-primary">Learn More</a>
      </div>
    </div>
  </div>
</section>

<style>
.content-section {
  padding: var(--space-16) 0;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-10);
  align-items: center;
}

.content-image img {
  width: 100%;
  height: auto;
  border-radius: 16px;
  box-shadow: 0 25px 50px rgba(0,0,0,0.12);
}

.content-text h2 {
  margin-bottom: var(--space-4);
}

.content-text p {
  margin-bottom: var(--space-4);
  font-size: var(--text-lg);
  line-height: 1.7;
}

.feature-list {
  list-style: none;
  padding: 0;
  margin: var(--space-6) 0;
}

.feature-list li {
  padding-left: var(--space-6);
  margin-bottom: var(--space-2);
  position: relative;
  color: var(--text-secondary);
}

.feature-list li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: var(--color-success);
  font-weight: bold;
}

@media (max-width: 768px) {
  .content-grid {
    grid-template-columns: 1fr;
    gap: var(--space-6);
  }
}
</style>
```

---

## 🎯 Button Styles (for:human inspired)

```css
/* Modern Button System */
.btn {
  display: inline-block;
  padding: 1rem 2rem;
  font-size: var(--text-base);
  font-weight: 500;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.3s ease;
  cursor: pointer;
  border: none;
  font-family: inherit;
}

.btn-primary {
  background: var(--color-gray-900);
  color: var(--color-white);
}

.btn-primary:hover {
  background: var(--color-gray-800);
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

.btn-secondary {
  background: transparent;
  color: var(--color-gray-900);
  border: 2px solid var(--color-gray-900);
}

.btn-secondary:hover {
  background: var(--color-gray-900);
  color: var(--color-white);
}

.btn-large {
  padding: 1.25rem 2.5rem;
  font-size: var(--text-lg);
}

.btn-small {
  padding: 0.75rem 1.5rem;
  font-size: var(--text-sm);
}
```

---

## 🔄 Animation & Interactions

**for:human uses subtle, purposeful animations:**

```css
/* Smooth Scroll */
html {
  scroll-behavior: smooth;
}

/* Fade In on Scroll */
.fade-in {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Card Hover Effects */
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.12);
}

/* Link Underline Effect */
.link-underline {
  position: relative;
  text-decoration: none;
}

.link-underline::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: currentColor;
  transition: width 0.3s ease;
}

.link-underline:hover::after {
  width: 100%;
}
```

**JavaScript for scroll animations:**
```javascript
// Fade in elements on scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

document.querySelectorAll('.fade-in').forEach(el => {
  observer.observe(el);
});
```

---

## 📱 Mobile-First Responsive Design

**for:human prioritizes mobile:**

```css
/* Mobile-First Approach */

/* Base styles (mobile) */
.section {
  padding: var(--space-10) var(--space-4);
}

.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
}

h1 {
  font-size: var(--text-4xl);
}

/* Tablet (768px+) */
@media (min-width: 768px) {
  .section {
    padding: var(--space-12) var(--space-6);
  }
  
  .grid {
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-6);
  }
  
  h1 {
    font-size: var(--text-5xl);
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .section {
    padding: var(--space-16) var(--space-8);
  }
  
  .grid {
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-8);
  }
  
  h1 {
    font-size: var(--text-6xl);
  }
}

/* Large Desktop (1280px+) */
@media (min-width: 1280px) {
  .section {
    padding: var(--space-20) 0;
  }
  
  h1 {
    font-size: var(--text-7xl);
  }
}
```

---

## 🎨 Complete Modern CSS Framework

Save this as `modern-tiger.css` and include in your Tiger CMS sites:

```css
/* ==========================================================================
   MODERN TIGER CMS FRAMEWORK
   Inspired by for:human™ Webflow Template
   ========================================================================== */

/* CSS Reset & Base */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  /* Typography */
  --font-primary: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-heading: "Inter", "SF Pro Display", sans-serif;
  
  /* Colors */
  --color-black: #0a0a0a;
  --color-gray-900: #1a1a1a;
  --color-gray-700: #4a5568;
  --color-gray-500: #a0aec0;
  --color-gray-300: #e2e8f0;
  --color-gray-100: #f7fafc;
  --color-white: #ffffff;
  --color-accent: #2563eb;
  
  /* Spacing */
  --space-1: 0.5rem;
  --space-2: 1rem;
  --space-3: 1.5rem;
  --space-4: 2rem;
  --space-6: 3rem;
  --space-8: 4rem;
  --space-10: 5rem;
  --space-12: 6rem;
  --space-16: 8rem;
  
  /* Typography Scale */
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;
  --text-6xl: 3.75rem;
  
  /* Layout */
  --container-max: 1280px;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-primary);
  font-size: var(--text-base);
  line-height: 1.6;
  color: var(--color-gray-900);
  background: var(--color-white);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.02em;
  color: var(--color-gray-900);
  margin-bottom: 1rem;
}

h1 { font-size: var(--text-6xl); }
h2 { font-size: var(--text-4xl); }
h3 { font-size: var(--text-2xl); }

p {
  margin-bottom: 1rem;
  color: var(--color-gray-700);
}

a {
  color: var(--color-accent);
  text-decoration: none;
  transition: color 0.2s ease;
}

a:hover {
  color: var(--color-gray-900);
}

/* Layout */
.container {
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--space-4);
}

.section {
  padding: var(--space-16) 0;
}

.grid {
  display: grid;
  gap: var(--space-6);
}

.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }

/* Buttons */
.btn {
  display: inline-block;
  padding: 1rem 2rem;
  font-size: var(--text-base);
  font-weight: 500;
  border-radius: var(--radius-md);
  transition: all 0.3s ease;
  cursor: pointer;
  border: none;
  text-align: center;
}

.btn-primary {
  background: var(--color-gray-900);
  color: var(--color-white);
}

.btn-primary:hover {
  background: var(--color-gray-700);
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

/* Cards */
.card {
  background: var(--color-white);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.08);
}

/* Responsive */
@media (max-width: 768px) {
  :root {
    --text-6xl: 2.5rem;
    --text-4xl: 1.875rem;
    --space-16: 5rem;
  }
  
  .grid-2, .grid-3, .grid-4 {
    grid-template-columns: 1fr;
  }
}
```

---

## 🚀 Quick Start Implementation

### Step 1: Add to Existing Tiger Sites

Add this to the `<head>` of each Tiger CMS HTML file:

```html
<link rel="stylesheet" href="assets/css/modern-tiger.css">
```

### Step 2: Update Hero Section

Replace existing hero with modern version:

```html
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <p class="hero-label">Medical Excellence</p>
      <h1>Transform Patient Care</h1>
      <p class="hero-description">
        Advanced medical solutions designed for better outcomes
      </p>
      <div class="hero-actions">
        <a href="#products" class="btn btn-primary">Explore Products</a>
        <a href="#contact" class="btn btn-secondary">Contact Us</a>
      </div>
    </div>
  </div>
</section>
```

### Step 3: Modernize Sections

Update existing sections with new classes:

```html
<section class="section">
  <div class="container">
    <div class="section-header">
      <h2>Our Solutions</h2>
      <p>Industry-leading medical technology</p>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <!-- content -->
      </div>
    </div>
  </div>
</section>
```

---

## 📊 Before & After Comparison

### Old Style (Current Tiger Sites):
- ❌ Dense layouts with little white space
- ❌ Small, hard-to-read text
- ❌ Inconsistent spacing
- ❌ Stock imagery
- ❌ Basic, dated buttons
- ❌ No hover effects
- ❌ Limited mobile optimization

### New Style (for:human inspired):
- ✅ Generous white space and breathing room
- ✅ Large, readable typography
- ✅ Consistent 8px spacing system
- ✅ High-quality, authentic imagery
- ✅ Modern, polished buttons
- ✅ Smooth animations and interactions
- ✅ Mobile-first responsive design

---

## 🎓 Learn More

**Key Resources:**
- [for:human Template](https://for-human-template.webflow.io/) - Original inspiration
- [Webflow University](https://university.webflow.com/) - Design education
- [Modern CSS](https://moderncss.dev/) - CSS best practices

---

## 📝 Action Items

### Immediate (This Week):
1. [ ] Add `modern-tiger.css` to all Tiger sites
2. [ ] Update hero sections with new markup
3. [ ] Implement button styles
4. [ ] Test mobile responsiveness

### Short-term (This Month):
1. [ ] Replace stock photos with authentic imagery
2. [ ] Implement scroll animations
3. [ ] Update all section layouts
4. [ ] Add hover effects to cards

### Long-term (This Quarter):
1. [ ] Complete redesign of all 11 sites
2. [ ] Professional photography shoot
3. [ ] Performance optimization
4. [ ] A/B testing new designs

---

**Remember:** Great design is about more than aesthetics—it's about creating an intuitive, enjoyable experience that builds trust with your audience.

🐅 **Let's modernize Tiger CMS!**




