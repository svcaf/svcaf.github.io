# SVCAF Article Tagging Rules

Every post must have **exactly 3 tags** from the approved 23-tag vocabulary below.

## The 23-Tag Vocabulary

### 📚 Educate Pillar
| Tag | Use when the post is about… |
|---|---|
| `civic-education` | Teaching civic rights, constitutional principles, how US democracy works |
| `education-policy` | K-12/university admissions, school board, curriculum, Prop 209/ACA-5 impact |
| `immigration` | Visa, green card, citizenship, immigration law/reform |
| `election-law` | Voting rights, election administration, redistricting |
| `legal-rights` | Civil rights, anti-discrimination law, constitutional protections |
| `healthcare` | **Only** posts actually about medical/health topics (COVID, PPE, hospitals) |
| `firearm-safety` | **Only** posts about SVCAF firearm safety training events |

### 🤝 Engage Pillar
| Tag | Use when the post is about… |
|---|---|
| `advocacy` | SVCAF taking a public position, writing letters, public statements |
| `community-action` | Community organizing, mutual aid, mobilization campaigns |
| `legislation` | Specific bills, propositions, ballot measures (AB/SB/Prop numbers) |
| `affirmative-action` | Affirmative action policy: ACA-5, Prop 16, Prop 209, etc. |
| `sffa-lawsuit` | The SFFA v. Harvard/UNC Supreme Court lawsuit specifically |
| `election-integrity` | Vote-by-mail security, ballot administration concerns |
| `ai4legislation` | SVCAF's AI4Legislation program specifically |

### 🏆 Recognize Pillar
| Tag | Use when the post is about… |
|---|---|
| `community-events` | Galas, meetups, forums, seminars, banquets, annual meetings |
| `awards` | Presenting or receiving awards; Voice of Chinese Americans |
| `chinese-american` | Chinese-American history, identity, community stories |
| `anti-discrimination` | Fighting discrimination, hate crimes, bias incidents, AAPI solidarity |
| `volunteer` | **Only** posts about volunteering, donations, or mutual aid drives |

### 🔧 General
| Tag | Use when the post is about… |
|---|---|
| `ai-technology` | AI tools, OpenClaw, technology, digital transformation |
| `svcaf-news` | Org announcements, board updates, internal news |

---

## ⚠️ Common Tagging Mistakes

| ❌ Wrong | ✅ Right | Why |
|---|---|---|
| `healthcare` on a UC admissions post | `education-policy` | No health content |
| `sffa-lawsuit` on a general college access post | `education-policy` or `affirmative-action` | SFFA = the specific Harvard/UNC case |
| `legislation` on a lawsuit post | `legal-rights` or `sffa-lawsuit` | Lawsuits ≠ legislation |
| `volunteer` on an advocacy post | `advocacy` or `community-action` | Volunteer = people giving time/money |
| `affirmative-action` on a COVID post | `healthcare` + `community-action` | AA policy not relevant |

---

## ✅ Tagging Process (Required Steps)

1. **Read the full post body** — not just the title or description
2. **Check keyword evidence** before using a high-risk tag:
   - `healthcare` → must have: hospital, medical, COVID, mask, doctor, etc.
   - `sffa-lawsuit` → must have: SFFA, Harvard, UNC, Supreme Court
   - `firearm-safety` → must have: firearm, gun, shooting
   - `volunteer` → must have: volunteer, donation, donate
3. **Before bulk tag changes** → show 10–15 sample posts to Chunhua for review
4. **Run the integrity scan** before committing: `python scripts/integrity-scan.py`
5. The scanner will flag: unknown tags, wrong count, suspicious tags with no keyword evidence

---

## Running the Tag Validator

```bash
# From repo root
python scripts/integrity-scan.py

# Save a full report
python scripts/integrity-scan.py --report
# Opens integrity-report.md
```

Exit code `1` = critical issues (unknown tags or wrong count). Fix before pushing.
