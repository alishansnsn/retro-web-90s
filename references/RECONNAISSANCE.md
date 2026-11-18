# Website reconnaissance protocol

## Objective

Understand what the website is, who it serves, what it says, and what must continue to work before changing its visual language.

## Inspection order

1. Homepage: title, hero, primary CTA, navigation, first-screen hierarchy, below-fold sections, footer.
2. Main conversion pages: product/service details, pricing, booking/demo/contact, checkout or signup.
3. Trust and context: about, team, case studies, testimonials, portfolio, FAQ, policies.
4. Supporting content: blog, resources, documentation, press, careers.
5. Interactive states: mobile menu, dropdowns, forms, tabs, accordions, search, filters, modals, logged-in areas if authorized.

Use the browser to inspect the rendered page. HTML extraction is useful for content and link discovery but cannot reliably reveal visual hierarchy, responsive behavior, dynamic content, or interaction states.

## What to record

### Business model

- Organization and product/service names
- B2B/B2C, industry, market, geography if relevant
- Target audience and their likely knowledge level
- User problem and offered outcome
- Revenue/conversion model
- Main conversion and supporting actions
- Differentiators and proof points

### Content architecture

- Route and page title
- Page purpose
- Main heading and supporting message
- Key sections and order
- Primary/secondary CTA
- Important images, diagrams, data, or media
- Internal and external links

### Brand system

- Existing logo and variants
- Brand colors and usage
- Fonts and typographic character
- Illustration/photography style
- Voice and vocabulary
- Existing design tokens/components

### Technical and functional inventory

- Framework, build tool, router, styling approach
- Package manager and scripts
- Shared layout and component entry points
- Forms, validation, API calls, server actions
- Authentication and authorization
- Payments, CRM, analytics, email, search, maps, embedded tools
- SEO metadata, structured data, canonical URLs
- Responsive breakpoints and navigation behavior

## URL crawl guidance

- Prefer sitemap.xml for route discovery. Check robots.txt and honor crawl restrictions.
- Stay on the supplied host unless the user explicitly asks to inspect linked properties.
- Avoid submitting forms, triggering purchases, creating accounts, or changing remote state during reconnaissance.
- Limit crawl depth and page count. Prioritize navigation and high-value routes.
- Query-string variants, pagination, filters, and tracking URLs should not explode the crawl. Normalize URLs and avoid duplicate content.
- Do not attempt to bypass login, paywalls, bot protection, or access controls.

The bundled `scripts/crawl_site.py` is a best-effort static HTML crawler. It extracts titles, descriptions, headings, visible-ish text, internal links, and image references. It is not a headless browser and will miss JavaScript-rendered content.

## Evidence discipline

Classify findings:

- **Observed:** directly visible or present in source.
- **Inferred:** likely, but not explicitly confirmed.
- **Unknown:** cannot be established from available evidence.

Never convert inferred or unknown details into public-facing copy. Preserve existing claims verbatim unless asked to rewrite them.

## Audit output template

```md
# Site audit
## Business and audience
## Main conversion and user journey
## Page/route inventory
## Content hierarchy
## Existing brand assets
## Functional behavior to preserve
## Technical stack and constraints
## Observed / inferred / unknown
## Risks and open questions
```
