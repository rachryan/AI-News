# TechTidy Project Standards

**Version:** 1.0  
**Last Updated:** July 2026

---

# Purpose

The TechTidy Project Standards define how the website is organized, developed, maintained, and expanded.

The goal is to ensure the project remains:

- Consistent
- Maintainable
- Accessible
- Performant
- Scalable

These standards apply to every new page, feature, component, and contribution.

---

# Project Philosophy

TechTidy is built to be:

- Easy to maintain
- Easy to understand
- Easy to expand

Code should prioritize readability over cleverness.

If a future developer cannot understand a solution within a few minutes, it is probably too complex.

---

# Repository Structure

```
/
│
├── index.html
├── about.html
├── contact.html
├── resources.html
├── training.html
│
├── learning/
│   ├── ai/
│   ├── security/
│   ├── microsoft365/
│   ├── cloud/
│   └── fundamentals/
│
├── css/
│   ├── variables.css
│   ├── base.css
│   ├── layout.css
│   ├── components.css
│   ├── article.css
│   ├── utilities.css
│   └── responsive.css
│
├── js/
│   ├── main.js
│   ├── navigation.js
│   ├── theme.js
│   └── search.js
│
├── assets/
│   ├── images/
│   ├── icons/
│   ├── logos/
│   └── downloads/
│
├── docs/
│   ├── STYLE-GUIDE.md
│   ├── COMPONENTS.md
│   ├── CONTENT-PLAYBOOK.md
│   ├── PROJECT-STANDARDS.md
│   └── ROADMAP.md
│
└── README.md
```

---

# Naming Conventions

## Files

Use lowercase.

Use hyphens.

Examples:

```
password-security.html

understanding-apis.html

cloud-computing.html
```

Avoid:

```
Passwords.html

Article1.html

CloudPage.html
```

---

## CSS Classes

Use descriptive names.

Good

```
article-section

hero-content

definition-box

key-takeaways
```

Avoid

```
box1

purple

left

bigText
```

---

## JavaScript

Use camelCase.

```
toggleTheme()

openMenu()

filterArticles()
```

---

# HTML Standards

Use semantic HTML whenever possible.

Prefer:

```
<header>

<nav>

<main>

<section>

<article>

<footer>
```

Avoid unnecessary div nesting.

Every page should contain only one H1.

Maintain proper heading hierarchy.

---

# CSS Standards

Use CSS variables.

Avoid magic numbers.

Organize CSS by responsibility.

```
Variables

↓

Base

↓

Layout

↓

Components

↓

Utilities

↓

Responsive
```

Never duplicate styles.

If multiple pages use the same styling, move it into a reusable component.

---

# JavaScript Standards

Keep JavaScript modular.

One responsibility per file.

Avoid global variables.

Prefer reusable functions.

Comment only when the code isn't self-explanatory.

---

# Images

Use SVG where possible.

Compress raster images.

Preferred formats:

SVG

WebP

PNG (only when necessary)

Avoid oversized images.

Every image must include descriptive alt text.

---

# Icons

Use one consistent icon library.

Avoid mixing icon styles.

Icons should support content, not replace it.

---

# Performance Standards

Target:

- Fast page loads
- Minimal JavaScript
- Optimized images
- Efficient CSS
- Lazy-load large images

Avoid unnecessary third-party libraries.

---

# Accessibility Standards

Every page must meet WCAG AA.

Requirements:

- Keyboard navigation
- Focus indicators
- Alt text
- Proper headings
- Colour contrast
- Accessible forms

Accessibility is not optional.

---

# Responsive Standards

Desktop-first.

Support:

Desktop

Tablet

Mobile

Avoid horizontal scrolling.

Tables should collapse gracefully.

Buttons should remain easy to tap.

---

# Content Standards

Every educational page must include:

- Hero
- Introduction
- Learning objectives
- Main content
- Key Takeaways
- Continue Learning
- Footer

Follow the Content Playbook.

---

# Git Standards

Commit often.

Keep commits focused.

Examples:

```
Add security lesson

Refactor article layout

Improve mobile navigation

Create comparison table component
```

Avoid:

```
Updates

Changes

Fixes

Misc
```

---

# Branch Strategy

Main

Production-ready code.

Feature branches

```
feature/article-template

feature/search

feature/newsletter
```

Bug fixes

```
fix/mobile-menu

fix/article-spacing
```

---

# Versioning

Major

Breaking structural changes.

Minor

New features.

Patch

Bug fixes.

Example:

```
1.0.0

1.1.0

1.1.2
```

---

# Quality Checklist

Before publishing:

- HTML validated
- CSS reviewed
- Mobile tested
- Dark mode verified
- Accessibility checked
- Links tested
- Images optimized
- Spelling reviewed
- Internal links added

---

# Documentation

Every major feature should update:

- ROADMAP.md
- COMPONENTS.md
- STYLE-GUIDE.md (if applicable)
- CONTENT-PLAYBOOK.md (if applicable)

Documentation should evolve alongside the project.

---

# Future Technologies

Potential additions:

- Search indexing
- Interactive diagrams
- Progressive Web App
- Member accounts
- Content management system
- Analytics dashboard
- Learning progress tracking

Evaluate new technologies based on long-term maintainability.

---

# Decision Framework

Before adding any new feature, ask:

1. Does it support the TechTidy mission?
2. Will it improve learning?
3. Can it be maintained?
4. Does an existing solution already exist?
5. Is the added complexity justified?

If the answer to any question is "no," reconsider the implementation.

---

# Guiding Principle

Every change to TechTidy should make the platform:

- Easier to learn from
- Easier to maintain
- Easier to navigate
- Easier to expand

Technology changes.

Well-designed systems adapt.

TechTidy should always favour clarity, consistency, and simplicity over unnecessary complexity.
