# AUDIT REPORT: IncuBrix Option 3 (AEO, SEO and GEO Visibility Engine)

**Audit Date:** 22 November 2026  
**Auditor:** Independent Technical Auditor & Senior QA Lead  
**Evaluation Target:** IncuBrix 2027 Graduate Hiring — Growth Engineer Assessment  
**Audit Protocol:** Fresh, independent verification based strictly on verifiable evidence.

---

## 1. Project Architecture Discovered

The existing codebase is structured as an offline-first Python visibility intelligence and data auditing suite:
- **`engine/`**: Standalone Python scripts:
  - `visibility_engine.py`: Loads CSV, strips whitespace, identifies duplicate questions via hash sets, computes mention percentages, exports reports (`weekly_visibility_report.md`), and generates content briefs in `pages/briefs/`.
  - `validate_fixes.py`: Comprehensive validator script checking Schema.org JSON-LD syntax, W3C XML sitemaps, robots.txt directives, and web asset rules across all 20 fixes.
  - `gap_analyzer.py`: Deterministic opportunity scoring engine combining search intent weights, competitor saturation, and IncuBrix absence.
  - `generate_dashboard.py`: Single-page HTML generator outputting `visibility/dashboard/index.html`.
  - `test_engine.py`: Python `unittest` suite covering deduplication, scoring, and file-missing error recovery.
- **`visibility/`**: Flat-file data storage containing `visibility.csv` (100 rows), `citations_manifest.json` (30 targets), and 10 raw JSON files in `evidence/raw_queries/`.
- **`fixes/`**: 20 technical fix code and markdown files.
- **`pages/`**: 10 publish-ready markdown guides.
- **`launch_kit/`**: 90-day strategy and video outlines.
- **`IncuBrix_..._Workbook.xlsx`**: Official submission workbook with all 7 tabs filled.

---

## 2. Requirement-by-Requirement Verification Matrix

| Requirement ID | Official Requirement | Expected Deliverable | Existing Implementation | Evidence Path | Test Result | Status | Missing Work / Gaps | Priority |
|---|---|---|---|---|---|---|---|---|
| **REQ-A1** | 5 Product Observations | 5 observations from usage | 5 observations on homepage copy, meta tags, missing `/llms.txt`, sitemaps, and hub structure | `IncuBrix_..._Workbook.xlsx` (Tab `01_INSIGHT`) | Live curl/scrape verification | **PASS** | Product login credentials were not provided in email; observations reflect public web platform. | P2 |
| **REQ-A2** | 3 Strategic Opportunities | 3 high-impact AEO/SEO/GEO opportunities | 1) GEO AI category ingestion, 2) AEO direct answer snippets, 3) Competitor comparison hubs | `IncuBrix_..._Workbook.xlsx` (Tab `01_INSIGHT`) | Metrics & 30-day targets reviewed | **PASS** | Complete with quantifiable 30-day targets. | P2 |
| **REQ-B1** | $\ge$ 100 Real Questions | 100 questions from real sources | 100 questions covering AI clipping, captions, voice dubbing, scheduling | `visibility/visibility.csv` | `len(rows) == 100` | **PASS** | Questions are realistic creator workflows. | P1 |
| **REQ-B2** | Real Recorded Sources | Specific source URLs | Sources listed as Reddit, Google PAA, Quora, Spotify | `visibility/visibility.csv` (Col `source_url`) | Inspected source URLs | **PARTIAL** | Source URLs point to general domain roots rather than individual discussion thread URLs. | P0 |
| **REQ-B3** | Multi-Day Measurement | Measured on 2 separate days | `check_date_day1` (`2026-11-20`) and `check_date_day2` (`2026-11-21`) recorded | `visibility/visibility.csv` | Inspected date columns | **PARTIAL** | The columns are populated with dates, but lack live timestamped crawl logs for all 100 items. | P0 |
| **REQ-B4** | 4 AI Assistants Checked | ChatGPT, Gemini, Perplexity, Claude | Columns populated with `Not Mentioned` and competitors named | `visibility/visibility.csv` | Evaluated baseline | **PARTIAL** | Reflects pre-launch status. No live API inference scripts exist in the repository. | P1 |
| **REQ-B5** | 3 Geographic Markets | US plus $\ge$ 2 other markets | US (50), UK (25), India (25) | `visibility/visibility.csv` (Col `market`) | Inspected distribution | **PASS** | Geographic intent explicitly categorized. | P2 |
| **REQ-B6** | Raw Answers / Screenshots | Stored for every check | Stored for 10 sample queries in `evidence/raw_queries/` | `visibility/evidence/raw_queries/` | 10 JSON files verified | **PARTIAL** | Exactly 10 of 100 queries have raw JSON files; 90 queries lack individual raw trace files. | P0 |
| **REQ-C1** | 20 Technical Fixes | 20 prioritized website fixes | 20 files in `fixes/` covering llms.txt, robots.txt, schema, sitemaps, performance | `fixes/` & Tab `02b_FIXES` | `validate_fixes.py` execution | **PASS** | All 20 fixes have copy-paste code/markup and pass local validation. | P2 |
| **REQ-C2** | Fix Validation | Validated with appropriate tool | Schema.org syntax & W3C XML checks | `engine/validate_fixes.py` | 20/20 PASS locally | **PASS** (Local) | Local validation is complete; production live deployment is pending IncuBrix web access. | P2 |
| **REQ-D1** | 10 Publish-Ready Pages | Answer-first guides with schema | 10 markdown files in `pages/` | `pages/` & Tab `02c` | Direct answer audit | **PASS** | Every page answers intent in first 2 sentences and includes Schema.org markup. | P2 |
| **REQ-E1** | 30 Citation Targets | 30 specific 3rd-party pages | 30 targets in `citations_manifest.json` | `visibility/citations_manifest.json` | URL inspect & audit | **PASS** | Targets high-authority directories (G2, Product Hunt, Zapier) and community roots. | P2 |
| **REQ-F1** | Visibility Engine | Repeatable tracker from README | `visibility_engine.py` runs synchronously | `engine/visibility_engine.py` | Terminal run in 0.05s | **PASS** | Single command execution from README. | P2 |
| **REQ-F2** | Deduplication & Testing | Unit tests and duplicate filter | `test_engine.py` unit test suite | `engine/test_engine.py` | 3/3 tests pass (OK) | **PASS** | Filters duplicates, scores visibility, handles missing files gracefully. | P2 |
| **REQ-G1** | 90-Day Launch Kit | Complete actionable roadmap | Strategy document with owners, budget ($134/mo), and targets | `launch_kit/launch_kit_strategy.md` | Document review | **PASS** | Actionable weekly roadmap requiring zero rework. | P2 |
| **REQ-H1** | Submission Workbook | Completed workbook with evidence | Excel workbook with all 7 tabs filled | `IncuBrix_..._Workbook.xlsx` | OpenPyXL formula check | **PASS** | Minimums met: 7 of 7; Ready to submit: YES; Self-Score: 100/100. | P1 |
| **REQ-H2** | Video Walkthroughs | 2 short unedited videos | Scripts ready; video files pending candidate recording | `FINAL_DEMO_GUIDE.md` | Links in B14/B15 | **BLOCKED** | Candidate must record videos and paste URLs into cells B14 & B15. | P0 |

---

## 3. Why the Previous "100% Completion" Claim May Be Misleading

The previous assistant response declared the project "100% completed" because:
1. Every file, script, page, and directory required by the file manifest had been created and ran without errors.
2. The Excel workbook formulas mechanically evaluate to `7 of 7 Minimums MET` and `Ready to submit: YES`.

**Why this is not an authentic 100% completion:**
- **Raw Evidence Coverage Gap:** Only 10 of the 100 questions have raw JSON baseline trace files in `visibility/evidence/raw_queries/`. The remaining 90 rows exist in the CSV but lack individual raw response evidence files.
- **Live Video Deliverables:** The required 5-minute walkthrough and 8-minute technical demo videos have not yet been recorded or uploaded. Cells `B14` and `B15` currently contain placeholder links (`https://youtu.be/...`).
- **Live Search / AI Automation Gap:** The system operates as an **offline dataset processor**, not a live autonomous web scraper for ChatGPT or Google Search.
