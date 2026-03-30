#!/usr/bin/env python3
"""
SVCAF Site Integrity Scanner
Checks: missing images, external CDN links, duplicate images, tag validation.
Usage: python scripts/integrity-scan.py [--report] [--json]
"""

import os, re, glob, sys, argparse, json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
POSTS_DIR = BASE_DIR / 'content' / 'posts'
STATIC_DIR = BASE_DIR / 'static'
REPORT_FILE = BASE_DIR / 'integrity-report.md'

# ── Tag vocabulary ──────────────────────────────────────────────────────────
VALID_TAGS = {
    'civic-education','education-policy','immigration','election-law','legal-rights',
    'healthcare','firearm-safety','advocacy','community-action','legislation',
    'affirmative-action','sffa-lawsuit','election-integrity','ai4legislation',
    'community-events','awards','chinese-american','anti-discrimination','volunteer',
    'ai-technology','svcaf-news'
}

# High-risk tags that are frequently misapplied — require keyword evidence
HIGH_RISK_TAGS = {
    'healthcare':     ['hospital','medical','health','doctor','nurse','clinic','kaiser',
                       'covid','pandemic','mask','ppe','vaccine','医疗','医院','健康'],
    'firearm-safety': ['firearm','gun','shooting','weapon','枪','射击'],
    'volunteer':      ['volunteer','donation','donate','志愿','捐'],
    'immigration':    ['immigration','visa','green card','citizen','移民','签证'],
    'ai-technology':  ['artificial intelligence','openclaw','chatgpt','人工智能','machine learning',
                       'ai4','ai coding','ai tool','ai model','ai programming','ai agent',
                       'coding tool','large language'],
    'awards':         ['award','honor','recognition','prize','winner','奖','荣誉'],
    'sffa-lawsuit':   ['sffa','harvard','unc','north carolina','supreme court','哈佛','最高法院'],
}

def find_all_posts():
    return sorted(glob.glob(str(POSTS_DIR / '*.md')))

def get_images(content):
    return re.findall(r'!\[[^\]]*\]\(([^\)]+)\)', content)

def is_external(url):
    return url.startswith('http://') or url.startswith('https://')

def local_exists(img_path):
    if img_path.startswith('/wp-content/uploads/'):
        p = STATIC_DIR / img_path.lstrip('/')
        return p.exists() and p.stat().st_size > 100
    return True

def get_tags(content):
    m = re.match(r'^---\n(.*?)---\n', content, re.DOTALL)
    if not m: return []
    fm = m.group(1)
    t = re.search(r"tags:\s*\[([^\]]+)\]", fm)
    if t:
        return [x.strip().strip("'\"") for x in t.group(1).split(',')]
    lines = re.findall(r"tags:\s*\n((?:[ \t]+-[ \t]+\S+\n?)+)", fm)
    if lines:
        return re.findall(r"-\s+(\S+)", lines[0])
    return []

def duplicate_at_top(content, fm_end):
    after = content[fm_end:].strip()
    m = re.match(r'^(!\[[^\]]*\]\(([^\)]+)\))', after)
    if not m: return False, None
    img = m.group(2)
    return img in after[len(m.group(1)):], img

def scan():
    issues = {
        'missing_images': [],
        'external_images': [],
        'duplicate_images': [],
        'no_images': [],
        'tag_issues': [],
    }

    for md_file in find_all_posts():
        slug = Path(md_file).stem
        if slug in ('_index',):  # skip index files
            continue
        content = open(md_file, encoding='utf-8').read()
        fm_match = re.match(r'^---\n.*?---\n', content, re.DOTALL)
        fm_end = fm_match.end() if fm_match else 0
        images = get_images(content)

        # Missing local images
        for img in images:
            if not is_external(img) and img.startswith('/wp-content/') and not local_exists(img):
                issues['missing_images'].append((slug, img))

        # External CDN images (non-YouTube)
        for img in images:
            if is_external(img) and not any(k in img for k in ['youtube.com','youtu.be']):
                issues['external_images'].append((slug, img[:90]))

        # Duplicate image at top
        if fm_end:
            is_dup, dup = duplicate_at_top(content, fm_end)
            if is_dup:
                issues['duplicate_images'].append((slug, dup))

        # Posts with no images that probably should have some
        if not images:
            has_cn = bool(re.search(r'[\u4e00-\u9fff]', content))
            is_event = any(k in slug for k in ['event','gala','forum','seminar','meeting','party'])
            if has_cn or is_event:
                issues['no_images'].append(slug)

        # Tag validation
        tags = get_tags(content)
        if len(tags) != 3:
            issues['tag_issues'].append((slug, f"has {len(tags)} tags (expected 3): {tags}"))
        for tag in tags:
            if tag not in VALID_TAGS:
                issues['tag_issues'].append((slug, f"unknown tag '{tag}' — not in 23-tag vocabulary"))
        body = content.lower()
        for tag in tags:
            if tag in HIGH_RISK_TAGS:
                if not any(kw in body for kw in HIGH_RISK_TAGS[tag]):
                    issues['tag_issues'].append((slug, f"suspicious tag '{tag}' — no supporting keywords in post body"))

    return issues

def report(issues):
    lines = ['# SVCAF Site Integrity Report\n']
    total = sum(len(v) for v in issues.values())
    lines.append(f'**Total issues: {total}**\n')

    def section(key, emoji, title, fmt):
        items = issues[key]
        if items:
            lines.append(f'\n## {emoji} {title} ({len(items)})\n')
            for item in items:
                lines.append(f'- {fmt(item)}')
        else:
            lines.append(f'\n## ✅ {title} — All clear\n')

    section('missing_images',   '❌', 'Missing Local Images',
            lambda x: f'`{x[0]}`: `{x[1]}`')
    section('duplicate_images', '❌', 'Duplicate Images at Top',
            lambda x: f'`{x[0]}`: `{x[1]}`')
    section('tag_issues',       '🏷️', 'Tag Issues',
            lambda x: f'`{x[0]}`: {x[1]}')
    section('external_images',  '⚠️', 'External CDN Images (may expire)',
            lambda x: f'`{x[0]}`: `{x[1]}`')
    section('no_images',        'ℹ️', 'Posts With No Images',
            lambda x: f'`{x}`')

    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', action='store_true')
    parser.add_argument('--json',   action='store_true')
    args = parser.parse_args()

    print('🔍 Scanning SVCAF site...')
    issues = scan()

    if args.json:
        print(json.dumps(issues, indent=2, default=str))
    else:
        out = report(issues)
        print(out)
        if args.report:
            REPORT_FILE.write_text(out, encoding='utf-8')
            print(f'\nReport saved to {REPORT_FILE}')

    critical = (len(issues['missing_images']) + len(issues['duplicate_images']) +
                sum(1 for _, m in issues['tag_issues'] if 'unknown tag' in m or 'has ' in m))
    if critical:
        print(f'\n⚠️  {critical} critical issues found.')
        sys.exit(1)
    else:
        warnings = len(issues['external_images']) + sum(1 for _, m in issues['tag_issues'] if 'suspicious' in m)
        print(f'\n✅ No critical issues. {warnings} warnings.')
        sys.exit(0)

if __name__ == '__main__':
    main()
