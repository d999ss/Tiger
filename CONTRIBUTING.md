# Contributing to Tiger CMS

Thank you for your interest in contributing to Tiger CMS! This document provides guidelines and instructions for contributing to this project.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Documentation](#documentation)

---

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring environment for all contributors. We expect all team members to:

- Be respectful and professional
- Accept constructive criticism gracefully
- Focus on what is best for the project
- Show empathy towards other team members

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Personal or political attacks
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have:

- [ ] Git installed and configured
- [ ] Access to the Tiger GitHub repository
- [ ] Python 3.8+ (for QA tools)
- [ ] Node.js 16+ (for build tools)
- [ ] A code editor (VS Code recommended)

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/d999ss/Tiger.git
   cd Tiger
   ```

2. **Set up your development environment**
   ```bash
   # Install QA dependencies
   cd qa-automation
   pip install -r requirements.txt
   cd ..
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## 💻 Development Workflow

### Branch Naming Convention

Use descriptive branch names that indicate the type and purpose of changes:

- `feature/` - New features
- `fix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or updates

**Examples:**
- `feature/add-new-product-page`
- `fix/navigation-mobile-bug`
- `docs/update-qa-guide`
- `refactor/optimize-images`

### Making Changes

1. **Work on your feature branch**
   ```bash
   git checkout feature/your-feature-name
   ```

2. **Make incremental commits** (commit early and often)

3. **Keep your branch updated**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

4. **Test your changes thoroughly** (see Testing Requirements)

---

## 📝 Coding Standards

### HTML

- Use semantic HTML5 elements
- Maintain proper indentation (2 spaces)
- Include descriptive `alt` attributes for images
- Ensure accessibility (ARIA labels where appropriate)
- Validate HTML with W3C validator

**Example:**
```html
<section class="product-info">
  <h2>Product Name</h2>
  <img src="product.jpg" alt="Detailed description of product">
  <p>Product description goes here.</p>
</section>
```

### CSS

- Use meaningful class names (BEM methodology preferred)
- Organize properties logically
- Maintain consistent spacing
- Use CSS variables for colors and repeated values
- Optimize for performance (avoid expensive selectors)

**Example:**
```css
.product-card {
  display: flex;
  padding: 1rem;
  border-radius: 8px;
}

.product-card__title {
  font-size: 1.5rem;
  color: var(--primary-color);
}
```

### JavaScript

- Use `const` and `let` (avoid `var`)
- Write descriptive variable and function names
- Add comments for complex logic
- Handle errors gracefully
- Optimize for performance

**Example:**
```javascript
// Fetch product data from API
async function fetchProductData(productId) {
  try {
    const response = await fetch(`/api/products/${productId}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch product:', error);
    return null;
  }
}
```

### Python (QA Scripts)

- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for functions and classes
- Handle exceptions properly

---

## 🧪 Testing Requirements

### Before Submitting

All changes must be tested using our QA automation suite:

```bash
cd qa-automation

# Run full test suite
./run-qa.sh

# Or run specific tests
python browser_qa.py       # Browser compatibility
python visual_qa.py        # Visual regression
python check_assets.py     # Asset verification
```

### Manual Testing Checklist

- [ ] Test on Chrome, Firefox, and Safari
- [ ] Test responsive design (mobile, tablet, desktop)
- [ ] Verify all links work correctly
- [ ] Check images load properly
- [ ] Test forms and user interactions
- [ ] Verify accessibility (keyboard navigation, screen readers)
- [ ] Check page load performance

### Test Coverage

- Write tests for new functionality
- Update existing tests when modifying features
- Ensure tests are reproducible

---

## 📝 Commit Guidelines

### Commit Message Format

Use clear, descriptive commit messages following this format:

```
Type: Brief description (50 chars or less)

More detailed explanation if needed (wrap at 72 chars).
Explain what changed and why, not how.

- Bullet points are okay
- Use imperative mood ("Add feature" not "Added feature")
```

### Commit Types

- **Add:** New feature or file
- **Update:** Modify existing functionality
- **Fix:** Bug fix
- **Remove:** Delete code or files
- **Refactor:** Code restructuring without changing functionality
- **Docs:** Documentation changes
- **Style:** Formatting, whitespace (no code change)
- **Test:** Add or update tests
- **Chore:** Maintenance tasks

### Examples

**Good commits:**
```
Add: Product comparison table to Tiger Aesthetics

Implement a responsive comparison table showing key features
across the regenerative aesthetics product line.
```

```
Fix: Navigation dropdown not closing on mobile

Resolved issue where mobile menu remained open after selection.
Added event listener to close menu on item click.
```

**Bad commits:**
```
fixed stuff          # Too vague
WIP                  # Work in progress - shouldn't be pushed
asdfasdf            # Meaningless
```

---

## 🔄 Pull Request Process

### Before Creating a PR

1. **Update your branch** with the latest from `main`
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run all tests** and ensure they pass

3. **Review your own changes** to catch any issues

### Creating a Pull Request

1. **Push your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request** on GitHub

3. **Fill out the PR template** with:
   - Clear description of changes
   - Related issue numbers (if applicable)
   - Screenshots (for UI changes)
   - Test results
   - Checklist of completed items

### PR Template

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Documentation update
- [ ] Refactoring

## Changes Made
- List specific changes
- Be detailed and clear

## Testing
- [ ] All QA tests pass
- [ ] Tested in multiple browsers
- [ ] Mobile responsive
- [ ] Accessibility verified

## Screenshots
(If applicable)

## Checklist
- [ ] Code follows project standards
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No console errors
- [ ] Reviewed own code
```

### Review Process

- **At least one approval** required before merging
- Address all feedback and comments
- Keep discussions professional and constructive
- Update PR based on feedback

### After Approval

1. **Squash commits** if requested
2. **Merge** into main branch
3. **Delete** feature branch after merge
4. **Verify** changes in production (if applicable)

---

## 📚 Documentation

### When to Update Documentation

Update documentation when you:

- Add new features
- Change existing functionality
- Add new scripts or tools
- Modify configuration
- Fix significant bugs

### Documentation Standards

- Keep documentation up-to-date
- Use clear, concise language
- Include code examples
- Add screenshots for UI changes
- Update table of contents
- Check for broken links

### Key Documentation Files

- `README.md` - Main project documentation
- `SITE_MAP.md` - Complete site structure
- `TIGER_SITE_ORGANIZATION.md` - Organization overview
- QA automation guides in `/qa-automation/`
- Individual company README files (if needed)

---

## 🐛 Reporting Issues

### Before Reporting

- Check if the issue already exists
- Verify it's reproducible
- Gather relevant information

### Issue Template

```markdown
**Description**
Clear description of the issue

**Steps to Reproduce**
1. Go to...
2. Click on...
3. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- Browser: [e.g., Chrome 120]
- OS: [e.g., macOS 14]
- Device: [e.g., iPhone 15]

**Screenshots**
Add screenshots if applicable

**Additional Context**
Any other relevant information
```

---

## 💡 Tips for Success

### Best Practices

1. **Commit early and often** - Small commits are easier to review
2. **Test thoroughly** - Catch issues before they reach production
3. **Ask questions** - No question is too small
4. **Document your changes** - Future you will thank you
5. **Review others' code** - Learn from your teammates

### Resources

- [Git Documentation](https://git-scm.com/doc)
- [HTML Best Practices](https://html.spec.whatwg.org/)
- [CSS Guidelines](https://cssguidelin.es/)
- [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

## 📞 Getting Help

If you need assistance:

1. Check existing documentation
2. Search for similar issues
3. Ask in team chat or meetings
4. Contact the development lead
5. Create a GitHub issue if needed

---

## 🙏 Thank You!

Your contributions make Tiger CMS better for everyone. We appreciate your time and effort in improving our platform!

---

**Questions?** Contact the development team:
- 📧 Email: dev@tigerbiosciences.com
- 💬 Slack: #tiger-cms-dev
- 🌐 Internal Wiki: [link to wiki]

