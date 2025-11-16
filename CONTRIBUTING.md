# Contributing to ECF Compass

Thank you for your interest in contributing to **ECF Compass**! We welcome contributions from the community and are grateful for your support in making this tool more effective and accessible.

This document provides guidelines for contributing to the project. By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Table of Contents

1. [Ways to Contribute](#ways-to-contribute)
2. [Getting Started](#getting-started)
3. [Development Workflow](#development-workflow)
4. [Code Guidelines](#code-guidelines)
5. [Documentation Guidelines](#documentation-guidelines)
6. [Research Contributions](#research-contributions)
7. [Translation Guidelines](#translation-guidelines)
8. [Reporting Issues](#reporting-issues)
9. [Suggesting Features](#suggesting-features)
10. [Pull Request Process](#pull-request-process)
11. [Community Guidelines](#community-guidelines)

---

## Ways to Contribute

We welcome many types of contributions:

### 🐛 Bug Reports
Help us identify and fix issues by reporting bugs you encounter.

### 💡 Feature Suggestions
Share ideas for new features or improvements to existing functionality.

### 🔧 Code Contributions
Submit bug fixes, new features, or improvements to the codebase.

### 📖 Documentation
Improve or expand the documentation, tutorials, or examples.

### 🌐 Translation
Help make ECF Compass accessible by translating content into other languages.

### 🔬 Research Contributions
Share validation studies, case studies, or theoretical insights.

### 💬 Community Support
Help other users in discussions, answer questions, and share experiences.

### 🎨 Design Improvements
Contribute UI/UX enhancements, graphics, or accessibility improvements.

---

## Getting Started

### Prerequisites

Before contributing code, ensure you have:

- **Git** installed and configured
- **Node.js** (v16 or higher) and npm
- A **GitHub account**
- Basic familiarity with **JavaScript/TypeScript** (for code contributions)
- Understanding of the [SOG Framework](https://ecf-compass.readthedocs.io/sog-manual) (helpful but not required)

### Set Up Your Development Environment

1. **Fork the Repository**
   ```bash
   # Visit https://github.com/riteofrenaissance/ecf-compass
   # Click "Fork" button in top right
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/ecf-compass.git
   cd ecf-compass
   ```

3. **Add Upstream Remote**
   ```bash
   git remote add upstream https://github.com/riteofrenaissance/ecf-compass.git
   ```

4. **Install Dependencies**
   ```bash
   npm install
   ```

5. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

6. **Run Development Server**
   ```bash
   npm run dev
   ```

---

## Development Workflow

### 1. Choose an Issue or Create One

- Check [existing issues](https://github.com/riteofrenaissance/ecf-compass/issues)
- Look for issues labeled `good first issue` or `help wanted`
- If working on something new, [create an issue](https://github.com/riteofrenaissance/ecf-compass/issues/new) first to discuss

### 2. Keep Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream into your main branch
git checkout main
git merge upstream/main

# Rebase your feature branch if needed
git checkout feature/your-feature-name
git rebase main
```

### 3. Make Your Changes

- Write clear, readable code
- Follow the [Code Guidelines](#code-guidelines)
- Add tests for new functionality
- Update documentation as needed

### 4. Test Your Changes

```bash
# Run tests
npm test

# Run linter
npm run lint

# Build project
npm run build
```

### 5. Commit Your Changes

Follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```bash
# Examples:
git commit -m "feat: add new assessment question type"
git commit -m "fix: correct scoring calculation for Obsession dimension"
git commit -m "docs: update SOG Manual with new examples"
git commit -m "refactor: simplify results display component"
```

**Commit Message Format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create Pull Request

- Go to your fork on GitHub
- Click "New Pull Request"
- Fill out the PR template completely
- Link related issues

---

## Code Guidelines

### General Principles

1. **Clarity over Cleverness**: Write code that's easy to understand
2. **Consistency**: Follow existing patterns in the codebase
3. **Modularity**: Keep functions small and focused
4. **Testability**: Write testable code with clear interfaces
5. **Documentation**: Comment complex logic, document public APIs

### Style Guide

We use **ESLint** and **Prettier** for code formatting. Run before committing:

```bash
npm run lint:fix
npm run format
```

### JavaScript/TypeScript Standards

```javascript
// ✅ Good: Clear naming, single responsibility
function calculateSovereigntyScore(responses) {
  const validResponses = filterValidResponses(responses);
  const average = computeAverage(validResponses);
  return normalizeScore(average);
}

// ❌ Bad: Unclear naming, doing too much
function calc(r) {
  let s = 0;
  for(let i = 0; i < r.length; i++) {
    if(r[i] != null) s += r[i];
  }
  return (s / r.length) * 10;
}
```

### React Component Guidelines

```jsx
// ✅ Good: Functional component with clear props
import { useState } from 'react';
import PropTypes from 'prop-types';

function AssessmentQuestion({ question, onAnswer, currentValue }) {
  const [selectedValue, setSelectedValue] = useState(currentValue || null);
  
  const handleChange = (value) => {
    setSelectedValue(value);
    onAnswer(question.id, value);
  };
  
  return (
    <div className="assessment-question">
      <h3>{question.text}</h3>
      <LikertScale 
        value={selectedValue}
        onChange={handleChange}
        min={1}
        max={5}
      />
    </div>
  );
}

AssessmentQuestion.propTypes = {
  question: PropTypes.shape({
    id: PropTypes.string.isRequired,
    text: PropTypes.string.isRequired,
  }).isRequired,
  onAnswer: PropTypes.func.isRequired,
  currentValue: PropTypes.number,
};

export default AssessmentQuestion;
```

### Testing Requirements

All new features must include tests:

```javascript
// Example test structure
describe('SOG Score Calculator', () => {
  describe('calculateSovereigntyScore', () => {
    it('should return correct score for valid responses', () => {
      const responses = [4, 5, 3, 4, 5];
      const score = calculateSovereigntyScore(responses);
      expect(score).toBeCloseTo(8.4, 1);
    });
    
    it('should handle missing responses', () => {
      const responses = [4, null, 3, undefined, 5];
      const score = calculateSovereigntyScore(responses);
      expect(score).toBeDefined();
    });
    
    it('should throw error for invalid input', () => {
      expect(() => calculateSovereigntyScore(null)).toThrow();
    });
  });
});
```

### Accessibility Standards

- Use semantic HTML
- Include ARIA labels where appropriate
- Ensure keyboard navigation works
- Maintain sufficient color contrast
- Test with screen readers

```jsx
// ✅ Good: Accessible form
<label htmlFor="question-1">
  How much control do you feel over your AI usage?
</label>
<select 
  id="question-1"
  aria-describedby="question-1-help"
  onChange={handleChange}
>
  <option value="">Select an answer</option>
  <option value="1">Very little control</option>
  <option value="5">Complete control</option>
</select>
<p id="question-1-help" className="help-text">
  Consider your ability to stop using AI when you choose.
</p>
```

---

## Documentation Guidelines

### Writing Style

- **Clear and concise**: Avoid jargon where possible
- **Active voice**: "The assessment measures..." not "The assessment is measured by..."
- **Examples**: Include concrete examples for abstract concepts
- **Inclusive language**: Use gender-neutral language

### Documentation Structure

```markdown
# Title (H1)

Brief introduction (1-2 sentences).

## Section Title (H2)

Content goes here.

### Subsection (H3)

More specific content.

#### Details (H4)

Fine-grained information.
```

### Code Examples in Documentation

````markdown
```javascript
// Always include comments explaining what the code does
const score = calculateScore(responses);

// Explain the result
console.log(score); // Output: { sovereignty: 7.5, obsession: 3.2, growth: 8.1 }
```
````

### Updating Documentation

When adding features, update:
- **README.md** if it affects the overview
- **User Guide** if it affects user experience
- **API Reference** if it changes the API
- **SOG Manual** if it affects assessment methodology

---

## Research Contributions

ECF Compass is built on **open science** principles. We welcome research contributions:

### Validation Studies

If you've validated the SOG Framework in your research:

1. **Pre-register your study** (we can help with this)
2. **Share your protocol** via GitHub or Zenodo
3. **Publish results** in open-access format
4. **Submit a PR** linking to your findings

### Case Studies

Real-world applications are valuable:

1. **Anonymize data** (no personal information)
2. **Document methodology** clearly
3. **Share outcomes** and insights
4. **Submit via GitHub Discussions** or PR

### Theoretical Contributions

Philosophical or theoretical insights:

1. **Reference existing framework** (cite properly)
2. **Explain your addition** clearly
3. **Provide examples** of application
4. **Discuss in GitHub Discussions** first

### Citation Requirements

When publishing research using ECF Compass:

```bibtex
@software{baladi2025ecfcompass,
  author = {Baladi, Samir},
  title = {ECF Compass: Interactive Cognitive Sovereignty Assessment Tool},
  year = {2025},
  publisher = {Rite of Renaissance Research Foundation},
  url = {https://github.com/riteofrenaissance/ecf-compass},
  doi = {10.5281/zenodo.PENDING}
}
```

---

## Translation Guidelines

We aim to make ECF Compass accessible globally. Translation contributions are highly valued.

### Translation Process

1. **Check existing translations** in `/locales` directory
2. **Create new locale file** (e.g., `fr-FR.json`)
3. **Translate all strings** maintaining meaning and tone
4. **Include context notes** for ambiguous terms
5. **Submit PR** with translation

### Translation File Structure

```json
{
  "lang": "fr-FR",
  "metadata": {
    "translator": "Your Name",
    "date": "2025-11-16",
    "version": "1.0"
  },
  "assessment": {
    "title": "Évaluation de la Souveraineté Cognitive",
    "question_1": {
      "text": "Je prends mes propres décisions même lorsque l'IA suggère des alternatives",
      "context": "Question about decisional autonomy"
    }
  }
}
```

### Translation Guidelines

- **Maintain meaning**: Capture the intent, not literal words
- **Cultural adaptation**: Adjust examples to local context
- **Consistency**: Use same terms throughout
- **Professional tone**: Match the academic/professional style
- **Technical terms**: Include original in parentheses if helpful

**Priority languages**: Spanish, French, German, Arabic, Mandarin, Hindi, Portuguese, Japanese

---

## Reporting Issues

### Before Reporting

1. **Search existing issues** to avoid duplicates
2. **Update to latest version** and check if issue persists
3. **Gather information**: browser, OS, steps to reproduce

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g., Windows 10, macOS 13]
 - Browser: [e.g., Chrome 118, Firefox 119]
 - ECF Compass Version: [e.g., 1.0.0]

**Additional context**
Any other relevant information.
```

[Report a bug →](https://github.com/riteofrenaissance/ecf-compass/issues/new?template=bug_report.md)

---

## Suggesting Features

We welcome feature suggestions! Here's how:

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Other solutions or features you've considered.

**How does this align with ECF Compass goals?**
How does this support cognitive sovereignty assessment?

**Additional context**
Mockups, examples, or related research.
```

### Feature Discussion Process

1. **Submit feature request** via GitHub Issues
2. **Community discussion** (we encourage feedback from others)
3. **Maintainer review** (we'll assess feasibility and alignment)
4. **Approval or refinement** (may need adjustments)
5. **Implementation** (by you or core team)

[Suggest a feature →](https://github.com/riteofrenaissance/ecf-compass/issues/new?template=feature_request.md)

---

## Pull Request Process

### Before Submitting PR

- ✅ Code follows style guidelines
- ✅ Tests pass (`npm test`)
- ✅ Linter passes (`npm run lint`)
- ✅ Documentation updated
- ✅ Commits follow conventional format
- ✅ Branch is up-to-date with main

### PR Description Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (please describe)

## Related Issue
Fixes #(issue number)

## Testing
Describe tests you've added or how you tested changes.

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented complex code
- [ ] I have updated documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing tests pass locally
- [ ] Any dependent changes have been merged

## Screenshots (if applicable)
Add screenshots showing the change.

## Additional Notes
Any other information for reviewers.
```

### Review Process

1. **Automated checks** run (tests, linting)
2. **Maintainer review** (usually within 3-7 days)
3. **Feedback and discussion** (address comments)
4. **Approval** (when all checks pass and changes approved)
5. **Merge** (by maintainer)

### After Merge

- Your contribution will be acknowledged in release notes
- You'll be added to CONTRIBUTORS.md
- Thank you! 🎉

---

## Community Guidelines

### Communication Channels

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Questions, ideas, general discussion
- **GitHub PRs**: Code reviews, technical discussion

### Expected Behavior

✅ **Do:**
- Be respectful and inclusive
- Provide constructive feedback
- Stay on topic
- Help others when you can
- Credit others' work

❌ **Don't:**
- Use offensive or discriminatory language
- Harass or attack others
- Spam or self-promote excessively
- Share others' private information
- Disrupt discussions

### Scope of Project

ECF Compass focuses on **cognitive sovereignty in human-AI interaction**. Contributions should align with this mission.

**In scope:**
- Assessment methodology improvements
- User experience enhancements
- Research validation
- Educational resources
- Accessibility improvements

**Out of scope:**
- General AI tools unrelated to sovereignty
- Commercial promotion
- Political advocacy unrelated to cognitive sovereignty
- Personal grievances

---

## Recognition

### Contributors

All contributors are recognized in:
- **CONTRIBUTORS.md** - List of all contributors
- **Release notes** - Specific contributions acknowledged
- **Documentation** - Authors credited in relevant sections

### Types of Contributions

We recognize many forms of contribution:
- 💻 Code
- 📖 Documentation
- 🌐 Translation
- 🔬 Research
- 🐛 Bug reports
- 💡 Ideas
- 💬 Community support

---

## Questions?

### Get Help

- **General questions**: [GitHub Discussions](https://github.com/riteofrenaissance/ecf-compass/discussions)
- **Technical issues**: [GitHub Issues](https://github.com/riteofrenaissance/ecf-compass/issues)
- **Private inquiries**: See [ORCID profile](https://orcid.org/0009-0003-8903-0029) for contact

### Additional Resources

- [User Guide](https://ecf-compass.readthedocs.io/guide)
- [SOG Manual](https://ecf-compass.readthedocs.io/sog-manual)
- [Philosophy Guide](https://ecf-compass.readthedocs.io/philosophy)
- [Code of Conduct](CODE_OF_CONDUCT.md)

---

## License

By contributing to ECF Compass, you agree that your contributions will be licensed under:
- **Code**: MIT License
- **Documentation**: CC BY 4.0

---

## Thank You!

Your contributions make ECF Compass better for everyone. We appreciate your time and effort in supporting cognitive sovereignty for all.

**Together, we can build tools that preserve human dignity and autonomy in the age of AI.**

---

*This document is adapted from open-source contribution guidelines and follows industry best practices. It will be updated as the project evolves.*

**Last Updated**: November 2025  
**Maintained by**: Rite of Renaissance Research Foundation