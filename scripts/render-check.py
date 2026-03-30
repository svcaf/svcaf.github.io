#!/usr/bin/env python3
"""
SVCAF Render Quality Checker
Scans built HTML in public/ for known rendering problems from WP migration.

Catches:
  1. Collapsed numbered lists  (- 1. text；- 2. text all on one line)
  2. Emoji inline bullets      (✅/🔹/📌 in a <p> instead of a <li>)
  3. Broken bold markdown      (**** artifacts in output)
  4. Collapsed link lists      (<a>text</a>- <a>text</a> on same line)
  5. Long paragraphs with list indicators (likely collapsed bullet lists)

Usage: python scripts/render-check.py [--report] [--dir public/]
"""

import re, glob, sys, argparse, json
from pathlib import Path

BASE_DIR   = Path(__file__).parent.parent
PUBLIC_DIR = BASE_DIR / 'public'
REPORT_FILE = BASE_DIR / 'render-report.md'

# Only list-style bullet emojis — NOT announcement/pin emojis (📢📌) which are
# legitimately used as standalone paragraph prefixes in contact/CTA sections.
EMOJI_BULLETS = ['✅', '🔹', '◆', '♦', '▶', '▸', '🔸', '🔶', '🔷']

def find_html_files(pub_dir):
    return sorted(glob.glob(str(pub_dir / 'posts' / '**' / 'index.html'), recursive=True))

def get_slug(html_path):
    parts = Path(html_path).parts
    try:
        i = parts.index('posts')
        return '/'.join(parts[i:i+2])
    except ValueError:
        return html_path

def extract_paragraphs(html):
    """Return list of (raw_html, text_content) tuples for all <p> tags."""
    paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
    result = []
    for p in paras:
        text = re.sub(r'<[^>]+>', '', p)  # strip tags
        result.append((p, text))
    return result

def check_collapsed_numbered_list(text):
    """Detect '1. item；2. item' or '- 1. text- 2. text' in paragraph."""
    # Multiple numbered items on one line
    if len(re.findall(r'[；;]\s*-?\s*\d+\.\s+\S', text)) >= 1:
        return True
    if len(re.findall(r'-\s*\d+\.\s+', text)) >= 2:
        return True
    return False

def check_emoji_bullets(text):
    """Detect emoji being used as bullets inside a <p> (not a <li>)."""
    for emoji in EMOJI_BULLETS:
        # Emoji at start of paragraph, or after a sentence ending
        if re.search(rf'(^|[.。！？!?\n])\s*{re.escape(emoji)}\s+\S', text):
            return emoji
    return None

def check_broken_bold(html):
    """Detect **** artifacts that survived into HTML as literal asterisks.
    Check plain text only (strip tags first) to avoid false positives from
    URLs or HTML attributes containing asterisks."""
    text = re.sub(r'<[^>]+>', '', html)
    return '****' in text or bool(re.search(r'\*\*\s*\*\*', text))

def check_collapsed_link_list(html):
    """Detect </a>- <a or </a>- [text] patterns = link list not split."""
    return bool(re.search(r'</a>\s*-\s*<a\b', html))

def check_long_para_with_bullets(text):
    """Long paragraph containing multiple bullet indicators = probable collapsed list."""
    if len(text) < 300:
        return False
    bullet_count = len(re.findall(r'[；;]\s*[-•]\s+\S', text))
    return bullet_count >= 2

def scan(pub_dir):
    issues = {
        'collapsed_numbered': [],
        'emoji_bullets':      [],
        'broken_bold':        [],
        'collapsed_links':    [],
        'collapsed_bullets':  [],
    }

    for html_file in find_html_files(pub_dir):
        slug = get_slug(html_file)
        try:
            html = open(html_file, encoding='utf-8').read()
        except Exception:
            continue

        # Extract only article body (between <article> tags if possible)
        body_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
        body_html = body_match.group(1) if body_match else html

        paragraphs = extract_paragraphs(body_html)

        for p_html, p_text in paragraphs:
            if check_collapsed_numbered_list(p_text):
                issues['collapsed_numbered'].append((slug, p_text[:120]))

            emoji = check_emoji_bullets(p_text)
            if emoji:
                issues['emoji_bullets'].append((slug, emoji, p_text[:120]))

            if check_broken_bold(p_html):
                issues['broken_bold'].append((slug, p_text[:120]))

            if check_long_para_with_bullets(p_text):
                issues['collapsed_bullets'].append((slug, p_text[:120]))

        if check_collapsed_link_list(body_html):
            issues['collapsed_links'].append(slug)

    return issues

def make_report(issues):
    lines = ['# SVCAF Render Quality Report\n']
    total = sum(len(v) for v in issues.values())
    lines.append(f'**Total issues: {total}**\n')

    def section(key, emoji, title, fmt):
        items = issues[key]
        if items:
            lines.append(f'\n## {emoji} {title} ({len(items)})\n')
            for item in items:
                lines.append(f'- {fmt(item)}')
        else:
            lines.append(f'\n## ✅ {title} — None found\n')

    section('collapsed_numbered', '❌', 'Collapsed Numbered Lists',
            lambda x: f'`{x[0]}`: `{x[1]}`')
    section('emoji_bullets', '❌', 'Emoji Used as Inline Bullets (not in <li>)',
            lambda x: f'`{x[0]}` [{x[1]}]: `{x[2]}`')
    section('broken_bold', '❌', 'Broken Bold Markers (****)',
            lambda x: f'`{x[0]}`: `{x[1]}`')
    section('collapsed_links', '❌', 'Collapsed Link Lists',
            lambda x: f'`{x}`')
    section('collapsed_bullets', '⚠️', 'Probable Collapsed Bullet Lists (long para)',
            lambda x: f'`{x[0]}`: `{x[1]}`')

    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', action='store_true')
    parser.add_argument('--json',   action='store_true')
    parser.add_argument('--dir',    default=str(PUBLIC_DIR))
    args = parser.parse_args()

    pub = Path(args.dir)
    if not pub.exists():
        print(f'ERROR: {pub} does not exist. Run Hugo build first.')
        sys.exit(2)

    print(f'🎨 Scanning rendered HTML in {pub}...')
    issues = scan(pub)

    if args.json:
        print(json.dumps(issues, indent=2, default=str))
    else:
        out = make_report(issues)
        print(out)
        if args.report:
            REPORT_FILE.write_text(out, encoding='utf-8')
            print(f'\nReport saved to {REPORT_FILE}')

    critical = (len(issues['collapsed_numbered']) + len(issues['emoji_bullets']) +
                len(issues['broken_bold']) + len(issues['collapsed_links']))
    if critical:
        print(f'\n⚠️  {critical} critical render issues found.')
        sys.exit(1)
    else:
        print(f'\n✅ No critical render issues.')
        sys.exit(0)

if __name__ == '__main__':
    main()
