#!/usr/bin/env python3
"""Small, polite, same-host static HTML crawler for website reconnaissance.

This is a supplement to browser inspection. It does not execute JavaScript,
submit forms, authenticate, or bypass access controls.

Usage:
  python scripts/crawl_site.py https://example.com --max-pages 30 --max-depth 2 --out site-audit.json
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.robotparser
import urllib.request
import xml.etree.ElementTree as ET
from collections import deque
from html.parser import HTMLParser
from pathlib import Path

USER_AGENT = "RetroWeb90sResearchBot/1.0 (+polite site reconnaissance)"

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts, self.description = [], ""
        self.headings = []
        self.links, self.images = [], []
        self.text_parts = []
        self._title = False
        self._heading = None
        self._skip = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript", "svg"):
            self._skip += 1
        if tag == "title": self._title = True
        if tag in ("h1", "h2", "h3"):
            self._heading = [tag, []]
        if tag == "meta" and a.get("name", "").lower() == "description":
            self.description = a.get("content", "")
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.images.append({"src": a["src"], "alt": a.get("alt", "")})
    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self._skip:
            self._skip -= 1
        if tag == "title": self._title = False
        if self._heading and tag == self._heading[0]:
            self.headings.append({"tag": self._heading[0], "text": " ".join(self._heading[1]).strip()})
            self._heading = None
    def handle_data(self, data):
        value = re.sub(r"\s+", " ", data).strip()
        if not value: return
        if self._title: self.title_parts.append(value)
        if self._heading: self._heading[1].append(value)
        if not self._skip: self.text_parts.append(value)

def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml;q=0.9,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as res:
        body = res.read(2_500_000)
        return res.geturl(), res.headers.get_content_type(), body

def normalize(url):
    p = urllib.parse.urlsplit(url)
    if p.scheme not in ("http", "https"): return None
    path = re.sub(r"/{2,}", "/", p.path or "/")
    return urllib.parse.urlunsplit((p.scheme.lower(), p.netloc.lower(), path, p.query, ""))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("url")
    ap.add_argument("--max-pages", type=int, default=25)
    ap.add_argument("--max-depth", type=int, default=2)
    ap.add_argument("--delay", type=float, default=0.7)
    ap.add_argument("--out", default="site-audit.json")
    args = ap.parse_args()
    start = normalize(args.url)
    if not start: ap.error("URL must use http or https")
    origin = urllib.parse.urlsplit(start)
    host = origin.netloc
    base = f"{origin.scheme}://{host}"

    robots = urllib.robotparser.RobotFileParser()
    robots.set_url(base + "/robots.txt")
    try: robots.read()
    except Exception: pass

    queue = deque([(start, 0)])
    seen, pages, errors = set(), [], []
    while queue and len(pages) < args.max_pages:
        url, depth = queue.popleft()
        url = normalize(url)
        if not url or url in seen: continue
        seen.add(url)
        if urllib.parse.urlsplit(url).netloc != host: continue
        if not robots.can_fetch(USER_AGENT, url):
            errors.append({"url": url, "error": "Disallowed by robots.txt"})
            continue
        try:
            final_url, ctype, body = fetch(url)
            if "html" not in ctype:
                continue
            parser = PageParser()
            parser.feed(body.decode("utf-8", errors="replace"))
            page = {
                "url": final_url,
                "title": " ".join(parser.title_parts).strip(),
                "description": parser.description,
                "headings": parser.headings,
                "text_excerpt": " ".join(parser.text_parts)[:6000],
                "links": [],
                "images": [],
            }
            for href in parser.links:
                absolute = normalize(urllib.parse.urljoin(final_url, href))
                if absolute and urllib.parse.urlsplit(absolute).netloc == host:
                    page["links"].append(absolute)
                    if depth < args.max_depth and absolute not in seen:
                        queue.append((absolute, depth + 1))
            for img in parser.images:
                img["src"] = urllib.parse.urljoin(final_url, img["src"])
                page["images"].append(img)
            page["links"] = list(dict.fromkeys(page["links"]))
            pages.append(page)
            print(f"[{len(pages)}/{args.max_pages}] {final_url}")
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            errors.append({"url": url, "error": str(exc)})
        except Exception as exc:
            errors.append({"url": url, "error": f"Unexpected: {exc}"})
        time.sleep(max(0.0, args.delay))

    result = {
        "start_url": start,
        "host": host,
        "pages_crawled": len(pages),
        "pages": pages,
        "errors": errors,
        "limitations": [
            "Static HTML only; JavaScript-rendered content may be missing.",
            "No screenshots, interaction testing, authentication, or form submission.",
            "This crawl is a discovery aid, not a complete website audit."
        ]
    }
    out = Path(args.out)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {out.resolve()} ({len(pages)} pages, {len(errors)} crawl notes)")

if __name__ == "__main__":
    main()
