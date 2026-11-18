# Visual language and art direction

## The art-director's job

Translate a real business into a plausible 1990s web genre. Do not simply decorate the current design. Decide what the business would have looked like if it had launched on the web in the selected year, given its audience, budget, category, and purpose.

## 1. Layout vocabulary

Choose a primary structure:

- **Document flow:** text and links in a simple vertical reading order.
- **Fixed central canvas:** a constrained page width with a centered or left-aligned composition.
- **Masthead + left rail:** branded top area, vertical navigation, main content column.
- **Portal grid:** dense categorized columns and link collections.
- **Editorial columns:** headline, article body, sidebars, image captions, section rules.
- **Catalogue:** category navigation, product rows/grids, prices, compact purchase actions.
- **Table-like composition:** visually aligned rows and columns, implemented with modern CSS Grid/Flexbox unless actual tabular data requires semantic tables.

Do not force a fixed desktop canvas to overflow on phones. Preserve the period desktop composition while reflowing gracefully on smaller screens.

## 2. Color

Build a palette with roles, not random nostalgia colors:

- Page background
- Main text
- Link / visited-link colors
- Masthead or brand panel
- Secondary panel
- Accent / callout
- Borders and rules
- Optional texture

Historically plausible families include:

- Early web: white/light gray, black, blue links, restrained accent colors.
- Personal homepage: vivid primaries, saturated purple/teal, patterned backgrounds, high contrast.
- Corporate late-90s: navy, deep blue, teal, burgundy, muted gold, gray, white, gradient or beveled accents.
- Editorial: paper-like neutrals, strong black typography, one or two saturated accents.

Do not default to neon. The right palette depends on the reference site and business category. Maintain readable contrast.

## 3. Typography

- Prefer system fonts plausibly available in the period: Times New Roman, Arial, Verdana, Georgia, Trebuchet MS, Courier New, and generic serif/sans-serif/monospace stacks.
- Use bitmap/pixel fonts selectively for tiny labels, decorative badges, or a specific gaming/personal-web direction. Avoid using them for long body copy.
- Create hierarchy through size, weight, color, underlining, capitalization, and spacing.
- Avoid importing a contemporary display font unless the user explicitly wants a modern-retro hybrid.

## 4. Links and navigation

- Links should look and behave like links. Underlines and clear hover/focus states are historically plausible and accessible.
- Navigation may use text links, compact button-like images, tabs, sidebars, or categorized lists depending on lineage.
- Preserve clear current-page indication.
- Do not hide navigation behind novelty interactions.

## 5. Borders, panels, and depth

Possible period treatments:

- 1px rules and beveled borders
- Inset/outset button edges
- Framed image panels
- Solid color blocks and nested panels
- Simple horizontal rules and dotted/dashed dividers
- Small drop shadows only where the historical reference supports them

Avoid modern soft-shadow card systems and huge rounded corners unless a specific late-90s reference justifies the treatment.

## 6. Graphics and motifs

Use a controlled asset vocabulary. Each graphic should have a reason to exist.

Possible asset types:

- Small pixel icons and bitmap pictograms
- Handcrafted wordmarks or logo lockups
- Horizontal divider strips
- Tiny repeating textures
- Image navigation tabs/buttons
- Product cutouts and low-resolution thumbnails
- Technical diagrams and annotated screenshots
- Starbursts, stamps, badges, arrows, bullets, and ornamental rules
- Original animated GIFs with restrained motion

Select motifs based on the website's subject. Examples:

- Software: terminal windows, schematic diagrams, floppy disks, compact computer illustrations, interface screenshots, technical callouts.
- Finance: charts, ledger motifs, calculator imagery, market-data panels, restrained institutional color.
- Creative agency: portfolio thumbnails, editorial typography, handmade studio graphics, compact project index.
- Retail: catalogue photography, product labels, category badges, price blocks.
- Food: menu panels, ingredient illustrations, product photography, warm palette.

Avoid unrelated clip-art. A spaceship, globe, cursor hand, or pixel heart is not automatically appropriate because the site is retro.

## 7. Motion and novelty

Use animation only when it reinforces the chosen direction:

- A subtle animated badge or tiny illustrative loop can feel period-appropriate.
- Marquee-like motion may be used for a nonessential decorative ticker only if the user wants that flavor.
- Do not animate primary copy, critical information, or navigation in a way that harms comprehension.
- Respect `prefers-reduced-motion`; provide a static alternative.
- No rapid flashing, strobing, or seizure-risk effects.
- No auto-playing sound.

## 8. Texture and image quality

- Small repeating textures can be effective, but check seams and contrast.
- Intentional pixelation is acceptable for period graphics; accidental blurry scaling is not.
- Avoid applying a global CRT/noise filter to all content. Use scanlines or display effects only for a specific concept and sparingly.
- Use consistent image borders, captions, and aspect ratios.
- Do not use a generic stock image simply to fill a column.

## 9. Token sheet template

Write tokens in the project's existing system. Example structure:

```css
:root {
  --retro-page: #f3f0e6;
  --retro-ink: #171717;
  --retro-link: #0000ee;
  --retro-visited: #551a8b;
  --retro-brand: #183c70;
  --retro-panel: #d9e3ed;
  --retro-accent: #c64b32;
  --retro-rule: #777;
  --retro-content-width: 960px;
}
```

These values are placeholders, not a default palette. Choose tokens from the reference direction and existing brand context.

## 10. Final art-direction test

Ask:

- Could this plausibly have been made in the chosen year?
- Does it look like a real site in its business category, rather than a costume?
- Are the graphics specific to the site's subject?
- Is the visual system consistent across every route?
- Does the design still make the business understandable and credible?
- Does it feel intentionally period-specific at first glance, without relying on a single gimmick?
