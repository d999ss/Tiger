#!/usr/bin/env node

/**
 * Import existing Tiger BioSciences content into Sanity CMS
 * This script extracts content from your HTML files and imports it to Sanity
 */

const fs = require('fs');
const path = require('path');
const { createClient } = require('@sanity/client');

// Sanity client configuration
const client = createClient({
  projectId: '0nxq33lj',
  dataset: 'production',
  useCdn: false,
  apiVersion: '2024-01-01',
  token: process.env.SANITY_TOKEN || '', // You'll need to add this
});

// Extract text content from HTML (simple parser)
function extractTextFromHTML(html) {
  return html
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
    .replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

// Parse homepage content from index.html
function parseHomepage() {
  const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
  
  // Extract hero content
  const badgeMatch = html.match(/<div class="hero-badge">([^<]+)<\/div>/);
  const titleMatch = html.match(/<h1 class="hero-title">([^<]+)<\/h1>/);
  const subtitleMatch = html.match(/<p class="hero-subtitle">([^<]+)<\/p>/);
  
  return {
    _type: 'homepage',
    _id: 'homepage',
    badge: badgeMatch ? badgeMatch[1] : 'The First of Its Kind',
    title: titleMatch ? titleMatch[1] : 'Tiger BioSciences',
    subtitle: subtitleMatch ? extractTextFromHTML(subtitleMatch[1]) : '',
    ctaPrimary: {
      text: 'Let\'s Get Together',
      link: 'contact.html'
    },
    ctaSecondary: {
      text: 'Our Story',
      link: 'about.html'
    },
    integrationTitle: 'The Tiger Way: The Power of Vertical Integration',
    integrationItems: [
      {
        title: 'Tissue Recovery',
        description: 'Complete oversight from donation to processing facilities'
      },
      {
        title: 'Tissue Processing',
        description: 'Precision and accountability under one roof'
      },
      {
        title: 'R&D Innovation',
        description: 'Redefining CAMPs and medical device development'
      },
      {
        title: 'Distribution',
        description: 'Fast, precise, and reliable nationwide delivery'
      }
    ],
    divisionsTitle: 'Comprehensive solutions across the healthcare spectrum',
    divisionsSubtitle: 'Our distinct advantage lies in our fully integrated approach—we oversee every stage of our products, from donor screening and tissue collection to research and development, manufacturing, and distribution.'
  };
}

// Parse divisions from homepage
function parseDivisions() {
  return [
    {
      _type: 'division',
      _id: 'div-regentx',
      name: 'RegenTX Division',
      slug: { _type: 'slug', current: 'regentx' },
      tagline: 'Tissue Science Redefined',
      description: 'RegenTX leads in tissue processing and CAMP-based innovation with rigorous protocols and advanced biotech ensuring exceptional tissue quality and consistency.',
      icon: '01',
      order: 1
    },
    {
      _type: 'division',
      _id: 'div-wound-care',
      name: 'Tiger Wound Care',
      slug: { _type: 'slug', current: 'wound-care' },
      tagline: 'Advanced CAMP Solutions for Complex Wounds',
      description: 'Providing Cellular, Acellular, and Matrix-like Products (CAMPs) tailored for chronic and hard-to-treat wounds with clinically validated results.',
      icon: '02',
      order: 2
    },
    {
      _type: 'division',
      _id: 'div-aesthetics',
      name: 'Tiger Aesthetics',
      slug: { _type: 'slug', current: 'aesthetics' },
      tagline: 'Shaping the Future of Aesthetics',
      description: 'Delivering cutting-edge solutions across reconstructive, cosmetic, and regenerative domains with advanced CAMP technologies.',
      icon: '03',
      order: 3
    },
    {
      _type: 'division',
      _id: 'div-international',
      name: 'Tiger International',
      slug: { _type: 'slug', current: 'international' },
      tagline: 'Global Access to Advanced Cell & Tissue Technologies',
      description: 'Enabling worldwide distribution of cutting-edge cell and tissue products with a focus on regulatory excellence.',
      icon: '04',
      order: 4
    },
    {
      _type: 'division',
      _id: 'div-production',
      name: 'Production & Services',
      slug: { _type: 'slug', current: 'production' },
      tagline: 'Medical Device Engineering for Tiger Innovation',
      description: 'In-house expertise covers concept, prototyping, validation, and manufacturing with precision and regulatory compliance.',
      icon: '05',
      order: 5
    },
    {
      _type: 'division',
      _id: 'div-integration',
      name: 'Vertical Integration',
      slug: { _type: 'slug', current: 'vertical-integration' },
      tagline: 'Complete Quality Control',
      description: 'Our comprehensive model ensures unparalleled quality, accountability, and confidence for both clinicians and patients through complete oversight of every stage.',
      icon: '06',
      order: 6
    }
  ];
}

// Parse FAQs from homepage
function parseFAQs() {
  return [
    {
      _type: 'faq',
      _id: 'faq-camps',
      question: 'What are Cellular, Acellular, and Matrix-like Products (CAMPs)?',
      answer: 'CAMPs are advanced biomaterial solutions that support tissue regeneration and wound healing. Our CAMP-based innovations leverage rigorous protocols and advanced biotech to ensure exceptional tissue quality and consistency for clinical applications.',
      category: 'camps',
      featured: true,
      order: 1
    },
    {
      _type: 'faq',
      _id: 'faq-integration',
      question: 'What makes vertical integration important?',
      answer: 'Our fully integrated approach means we oversee every stage—from donor screening and tissue collection to R&D, manufacturing, and distribution. This comprehensive model ensures unparalleled quality, accountability, and confidence for both clinicians and patients.',
      category: 'general',
      featured: true,
      order: 2
    },
    {
      _type: 'faq',
      _id: 'faq-quality',
      question: 'How do you ensure product quality?',
      answer: 'Every donor is carefully screened, and every tissue is handled with respect and precision under rigorous ethical, safety, and regulatory standards. Our processing pipeline is built on precision and accountability, with all work managed under one roof.',
      category: 'quality',
      featured: true,
      order: 3
    },
    {
      _type: 'faq',
      _id: 'faq-access',
      question: 'How can I access Tiger BioSciences products?',
      answer: 'Experience fast, precise, and reliable distribution through our advanced nationwide network. Contact us at 1-888-665-5005 or visit our contact page to learn more about accessing our products and solutions.',
      category: 'ordering',
      featured: true,
      order: 4
    }
  ];
}

// Parse testimonials from homepage
function parseTestimonials() {
  return [
    {
      _type: 'testimonial',
      _id: 'test-tissue-processing',
      quote: 'Our processing pipeline is built on precision and accountability. By managing all tissue processing under one roof, we ensure careful preparation, rigorous cleansing, and controlled preservation of every tissue material—creating dependable products for clinicians who count on us.',
      authorName: 'Tissue Processing',
      authorTitle: 'Precision Manufacturing Excellence',
      authorAvatar: 'TP',
      featured: true,
      order: 1
    },
    {
      _type: 'testimonial',
      _id: 'test-rd',
      quote: 'Tiger BioSciences is redefining how CAMPs and medical devices are developed and optimized. Our multidisciplinary research teams explore innovative materials, tissue models, and processing techniques—pushing boundaries to develop next-generation solutions.',
      authorName: 'Research & Development',
      authorTitle: 'Innovation and Discovery',
      authorAvatar: 'RD',
      featured: true,
      order: 2
    }
  ];
}

// Parse site settings
function parseSiteSettings() {
  return {
    _type: 'siteSettings',
    _id: 'siteSettings',
    siteName: 'Tiger BioSciences™',
    tagline: 'Elevate healthcare with a human touch',
    address: {
      street: '555 E North Ln, Ste 5000, Bldg D',
      city: 'Conshohocken',
      state: 'PA',
      zip: '19428'
    },
    phone: '(+1) 888 665 5005',
    footerText: '© 2025 Copyright Tiger BioSciences. Realized by Cloud54.'
  };
}

// Main import function
async function importContent() {
  console.log('🚀 Starting content import to Sanity...\n');

  try {
    // Check if we have a token
    if (!process.env.SANITY_TOKEN) {
      console.log('⚠️  SANITY_TOKEN environment variable not set.');
      console.log('📝 To import content, you need a write token from:');
      console.log('   https://www.sanity.io/manage/personal/tokens\n');
      console.log('Then run:');
      console.log('   export SANITY_TOKEN="your-token-here"');
      console.log('   node import-content-to-sanity.js\n');
      
      // Still print what would be imported
      console.log('📋 Content ready to import:\n');
      
      const homepage = parseHomepage();
      const divisions = parseDivisions();
      const faqs = parseFAQs();
      const testimonials = parseTestimonials();
      const settings = parseSiteSettings();
      
      console.log(`✅ Homepage: ${homepage.title}`);
      console.log(`✅ Divisions: ${divisions.length} items`);
      console.log(`✅ FAQs: ${faqs.length} items`);
      console.log(`✅ Testimonials: ${testimonials.length} items`);
      console.log(`✅ Site Settings: ${settings.siteName}\n`);
      
      // Save to JSON file for manual import
      const allContent = {
        homepage,
        divisions,
        faqs,
        testimonials,
        settings
      };
      
      fs.writeFileSync('sanity-content-export.json', JSON.stringify(allContent, null, 2));
      console.log('💾 Content saved to: sanity-content-export.json');
      console.log('   You can manually import this through Sanity Studio\n');
      
      return;
    }

    // Parse all content
    const homepage = parseHomepage();
    const divisions = parseDivisions();
    const faqs = parseFAQs();
    const testimonials = parseTestimonials();
    const settings = parseSiteSettings();

    // Import to Sanity
    console.log('📤 Importing homepage...');
    await client.createOrReplace(homepage);

    console.log('📤 Importing divisions...');
    for (const division of divisions) {
      await client.createOrReplace(division);
    }

    console.log('📤 Importing FAQs...');
    for (const faq of faqs) {
      await client.createOrReplace(faq);
    }

    console.log('📤 Importing testimonials...');
    for (const testimonial of testimonials) {
      await client.createOrReplace(testimonial);
    }

    console.log('📤 Importing site settings...');
    await client.createOrReplace(settings);

    console.log('\n✅ Content import complete!');
    console.log('🌐 View in Sanity Studio: http://localhost:3333\n');

  } catch (error) {
    console.error('❌ Error importing content:', error.message);
    process.exit(1);
  }
}

// Run the import
if (require.main === module) {
  importContent();
}

module.exports = { importContent };
