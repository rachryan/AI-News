# TechTidy

[TechTidy](https://techtidy.ca/) is an independent community learning project created by Rachel Ryan. It provides free, plain-language technology lessons and an eight-week Digital Confidence program for adults who want practical support with everyday technology, online safety, and AI.

## What the project demonstrates

- Audience-centred technical communication
- Curriculum and learning-path design
- Technology adoption and digital-confidence support
- Responsive and accessible front-end development
- Version-controlled publishing and continuous improvement
- Responsible use of AI during research, writing, and development

The [Building TechTidy case study](https://techtidy.ca/learning/building-techtidy.html) explains the project decisions and delivery approach in more detail.

## Main sections

- `/` — community-focused project overview
- `/learning/` — free learning hub
- `/digital-confidence/` — eight-week community program
- `/learning/building-techtidy.html` — project case study
- `/training.html` — curated external training library

## Learning paths

1. Security & Privacy
2. AI Fundamentals
3. Technology Fundamentals
4. Digital Productivity

## Technical approach

The site intentionally uses a lightweight static architecture:

- Semantic HTML
- Responsive CSS with dark and light themes
- Small, progressively enhanced JavaScript
- Git and GitHub for controlled changes
- GitHub Pages with the `techtidy.ca` custom domain
- Formspree for contact and program-interest forms
- Google Analytics for basic usage evidence

Core learning content remains available without JavaScript.

## Project structure

```text
/
├── index.html                 Homepage
├── learning/                  Learning hub, paths, and articles
├── digital-confidence/        Community program and PDF guide
├── training.html              Curated external learning library
├── resources/                 Legacy URLs retained for compatibility
├── images/                    Site imagery
├── templates/                 Article template
├── docs/                      Standards, components, and roadmap
├── style.css                  Shared visual system
├── site.js                    Theme and navigation enhancement
├── sitemap.xml                Search-engine URL inventory
├── robots.txt                 Crawler guidance
└── CNAME                      GitHub Pages custom domain
```

## Publishing safeguards

The live site publishes from `main`. Substantive changes are prepared on a separate branch, checked for broken internal links and required integrations, reviewed, and then merged as one reversible release.

The custom domain, analytics configuration, and form endpoints should be verified before every deployment.

## Current direction

TechTidy is positioned as a community learning project and working professional case study—not primarily as a consulting storefront. The immediate priorities are improving existing learning paths, piloting the Digital Confidence program with community partners, and using learner feedback to guide future development.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for current priorities.
