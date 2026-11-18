# Implementation playbook

## Before editing

- Read repository instructions and package scripts.
- Check git status and preserve uncommitted user work.
- Identify shared layouts, design tokens, component primitives, route conventions, and asset pipeline.
- Establish a baseline: run the app if possible and inspect key pages before changes.
- Keep a list of important flows that must not regress.

## Plan the change

Prefer a shared visual system over page-by-page one-off styling. Usually modify:

1. Global tokens, typography, base styles
2. Site shell: header, navigation, footer, page container
3. Shared UI: buttons, links, panels, forms, notices, lists, cards
4. Page-specific composition and graphics
5. Responsive behavior and interaction states

Do not replace the entire application architecture or delete components simply because a fresh implementation seems easier.

## Modern implementation of historical appearance

| Historical appearance | Modern implementation |
|---|---|
| Table-based page columns | CSS Grid/Flexbox; semantic `<table>` only for tabular data |
| Spacer GIFs | CSS spacing and alignment |
| Image-only buttons | Semantic buttons/links with text or accessible names; CSS/graphics as decoration |
| Frames | Modern routes and layout components |
| `<font>`, `<center>`, `<marquee>`, `<blink>` | CSS styling and accessible alternatives |
| Background image tiles | CSS background-image with controlled repeat and contrast |
| Image maps | Accessible links/buttons positioned with modern layout, or ordinary navigation |
| Animated GIF | Optimized animation with reduced-motion fallback where possible |

## Accessibility requirements

- Semantic landmarks and heading order.
- Keyboard-operable navigation and controls.
- Visible focus indicators.
- Form labels, instructions, validation messages, and error associations.
- Descriptive link text; avoid “click here” as the only context.
- Useful alt text for meaningful images; empty alt for decorative imagery.
- Sufficient contrast even when using period palettes.
- Reduced-motion support.
- Responsive zoom and reflow; no horizontal page-level scrolling at common mobile widths.

## SEO and performance

Preserve title, description, canonical URL, Open Graph metadata, structured data, sitemap, robots rules, analytics, and internal links unless changes are requested. Avoid loading large unoptimized GIFs or giant background images. Lazy-load below-fold media when appropriate, but do not lazy-load the primary hero/LCP image indiscriminately.

## Asset generation brief

For every proposed graphic, specify:

- Role and placement
- Subject and connection to the business
- Chosen year/lineage
- Pixel dimensions and aspect ratio
- Palette and rendering style
- Whether it is decorative or informative
- Alt-text treatment
- File format and optimization needs

Keep a consistent asset family. Do not mix unrelated clip-art styles, glossy 3D icons, vector gradients, and pixel sprites without a deliberate art-direction reason.

## Content mapping

For every original page section, decide:

- Keep as-is
- Restyle without copy changes
- Rewrite for clarity (only if appropriate and authorized)
- Move while preserving meaning
- Remove only with explicit justification

Keep legal, pricing, feature, and customer proof content accurate.

## Completion note

Report actual files/components changed, assets created, commands executed, tests and build status, browser checks, and known gaps. Never report a check as passed unless it was run.
