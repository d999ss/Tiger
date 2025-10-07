/**
 * Enhanced Sanity Client for Tiger BioSciences
 * Renders all page sections dynamically from Sanity CMS
 */

const SANITY_CONFIG = {
  projectId: '0nxq33lj',
  dataset: 'production',
  apiVersion: '2024-01-01',
  useCdn: true,
};

const SANITY_API_URL = `https://${SANITY_CONFIG.projectId}.api.sanity.io/v${SANITY_CONFIG.apiVersion}/data/query/${SANITY_CONFIG.dataset}`;

/**
 * Fetch data from Sanity
 */
async function fetchFromSanity(query) {
  const url = `${SANITY_API_URL}?query=${encodeURIComponent(query)}`;
  
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Sanity API error: ${response.status}`);
    }
    const data = await response.json();
    return data.result;
  } catch (error) {
    console.error('Error fetching from Sanity:', error);
    return null;
  }
}

/**
 * Build Sanity image URL
 */
function getImageUrl(imageRef, width = 1200) {
  if (!imageRef || !imageRef.asset) return '';
  
  const ref = imageRef.asset._ref || imageRef.asset;
  const [, id, dimensions, format] = ref.match(/image-([a-f0-9]+)-(\d+x\d+)-(\w+)/) || [];
  
  if (!id) return '';
  
  return `https://cdn.sanity.io/images/${SANITY_CONFIG.projectId}/${SANITY_CONFIG.dataset}/${id}-${dimensions}.${format}?w=${width}&auto=format&q=85`;
}

/**
 * Render Hero Section
 */
function renderHeroSection(section) {
  const bgClass = section.useGradient ? 'hero-gradient' : '';
  const bgImage = section.backgroundImage && !section.useGradient 
    ? `style="background-image: url('${getImageUrl(section.backgroundImage)}'); background-size: cover;"` 
    : '';
  
  const buttons = section.ctaButtons?.map(btn => {
    const btnClass = btn.style === 'primary' ? 'btn btn-primary' : 'btn btn-outline';
    return `<a href="${btn.url}" class="${btnClass}">${btn.text}</a>`;
  }).join('') || '';
  
  return `
    <section class="hero ${bgClass}" ${bgImage} role="banner" aria-label="Page hero">
      <div class="hero-content">
        ${section.badge ? `<div class="hero-badge">${section.badge}</div>` : ''}
        <h1 class="hero-title">${section.title}</h1>
        <p class="hero-subtitle">${section.subtitle}</p>
        ${buttons ? `<div class="hero-buttons">${buttons}</div>` : ''}
      </div>
    </section>
  `;
}

/**
 * Render Feature Grid Section
 */
function renderFeatureGrid(section) {
  const features = section.features?.map(feature => `
    <div class="feature-card">
      <div class="feature-icon">${feature.icon || '✓'}</div>
      <h3 class="feature-title">${feature.title}</h3>
      <p class="feature-description">${feature.description}</p>
    </div>
  `).join('') || '';
  
  const sectionClass = section.backgroundColor === 'light' ? 'section section-light' : 'section';
  
  return `
    <section class="${sectionClass}">
      <div class="section-container">
        <div class="section-header">
          ${section.sectionLabel ? `<div class="section-label">${section.sectionLabel}</div>` : ''}
          <h2 class="section-title">${section.title}</h2>
          ${section.description ? `<p class="section-description">${section.description}</p>` : ''}
        </div>
        <div class="features-grid">
          ${features}
        </div>
      </div>
    </section>
  `;
}

/**
 * Render Stats Section
 */
function renderStatsSection(section) {
  const stats = section.stats?.map(stat => {
    const isNumeric = /^\d+$/.test(stat.number);
    const dataAttr = isNumeric && stat.animated ? `data-target="${stat.number}"` : '';
    const displayNumber = isNumeric && stat.animated ? '0' : stat.number;
    
    return `
      <div class="stat-item">
        <div class="stat-number" ${dataAttr}>${displayNumber}</div>
        <div class="stat-label">${stat.label}</div>
      </div>
    `;
  }).join('') || '';
  
  return `
    <section class="stats" aria-label="Company statistics">
      <div class="stats-grid" role="list">
        ${stats}
      </div>
    </section>
  `;
}

/**
 * Render Testimonial Section
 */
function renderTestimonialSection(section) {
  const testimonials = section.testimonials?.map(t => {
    const avatarContent = t.authorImage 
      ? `<img src="${getImageUrl(t.authorImage, 200)}" alt="${t.authorName}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">` 
      : t.authorAvatar || 'TM';
    
    return `
      <div class="testimonial-card">
        <p class="testimonial-quote">"${t.quote}"</p>
        <div class="testimonial-author">
          <div class="author-avatar">${avatarContent}</div>
          <div class="author-info">
            <h5>${t.authorName}</h5>
            <p>${t.authorTitle || ''}${t.authorOrganization ? ` - ${t.authorOrganization}` : ''}</p>
          </div>
        </div>
      </div>
    `;
  }).join('') || '';
  
  return `
    <section class="testimonials">
      ${section.sectionTitle ? `
        <div class="testimonials-header">
          <h2>${section.sectionTitle}</h2>
          ${section.sectionSubtitle ? `<p>${section.sectionSubtitle}</p>` : ''}
        </div>
      ` : ''}
      <div class="testimonials-grid">
        ${testimonials}
      </div>
    </section>
  `;
}

/**
 * Render FAQ Section
 */
function renderFAQSection(section) {
  const faqs = section.faqs?.map(faq => `
    <div class="faq-item" data-faq>
      <button class="faq-question" aria-expanded="false">
        <h4>${faq.question}</h4>
        <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
        </svg>
      </button>
      <div class="faq-answer">
        <p>${faq.answer}</p>
      </div>
    </div>
  `).join('') || '';
  
  return `
    <section class="faq">
      <div class="faq-container">
        ${section.sectionTitle ? `
          <div class="faq-header">
            <h2>${section.sectionTitle}</h2>
            ${section.sectionSubtitle ? `<p>${section.sectionSubtitle}</p>` : ''}
          </div>
        ` : ''}
        ${faqs}
      </div>
    </section>
  `;
}

/**
 * Render Image + Content Section
 */
function renderImageContentSection(section) {
  // Convert portable text to HTML
  const contentHTML = section.content?.map(block => {
    if (block._type === 'block') {
      const text = block.children?.map(child => {
        let content = child.text || '';
        if (child.marks?.includes('strong')) content = `<strong>${content}</strong>`;
        if (child.marks?.includes('em')) content = `<em>${content}</em>`;
        return content;
      }).join('') || '';
      
      if (block.style === 'h3') return `<h3 style="font-size: 2rem; margin-bottom: 1.5rem;">${text}</h3>`;
      if (block.style === 'h4') return `<h4 style="font-size: 1.5rem; margin-bottom: 1rem;">${text}</h4>`;
      return `<p style="margin-bottom: 1.5rem;">${text}</p>`;
    }
    return '';
  }).join('') || '';
  
  const imageContent = section.useVisual 
    ? `<svg class="dna-visual" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="imgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#991514;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#7f1d1d;stop-opacity:1" />
          </linearGradient>
        </defs>
        <path d="M40,20 Q100,40 160,20" stroke="url(#imgGrad)" stroke-width="3" fill="none" opacity="0.8"/>
        <path d="M40,60 Q100,80 160,60" stroke="url(#imgGrad)" stroke-width="3" fill="none" opacity="0.8"/>
        <path d="M40,100 Q100,120 160,100" stroke="url(#imgGrad)" stroke-width="3" fill="none" opacity="0.8"/>
        <path d="M40,140 Q100,160 160,140" stroke="url(#imgGrad)" stroke-width="3" fill="none" opacity="0.8"/>
        <circle cx="100" cy="50" r="5" fill="#991514"/>
        <circle cx="100" cy="90" r="5" fill="#991514"/>
        <circle cx="100" cy="130" r="5" fill="#991514"/>
      </svg>`
    : section.image 
      ? `<img src="${getImageUrl(section.image, 800)}" alt="${section.image.alt || ''}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 1rem;">`
      : '';
  
  const ctaButton = section.ctaButton 
    ? `<a href="${section.ctaButton.url}" class="learn-more">
        ${section.ctaButton.text}
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </a>`
    : '';
  
  const contentSide = `<div class="image-content-text">
    <h2>${section.title}</h2>
    ${contentHTML}
    ${ctaButton}
  </div>`;
  
  const imageSide = `<div class="image-content-image">${imageContent}</div>`;
  
  const gridContent = section.imagePosition === 'left' 
    ? imageSide + contentSide 
    : contentSide + imageSide;
  
  return `
    <section class="image-content-section">
      <div class="image-content-grid">
        ${gridContent}
      </div>
    </section>
  `;
}

/**
 * Render CTA Section
 */
function renderCTASection(section) {
  const buttons = section.buttons?.map(btn => {
    const btnClass = btn.style === 'light' ? 'btn btn-primary btn-cta-light' : 'btn btn-outline btn-cta-outline';
    return `<a href="${btn.url}" class="${btnClass}">${btn.text}</a>`;
  }).join('') || '';
  
  return `
    <section class="cta">
      <div class="cta-title">${section.title}</div>
      ${section.description ? `<p class="cta-description">${section.description}</p>` : ''}
      ${buttons ? `<div class="hero-buttons">${buttons}</div>` : ''}
    </section>
  `;
}

/**
 * Render Rich Text Section
 */
function renderRichTextSection(section) {
  const contentHTML = section.content?.map(block => {
    if (block._type === 'block') {
      const text = block.children?.map(child => {
        let content = child.text || '';
        
        // Handle marks
        if (child.marks) {
          child.marks.forEach(mark => {
            if (mark === 'strong') content = `<strong>${content}</strong>`;
            if (mark === 'em') content = `<em>${content}</em>`;
          });
        }
        
        return content;
      }).join('') || '';
      
      // Handle styles
      if (block.style === 'h2') return `<h2 style="font-size: 3rem; margin-bottom: 1.5rem; color: var(--neutral-900);">${text}</h2>`;
      if (block.style === 'h3') return `<h3 style="font-size: 2rem; margin-bottom: 1rem; color: var(--neutral-900);">${text}</h3>`;
      if (block.style === 'h4') return `<h4 style="font-size: 1.5rem; margin-bottom: 0.75rem; color: var(--neutral-900);">${text}</h4>`;
      if (block.style === 'blockquote') return `<blockquote style="border-left: 3px solid var(--red-primary); padding-left: 1.5rem; font-style: italic; margin: 2rem 0;">${text}</blockquote>`;
      
      // Handle lists
      if (block.listItem === 'bullet') return `<li style="margin-left: 1.5rem;">${text}</li>`;
      if (block.listItem === 'number') return `<li style="margin-left: 1.5rem;">${text}</li>`;
      
      return `<p style="margin-bottom: 1.5rem; line-height: 1.8;">${text}</p>`;
    }
    
    if (block._type === 'image') {
      return `<img src="${getImageUrl(block, 1200)}" alt="${block.alt || ''}" style="width: 100%; border-radius: 1rem; margin: 2rem 0;" />`;
    }
    
    return '';
  }).join('') || '';
  
  const sectionClass = section.backgroundColor === 'light' ? 'section section-light' : 'section';
  
  return `
    <section class="${sectionClass}">
      <div class="section-container">
        ${section.sectionLabel || section.title ? `
          <div class="section-header">
            ${section.sectionLabel ? `<div class="section-label">${section.sectionLabel}</div>` : ''}
            ${section.title ? `<h2 class="section-title">${section.title}</h2>` : ''}
          </div>
        ` : ''}
        <div style="max-width: 75rem; margin: 0 auto;">
          ${contentHTML}
        </div>
      </div>
    </section>
  `;
}

/**
 * Render Endorsed Section
 */
function renderEndorsedSection(section) {
  const items = section.items?.map(item => `
    <div class="endorsed-item">
      <h4>${item.title}</h4>
      <p>${item.description}</p>
    </div>
  `).join('') || '';
  
  return `
    <section class="endorsed" aria-labelledby="endorsed-title">
      <div class="endorsed-container">
        ${section.label ? `<div class="endorsed-label" id="endorsed-title">${section.label}</div>` : ''}
        <div class="endorsed-grid">
          ${items}
        </div>
      </div>
    </section>
  `;
}

/**
 * Main section router
 */
function renderSection(section) {
  if (!section || !section._type) return '';
  
  switch (section._type) {
    case 'heroSection':
      return renderHeroSection(section);
    case 'featureGrid':
      return renderFeatureGrid(section);
    case 'statsSection':
      return renderStatsSection(section);
    case 'testimonialSection':
      return renderTestimonialSection(section);
    case 'faqSection':
      return renderFAQSection(section);
    case 'imageContentSection':
      return renderImageContentSection(section);
    case 'ctaSection':
      return renderCTASection(section);
    case 'richTextSection':
      return renderRichTextSection(section);
    case 'endorsedSection':
      return renderEndorsedSection(section);
    default:
      console.warn(`Unknown section type: ${section._type}`);
      return '';
  }
}

/**
 * Render entire page from Sanity
 */
async function renderPage(slug) {
  console.log(`🔄 Loading page: ${slug}`);
  
  const query = `*[_type == "page" && slug.current == "${slug}"][0]{
    title,
    badge,
    subtitle,
    sections[]{
      _type,
      _key,
      ...
    },
    seo
  }`;
  
  const page = await fetchFromSanity(query);
  
  if (!page) {
    console.warn(`Page not found in Sanity: ${slug}`);
    return;
  }
  
  // Update page meta tags
  if (page.seo?.metaTitle) {
    document.title = page.seo.metaTitle;
    document.querySelector('meta[name="title"]')?.setAttribute('content', page.seo.metaTitle);
  }
  
  if (page.seo?.metaDescription) {
    document.querySelector('meta[name="description"]')?.setAttribute('content', page.seo.metaDescription);
  }
  
  // Render sections
  if (page.sections && page.sections.length > 0) {
    const sectionsHTML = page.sections.map(section => renderSection(section)).join('');
    
    // Find main content area and inject
    const mainContent = document.querySelector('#dynamic-content');
    if (mainContent) {
      mainContent.innerHTML = sectionsHTML;
      
      // Re-initialize FAQ accordions
      initializeFAQAccordions();
      
      // Re-initialize stats counters
      initializeStatsCounters();
      
      console.log(`✅ Page loaded: ${slug} with ${page.sections.length} sections`);
    }
  }
}

/**
 * Render Navigation from Sanity
 */
async function renderNavigation() {
  console.log('🔄 Loading navigation from Sanity...');
  
  const query = `*[_type == "navigation"][0]{
    logo,
    megaMenus[]{
      title,
      columns[]{
        heading,
        links[]{label, url}
      },
      featuredCard
    },
    directLinks[]{label, url},
    ctaButton
  }`;
  
  const nav = await fetchFromSanity(query);
  
  if (!nav) {
    console.log('⚠️  Navigation not found in Sanity, using static HTML');
    return;
  }
  
  // Build mega menu HTML
  const megaMenusHTML = nav.megaMenus?.map(menu => {
    const columnsHTML = menu.columns?.map(col => `
      <div class="mega-menu-section">
        <h4>${col.heading}</h4>
        <ul class="mega-menu-links">
          ${col.links?.map(link => `<li><a href="${link.url}">${link.label}</a></li>`).join('') || ''}
        </ul>
      </div>
    `).join('') || '';
    
    const featuredHTML = menu.featuredCard ? `
      <div class="mega-menu-featured">
        <div class="featured-badge">${menu.featuredCard.badge}</div>
        <h5>${menu.featuredCard.title}</h5>
        <p>${menu.featuredCard.description}</p>
        <a href="${menu.featuredCard.ctaUrl}" class="featured-link">
          ${menu.featuredCard.ctaText}
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </a>
      </div>
    ` : '';
    
    return `
      <li class="nav-item">
        <a href="#" class="nav-link">
          ${menu.title}
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
          </svg>
        </a>
        <div class="mega-menu">
          <div class="mega-menu-content">
            <div class="mega-menu-left">
              ${columnsHTML}
            </div>
            ${featuredHTML}
          </div>
        </div>
      </li>
    `;
  }).join('') || '';
  
  const directLinksHTML = nav.directLinks?.map(link => `
    <li class="nav-item">
      <a href="${link.url}" class="nav-link">${link.label}</a>
    </li>
  `).join('') || '';
  
  const ctaButtonHTML = nav.ctaButton ? `
    <li class="nav-item">
      <a href="${nav.ctaButton.url}" class="btn-nav">${nav.ctaButton.text}</a>
    </li>
  ` : '';
  
  // Update navigation in DOM
  const navMenu = document.querySelector('.nav-menu');
  if (navMenu) {
    navMenu.innerHTML = megaMenusHTML + directLinksHTML + ctaButtonHTML;
  }
  
  const logo = document.querySelector('.logo');
  if (logo && nav.logo) {
    logo.textContent = nav.logo;
  }
  
  console.log('✅ Navigation loaded from Sanity');
}

/**
 * Initialize FAQ accordions
 */
function initializeFAQAccordions() {
  document.querySelectorAll('[data-faq]').forEach(faqItem => {
    const question = faqItem.querySelector('.faq-question');
    const answer = faqItem.querySelector('.faq-answer');
    const icon = faqItem.querySelector('.faq-icon');
    
    if (!question || !answer || !icon) return;
    
    // Set initial state
    answer.style.maxHeight = '0';
    answer.style.overflow = 'hidden';
    answer.style.transition = 'max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease';
    answer.style.opacity = '0';
    
    // Remove old listeners
    const newQuestion = question.cloneNode(true);
    question.parentNode.replaceChild(newQuestion, question);
    
    newQuestion.addEventListener('click', () => {
      const isExpanded = newQuestion.getAttribute('aria-expanded') === 'true';
      
      // Close all other FAQs
      document.querySelectorAll('[data-faq]').forEach(item => {
        if (item !== faqItem) {
          const otherQuestion = item.querySelector('.faq-question');
          const otherAnswer = item.querySelector('.faq-answer');
          const otherIcon = item.querySelector('.faq-icon');
          
          if (otherQuestion && otherAnswer && otherIcon) {
            otherQuestion.setAttribute('aria-expanded', 'false');
            otherAnswer.style.maxHeight = '0';
            otherAnswer.style.opacity = '0';
            otherIcon.style.transform = 'rotate(0deg)';
          }
        }
      });
      
      // Toggle current FAQ
      if (isExpanded) {
        newQuestion.setAttribute('aria-expanded', 'false');
        answer.style.maxHeight = '0';
        answer.style.opacity = '0';
        icon.style.transform = 'rotate(0deg)';
      } else {
        newQuestion.setAttribute('aria-expanded', 'true');
        answer.style.maxHeight = answer.scrollHeight + 'px';
        answer.style.opacity = '1';
        icon.style.transform = 'rotate(180deg)';
      }
    });
  });
}

/**
 * Initialize stats counters
 */
function initializeStatsCounters() {
  const animateCounter = (element, target, suffix = '') => {
    const duration = 2000;
    const increment = target / (duration / 16);
    let current = 0;
    
    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        element.textContent = target + suffix;
        clearInterval(timer);
      } else {
        element.textContent = Math.floor(current) + suffix;
      }
    }, 16);
  };
  
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && entry.target.textContent === '0') {
        const target = parseInt(entry.target.dataset.target);
        const suffix = target >= 100 ? '+' : '';
        animateCounter(entry.target, target, suffix);
      }
    });
  }, {threshold: 0.5});
  
  document.querySelectorAll('.stat-number[data-target]').forEach(stat => {
    statsObserver.observe(stat);
  });
}

/**
 * Get page slug from URL or filename
 */
function getPageSlug() {
  const path = window.location.pathname;
  const match = path.match(/\/([^\/]+)\.html$/);
  return match ? match[1] : 'index';
}

/**
 * Initialize page content from Sanity
 */
async function initSanityContent() {
  console.log('🚀 Initializing Sanity CMS content...');
  
  try {
    const slug = getPageSlug();
    
    // Load navigation
    await renderNavigation();
    
    // Load page content if dynamic content area exists
    if (document.querySelector('#dynamic-content')) {
      await renderPage(slug);
    }
    
    console.log('✅ Sanity content initialized!');
  } catch (error) {
    console.error('❌ Error loading Sanity content:', error);
  }
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initSanityContent);
} else {
  initSanityContent();
}

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    renderSection,
    renderPage,
    renderNavigation,
    fetchFromSanity,
  };
}

