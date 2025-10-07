# 🐯 Tiger CMS - Enterprise Medical Website Platform

[![License](https://img.shields.io/badge/license-Proprietary-blue.svg)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://www.javascript.com/)

A comprehensive content management system for Tiger Biosciences and its family of medical, aesthetics, and wound care companies.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Company Websites](#company-websites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [QA & Testing](#qa--testing)
- [Documentation](#documentation)
- [Development](#development)
- [Contributing](#contributing)

---

## 🌟 Overview

Tiger CMS manages **8 distinct company websites** across multiple medical specialties:

- **Tiger Biosciences** - Parent company and corporate hub
- **Tiger Aesthetics** - Aesthetic medicine solutions
- **Tiger Wound Care** - Advanced wound care products
- **Sientra** - Breast implants and aesthetics
- **Airway Medix** - Respiratory medical devices
- **myAveli** - Cellulite treatment solutions
- **Extremity Care** - Orthopedic and extremity solutions
- **Lizard Health** - European medical device engineering

---

## 🏢 Company Websites

### Primary Sites

| Website | Description | Directory |
|---------|-------------|-----------|
| **tigerbiosciences.com** | Corporate parent company | `/tigerbiosciences.com/` |
| **tiger-aesthetics.com** | Regenerative aesthetics portfolio | `/tiger-aesthetics.com/` |
| **tigerwoundcare.com** | CAMPS tissue products | `/tigerwoundcare.com/` |
| **sientra.com** | Breast implants & reconstruction | `/sientra.com/` |
| **myaveli.com** | Aveli cellulite treatment | `/myaveli.com/` |

### Subsidiary Sites

| Website | Focus Area | Directory |
|---------|-----------|-----------|
| **airway-medix.com** | Respiratory care | `/airway-medix.com/` |
| **extremitycare.com** | Orthopedic solutions | `/extremitycare.com/` |
| **lizard-health.com** | EU medical devices | `/lizard-health.com/` |
| **bellafill.com** | Dermal fillers | `/bellafill.com/` |
| **birthtissuerecovery.com** | Tissue donation | `/birthtissuerecovery.com/` |
| **encoresurgicalsupplies.com** | Surgical supplies | `/encoresurgicalsupplies.com/` |

---

## 📁 Project Structure

```
Tiger CMS/
├── tigerbiosciences.com/       # Corporate website
├── tiger-aesthetics.com/       # Aesthetics division
├── tigerwoundcare.com/         # Wound care division
├── sientra.com/                # Sientra breast products
├── myaveli.com/                # Aveli cellulite treatment
├── airway-medix.com/           # Respiratory products
├── extremitycare.com/          # Extremity care solutions
├── lizard-health.com/          # European operations
├── bellafill.com/              # Bellafill dermal filler
├── birthtissuerecovery.com/    # Birth tissue recovery
├── encoresurgicalsupplies.com/ # Surgical supplies
│
├── qa-automation/              # Testing & QA tools
│   ├── browser_qa.py          # Browser-based testing
│   ├── visual_qa.py           # Visual regression testing
│   ├── check_assets.py        # Asset verification
│   ├── compare_screenshots.py # Screenshot comparison
│   ├── quick-screenshot.js    # Quick screenshot tool
│   └── run-qa.sh              # QA runner script
│
├── vibetest-use/              # Vibetest integration
│   ├── vibetest/              # Core vibetest module
│   ├── check-python.sh        # Python setup checker
│   └── complete-setup.sh      # Complete setup script
│
├── *.html                     # Root-level pages
├── *.sh                       # Build & deployment scripts
└── *.md                       # Documentation files
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** (for QA automation)
- **Node.js 16+** (for build tools)
- **Web Server** (Apache, Nginx, or similar)
- **Modern Browser** (Chrome, Firefox, Safari)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/d999ss/Tiger.git
   cd Tiger
   ```

2. **Set up QA tools** (optional)
   ```bash
   cd qa-automation
   pip install -r requirements.txt
   ```

3. **Run local server**
   ```bash
   # Python simple server
   python -m http.server 8000
   
   # Or use any web server pointing to the root directory
   ```

4. **Access websites**
   - Navigate to `http://localhost:8000/[company-name].com/`
   - Example: `http://localhost:8000/tiger-aesthetics.com/`

### Build Scripts

```bash
# Create all pages at once
./create-all-pages.sh

# Update all pages
./update-all-pages.sh
```

---

## 🧪 QA & Testing

### Automated Testing

The project includes comprehensive QA automation tools:

```bash
cd qa-automation

# Run full QA suite
./run-qa.sh

# Browser testing
python browser_qa.py

# Visual regression testing
python visual_qa.py

# Asset verification
python check_assets.py

# Screenshot comparison
python compare_screenshots.py
```

### Quick Testing

```bash
# Quick screenshot capture
node quick-screenshot.js

# Test Python setup
cd vibetest-use
./check-python.sh
```

### Documentation

- 📖 [QA Automation Summary](QA_AUTOMATION_SUMMARY.md)
- 📖 [Getting Started Guide](qa-automation/GETTING_STARTED.md)
- 📖 [Setup Guide](qa-automation/SETUP_GUIDE.md)
- 📖 [Quick Reference](qa-automation/QUICK_REFERENCE.md)
- 📖 [Examples](qa-automation/EXAMPLES.md)

---

## 📚 Documentation

### Key Documentation Files

| Document | Description |
|----------|-------------|
| [SITE_MAP.md](SITE_MAP.md) | Complete site map of all pages |
| [TIGER_SITE_ORGANIZATION.md](TIGER_SITE_ORGANIZATION.md) | Site organization structure |
| [COMPLETE_BUILD_SUMMARY.md](COMPLETE_BUILD_SUMMARY.md) | Build process summary |
| [CONTENT_COMPLETED.md](CONTENT_COMPLETED.md) | Content completion status |
| [FINAL_DELIVERY.md](FINAL_DELIVERY.md) | Final delivery notes |
| [QUICK_START_GUIDE.md](QUICK_START_GUIDE.md) | Quick start instructions |
| [PYTHON_INSTALL_INSTRUCTIONS.md](PYTHON_INSTALL_INSTRUCTIONS.md) | Python setup guide |

### Vibetest Documentation

- [Vibetest Quick Start](VIBETEST_QUICK_START.md)
- [Vibetest Setup Guide](VIBETEST_SETUP_GUIDE.md)

---

## 💻 Development

### File Organization

Each company website follows a similar structure:

```
[company].com/
├── index.html              # Homepage
├── about/                  # About pages
├── products/               # Product pages
├── contact/                # Contact forms
├── wp-content/             # WordPress assets
│   ├── uploads/           # Images, PDFs, documents
│   ├── themes/            # Theme files
│   └── plugins/           # Plugin assets
├── wp-includes/           # WordPress core assets
└── wp-json/               # REST API endpoints
```

### Asset Management

- **Images**: WebP, PNG, JPG formats
- **Documents**: PDFs in `wp-content/uploads/`
- **Fonts**: Custom fonts in theme directories
- **Styles**: CSS in `wp-content/themes/`
- **Scripts**: JavaScript in `wp-content/themes/` and `wp-includes/`

### Editing Workflow

1. Make changes to HTML/CSS/JS files
2. Test locally using a web server
3. Run QA automation to verify changes
4. Commit and push to repository
5. Deploy to production server

---

## 🤝 Contributing

### Workflow

1. Create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and test thoroughly

3. Run QA automation
   ```bash
   cd qa-automation
   ./run-qa.sh
   ```

4. Commit with clear messages
   ```bash
   git commit -m "Add: description of changes"
   ```

5. Push and create pull request
   ```bash
   git push origin feature/your-feature-name
   ```

### Code Standards

- Use semantic HTML5
- Follow CSS best practices
- Maintain responsive design
- Optimize images and assets
- Test across browsers
- Document major changes

---

## 📊 Repository Stats

- **Total Files**: 4,310+
- **Companies**: 11 websites
- **Languages**: HTML, CSS, JavaScript, Python
- **Assets**: 1,500+ images, 500+ PDFs
- **Documentation**: 15+ comprehensive guides

---

## 📞 Support

For questions or issues:

- 📧 **Email**: support@tigerbiosciences.com
- 🌐 **Website**: https://tigerbiosciences.com
- 📱 **Phone**: Contact via company website

---

## 📄 License

Proprietary - © 2025 Tiger Biosciences. All rights reserved.

This software and associated documentation files are proprietary to Tiger Biosciences and its subsidiaries. Unauthorized copying, distribution, or use is strictly prohibited.

---

## 🏆 Acknowledgments

- Tiger Biosciences team
- Web development partners
- QA and testing contributors
- Medical content experts

---

<p align="center">
  <strong>Built with ❤️ for Tiger Biosciences</strong><br>
  Advancing healthcare through innovation
</p>

