#!/usr/bin/env python3
"""
SVCAF Site Integrity Scanner
Detects broken images, missing files, duplicate images, and external CDN links.
Run: python scripts/integrity-scan.py [--report] [--fix-duplicates]
"""

import os, re, glob, sys, argparse, json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
POSTS_DIR = BASE_DIR / 'content' / 'posts'
STATIC_DIR = BASE_DIR / 'static'
REPORT_FILE = BASE_DIR / 'integrity-report.md'

def find_all_posts():
    return sorted(glob.glob(str(POSTS_DIR / '*.md')))

def get_images_from_post(content):
    """Return all image URLs referenced in a markdown post."""
    return re.findall(r'!\[[^\]]*\]\(([^\)]+)\)', content)

def check_local_image(img_path, static_dir):
    """Check if a local /wp-content/uploads/... image exists on disk."""
    if img_path.startswith('/wp-content/uploads/'):
        full = static_dir / img_path.lstrip('/')
        return full.exists() and full.stat().st_size > 100
    return True  # non-local, skip disk check

def is_external_url(img_path):
    return img_path.startswith('http://') or img_path.startswith('https://')

def has_duplicate_image_at_top(content, front_matter_end):
    """Detect if the same image appears right after front matter AND again in body."""
    after_fm = content[front_matter_end:].strip()
    m = re.match(r'^(!\[[^\]]*\]\(([^\)]+)\))', after_fm)
    if not m:
        return False, None
    top_img = m.group(2)
    rest = after_fm[len(m.group(1)):]
    return top_img in rest, top_img

def scan_all_posts(static_dir, verbose=True):
    issues = {
        'missing_local_images': [],
        'external_images': [],
        'duplicate_images': [],
        'posts_no_images': [],
    }

    posts = find_all_posts()
    for md_file in posts:
        content = open(md_file).read()
        slug = Path(md_file).stem

        # Find front matter end
        fm_match = re.match(r'^---\n.*?---\n', content, re.DOTALL)
        fm_end = fm_match.end() if fm_match else 0

        images = get_images_from_post(content)

        # Check for missing local images
        for img in images:
            if not is_external_url(img) and img.startswith('/wp-content/'):
                if not check_local_image(img, static_dir):
                    issues['missing_local_images'].append((slug, img))

        # Check for external/CDN images
        for img in images:
            if is_external_url(img):
                known_ok = ['youtube.com', 'youtu.be']
                if not any(k in img for k in known_ok):
                    issues['external_images'].append((slug, img[:80]))

        # Check for duplicates at top
        if fm_end > 0:
            is_dup, dup_img = has_duplicate_image_at_top(content, fm_end)
            if is_dup:
                issues['duplicate_images'].append((slug, dup_img))

        # Posts with zero images (might be missing featured image)
        if not images:
            # Only flag posts that likely should have images (has Chinese content or is an event)
            if re.search(r'[\u4e00-\u9fff]', content) or 'event' in slug or 'gala' in slug or 'forum' in slug or 'seminar' in slug:
                issues['posts_no_images'].append(slug)

    return issues

def generate_report(issues):
    lines = ['# SVCAF Site Integrity Report\n']

    total = sum(len(v) for v in issues.values())
    lines.append(f'**Total issues found: {total}**\n')

    # Missing local images
    if issues['missing_local_images']:
        lines.append(f'\n## ❌ Missing Local Images ({len(issues["missing_local_images"])})\n')
        lines.append('These files are referenced in posts but not found in static/:\n')
        for slug, img in issues['missing_local_images']:
            lines.append(f'- `{slug}`: `{img}`')
    else:
        lines.append('\n## ✅ Local Images — All present\n')

    # External images
    if issues['external_images']:
        lines.append(f'\n## ⚠️ External CDN Images ({len(issues["external_images"])})\n')
        lines.append('These images are hosted externally and may expire/break:\n')
        for slug, img in issues['external_images']:
            lines.append(f'- `{slug}`: `{img}`')
    else:
        lines.append('\n## ✅ External Images — None found\n')

    # Duplicates
    if issues['duplicate_images']:
        lines.append(f'\n## ⚠️ Duplicate Images at Top ({len(issues["duplicate_images"])})\n')
        for slug, img in issues['duplicate_images']:
            lines.append(f'- `{slug}`: `{img}`')
    else:
        lines.append('\n## ✅ Duplicate Images — None found\n')

    # Posts with no images
    if issues['posts_no_images']:
        lines.append(f'\n## ℹ️ Posts With No Images ({len(issues["posts_no_images"])})\n')
        lines.append('These posts may be missing photos (events/Chinese-language posts with no images):\n')
        for slug in issues['posts_no_images']:
            lines.append(f'- `{slug}`')

    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', action='store_true', help='Write integrity-report.md')
    parser.add_argument('--json', action='store_true', help='Output JSON')
    args = parser.parse_args()

    print('🔍 Scanning SVCAF site for integrity issues...')
    issues = scan_all_posts(STATIC_DIR)

    total = sum(len(v) for v in issues.values())

    if args.json:
        print(json.dumps(issues, indent=2))
    else:
        report = generate_report(issues)
        print(report)
        if args.report:
            REPORT_FILE.write_text(report)
            print(f'\nReport written to: {REPORT_FILE}')

    # Exit with error code if critical issues found
    critical = len(issues['missing_local_images']) + len(issues['duplicate_images'])
    if critical > 0:
        print(f'\n⚠️ {critical} critical issues found (missing files or duplicates)')
        sys.exit(1)
    else:
        print(f'\n✅ No critical issues. {len(issues["external_images"])} warnings (external images).')
        sys.exit(0)

if __name__ == '__main__':
    main()
