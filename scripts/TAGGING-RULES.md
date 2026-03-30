# SVCAF Tagging Rules

## The 23-Tag Controlled Vocabulary

Every post must have **exactly 3 tags** from this list. Tags enable semantic search, topic clustering, and content discovery.

| Tag | When to Use | Keywords to Look For |
|-----|-------------|----------------------|
| **civic-education** | Educational content about civic participation, government processes, voting rights | civic, participation, democracy, voting, government, citizen education |
| **education-policy** | K-12, college admissions, merit-based systems, education equity | school, college, admissions, test scores, merit, equity, AA-22 |
| **immigration** | Immigration law, visa issues, citizenship, border policy | immigration, visa, green card, citizenship, border, 移民, 签证 |
| **election-law** | Voting rights, ballot measures, election integrity, redistricting | voting, ballot, election, redistricting, voter ID, electoral |
| **legal-rights** | Civil rights, discrimination law, constitutional rights | civil rights, constitution, discrimination, legal protection, lawsuit |
| **healthcare** | Health policy, medical access, public health (NOT general wellness) | hospital, medical, health policy, doctor, nurse, Covid, pandemic, 医疗, 医院 |
| **firearm-safety** | Gun safety education, Second Amendment, responsible ownership | firearm, gun, shooting, weapon, safety training, 枪, 射击 |
| **advocacy** | Lobbying, policy campaigns, grassroots organizing (action-oriented) | lobby, campaign, petition, advocacy, grassroots, organizing |
| **community-action** | Volunteer projects, community service, local initiatives | volunteer project, community service, neighborhood, local action |
| **legislation** | Bills, laws, legislative process, policy analysis | bill, law, legislation, congress, senate, assembly, policy |
| **affirmative-action** | Race-based admissions, AA policy debates (generic education equity) | affirmative action, race-conscious, diversity, equity in admissions |
| **sffa-lawsuit** | Students for Fair Admissions cases (Harvard, UNC, Supreme Court) | SFFA, Harvard, UNC, North Carolina, Supreme Court, 哈佛, 最高法院 |
| **election-integrity** | Vote security, election fraud prevention, ballot accuracy | election security, fraud, ballot integrity, vote counting, audits |
| **ai4legislation** | SVCAF's AI4Legislation project (AI tools for civic engagement) | AI4Legislation, BillTrack50, civic tech, AI tools, legislation tracking |
| **community-events** | SVCAF-organized events (galas, forums, seminars, picnics) | gala, forum, seminar, picnic, fundraiser, event, 活动 |
| **awards** | Voice of Chinese Americans Award, honors, recognitions | award, honor, recognition, prize, winner, 奖, 荣誉 |
| **chinese-american** | Content specifically about Chinese American community/culture | Chinese American, 华裔, 华人, community identity, heritage |
| **anti-discrimination** | Fighting bias, racial justice, equality advocacy | discrimination, bias, racism, equality, justice, prejudice |
| **volunteer** | Volunteer recruitment, donation appeals, service opportunities | volunteer, donation, donate, fundraising, 志愿, 捐 |
| **ai-technology** | AI tools, automation, tech innovation (NOT ai4legislation) | AI, artificial intelligence, OpenClaw, ChatGPT, automation, 人工智能 |
| **svcaf-news** | Internal SVCAF updates, board announcements, org milestones | SVCAF update, board, announcement, milestone, organization news |

---

## Tag Selection Guidelines

### Rule 1: Exactly 3 Tags
- Too few = under-categorized
- Too many = dilutes signal
- If post spans 4+ topics → pick the 3 most prominent

### Rule 2: Read the Body, Not Just the Title
Titles can be misleading. Always scan the full post for keywords before tagging.

### Rule 3: Prefer Specific Over General
- ✅ `sffa-lawsuit` > `affirmative-action` (when Harvard/UNC mentioned)
- ✅ `ai4legislation` > `ai-technology` (when project-specific)
- ✅ `firearm-safety` > `civic-education` (when guns are the focus)

### Rule 4: High-Risk Tags Require Evidence
These tags trigger semantic validation—the post MUST contain supporting keywords:

| Tag | Required Evidence |
|-----|-------------------|
| `healthcare` | hospital, medical, health policy, doctor, nurse, Covid, pandemic, 医疗, 医院 |
| `firearm-safety` | firearm, gun, shooting, weapon, 枪, 射击 |
| `volunteer` | volunteer, donation, donate, 志愿, 捐 |
| `immigration` | immigration, visa, green card, citizenship, 移民, 签证 |
| `ai-technology` | AI, artificial intelligence, OpenClaw, ChatGPT, 人工智能 |
| `awards` | award, honor, recognition, prize, winner, 奖, 荣誉 |
| `sffa-lawsuit` | SFFA, Harvard, UNC, North Carolina, Supreme Court, 哈佛, 最高法院 |

If you tag a post `healthcare` but it never mentions medical/health terms → **validation fails**.

---

## Common Mistakes

### ❌ Don't Tag `healthcare` for General Wellness Posts
```
BAD: "Community picnic promotes healthy living" → healthcare ❌
GOOD: "Community picnic promotes healthy living" → community-events, community-action, chinese-american ✅
```

### ❌ Don't Tag `sffa-lawsuit` for Generic Education Posts
```
BAD: "Merit-based admissions debate" → sffa-lawsuit ❌
GOOD: "Merit-based admissions debate" → education-policy, affirmative-action, advocacy ✅
```

### ❌ Don't Tag `volunteer` for Advocacy Posts
```
BAD: "Join our lobbying campaign" → volunteer ❌
GOOD: "Join our lobbying campaign" → advocacy, community-action, legislation ✅
```

### ❌ Don't Tag Based on Organization, Tag Based on Content
```
BAD: "SVCAF hosts AI seminar" → svcaf-news ❌ (that's an event, not org news)
GOOD: "SVCAF hosts AI seminar" → community-events, ai4legislation, civic-education ✅
```

### ✅ When in Doubt, Search Existing Posts
```bash
# Find similar posts and see how they're tagged
grep -r "Harvard lawsuit" content/posts/*.md
```

---

## Validation Workflow

### Before Committing Tag Changes

1. **Run the integrity scanner:**
   ```bash
   python scripts/integrity-scan.py --report
   ```

2. **Review validation failures:**
   - Tag count errors (not 3)
   - Unknown tags (not in vocabulary)
   - Semantic mismatches (tag doesn't fit content)

3. **Show 10-15 sample posts to Chunhua** before bulk commits:
   ```bash
   # Show posts with tag changes
   git diff --name-only | head -15 | xargs -I{} echo "File: {}" && cat {}
   ```

4. **Fix errors, re-run scanner, then commit**

---

## Emergency Override (Use Sparingly)

If a post MUST use a non-standard tag for legitimate reasons:
1. Document why in a `# TAGGING OVERRIDE` comment in the front matter
2. Get approval from Chunhua
3. Add the tag to `VALID_TAGS` in `scripts/integrity-scan.py`

Example:
```yaml
---
title: "Post Title"
tags: ['civic-education', 'special-project', 'chinese-american']
# TAGGING OVERRIDE: special-project approved by Chunhua 2026-03-29 for one-time use
---
```

---

## Tag Analytics (Future)

Once tagging is complete, we can:
- Build tag-based navigation on svcaf.org
- Generate "Related Posts" recommendations
- Create topic landing pages (e.g., `/tags/sffa-lawsuit/`)
- Track engagement by topic category
- Power semantic search with vector embeddings

**Tags are infrastructure.** Get them right now, benefit forever.
