# SVCAF Site Scripts

## integrity-scan.py

Scans all Hugo posts for site integrity issues.

### What it checks
- **Missing local images** — `/wp-content/uploads/` paths referenced in posts but file not in `static/`
- **External CDN images** — Images hosted on 3rd-party CDNs (LinkedIn, etc.) that may expire
- **Duplicate images** — Same image appearing at top AND in body of post
- **Posts missing images** — Event/Chinese-language posts with no images at all

### Usage
```bash
# Quick scan with report
python scripts/integrity-scan.py --report

# JSON output (for automation)
python scripts/integrity-scan.py --json

# Run from repo root
cd /path/to/svcaf-site && python scripts/integrity-scan.py
```

### Exit codes
- `0` — No critical issues (missing files or duplicates)
- `1` — Critical issues found

### GitHub Actions
- Runs on every push to main
- Runs every Monday at 10am UTC
- Can be triggered manually via Actions tab
- Report uploaded as artifact after each run
