# TechTidy Component Library

**Version:** 1.0  
**Last Updated:** July 2026

---

# Purpose

The TechTidy Component Library defines every reusable interface element used throughout the website.

The goal is consistency.

Pages should be assembled from existing components rather than creating new layouts for every page.

If a component already exists, reuse it.

---

# Component Philosophy

Every component should be:

- Simple
- Reusable
- Accessible
- Responsive
- Easy to understand

A component should solve one problem well.

Avoid creating one-off components.

---

# Component Categories

## Layout

- Container
- Section
- Grid
- Flex Row
- Hero
- Article Content
- Sidebar (future)

---

## Navigation

### Header

Purpose:

Primary navigation.

Contains:

- Logo
- Navigation Links
- Theme Toggle
- Mobile Menu

Used on:

Every page.

---

### Breadcrumbs (Future)

Purpose:

Help users navigate lessons.

Example:

Home → Learning Hub → Security → Passwords

---

# Hero

Purpose:

Introduce every lesson.

Contains:

- Category
- Article Title
- Summary
- Reading Time
- Difficulty
- Last Updated

Rules:

Only one hero per page.

---

# Content Components

## Article Section

Purpose:

Primary learning content.

Contains:

- H2 Heading
- Paragraph
- Optional List
- Optional Illustration
- Optional Callout

---

## Definition

Purpose:

Explain terminology.

Accent:

Purple

Usage:

Only when introducing new technical terms.

---

## Example

Purpose:

Show real-world context.

Accent:

Neutral Gray

---

## Tip

Purpose:

Provide practical advice.

Accent:

Blue

---

## Warning

Purpose:

Highlight risks.

Accent:

Orange

Use sparingly.

---

## Key Takeaways

Purpose:

Summarize the lesson.

Rules:

- 3–5 bullets
- Present on every educational article

---

## Continue Learning

Purpose:

Guide readers to related lessons.

Appears after Key Takeaways.

---

# Tables

Purpose:

Compare concepts.

Examples:

Static vs Dynamic

Windows vs macOS

OneDrive vs SharePoint

Rules:

- Consistent styling
- Responsive
- Avoid excessive rows

---

# Cards

Cards should emphasize information.

Cards should never replace page structure.

Good:

Definition

Tip

Example

Bad:

Entire article inside cards.

---

# Buttons

## Primary

Purpose:

Main action.

Example:

Start Learning

---

## Secondary

Purpose:

Supporting actions.

Example:

Read More

---

## Text Link

Purpose:

Internal navigation.

---

# Forms

Current:

Contact Form

Newsletter Signup

Future:

Resource Downloads

Workshop Registration

Rules:

- Simple labels
- Visible validation
- Accessible inputs

---

# Footer

Contains:

- Copyright
- Navigation
- Social Links
- Newsletter
- Contact

Consistent across all pages.

---

# Responsive Behaviour

Desktop

Maximum reading width:

760–800px

Tablet

Reduce spacing.

Collapse navigation.

Mobile

Single-column layout.

Full-width buttons.

Responsive tables.

---

# Accessibility

Every component must support:

- Keyboard navigation
- Visible focus state
- Semantic HTML
- Proper heading hierarchy
- Screen readers
- Color contrast AA

Accessibility is required.

---

# Animation

Animations should support usability.

Allowed:

Fade

Slide

Hover

Transition

Avoid:

Bounce

Spin

Attention-grabbing effects

Animation should feel subtle.

---

# HTML Naming Convention

Use descriptive class names.

Examples:

article-section

article-hero

definition-box

tip-box

warning-box

comparison-table

key-takeaways

Avoid:

box1

section2

purpleCard

---

# CSS Guidelines

Prefer reusable utility classes.

Use design tokens.

Avoid inline styles.

Avoid duplicate rules.

Organize CSS by component.

---

# Development Rules

Before creating a new component ask:

1. Does a component already exist?

If yes:

Reuse it.

If no:

Will it be reused at least three times?

If not:

Don't create it.

---

# Future Components

Potential additions:

- Timeline
- Accordion
- Quiz
- Progress Tracker
- Interactive Diagram
- Code Block
- Video Lesson
- Download Card

Only add components that improve learning.

---

# Guiding Principle

Every interface component should make technology easier to understand.

If a component adds visual complexity without improving comprehension, it should not be included.
