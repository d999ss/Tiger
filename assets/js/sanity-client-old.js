/**
 * Sanity Client for Tiger BioSciences
 * Fetches content from Sanity CMS and renders it dynamically
 */

const SANITY_CONFIG = {
  projectId: '0nxq33lj',
  dataset: 'production',
  apiVersion: '2024-01-01',
  useCdn: true,
};

const SANITY_API_URL = `https://${SANITY_CONFIG.projectId}.api.sanity.io/${SANITY_CONFIG.apiVersion}/data/query/${SANITY_CONFIG.dataset}`;

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
 * Get homepage content
 */
async function getHomepage() {
  const query = `*[_type == "homepage"][0]{
    badge,
    title,
    subtitle,
    ctaPrimary,
    ctaSecondary,
    integrationTitle,
    integrationItems,
    divisionsTitle,
    divisionsSubtitle
  }`;
  
  return await fetchFromSanity(query);
}

/**
 * Get all divisions
 */
async function getDivisions() {
  const query = `*[_type == "division"] | order(order asc){
    _id,
    name,
    slug,
    tagline,
    description,
    icon,
    order
  }`;
  
  return await fetchFromSanity(query);
}

/**
 * Get featured FAQs
 */
async function getFeaturedFAQs() {
  const query = `*[_type == "faq" && featured == true] | order(order asc){
    _id,
    question,
    answer,
    category
  }`;
  
  return await fetchFromSanity(query);
}

/**
 * Get featured testimonials
 */
async function getFeaturedTestimonials() {
  const query = `*[_type == "testimonial" && featured == true] | order(order asc){
    _id,
    quote,
    authorName,
    authorTitle,
    authorAvatar
  }`;
  
  return await fetchFromSanity(query);
}

/**
 * Get site settings
 */
async function getSiteSettings() {
  const query = `*[_type == "siteSettings"][0]{
    siteName,
    tagline,
    address,
    phone,
    email,
    footerText
  }`;
  
  return await fetchFromSanity(query);
}

/**
 * Render homepage content
 */
async function renderHomepage() {
  const homepage = await getHomepage();
  if (!homepage) return;

  // Update hero badge
  const heroBadge = document.querySelector('.hero-badge');
  if (heroBadge && homepage.badge) {
    heroBadge.textContent = homepage.badge;
  }

  // Update hero title
  const heroTitle = document.querySelector('.hero-title');
  if (heroTitle && homepage.title) {
    heroTitle.textContent = homepage.title;
  }

  // Update hero subtitle
  const heroSubtitle = document.querySelector('.hero-subtitle');
  if (heroSubtitle && homepage.subtitle) {
    heroSubtitle.textContent = homepage.subtitle;
  }

  // Update CTA buttons
  if (homepage.ctaPrimary) {
    const primaryBtn = document.querySelector('.hero-buttons .btn-primary');
    if (primaryBtn) {
      primaryBtn.textContent = homepage.ctaPrimary.text;
      primaryBtn.href = homepage.ctaPrimary.link;
    }
  }

  if (homepage.ctaSecondary) {
    const secondaryBtn = document.querySelector('.hero-buttons .btn-outline');
    if (secondaryBtn) {
      secondaryBtn.textContent = homepage.ctaSecondary.text;
      secondaryBtn.href = homepage.ctaSecondary.link;
    }
  }

  // Update integration section
  if (homepage.integrationTitle) {
    const integrationLabel = document.querySelector('.endorsed-label');
    if (integrationLabel) {
      integrationLabel.textContent = homepage.integrationTitle;
    }
  }

  // Update integration items
  if (homepage.integrationItems && homepage.integrationItems.length > 0) {
    const integrationItems = document.querySelectorAll('.endorsed-item');
    homepage.integrationItems.forEach((item, index) => {
      if (integrationItems[index]) {
        const title = integrationItems[index].querySelector('h4');
        const desc = integrationItems[index].querySelector('p');
        if (title) title.textContent = item.title;
        if (desc) desc.textContent = item.description;
      }
    });
  }

  // Update divisions section
  if (homepage.divisionsTitle) {
    const divisionsTitle = document.querySelector('.section-title');
    if (divisionsTitle) {
      divisionsTitle.textContent = homepage.divisionsTitle;
    }
  }

  if (homepage.divisionsSubtitle) {
    const divisionsDesc = document.querySelector('.section-description');
    if (divisionsDesc) {
      divisionsDesc.textContent = homepage.divisionsSubtitle;
    }
  }
}

/**
 * Render divisions
 */
async function renderDivisions() {
  const divisions = await getDivisions();
  if (!divisions || divisions.length === 0) return;

  const featureCards = document.querySelectorAll('.feature-card');
  
  divisions.forEach((division, index) => {
    if (featureCards[index]) {
      const icon = featureCards[index].querySelector('.feature-icon');
      const title = featureCards[index].querySelector('.feature-title');
      const desc = featureCards[index].querySelector('.feature-description');
      
      if (icon && division.icon) icon.textContent = division.icon;
      if (title && division.name) title.textContent = division.name;
      if (desc && division.description) desc.textContent = division.description;
    }
  });
}

/**
 * Render FAQs
 */
async function renderFAQs() {
  const faqs = await getFeaturedFAQs();
  if (!faqs || faqs.length === 0) return;

  const faqItems = document.querySelectorAll('.faq-item');
  
  faqs.forEach((faq, index) => {
    if (faqItems[index]) {
      const question = faqItems[index].querySelector('h4');
      const answer = faqItems[index].querySelector('p');
      
      if (question) question.textContent = faq.question;
      if (answer) answer.textContent = faq.answer;
    }
  });
}

/**
 * Render testimonials
 */
async function renderTestimonials() {
  const testimonials = await getFeaturedTestimonials();
  if (!testimonials || testimonials.length === 0) return;

  const testimonialCards = document.querySelectorAll('.testimonial-card');
  
  testimonials.forEach((testimonial, index) => {
    if (testimonialCards[index]) {
      const quote = testimonialCards[index].querySelector('.testimonial-quote');
      const avatar = testimonialCards[index].querySelector('.author-avatar');
      const name = testimonialCards[index].querySelector('.author-info h5');
      const title = testimonialCards[index].querySelector('.author-info p');
      
      if (quote) quote.textContent = `"${testimonial.quote}"`;
      if (avatar && testimonial.authorAvatar) avatar.textContent = testimonial.authorAvatar;
      if (name) name.textContent = testimonial.authorName;
      if (title) title.textContent = testimonial.authorTitle;
    }
  });
}

/**
 * Render site settings
 */
async function renderSiteSettings() {
  const settings = await getSiteSettings();
  if (!settings) return;

  // Update announcement bar
  if (settings.address && settings.phone) {
    const announcement = document.querySelector('.announcement');
    if (announcement) {
      const addressText = `${settings.address.street}, ${settings.address.city}, ${settings.address.state} ${settings.address.zip}`;
      announcement.innerHTML = `${addressText} <a href="tel:${settings.phone.replace(/[^0-9+]/g, '')}">${settings.phone}</a>`;
    }
  }

  // Update footer
  if (settings.footerText) {
    const footerBottom = document.querySelector('.footer-bottom p');
    if (footerBottom) {
      footerBottom.textContent = settings.footerText;
    }
  }
}

/**
 * Initialize Sanity content
 */
async function initSanityContent() {
  console.log('🚀 Loading content from Sanity CMS...');
  
  try {
    await Promise.all([
      renderHomepage(),
      renderDivisions(),
      renderFAQs(),
      renderTestimonials(),
      renderSiteSettings()
    ]);
    
    console.log('✅ Content loaded from Sanity!');
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
