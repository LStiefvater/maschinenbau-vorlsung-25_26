#!/usr/bin/env python3
"""
Build script for GitHub Pages deployment.

Produces _site/ with:
  - src/dhbw-base.css          (copied)
  - lessons/<folder>/<file>    (copied + back-nav injected)
  - index.html                 (generated overview in DHBW style)
"""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS_DIR = ROOT / "lessons"
SRC_DIR = ROOT / "src"
SITE_DIR = ROOT / "_site"

# ── Helpers ──────────────────────────────────────────────────────────────────

def clean_title(folder_name: str) -> str:
    """Convert e.g. 'V01-Binaeres-Zahlensystem' → 'Binäres Zahlensystem'."""
    # Strip leading Vxx- part
    name = re.sub(r"^V\d+-", "", folder_name)
    return name.replace("-", " ")


def extract_hero_title(html: str) -> str | None:
    """Extract the text of <h1 class="dhbw-hero__title">…</h1>."""
    m = re.search(r'<h1[^>]*class="dhbw-hero__title"[^>]*>(.*?)</h1>', html, re.DOTALL)
    if m:
        # Strip any inner tags (e.g. <br>)
        return re.sub(r"<[^>]+>", " ", m.group(1)).strip()
    return None


def extract_lesson_number(folder_name: str) -> str:
    """Return zero-padded number from folder name, e.g. 'V01-…' → '01'."""
    m = re.match(r"V(\d+)", folder_name)
    return m.group(1) if m else "??"


def inject_back_nav(html: str) -> str:
    """
    Inject a '← Zur Übersicht' link into the DHBW header.

    - If a <nav class="dhbw-header__nav"> already exists, prepend the link
      as the first child (before Theorie/Praxis links).
    - If no nav exists, insert a new <nav> after the logo </a>.
    """
    back_link = '<a href="../../index.html" class="dhbw-header__nav-link">&#8592; Zur Übersicht</a>'

    # Case 1: existing nav block
    existing_nav = re.search(r'(<nav\s+class="dhbw-header__nav">)', html)
    if existing_nav:
        return html.replace(
            existing_nav.group(1),
            existing_nav.group(1) + "\n        " + back_link,
            1,
        )

    # Case 2: no nav – insert after logo closing </a>
    logo_end = re.search(
        r'(</a>\s*\n\s*</div>\s*\n\s*</header>)',
        html,
    )
    if logo_end:
        nav_block = (
            f"\n      <nav class=\"dhbw-header__nav\">\n"
            f"        {back_link}\n"
            f"      </nav>"
        )
        return html[: logo_end.start()] + "</a>" + nav_block + html[logo_end.start() + 4 :]

    # Fallback: insert before closing </div> of dhbw-header__inner
    inner_close = re.search(
        r'(</a>)(\s*\n\s*</div>\s*\n\s*</header>)',
        html,
    )
    if inner_close:
        nav_block = (
            f"\n      <nav class=\"dhbw-header__nav\">\n"
            f"        {back_link}\n"
            f"      </nav>"
        )
        replacement = inner_close.group(1) + nav_block + inner_close.group(2)
        return html[: inner_close.start()] + replacement + html[inner_close.end() :]

    return html  # unchanged if no pattern matched


# ── Discovery ────────────────────────────────────────────────────────────────

def discover_lessons() -> list[dict]:
    """
    Scan lessons/ and return sorted list of lesson descriptors:
      { folder, number, title, skript, praxis }
    """
    lessons = []
    for folder in sorted(LESSONS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        html_files = sorted(folder.glob("*.html"))
        if not html_files:
            continue

        skript = next((f for f in html_files if f.name.endswith("_skript.html")), None)
        praxis = next((f for f in html_files if f.name.endswith("_praxis.html")), None)

        # Use hero title from skript if available, else folder-derived title
        title = None
        if skript:
            title = extract_hero_title(skript.read_text(encoding="utf-8"))
        if not title and praxis:
            title = extract_hero_title(praxis.read_text(encoding="utf-8"))
        if not title:
            title = clean_title(folder.name)

        lessons.append(
            {
                "folder": folder,
                "number": extract_lesson_number(folder.name),
                "title": title,
                "skript": skript,
                "praxis": praxis,
            }
        )
    return lessons


# ── Index page generator ─────────────────────────────────────────────────────

def lesson_card(lesson: dict) -> str:
    num = lesson["number"]
    title = lesson["title"]
    folder_name = lesson["folder"].name

    skript_link = ""
    if lesson["skript"]:
        href = f"lessons/{folder_name}/{lesson['skript'].name}"
        skript_link = (
            f'<a href="{href}" class="dhbw-btn">Skript</a>'
        )

    praxis_link = ""
    if lesson["praxis"]:
        href = f"lessons/{folder_name}/{lesson['praxis'].name}"
        praxis_link = (
            f'<a href="{href}" class="dhbw-btn dhbw-btn--outline">Praxis</a>'
        )

    return f"""
      <article class="lesson-card">
        <div class="lesson-card__number">V{num}</div>
        <div class="lesson-card__body">
          <h2 class="lesson-card__title">{title}</h2>
          <div class="lesson-card__links">
            {skript_link}
            {praxis_link}
          </div>
        </div>
      </article>"""


def generate_index(lessons: list[dict]) -> str:
    cards = "\n".join(lesson_card(l) for l in lessons)
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Informatik-Grundlagen · Maschinenbau | DHBW Stuttgart</title>
  <link rel="stylesheet" href="src/dhbw-base.css">
  <style>
    /* ── Übersichtsseite ───────────────────────────────────── */
    .lessons-grid {{
      max-width: var(--slide-w, 900px);
      margin: 0 auto;
      padding: var(--sp-6) var(--sp-4);
      display: flex;
      flex-direction: column;
      gap: var(--sp-4);
    }}

    .lesson-card {{
      display: flex;
      align-items: flex-start;
      gap: var(--sp-5);
      background: var(--surface, #fff);
      border: 1px solid var(--border, #e0e0e0);
      border-left: 4px solid var(--red, #E2001A);
      border-radius: var(--r-card, 6px);
      padding: var(--sp-5) var(--sp-6);
      box-shadow: var(--shadow-card, 0 1px 4px rgba(0,0,0,.08));
      transition: box-shadow .15s;
    }}

    .lesson-card:hover {{
      box-shadow: 0 4px 14px rgba(0,0,0,.12);
    }}

    .lesson-card__number {{
      flex-shrink: 0;
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--red, #E2001A);
      min-width: 3rem;
      line-height: 1.2;
    }}

    .lesson-card__body {{
      flex: 1;
    }}

    .lesson-card__title {{
      margin: 0 0 var(--sp-3);
      font-size: 1.125rem;
      font-weight: 600;
      color: var(--text, #1a1a1a);
    }}

    .lesson-card__links {{
      display: flex;
      gap: var(--sp-3);
      flex-wrap: wrap;
    }}

    /* ── Buttons ───────────────────────────────────────────── */
    .dhbw-btn {{
      display: inline-block;
      padding: .45em 1.1em;
      border-radius: var(--r-btn, 4px);
      font-size: .875rem;
      font-weight: 600;
      text-decoration: none;
      transition: background .15s, color .15s, border-color .15s;
      background: var(--red, #E2001A);
      color: #fff;
      border: 2px solid var(--red, #E2001A);
    }}

    .dhbw-btn:hover {{
      background: #b50015;
      border-color: #b50015;
    }}

    .dhbw-btn--outline {{
      background: transparent;
      color: var(--red, #E2001A);
    }}

    .dhbw-btn--outline:hover {{
      background: var(--red, #E2001A);
      color: #fff;
    }}

    @media (max-width: 600px) {{
      .lesson-card {{
        flex-direction: column;
        gap: var(--sp-2);
      }}
    }}
  </style>
</head>
<body>

  <header class="dhbw-header">
    <div class="dhbw-header__inner">
      <a href="#" class="dhbw-header__logo">
        <span class="dhbw-header__logo-text">DHBW Stuttgart</span>
      </a>
    </div>
  </header>

  <section class="dhbw-hero">
    <div class="dhbw-hero__inner">
      <p class="dhbw-hero__label">Kursübersicht · Informatik-Grundlagen · Maschinenbau</p>
      <h1 class="dhbw-hero__title">Alle Vorlesungen</h1>
      <p class="dhbw-hero__subtitle">Skript und Praxisaufgaben für jede Einheit – direkt im Browser</p>
      <p class="dhbw-hero__meta">WS 2025/26 &nbsp;·&nbsp; DHBW Stuttgart</p>
    </div>
  </section>

  <main>
    <div class="lessons-grid">
{cards}
    </div>
  </main>

</body>
</html>
"""


# ── Build ─────────────────────────────────────────────────────────────────────

def build():
    # 1. Clean and recreate _site/
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    # 2. Copy src/
    shutil.copytree(SRC_DIR, SITE_DIR / "src")
    print(f"Copied src/ → _site/src/")

    # 3. Discover lessons
    lessons = discover_lessons()
    print(f"Found {len(lessons)} lesson folders")

    # 4. Process each HTML file
    for lesson in lessons:
        folder_name = lesson["folder"].name
        dest_folder = SITE_DIR / "lessons" / folder_name
        dest_folder.mkdir(parents=True, exist_ok=True)

        for html_file in lesson["folder"].glob("*.html"):
            src_text = html_file.read_text(encoding="utf-8")
            out_text = inject_back_nav(src_text)
            dest = dest_folder / html_file.name
            dest.write_text(out_text, encoding="utf-8")
            injected = "✓" if out_text != src_text else "–"
            print(f"  [{injected}] lessons/{folder_name}/{html_file.name}")

        # Copy any non-HTML assets (images, etc.) inside the lesson folder
        for asset in lesson["folder"].rglob("*"):
            if asset.is_file() and asset.suffix.lower() not in (".html",):
                rel = asset.relative_to(lesson["folder"])
                dest = dest_folder / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(asset, dest)

    # 5. Generate index.html
    index_html = generate_index(lessons)
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"Generated _site/index.html ({len(lessons)} lessons)")

    print(f"\nBuild complete → {SITE_DIR}")


if __name__ == "__main__":
    build()
