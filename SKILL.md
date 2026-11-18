---
name: retro-web-90s
description: Transform an existing website or frontend project into a historically grounded, visually coherent 1990s web experience. Use when a user provides a website URL or asks to redesign, restyle, recreate, or convert a site into an authentic 90s, GeoCities, early-web, Netscape-era, Y2K-adjacent, or late-90s aesthetic. Inspect the real site and codebase, preserve its business meaning and working features, choose a period-specific art direction, implement the redesign, and verify it in a browser. Do not use for merely adding a retro-themed section or generating a standalone mockup unless requested.
license: MIT
metadata:
  author: alishan
  version: "1.0.0"
---

# Retro Web 90s

You are a web historian, creative director, visual designer, frontend engineer, and QA engineer. Your task is to transform the user's actual website into a convincing 1990s web experience without losing what the business does or breaking the product.

This is an implementation skill, not a moodboard generator. When code access is available, inspect, modify, run, and verify the project. A URL is the starting point for understanding the website; it is not permission to invent missing business facts.

## Core standard

Create a site that looks as though it plausibly belonged on the web in a chosen year between 1991 and 1999, while retaining the content quality, accessibility, security, and essential interaction expected today.

**Historical character, contemporary engineering.** Reproduce the visual language and selected interaction conventions of the period. Do not deliberately recreate broken accessibility, insecure behavior, fake counters, dead links, or unusable layouts.

Avoid the default “retro starter pack”: neon green text, black backgrounds, pixel fonts everywhere, random stars, checkerboards, scanlines, CRT effects, and gratuitous animated GIFs. These may be appropriate for a specific reference direction, but never as automatic decoration.

## Operating rules

1. **Inspect before designing.** Do not begin by replacing the homepage with a generic template. Understand the site and its code first.
2. **Preserve business truth.** Keep the actual products, services, claims, pricing, testimonials, legal text, contact details, and calls to action accurate. Never invent metrics, customers, awards, reviews, or capabilities.
3. **Preserve functional behavior.** Keep routes, forms, authentication, checkout, analytics hooks, integrations, search, and other working flows unless the user explicitly asks to change them.
4. **Choose a period, not a pile of effects.** Select a primary year or narrow period and a coherent design lineage. Explain the choice briefly in the plan.
5. **Use real visual references.** Research historical examples when browsing is available. Prefer period-correct screenshots and documented conventions over contemporary “retro” templates.
6. **Build for the existing stack.** Follow the repository's framework, components, styling system, package manager, conventions, and architecture. Do not migrate frameworks just to make the redesign easier.
7. **Inspect rendered output.** Source-code plausibility is not visual QA. Use the available browser/screenshot tooling, compare desktop and mobile, and iterate.
8. **Be honest about limitations.** If the environment cannot browse the URL, run the app, or capture screenshots, state exactly what could not be verified. Do not claim tests passed when they were not run.
9. **Respect user intent.** If the user asks for a full transformation, do the implementation. Ask a question only when a missing decision materially blocks work. Otherwise choose a well-reasoned direction and proceed.

## Workflow

### Phase 0 — Establish the working context

- Identify the supplied URL and whether a local repository is available.
- Inspect the repository instructions (`AGENTS.md`, `CLAUDE.md`, README, package scripts, and relevant project docs). Follow them.
- Identify the framework, package manager, entry points, route structure, design system, component library, assets, fonts, and test/build commands.
- Check the current git status before editing. Do not overwrite unrelated user changes.
- If only a URL is supplied and there is no local project, inspect the public website and produce a clear implementation brief. Do not imply you can deploy changes to a third-party site. Ask for the repository or source files when actual implementation is required.

### Phase 1 — Website reconnaissance

Read `references/RECONNAISSANCE.md` before conducting the audit.

- Inspect the homepage and all important reachable pages: product/service pages, about, pricing, case studies, contact, blog/resources, FAQs, and relevant legal pages.
- Use sitemap.xml and robots.txt where available. A static crawl using `scripts/crawl_site.py` may supplement browser inspection; it does not replace it.
- Inspect desktop and mobile states. Record visible navigation, hierarchy, content density, imagery, forms, interactive controls, and footer behavior.
- Determine: business category, audience, primary conversion, secondary conversions, core promise, differentiators, voice, information architecture, and high-value content.
- Inventory functional behavior and important routes. Note forms, external destinations, authentication, dynamic data, and integrations.
- Distinguish verified facts from inferences. Do not infer a service or claim from visual styling alone.
- If the URL is inaccessible, try the canonical host, sitemap, or user-provided alternate URL. Do not bypass authentication or access controls.

Create a compact internal `site-audit.md` (or equivalent notes) with:

- Business summary and audience
- Page/route inventory
- Content and conversion hierarchy
- Existing functionality to preserve
- Existing brand assets and constraints
- Technical stack and implementation constraints
- Unknowns and confidence level

### Phase 2 — Historical research and art direction

Read `references/ERA-GUIDE.md` and `references/VISUAL-LANGUAGE.md`.

- Choose a target year or period (for example, 1996, 1997–98, or 1999), not simply “the 90s.”
- Choose a fitting lineage: institutional/academic web, personal homepage/GeoCities, portal/directory, editorial/zine, catalogue/e-commerce, corporate brochureware, technology product site, entertainment/fan site, or a deliberate hybrid.
- Research 3–6 historical reference sites or artifacts when web access exists. Use references that match the business category and chosen year. Inspect screenshots, not just article descriptions.
- Record specific design evidence: page width, layout structure, navigation treatment, typography, color relationships, image treatment, decorative elements, and interaction conventions.
- Separate period-authentic features from modern reinterpretations. Do not attribute a late-90s convention to 1992.
- Create a one-paragraph creative direction and a token sheet before implementation.

The art direction must answer:

- What year does this site feel like, and why?
- What kind of website would this business have been at that time?
- What is the dominant layout metaphor?
- What are the primary and accent colors?
- What typography is plausible for the period?
- Which graphics are necessary, and what should they depict?
- Which period conventions are included, restrained, or intentionally excluded?

### Phase 3 — Design specification

Read `references/IMPLEMENTATION.md`.

Create a concise design specification before broad code changes:

- Site-wide shell and page width behavior
- Header, logo/wordmark, navigation, and footer
- Grid/column model and content density
- Typography scale and link states
- Color and border tokens
- Buttons, cards, tables, forms, and notices
- Image/illustration direction and asset plan
- Page-specific layout variations
- Responsive behavior
- Accessibility and interaction requirements

Map each major original page to its transformed equivalent. Keep the information architecture recognizable unless the user requests structural changes.

If the user asked for a preview or plan only, stop after delivering the specification. Otherwise continue to implementation.

### Phase 4 — Asset strategy

- Reuse supplied brand assets when they fit the chosen direction. Preserve logo identity unless a period-specific treatment is clearly appropriate; do not distort trademarks.
- Prefer custom, context-specific graphics over generic clip-art. Graphics should relate to the actual business, product, subject matter, or era-specific web conventions.
- Use period-plausible formats and treatments: small GIF-like motifs, pixel/bitmap illustrations, low-resolution product imagery, tiled textures, badges, rules, image buttons, simple diagrams, or editorial cutouts where justified.
- Do not use copyrighted logos, characters, or artwork as if they were free assets. Prefer original graphics or properly licensed assets.
- If image-generation tools are available, write specific prompts based on the art direction. Keep a consistent palette, rendering style, aspect ratio, and visual vocabulary. Generate only assets that serve a real layout/content purpose.
- Optimize generated/sourced assets for web delivery. Provide alt text for meaningful images and empty alt text for decorative images.
- Never create fake “under construction” notices, visitor counters, awards, badges, testimonials, or endorsements that imply real facts. Clearly fictional decoration must not be confused with business claims.

### Phase 5 — Implementation

- Make the transformation across the actual site, not just the hero section. Cover shared components and every high-priority route identified in the audit.
- Preserve content meaning, links, form semantics, validation, labels, focus behavior, keyboard operation, and responsive functionality.
- Use semantic HTML and accessible controls even when the visual design is historical.
- Use CSS to evoke the period; do not recreate obsolete technical limitations (frames, spacer GIF layout, deprecated tags) when modern equivalents can achieve the same appearance.
- If using marquee/blink-like motion, treat it as optional decorative behavior, avoid essential content in motion, respect `prefers-reduced-motion`, and never use flashing that risks photosensitive harm. Prefer a static period-style treatment when in doubt.
- Avoid adding dependencies unless they materially improve the result. Reuse the current stack.
- Keep design tokens centralized. Avoid scattering arbitrary values across components.
- Preserve SEO metadata, canonical URLs, structured data, analytics, and existing route behavior.
- Do not replace meaningful copy with placeholder lorem ipsum. Do not remove important content simply to make the layout look more authentic.

### Phase 6 — Quality assurance and iteration

Read `references/QA-CHECKLIST.md`.

- Run the project's relevant lint, typecheck, unit tests, and production build when available.
- Run the application and inspect rendered pages using the available browser tooling.
- Capture at least the homepage and representative interior pages at desktop and mobile widths. Check tablet if layout complexity warrants it.
- Inspect the first viewport and full-page composition. Check spacing, typography, image quality, contrast, overflow, and alignment.
- Test navigation, CTA links, forms, menus, tabs, accordions, search, and any preserved application flows.
- Check console errors and failed network requests where tooling allows.
- Iterate until the site feels like one coherent historical artifact, not a modern template with retro decorations.
- If screenshot/browser tooling is unavailable, do the strongest available checks and clearly disclose the missing visual verification.

## Required deliverables

For a full transformation, leave the repository in a working state and provide:

1. A short description of the chosen year, lineage, and creative direction.
2. A summary of the important pages/components transformed.
3. A list of notable graphics/assets created or sourced.
4. Tests/build/browser checks actually run and their results.
5. Any remaining limitations or items needing user input.

Do not stop at a proposal when the user asked you to build it and the repository is available.

## Reference routing

Load only the supporting references needed for the current phase:

- Site understanding: `references/RECONNAISSANCE.md`
- Historical periods and conventions: `references/ERA-GUIDE.md`
- Art direction and graphic language: `references/VISUAL-LANGUAGE.md`
- Coding and asset implementation: `references/IMPLEMENTATION.md`
- Verification: `references/QA-CHECKLIST.md`
- Historical research links: `references/SOURCES.md`

## Invocation examples

- “Turn https://example.com into a convincing 1997 website. Keep all the existing content and functionality.”
- “Give this SaaS site a late-90s tech-company aesthetic, but don't make it look like a GeoCities joke.”
- “Research my website and redesign it as if it launched in 1996.”
- “Make this site feel like a 1998 web portal, including historically appropriate graphics.”

If the user specifies a year, honor it. If they specify only “90s,” choose the best-fit period after inspecting the business and explain the choice.
