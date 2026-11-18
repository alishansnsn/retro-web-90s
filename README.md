# retro-web-90s

A Claude Code skill that rebuilds your website as if it launched in the 90s.

Give it a URL. It reads the real site, picks a year between 1991 and 1999, pulls up actual sites from that year on the Wayback Machine, then rebuilds your pages in plain HTML and CSS. Your copy and links stay as they are. You won't get fake visitor counters or a neon starfield.

![Five homepages, 1994 to 1999](images/all-five.png)

See them live: **[90s.pylondev.com](https://90s.pylondev.com)**

| | |
|---|---|
| **Notion, 1994** ![Notion as a 1994 page](images/notion-1994.png) | **Figma, 1996** ![Figma as a 1996 GeoCities page](images/figma-1996.png) |
| **Airbnb, 1997** ![Airbnb as a 1997 travel portal](images/airbnb-1997.png) | **Linear, 1998** ![Linear as a 1998 software site](images/linear-1998.png) |
| **Stripe, 1999** ![Stripe as a 1999 corporate site](images/stripe-1999.png) | |

These are unofficial fan redesigns, not affiliated with any of those companies.

## Install

```
git clone https://github.com/alishansnsn/retro-web-90s ~/.claude/skills/retro-web-90s
```

For Codex, clone it into `.agents/skills/retro-web-90s` inside your project.

## Use

```
/retro-web-90s https://yoursite.com
```

Or ask: "make my site look like it launched in 1997."

MIT
