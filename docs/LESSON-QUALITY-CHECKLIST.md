# TechTidy Lesson Quality Checklist

**Version:** 1.0

**Status:** Official publishing standard

**Reference lesson:** `learning/hardware-vs-software.html`

**Template:** `templates/lesson-template.html`

Use this checklist for every instructional lesson before publishing or substantially revising it. Opinion pieces, case studies, learning-path pages, and program pages use their own structures.

## Definition of done

A TechTidy lesson is ready to publish when a beginner can understand why the topic matters, explain the central idea in their own words, complete one useful activity, check their understanding, and identify a sensible next step.

The page must also be accessible, technically valid, accurately described in its metadata, connected to its learning path, and safe to publish.

## 1. Purpose and learner outcome

- [ ] The lesson teaches one clear topic rather than several loosely connected topics.
- [ ] The intended learner can be described in one sentence.
- [ ] The introduction explains why the topic is useful in everyday life, learning, or work.
- [ ] There are three to five observable learning outcomes.
- [ ] Each outcome is supported by the lesson content and checked by an activity or question.
- [ ] The lesson is labelled honestly as beginner, intermediate, deep dive, or reference material.
- [ ] The estimated reading time is realistic.

## 2. Required lesson structure

- [ ] Learning path and lesson number
- [ ] One clear page title (`h1`)
- [ ] Plain-language introduction
- [ ] Reading time and lesson features
- [ ] “What You’ll Learn” outcomes
- [ ] Core explanation in short sections
- [ ] At least one familiar, real-life example
- [ ] One participant activity
- [ ] Safety, privacy, consent, or troubleshooting guidance when relevant
- [ ] Two to four knowledge-check questions with answers
- [ ] Three to five key takeaways containing no new information
- [ ] A clear next step or return-to-path link

Sections can be combined when that improves the learning experience. Do not add empty sections simply to satisfy the template.

## 3. Plain language and readability

- [ ] The first explanation uses everyday words before technical terminology.
- [ ] Every necessary technical term is defined when it first appears.
- [ ] Paragraphs generally contain one idea.
- [ ] Headings describe the question or idea that follows.
- [ ] Sentences are direct and reasonably short.
- [ ] Instructions use active verbs and a clear order.
- [ ] Examples are familiar to the intended learner.
- [ ] Analogies clarify the concept without becoming misleading.
- [ ] The writing is respectful and never talks down to the reader.
- [ ] Buzzwords, hype, fear tactics, and unnecessary marketing language have been removed.
- [ ] Canadian spelling and consistent terminology are used throughout.

## 4. Activity design

- [ ] The activity practises a stated learning outcome rather than merely repeating information.
- [ ] A learner can complete it remotely.
- [ ] It requires no paid account or special software unless clearly stated.
- [ ] It can be completed safely in approximately five to ten minutes.
- [ ] It uses fictional, public, or deliberately sanitized information.
- [ ] It never asks learners to expose passwords, account numbers, private records, or other sensitive information.
- [ ] The instructions explain what to do, what to notice, and what success looks like.
- [ ] An example answer, model response, or reflection prompt is provided.
- [ ] The activity can be adapted for learners using different devices or assistive technology.

## 5. Knowledge check

- [ ] Questions test understanding or decision-making, not trivia.
- [ ] Questions align directly with the learning outcomes.
- [ ] Answers are available without requiring an account or form submission.
- [ ] Every answer includes a short explanation.
- [ ] Incorrect options are believable but not intentionally confusing.
- [ ] A learner can retry or review the relevant section without penalty.

## 6. Visuals and media

- [ ] Every visual has a teaching purpose; decorative images are optional.
- [ ] SVG is preferred for diagrams, processes, labels, and comparisons.
- [ ] Raster images are appropriately sized and compressed.
- [ ] The visual remains readable on a phone and at 200% zoom.
- [ ] Text contrast and label size are sufficient.
- [ ] Meaning is not communicated through colour alone.
- [ ] Informative images have alt text that communicates the learning point.
- [ ] Complex diagrams include a visible caption or nearby equivalent explanation.
- [ ] Decorative images use empty alt text (`alt=""`).
- [ ] Image dimensions are included to reduce page movement while loading.
- [ ] Copyright, licensing, and attribution requirements have been checked.

## 7. Accessibility

- [ ] A “Skip to main content” link is present.
- [ ] The page uses semantic landmarks: navigation, header, main, sections, and footer.
- [ ] There is exactly one `h1`.
- [ ] Headings follow a logical hierarchy without skipped levels.
- [ ] Link text describes its destination; avoid “click here.”
- [ ] Interactive elements work with a keyboard.
- [ ] Answer reveals use native, labelled controls such as `details` and `summary`.
- [ ] Instructions do not rely only on position, shape, sound, or colour.
- [ ] Tables are used only for genuine row-and-column relationships and have headings.
- [ ] Lists use semantic `ul` or `ol` elements.
- [ ] The page remains understandable when styles or images do not load.
- [ ] The page is checked at mobile width and at 200% browser zoom.

## 8. Safety, privacy, and responsible use

- [ ] Personal stories are necessary, proportionate, and authorized for public use.
- [ ] No sensitive personal information is included unintentionally.
- [ ] Examples involving people, clients, workplaces, or learners are fictionalized or sanitized.
- [ ] The lesson distinguishes general education from professional medical, legal, or financial advice when relevant.
- [ ] Safety guidance is calm, specific, and actionable.
- [ ] High-stakes decisions retain meaningful human review.
- [ ] AI examples address privacy, verification, consent, and accountability when relevant.
- [ ] Current product behaviour, policies, and legal claims are verified using primary sources before publication.

## 9. Metadata and search visibility

- [ ] The title is unique, descriptive, and ends with `| TechTidy`.
- [ ] The meta description accurately summarizes the visible lesson.
- [ ] The canonical URL uses the final public HTTPS address.
- [ ] Open Graph title, description, URL, image, dimensions, and alt text are present.
- [ ] X/Twitter card metadata is present.
- [ ] Social image URLs are absolute and return successfully.
- [ ] JSON-LD parses as valid JSON.
- [ ] Structured data describes only content visible on the page.
- [ ] `LearningResource`, breadcrumb, learning path, duration, and outcomes are accurate.
- [ ] All instances of `lesson-slug`, `path-slug`, and bracketed placeholders are removed.
- [ ] The template’s `noindex, nofollow` directive is removed from the production lesson.
- [ ] The published canonical URL is added to `sitemap.xml` with an accurate `lastmod` date.

## 10. Navigation and learning-path consistency

- [ ] The back link returns to the correct learning path.
- [ ] The learning-path page links to this lesson.
- [ ] The displayed lesson count is updated wherever it appears.
- [ ] Lesson numbering matches the intended sequence.
- [ ] Previous and next links point only to published pages.
- [ ] Unpublished lessons are labelled “in development” and are not presented as live links.
- [ ] Related lessons are relevant rather than promotional.
- [ ] No duplicate or conflicting version of the lesson is publicly linked.

## 11. Technical and publishing checks

- [ ] The existing analytics ID `G-9TF9JT3DVX` is preserved.
- [ ] Existing form endpoints are unchanged unless the change was explicitly approved.
- [ ] HTML structure is valid and `git diff --check` reports no whitespace errors.
- [ ] JSON-LD and XML parse successfully.
- [ ] All internal links and image paths resolve locally.
- [ ] The page introduces no console errors.
- [ ] The page is tested in both light and dark themes when applicable.
- [ ] The page title, activity, knowledge check, and CTA are visible on the deployed page.
- [ ] The lesson returns HTTP `200` after deployment.
- [ ] Images, styles, and scripts return successfully after deployment.
- [ ] The updated sitemap is live and includes the final lesson URL.
- [ ] Analytics and forms have not been tested by submitting real personal information.

## 12. Final editorial review

- [ ] Read the page once as a complete beginner.
- [ ] Confirm the lesson answers the question promised by its title.
- [ ] Remove any section that adds length without improving understanding.
- [ ] Confirm the activity is possible from the instructions alone.
- [ ] Confirm the answers do not introduce unexplained new concepts.
- [ ] Confirm the next step is useful and honest.
- [ ] Record the reviewer and review date in the pull request or release notes.

## Publishing decision

- [ ] **Ready:** All required items pass; publish and verify the live page.
- [ ] **Needs revision:** A learner-facing or technical requirement is incomplete; do not publish yet.
- [ ] **Not applicable:** An optional item was considered and deliberately excluded, with the reason recorded.
