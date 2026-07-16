# TechTidy Design System & Style Guide

**Version:** 1.0  
**Last Updated:** July 2026

---

# Introduction

The TechTidy Design System establishes the visual, structural, and editorial standards used throughout the website.

Its purpose is to ensure every page feels cohesive, approachable, and easy to learn from while reducing maintenance and design inconsistency as the site grows.

This document is the single source of truth for all future design and development decisions.

---

# Brand Philosophy

> **Technology is already complicated. Learning it shouldn't be.**

TechTidy exists to make technology practical, understandable, and approachable.

Every page should reduce cognitive load rather than increase it.

Whenever multiple design solutions exist, choose the one that makes the content easier to understand.

---

# Brand Personality

Every page should feel:

- Calm
- Modern
- Practical
- Trustworthy
- Educational
- Accessible
- Minimal

Avoid:

- Corporate
- Sales-heavy
- Over-designed
- Cluttered
- Intimidating

---

# Core Design Principles

## Content Comes First

Visual design exists to support learning—not compete with it.

---

## Whitespace is a Feature

Empty space improves comprehension.

Never fill space simply because it exists.

---

## Consistency Over Creativity

Reusable patterns create familiarity.

If an existing component solves the problem, use it.

---

## Teach Visually

Whenever possible, explain concepts using:

1. Diagrams
2. Examples
3. Lists
4. Paragraphs

---

## Simplicity Wins

Every component should have one clear purpose.

---

# Design Tokens

## Spacing Scale

| Token | Size |
|--------|------|
| --space-xs | 8px |
| --space-sm | 16px |
| --space-md | 24px |
| --space-lg | 32px |
| --space-xl | 48px |
| --space-2xl | 64px |
| --space-3xl | 80px |

Use spacing tokens instead of arbitrary values.

---

## Border Radius

| Token | Size |
|--------|------|
| Small | 8px |
| Medium | 12px |
| Large | 20px |

---

## Shadows

Keep shadows subtle.

Avoid dramatic elevation.

---

# Typography

## Font Families

Heading

JetBrains Mono

Body

Inter

---

## Heading Hierarchy

H1 — Article Title

H2 — Primary Sections

H3 — Subsections

Body Text

Caption

Rules:

- One H1 per page
- Never skip heading levels
- Keep headings descriptive

---

# Color System

Color represents meaning.

| Purpose | Usage |
|----------|-------|
| Purple | Brand, definitions, highlights |
| Blue | Tips and helpful information |
| Green | Success and key takeaways |
| Orange | Warnings and security |
| Gray | Examples and supporting notes |

---

# Layout System

Maximum reading width:

760–800px

Sections should follow consistent spacing using the spacing scale.

Every page should contain generous whitespace.

---

# Component Library

## Hero

Appears on every article.

Contains:

- Category
- Title
- Summary
- Reading Time
- Difficulty
- Last Updated

---

## Article Section

Contains:

- Heading
- Explanation
- Example
- Optional callout
- Optional illustration

---

## Definition

Purpose:

Explain terminology.

Style:

Purple accent.

---

## Tip

Purpose:

Helpful recommendations.

Style:

Blue accent.

---

## Warning

Purpose:

Important security or technical cautions.

Style:

Orange accent.

---

## Example

Purpose:

Provide real-world context.

Style:

Neutral gray.

---

## Comparison Table

Purpose:

Compare concepts.

Use consistent styling throughout the site.

---

## Key Takeaways

Required on every article.

Three to five concise bullets.

---

## Continue Learning

Links readers to related lessons.

Required on educational pages.

---

# Standard Article Structure

Every educational article follows this structure.

Navigation

↓

Hero

↓

Introduction

↓

Section

↓

Section

↓

Section

↓

Optional Diagram

↓

Optional Comparison Table

↓

Key Takeaways

↓

Continue Learning

↓

Footer

---

# Writing Style

Use plain language.

Explain concepts before introducing technical terminology.

Keep paragraphs short.

One idea per paragraph.

Use examples frequently.

Avoid unnecessary jargon.

Write for curious beginners without oversimplifying.

---

# Visual Content

Images should teach.

Preferred visuals:

- Diagrams
- Architecture illustrations
- Process flows
- Comparison graphics

Avoid:

- Decorative stock photography
- Generic business imagery
- Unnecessary icons

---

# Accessibility

Every page should include:

- Proper heading hierarchy
- Keyboard navigation
- Visible focus states
- Descriptive alt text
- AA color contrast
- Responsive layout

Accessibility is a core requirement—not an enhancement.

---

# Responsive Design

Desktop-first.

Responsive by design.

Tables should stack where necessary.

Buttons should remain easy to tap.

Avoid horizontal scrolling.

---

# Development Standards

Use reusable CSS classes.

Avoid inline styles.

Use design tokens.

Prefer semantic HTML.

Keep components modular.

Minimize custom one-off styling.

---

# Content Standards

Every lesson should answer:

Why does this matter?

How does it work?

Where will I encounter it?

What should I remember?

End every article with:

- Key Takeaways
- Continue Learning

---

# Future Components

Potential additions include:

- Interactive diagrams
- Knowledge checks
- Downloadable quick references
- Embedded videos
- Dark mode refinements
- Search enhancements

Only introduce new components if they solve a recurring problem.

---

# Guiding Principle

Every design decision should support one objective:

> **Help people build digital confidence by making technology easier to understand.**

If a feature increases complexity without improving understanding, it does not belong in TechTidy.
