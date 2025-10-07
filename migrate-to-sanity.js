#!/usr/bin/env node
/**
 * Migrate all 52 pages to Sanity CMS
 * Populates the CMS with initial content for client editing
 */

const sanityClient = require('@sanity/client');
const fs = require('fs');

// Initialize Sanity client with write token
const client = sanityClient({
  projectId: '0nxq33lj',
  dataset: 'production',
  apiVersion: '2024-01-01',
  token: process.env.SANITY_WRITE_TOKEN || process.env.SANITY_TOKEN,
  useCdn: false,
});

// Load page data
const pageData = JSON.parse(fs.readFileSync('./page-content-data.json', 'utf8'));

/**
 * Create sections based on page type
 */
function createSectionsForPage(filename, data) {
  const slug = filename.replace('.html', '');
  const sections = [];
  
  // Determine page type
  const isProduct = ['healpack', 'caregraft', 'alloply', 'acapatch', 'bellafill', 'aveli', 'breast',
                     'general-surgery', 'plastic-surgery', 'podiatry'].includes(slug);
  
  const isScience = ['wound-care', 'tissue-reconstruction', 'aesthetic-medicine', 'regenerative-medicine',
                     'orthopedic', 'research-pipeline', 'clinical-trials', 'publications', 'camps-technology',
                     'patents', 'quality-assurance', 'regulatory', 'manufacturing', 'certifications'].includes(slug);
  
  const isSolution = ['hospitals', 'wound-centers', 'facilities', 'healthcare-professionals',
                      'training', 'clinical-support', 'reimbursement', 'ordering', 'support',
                      'investigator', 'partnerships', 'catalog', 'solutions'].includes(slug);
  
  // Add hero section
  sections.push({
    _type: 'heroSection',
    _key: 'hero',
    badge: data.badge || 'Tiger BioSciences',
    title: data.hero_title || slug.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
    subtitle: data.hero_subtitle || 'Advanced solutions for better patient outcomes.',
    useGradient: true,
    ctaButtons: [
      {text: 'Contact Us', url: 'contact.html', style: 'primary'},
      {text: 'Learn More', url: 'about.html', style: 'outline'}
    ]
  });
  
  // Add content sections based on type
  if (isProduct) {
    // Feature grid for products
    sections.push({
      _type: 'featureGrid',
      _key: 'features',
      sectionLabel: 'Product Overview',
      title: 'Advanced Technology for Better Outcomes',
      description: 'Clinically proven solutions designed for optimal patient outcomes.',
      features: [
        {icon: '🔬', title: 'Clinically Proven', description: 'Backed by rigorous clinical studies and peer-reviewed research demonstrating superior efficacy and safety.'},
        {icon: '✓', title: 'FDA Compliant', description: 'Meets all FDA regulations and quality standards with comprehensive documentation and traceability.'},
        {icon: '📊', title: 'Evidence Based', description: 'Demonstrated efficacy in clinical applications with published outcomes and case studies.'},
        {icon: '🏆', title: 'Industry Leading', description: 'Setting new standards in tissue technology and regenerative medicine innovation.'},
        {icon: '🌍', title: 'Globally Trusted', description: 'Used by leading healthcare institutions in over 100 countries worldwide.'},
        {icon: '🔒', title: 'Quality Assured', description: 'Every product batch undergoes comprehensive testing and quality verification.'}
      ]
    });
    
    // FAQ section for products
    sections.push({
      _type: 'faqSection',
      _key: 'faq',
      sectionTitle: 'Frequently Asked Questions',
      sectionSubtitle: `Common questions about ${data.hero_title || 'this product'}`,
      faqs: [
        {question: 'What makes this product different?', answer: 'Our vertical integration ensures complete quality control from tissue recovery through processing to distribution, resulting in superior product consistency, safety, and efficacy.'},
        {question: 'What are the storage requirements?', answer: 'The product features convenient storage requirements with extended shelf life. Detailed specifications are provided with each shipment.'},
        {question: 'Is reimbursement available?', answer: 'Yes, reimbursement is available through various insurance providers. Our reimbursement support team provides comprehensive assistance.'},
        {question: 'What training is available?', answer: 'We provide comprehensive clinical training including hands-on workshops, online modules, and ongoing consultation support.'}
      ]
    });
  }
  
  if (isScience) {
    // Image + content for science pages
    sections.push({
      _type: 'imageContentSection',
      _key: 'science-content',
      title: 'Scientific Foundation',
      useVisual: true,
      imagePosition: 'right',
      content: [
        {
          _type: 'block',
          style: 'normal',
          children: [{_type: 'span', text: 'Our research combines decades of tissue science expertise with cutting-edge biotechnology to develop next-generation regenerative medicine solutions.', marks: []}]
        },
        {
          _type: 'block',
          style: 'normal',
          children: [{_type: 'span', text: 'Biological Understanding:', marks: ['strong']}, {_type: 'span', text: ' Deep knowledge of tissue architecture, cellular behavior, and healing mechanisms informs our product development.', marks: []}]
        },
        {
          _type: 'block',
          style: 'normal',
          children: [{_type: 'span', text: 'Material Science:', marks: ['strong']}, {_type: 'span', text: ' Advanced biomaterial engineering creates products with optimal physical and biological properties.', marks: []}]
        },
        {
          _type: 'block',
          style: 'normal',
          children: [{_type: 'span', text: 'Clinical Translation:', marks: ['strong']}, {_type: 'span', text: ' Bridging laboratory research and clinical application through systematic validation and testing.', marks: []}]
        }
      ],
      ctaButton: {text: 'Learn More About Our Research', url: 'research-pipeline.html'}
    });
    
    // Endorsed section for research areas
    sections.push({
      _type: 'endorsedSection',
      _key: 'research-areas',
      label: 'Research Focus Areas',
      items: [
        {title: 'Advanced Processing', description: 'Novel processing techniques that preserve biological activity while ensuring safety.'},
        {title: 'Enhanced Biomaterials', description: 'Next-generation biomaterials with improved properties and performance.'},
        {title: 'Clinical Outcomes', description: 'Comprehensive studies documenting clinical effectiveness and patient outcomes.'},
        {title: 'Mechanism Research', description: 'Understanding how our products promote healing at cellular and molecular levels.'}
      ]
    });
  }
  
  if (isSolution) {
    // Feature grid for solutions
    sections.push({
      _type: 'featureGrid',
      _key: 'solution-features',
      sectionLabel: 'Comprehensive Solutions',
      title: 'Supporting Healthcare Excellence',
      description: 'End-to-end support for healthcare professionals and institutions.',
      features: [
        {icon: '🏥', title: 'Integrated Support', description: 'Complete support from initial consultation through ongoing patient care.'},
        {icon: '📚', title: 'Education & Training', description: 'Extensive educational resources including workshops, webinars, and hands-on training.'},
        {icon: '💼', title: 'Business Support', description: 'Reimbursement assistance, inventory management, and operational consulting.'},
        {icon: '📞', title: '24/7 Clinical Support', description: 'Expert clinical support available whenever you need it.'}
      ]
    });
    
    // Testimonials for solutions
    sections.push({
      _type: 'testimonialSection',
      _key: 'testimonials',
      sectionTitle: 'Partner Success Stories',
      sectionSubtitle: 'Trusted by healthcare professionals worldwide',
      testimonials: [
        {quote: 'Tiger BioSciences provides exceptional support and quality products that help us deliver the best possible patient care.', authorName: 'Healthcare Professional', authorTitle: 'Medical Director', authorAvatar: 'MD'},
        {quote: 'The comprehensive training and ongoing support make Tiger BioSciences an invaluable partner for our organization.', authorName: 'Clinical Leader', authorTitle: 'Director of Operations', authorAvatar: 'DO'}
      ]
    });
  }
  
  // Add CTA section to all pages
  sections.push({
    _type: 'ctaSection',
    _key: 'cta',
    title: 'Get In Touch',
    description: 'Contact our team to learn more about how Tiger BioSciences can support your needs.',
    backgroundColor: 'gradient',
    buttons: [
      {text: 'Contact Us', url: 'contact.html', style: 'light'},
      {text: 'View Products', url: 'products.html', style: 'outline'}
    ]
  });
  
  return sections;
}

/**
 * Create navigation document
 */
async function createNavigation() {
  console.log('Creating navigation document...');
  
  const navigation = {
    _id: 'navigation',
    _type: 'navigation',
    title: 'Main Navigation',
    logo: 'TIGER BIOSCIENCES™',
    megaMenus: [
      {
        title: 'Our Science',
        columns: [
          {
            heading: 'Research Areas',
            links: [
              {label: 'Wound Care', url: 'wound-care.html'},
              {label: 'Tissue Reconstruction', url: 'tissue-reconstruction.html'},
              {label: 'Aesthetic Medicine', url: 'aesthetic-medicine.html'},
              {label: 'Regenerative Medicine', url: 'regenerative-medicine.html'},
              {label: 'Orthopedic Applications', url: 'orthopedic.html'}
            ]
          },
          {
            heading: 'Innovation',
            links: [
              {label: 'Research Pipeline', url: 'research-pipeline.html'},
              {label: 'Clinical Trials', url: 'clinical-trials.html'},
              {label: 'Publications', url: 'publications.html'},
              {label: 'CAMPs Technology', url: 'camps-technology.html'},
              {label: 'Patents & IP', url: 'patents.html'}
            ]
          },
          {
            heading: 'Quality',
            links: [
              {label: 'Quality Assurance', url: 'quality-assurance.html'},
              {label: 'Regulatory', url: 'regulatory.html'},
              {label: 'Manufacturing', url: 'manufacturing.html'},
              {label: 'Certifications', url: 'certifications.html'}
            ]
          },
          {
            heading: 'Resources',
            links: [
              {label: 'Science', url: 'science.html'},
              {label: 'Training', url: 'training.html'},
              {label: 'Support', url: 'support.html'},
              {label: 'FAQ', url: 'faq.html'}
            ]
          }
        ],
        featuredCard: {
          badge: 'Featured',
          title: 'Revolutionary CAMPs Technology',
          description: 'Discover how our proprietary CAMPs technology is transforming healthcare.',
          ctaText: 'Explore CAMPs',
          ctaUrl: 'camps-technology.html'
        }
      },
      {
        title: 'Products',
        columns: [
          {
            heading: 'Wound Care',
            links: [
              {label: 'HealPack', url: 'healpack.html'},
              {label: 'CarGraft', url: 'caregraft.html'},
              {label: 'AlloPly', url: 'alloply.html'},
              {label: 'Wound Centers', url: 'wound-centers.html'}
            ]
          },
          {
            heading: 'Aesthetic',
            links: [
              {label: 'Bellafill', url: 'bellafill.html'},
              {label: 'Aveli', url: 'aveli.html'},
              {label: 'Breast Solutions', url: 'breast.html'},
              {label: 'Plastic Surgery', url: 'plastic-surgery.html'}
            ]
          },
          {
            heading: 'Surgical',
            links: [
              {label: 'General Surgery', url: 'general-surgery.html'},
              {label: 'Orthopedic', url: 'orthopedic.html'},
              {label: 'Podiatry', url: 'podiatry.html'},
              {label: 'Tissue Reconstruction', url: 'tissue-reconstruction.html'}
            ]
          },
          {
            heading: 'Specialty',
            links: [
              {label: 'Regenerative Medicine', url: 'regenerative-medicine.html'},
              {label: 'AcaPatch', url: 'acapatch.html'}
            ]
          }
        ],
        featuredCard: {
          badge: 'New',
          title: 'Advanced Wound Healing Solutions',
          description: 'Our latest innovations in wound care technology.',
          ctaText: 'View All Products',
          ctaUrl: 'products.html'
        }
      },
      {
        title: 'Solutions',
        columns: [
          {
            heading: 'Healthcare Systems',
            links: [
              {label: 'Hospitals', url: 'hospitals.html'},
              {label: 'Wound Centers', url: 'wound-centers.html'},
              {label: 'Facilities', url: 'facilities.html'},
              {label: 'Healthcare Professionals', url: 'healthcare-professionals.html'}
            ]
          },
          {
            heading: 'Clinical Support',
            links: [
              {label: 'Training Programs', url: 'training.html'},
              {label: 'Clinical Support', url: 'clinical-support.html'},
              {label: 'Reimbursement', url: 'reimbursement.html'},
              {label: 'Ordering', url: 'ordering.html'}
            ]
          },
          {
            heading: 'Research',
            links: [
              {label: 'Investigator Portal', url: 'investigator.html'},
              {label: 'Clinical Trials', url: 'clinical-trials.html'},
              {label: 'Research Pipeline', url: 'research-pipeline.html'},
              {label: 'Partnerships', url: 'partnerships.html'}
            ]
          },
          {
            heading: 'Resources',
            links: [
              {label: 'Product Catalog', url: 'catalog.html'},
              {label: 'Publications', url: 'publications.html'},
              {label: 'News & Updates', url: 'news.html'},
              {label: 'Customer Support', url: 'support.html'}
            ]
          }
        ],
        featuredCard: {
          badge: 'Comprehensive',
          title: 'End-to-End Healthcare Solutions',
          description: 'From clinical research to patient care.',
          ctaText: 'Explore Solutions',
          ctaUrl: 'solutions.html'
        }
      }
    ],
    directLinks: [
      {label: 'About', url: 'about.html'},
      {label: 'Contact', url: 'contact.html'}
    ],
    ctaButton: {
      text: 'Get Started',
      url: 'contact.html'
    }
  };
  
  return navigation;
}

/**
 * Migrate all pages
 */
async function migratePages() {
  console.log('🚀 Starting migration to Sanity CMS...');
  console.log('='.repeat(60));
  
  if (!process.env.SANITY_WRITE_TOKEN && !process.env.SANITY_TOKEN) {
    console.error('❌ ERROR: SANITY_WRITE_TOKEN environment variable not set!');
    console.log('\nPlease set your Sanity write token:');
    console.log('  export SANITY_WRITE_TOKEN="your-token-here"');
    console.log('\nGet your token from: https://www.sanity.io/manage/project/0nxq33lj/api');
    process.exit(1);
  }
  
  let created = 0;
  let errors = 0;
  
  // Create navigation first
  try {
    const nav = await createNavigation();
    await client.createOrReplace(nav);
    console.log('✓ Created navigation');
    created++;
  } catch (error) {
    console.error('❌ Error creating navigation:', error.message);
    errors++;
  }
  
  // Migrate each page
  for (const [filename, data] of Object.entries(pageData.pages)) {
    const slug = filename.replace('.html', '');
    
    try {
      const sections = createSectionsForPage(filename, data);
      
      const pageDoc = {
        _id: `page-${slug}`,
        _type: 'page',
        title: data.title || slug.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
        slug: {
          _type: 'slug',
          current: slug
        },
        badge: data.badge || 'Tiger BioSciences',
        subtitle: data.hero_subtitle || '',
        sections: sections,
        seo: {
          metaTitle: data.title,
          metaDescription: data.meta_description
        }
      };
      
      await client.createOrReplace(pageDoc);
      console.log(`✓ ${filename}`);
      created++;
      
    } catch (error) {
      console.error(`❌ Error migrating ${filename}:`, error.message);
      errors++;
    }
  }
  
  console.log('='.repeat(60));
  console.log(`✅ Migration complete!`);
  console.log(`   Created/Updated: ${created} documents`);
  if (errors > 0) {
    console.log(`   Errors: ${errors}`);
  }
  console.log('\n📋 Next steps:');
  console.log('   1. Start Sanity Studio: cd studio && npm run dev');
  console.log('   2. Visit: http://localhost:3333');
  console.log('   3. Review and edit content');
}

// Run migration
migratePages().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});

