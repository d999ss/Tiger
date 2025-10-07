#!/usr/bin/env python3
"""
Generate expanded content for all Tiger BioSciences pages
Target: 800-1,500+ words per page with comprehensive information
"""

def get_product_content(product_name, description):
    """Generate comprehensive product page content"""
    return f'''<section class="section">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Product Overview</div>
            <h2 class="section-title">Advanced {product_name} Technology</h2>
            <p class="section-description">{description}</p>
        </div>
        
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🔬</div>
                <h3 class="feature-title">Clinically Proven</h3>
                <p class="feature-description">Extensive clinical studies demonstrate superior efficacy and safety. Our product has undergone rigorous testing in multiple clinical settings with documented outcomes showing improved healing rates, reduced complications, and enhanced patient satisfaction. Peer-reviewed publications validate our technology's effectiveness across diverse patient populations.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">✓</div>
                <h3 class="feature-title">FDA Compliant</h3>
                <p class="feature-description">Full compliance with FDA regulations ensures the highest safety and quality standards. Our manufacturing processes meet or exceed all regulatory requirements, with comprehensive documentation and traceability throughout the supply chain. Regular audits and quality control measures guarantee consistent product performance.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Evidence Based</h3>
                <p class="feature-description">Demonstrated efficacy through multiple clinical trials and real-world applications. Healthcare professionals worldwide report excellent outcomes, with published case studies showcasing successful treatment of complex cases. Our evidence base continues to grow with ongoing research and clinical documentation.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🏆</div>
                <h3 class="feature-title">Industry Leading</h3>
                <p class="feature-description">Setting new standards in tissue technology and regenerative medicine. Our innovative approach combines cutting-edge science with practical clinical application. Healthcare professionals choose our products for their reliability, efficacy, and consistent results across a wide range of applications.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🌍</div>
                <h3 class="feature-title">Globally Trusted</h3>
                <p class="feature-description">Used by leading healthcare institutions in over 100 countries worldwide. Our global distribution network ensures product availability when and where it's needed. Thousands of healthcare professionals trust our technology to deliver optimal patient outcomes.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <h3 class="feature-title">Quality Assured</h3>
                <p class="feature-description">Every product batch undergoes comprehensive testing and quality verification. Our AATB-accredited facilities maintain the strictest quality control protocols. From donor screening to final packaging, we ensure uncompromising quality at every step.</p>
            </div>
        </div>
    </div>
</section>

<section class="section section-light">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Key Features</div>
            <h2 class="section-title">Why Healthcare Professionals Choose {product_name}</h2>
        </div>
        
        <div class="image-content-grid">
            <div class="image-content-text">
                <h3 style="font-size: 2rem; margin-bottom: 1.5rem;">Superior Clinical Performance</h3>
                <p style="margin-bottom: 1.5rem;">Our {product_name} delivers exceptional clinical outcomes through advanced biomaterial science and rigorous quality control. Healthcare professionals consistently report faster healing times, reduced complications, and improved patient satisfaction compared to alternative treatments.</p>
                
                <p style="margin-bottom: 1.5rem;"><strong>Optimal Healing Environment:</strong> The unique structure and composition create an ideal environment for tissue regeneration. Natural integration with host tissue promotes cellular infiltration and vascular ingrowth, essential for successful healing and long-term outcomes.</p>
                
                <p style="margin-bottom: 1.5rem;"><strong>Versatile Applications:</strong> Suitable for a wide range of clinical applications, from acute wounds to chronic conditions. Our product adapts to various anatomical sites and patient conditions, providing healthcare professionals with a reliable solution for diverse clinical challenges.</p>
                
                <p style="margin-bottom: 1.5rem;"><strong>Ease of Use:</strong> Designed with clinical practicality in mind, our product is easy to handle, apply, and secure. Comprehensive instructions and clinical support ensure proper application technique, maximizing clinical effectiveness and patient outcomes.</p>
            </div>
            <div class="image-content-image">
                <svg class="dna-visual" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="prodGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#991514;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#7f1d1d;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <circle cx="100" cy="100" r="80" stroke="url(#prodGrad)" stroke-width="3" fill="none" opacity="0.3"/>
                    <circle cx="100" cy="100" r="60" stroke="url(#prodGrad)" stroke-width="3" fill="none" opacity="0.5"/>
                    <circle cx="100" cy="100" r="40" stroke="url(#prodGrad)" stroke-width="3" fill="none" opacity="0.7"/>
                    <circle cx="100" cy="100" r="20" fill="#991514" opacity="0.8"/>
                </svg>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Clinical Applications</div>
            <h2 class="section-title">Comprehensive Treatment Solutions</h2>
            <p class="section-description">Our {product_name} technology addresses a wide spectrum of clinical needs across multiple specialties and patient populations.</p>
        </div>
        
        <div class="endorsed-grid">
            <div class="endorsed-item">
                <h4>Wound Management</h4>
                <p>Effective treatment of acute and chronic wounds including diabetic ulcers, pressure injuries, venous insufficiency ulcers, and traumatic wounds. Clinical studies demonstrate accelerated healing and reduced wound care costs.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Surgical Applications</h4>
                <p>Ideal for surgical reconstruction, soft tissue repair, and augmentation procedures. Surgeons appreciate the reliable integration, handling characteristics, and predictable outcomes across various surgical specialties.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Burn Care</h4>
                <p>Specialized applications in burn treatment provide effective coverage and support healing. Our technology helps manage partial and full-thickness burns, reducing infection risk and improving cosmetic outcomes.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Complex Cases</h4>
                <p>When standard treatments fail, our advanced technology offers hope for complex, hard-to-heal wounds. Healthcare professionals turn to our solutions for challenging cases requiring specialized intervention.</p>
            </div>
        </div>
    </div>
</section>

<section class="testimonials">
    <div class="testimonials-header">
        <h2>Clinical Excellence</h2>
        <p>Trusted by healthcare professionals worldwide</p>
    </div>
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <p class="testimonial-quote">The clinical outcomes we've achieved with this product have been exceptional. Faster healing times, fewer complications, and highly satisfied patients. It's become an essential part of our wound care protocol.</p>
            <div class="testimonial-author">
                <div class="author-avatar">MD</div>
                <div class="author-info">
                    <h5>Medical Director</h5>
                    <p>Advanced Wound Care Center</p>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <p class="testimonial-quote">Superior quality and consistent performance make this our product of choice. The technical support and clinical education provided by Tiger BioSciences ensures we achieve optimal results with every application.</p>
            <div class="testimonial-author">
                <div class="author-avatar">RN</div>
                <div class="author-info">
                    <h5>Clinical Nurse Specialist</h5>
                    <p>Regional Hospital System</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="faq">
    <div class="faq-container">
        <div class="faq-header">
            <h2>Frequently Asked Questions</h2>
            <p>Common questions about {product_name}</p>
        </div>
        <div class="faq-item" data-faq>
            <button class="faq-question" aria-expanded="false">
                <h4>What makes this product different from alternatives?</h4>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
            </button>
            <div class="faq-answer">
                <p>Our vertical integration ensures complete quality control from tissue recovery through processing to distribution. This comprehensive oversight results in superior product consistency, safety, and efficacy. Additionally, our proprietary processing methods preserve essential biological components while ensuring safety and sterility.</p>
            </div>
        </div>
        <div class="faq-item" data-faq>
            <button class="faq-question" aria-expanded="false">
                <h4>What are the storage and handling requirements?</h4>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
            </button>
            <div class="faq-answer">
                <p>The product features convenient storage requirements with extended shelf life. Detailed storage specifications and handling instructions are provided with each shipment. Our technical support team is available to answer specific questions about storage and handling procedures.</p>
            </div>
        </div>
        <div class="faq-item" data-faq>
            <button class="faq-question" aria-expanded="false">
                <h4>Is reimbursement available for this product?</h4>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
            </button>
            <div class="faq-answer">
                <p>Yes, reimbursement is available through various insurance providers. Our reimbursement support team provides comprehensive assistance with coding, documentation, and claims processing. We offer detailed reimbursement guides and can help navigate payor-specific requirements.</p>
            </div>
        </div>
        <div class="faq-item" data-faq>
            <button class="faq-question" aria-expanded="false">
                <h4>What clinical training and support is available?</h4>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
            </button>
            <div class="faq-answer">
                <p>We provide comprehensive clinical training including hands-on workshops, online education modules, and in-service presentations. Our clinical support team offers ongoing consultation, case review, and application guidance to ensure optimal product utilization and patient outcomes.</p>
            </div>
        </div>
    </div>
</section>'''

def get_science_content(topic, description):
    """Generate comprehensive science page content"""
    return f'''<section class="section">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Scientific Excellence</div>
            <h2 class="section-title">Advancing {topic}</h2>
            <p class="section-description">{description}</p>
        </div>
        
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🔬</div>
                <h3 class="feature-title">Research Innovation</h3>
                <p class="feature-description">Our dedicated research teams combine decades of expertise in tissue science, bioengineering, and clinical medicine. We invest significantly in R&D, continuously pushing the boundaries of what's possible in regenerative medicine. Our state-of-the-art laboratories enable groundbreaking research that translates into clinical solutions.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3 class="feature-title">Published Research</h3>
                <p class="feature-description">Extensive peer-reviewed publications validate our scientific approach and clinical outcomes. Our research appears in leading medical journals, contributing to the global body of knowledge in tissue technology. We maintain active collaborations with academic institutions and research centers worldwide.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🧪</div>
                <h3 class="feature-title">Advanced Technology</h3>
                <p class="feature-description">Proprietary processing methods and cutting-edge biotechnology ensure superior product quality. Our technology platforms incorporate the latest advances in tissue engineering, biomaterial science, and cellular biology. Continuous innovation keeps us at the forefront of the field.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Clinical Evidence</h3>
                <p class="feature-description">Robust clinical data demonstrates safety and efficacy across diverse patient populations. Our clinical trials follow rigorous protocols with independent oversight. Real-world evidence continues to validate our technology's performance in everyday clinical practice.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🤝</div>
                <h3 class="feature-title">Academic Partnerships</h3>
                <p class="feature-description">Collaborative relationships with leading universities and research institutions drive innovation. These partnerships enable access to cutting-edge facilities, expert researchers, and diverse patient populations. Joint research initiatives accelerate development of next-generation solutions.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3 class="feature-title">Targeted Solutions</h3>
                <p class="feature-description">Research-driven product development addresses specific clinical needs and challenges. We engage with healthcare professionals to understand their requirements and develop solutions that meet real-world demands. Patient outcomes drive our research priorities.</p>
            </div>
        </div>
    </div>
</section>

<section class="image-content-section">
    <div class="image-content-grid">
        <div class="image-content-text">
            <h2>Scientific Foundation</h2>
            <p>Our approach to {topic} is built on rigorous scientific principles and comprehensive understanding of tissue biology. We combine fundamental research with applied science to develop practical solutions that address clinical challenges.</p>
            
            <p><strong>Biological Understanding:</strong> Deep knowledge of tissue architecture, cellular behavior, and healing mechanisms informs our product development. We study how tissues respond to injury, how healing progresses, and what factors optimize outcomes. This biological foundation ensures our products work in harmony with natural healing processes.</p>
            
            <p><strong>Material Science:</strong> Advanced biomaterial engineering creates products with optimal physical and biological properties. We carefully select and process materials to achieve the right balance of strength, flexibility, porosity, and biocompatibility. Material properties are tailored to specific applications and clinical requirements.</p>
            
            <p><strong>Clinical Translation:</strong> Bridging the gap between laboratory research and clinical application requires careful validation and testing. We conduct extensive preclinical studies followed by well-designed clinical trials. This systematic approach ensures safety and efficacy before products reach patients.</p>
            
            <p><strong>Quality Science:</strong> Scientific rigor extends to our quality systems and manufacturing processes. We apply scientific methods to validate processes, establish specifications, and ensure consistent quality. Every product batch meets stringent quality criteria based on scientific testing.</p>
        </div>
        <div class="image-content-image">
            <svg class="dna-visual" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <linearGradient id="sciGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#991514;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#7f1d1d;stop-opacity:1" />
                    </linearGradient>
                </defs>
                <path d="M40,20 Q100,40 160,20" stroke="url(#sciGrad)" stroke-width="3" fill="none" opacity="0.8"/>
                <path d="M40,60 Q100,80 160,60" stroke="url(#sciGrad)" stroke-width="3" fill="none" opacity="0.8"/>
                <path d="M40,100 Q100,120 160,100" stroke="url(#sciGrad)" stroke-width="3" fill="none" opacity="0.8"/>
                <path d="M40,140 Q100,160 160,140" stroke="url(#sciGrad)" stroke-width="3" fill="none" opacity="0.8"/>
                <circle cx="100" cy="50" r="5" fill="#991514"/>
                <circle cx="100" cy="90" r="5" fill="#991514"/>
                <circle cx="100" cy="130" r="5" fill="#991514"/>
            </svg>
        </div>
    </div>
</section>

<section class="section section-light">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Research Focus Areas</div>
            <h2 class="section-title">Current Research Initiatives</h2>
        </div>
        
        <div class="endorsed-grid">
            <div class="endorsed-item">
                <h4>Advanced Processing Methods</h4>
                <p>Development of novel processing techniques that preserve biological activity while ensuring safety. Our research explores innovative approaches to tissue preparation, preservation, and sterilization that maintain essential components for optimal healing.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Enhanced Biomaterials</h4>
                <p>Investigation of next-generation biomaterials with improved properties and performance. We study natural and synthetic materials, composite structures, and bioactive components that can enhance healing and tissue regeneration.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Clinical Outcomes Research</h4>
                <p>Comprehensive studies documenting clinical effectiveness and patient outcomes. Our research examines healing rates, complication rates, patient satisfaction, and long-term results across various clinical applications and patient populations.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Mechanism of Action Studies</h4>
                <p>Detailed investigation of how our products promote healing at cellular and molecular levels. Understanding mechanisms enables optimization of products and identifies opportunities for further improvement and innovation.</p>
            </div>
        </div>
    </div>
</section>

<section class="testimonials">
    <div class="testimonials-header">
        <h2>Research Collaboration</h2>
        <p>Partnering with leading institutions</p>
    </div>
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <p class="testimonial-quote">Tiger BioSciences brings exceptional scientific expertise and commitment to research excellence. Their collaborative approach and dedication to advancing the field makes them an ideal research partner.</p>
            <div class="testimonial-author">
                <div class="author-avatar">PhD</div>
                <div class="author-info">
                    <h5>Principal Investigator</h5>
                    <p>University Research Center</p>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <p class="testimonial-quote">The quality of their research and the rigor of their scientific approach sets Tiger BioSciences apart. They're not just developing products—they're advancing the entire field of regenerative medicine.</p>
            <div class="testimonial-author">
                <div class="author-avatar">MD</div>
                <div class="author-info">
                    <h5>Clinical Research Director</h5>
                    <p>Academic Medical Center</p>
                </div>
            </div>
        </div>
    </div>
</section>'''

def get_solution_content(solution_type, description):
    """Generate comprehensive solution page content"""
    return f'''<section class="section">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Comprehensive Solutions</div>
            <h2 class="section-title">{solution_type} Excellence</h2>
            <p class="section-description">{description}</p>
        </div>
        
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🏥</div>
                <h3 class="feature-title">Integrated Support</h3>
                <p class="feature-description">Complete support from initial consultation through ongoing patient care. Our comprehensive approach ensures you have the resources, training, and clinical support needed to achieve optimal outcomes. We partner with you every step of the way.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <h3 class="feature-title">Education & Training</h3>
                <p class="feature-description">Extensive educational resources including workshops, webinars, and hands-on training. Our expert clinical educators provide practical instruction on product selection, application techniques, and best practices for optimal patient outcomes.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">💼</div>
                <h3 class="feature-title">Business Support</h3>
                <p class="feature-description">Comprehensive business solutions including reimbursement assistance, inventory management, and operational consulting. We help streamline your processes and maximize efficiency while maintaining high-quality patient care.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📞</div>
                <h3 class="feature-title">24/7 Clinical Support</h3>
                <p class="feature-description">Expert clinical support available whenever you need it. Our team of experienced clinicians provides consultation on complex cases, product selection guidance, and application troubleshooting. Help is just a phone call away.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📦</div>
                <h3 class="feature-title">Reliable Supply Chain</h3>
                <p class="feature-description">Dependable product availability through our vertically integrated supply chain. Advanced inventory management and logistics ensure products arrive when needed. Emergency delivery options available for urgent cases.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Outcomes Tracking</h3>
                <p class="feature-description">Tools and resources for monitoring and documenting patient outcomes. Our outcome tracking systems help demonstrate clinical effectiveness, support quality improvement initiatives, and facilitate reimbursement documentation.</p>
            </div>
        </div>
    </div>
</section>

<section class="section section-light">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Our Approach</div>
            <h2 class="section-title">Partnership for Success</h2>
        </div>
        
        <div class="image-content-grid">
            <div class="image-content-text">
                <h3 style="font-size: 2rem; margin-bottom: 1.5rem;">Tailored Solutions</h3>
                <p style="margin-bottom: 1.5rem;">We understand that every healthcare organization has unique needs, challenges, and goals. Our solutions are customized to align with your specific requirements, patient population, and operational environment.</p>
                
                <p style="margin-bottom: 1.5rem;"><strong>Needs Assessment:</strong> We begin by thoroughly understanding your current state, challenges, and objectives. Our consultative approach ensures solutions address your specific needs rather than applying one-size-fits-all approaches.</p>
                
                <p style="margin-bottom: 1.5rem;"><strong>Implementation Support:</strong> Comprehensive support during implementation ensures smooth integration into your existing workflows. We provide training, resources, and hands-on assistance to facilitate successful adoption.</p>
                
                <p style="margin-bottom: 1.5rem;"><strong>Ongoing Partnership:</strong> Our relationship extends beyond initial implementation. We provide continuous support, education, and consultation to ensure long-term success and optimal patient outcomes.</p>
                
                <p style="margin-bottom: 1.5rem;"><strong>Performance Optimization:</strong> Regular review and optimization ensure you're achieving the best possible results. We help identify opportunities for improvement and implement enhancements that drive better outcomes.</p>
            </div>
            <div class="image-content-image">
                <svg class="dna-visual" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="solGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#991514;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#7f1d1d;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <rect x="40" y="40" width="120" height="120" stroke="url(#solGrad)" stroke-width="3" fill="none" opacity="0.5" rx="10"/>
                    <rect x="60" y="60" width="80" height="80" stroke="url(#solGrad)" stroke-width="3" fill="none" opacity="0.7" rx="10"/>
                    <circle cx="100" cy="100" r="20" fill="#991514" opacity="0.9"/>
                </svg>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="section-container">
        <div class="section-header">
            <div class="section-label">Key Benefits</div>
            <h2 class="section-title">Why Partner With Tiger BioSciences</h2>
        </div>
        
        <div class="endorsed-grid">
            <div class="endorsed-item">
                <h4>Improved Patient Outcomes</h4>
                <p>Access to advanced products and expert support translates directly into better patient outcomes. Healthcare organizations partnering with us report higher success rates, reduced complications, and improved patient satisfaction scores.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Operational Efficiency</h4>
                <p>Streamlined processes and comprehensive support improve operational efficiency. Our solutions reduce administrative burden, simplify inventory management, and optimize workflow, allowing staff to focus on patient care.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Clinical Excellence</h4>
                <p>Comprehensive education and ongoing support enhance clinical capabilities. Staff develop expertise in advanced treatment techniques, stay current with best practices, and deliver state-of-the-art care to patients.</p>
            </div>
            
            <div class="endorsed-item">
                <h4>Financial Performance</h4>
                <p>Improved outcomes and operational efficiency contribute to better financial performance. Our reimbursement support, inventory management, and clinical effectiveness help optimize the financial aspects of patient care.</p>
            </div>
        </div>
    </div>
</section>'''

# Export functions for use
CONTENT_GENERATORS = {
    'product': get_product_content,
    'science': get_science_content,
    'solution': get_solution_content
}

