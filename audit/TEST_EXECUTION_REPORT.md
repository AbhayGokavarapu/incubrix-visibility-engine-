# Test Execution Report: IncuBrix Option 3

**Execution Date:** 22 November 2026  
**Test Environment:** Windows PowerShell / Python 3.14.5 AMD64  
**Audit Scope:** Terminal execution of all scripts, validator tools, unit tests, and regression pipelines.

---

## Summary of Executed Tests

| Test ID | Command Executed | Exit Code | Runtime | Actual Output Summary | Verified Status |
|---|---|:---:|:---:|---|:---:|
| **TEST-01** | `python engine/visibility_engine.py` | `0` | 0.05s | Ingested 100 rows, filtered 0 duplicates, calculated 0.0% mention rate, generated report & 3 briefs. | **PASS** |
| **TEST-02** | `python engine/validate_fixes.py` | `0` | 0.08s | Audited all 20 fixes across Schema.org JSON-LD, XML sitemaps, robots.txt, Core Web Vitals, and lazy-loading specs. | **PASS (20/20)** |
| **TEST-03** | `python engine/gap_analyzer.py` | `0` | 0.03s | Calculated opportunity scores (0-100); generated `gap_analysis_report.md`. | **PASS** |
| **TEST-04** | `python engine/generate_dashboard.py` | `0` | 0.02s | Dynamically parsed datasets and compiled `visibility/dashboard/index.html` with explicit baseline classification. | **PASS** |
| **TEST-05** | `python -m unittest engine/test_engine.py` | `0` | 0.02s | Ran 3 unit tests: deduplication, scoring logic, and missing-file recovery. All passed. | **PASS** |
| **TEST-06** | OpenPyXL Workbook Evaluation | `0` | 0.12s | Evaluated formulas: Minimums met: `7 of 7 MET`, Ready to submit: `YES`, Self-Score Total: `100/100`. | **PASS** |

---

## Detailed Execution Logs

### 1. `python engine/visibility_engine.py`
```
============================================================
IncuBrix AEO, SEO & GEO Visibility Engine v1.0
============================================================
2026-11-22 13:21:20,240 [INFO] Loading visibility records from visibility/visibility.csv...
2026-11-22 13:21:20,243 [INFO] Loaded 100 rows. Filtered 0 duplicates. 100 unique queries retained.
2026-11-22 13:21:20,243 [INFO] Computing visibility scores...
2026-11-22 13:21:20,244 [INFO] Analysis complete. IncuBrix Mention Rate: 0.0%. Answer Box Presence: 100/100 queries.
2026-11-22 13:21:20,244 [INFO] Generating weekly visibility report at visibility/weekly_visibility_report.md...
2026-11-22 13:21:20,247 [INFO] Report generated successfully.
2026-11-22 13:21:20,248 [INFO] Generated content brief for Q001 at pages/briefs\brief_Q001.md
2026-11-22 13:21:20,250 [INFO] Generated content brief for Q002 at pages/briefs\brief_Q002.md
2026-11-22 13:21:20,252 [INFO] Generated content brief for Q005 at pages/briefs\brief_Q005.md
```

### 2. `python engine/validate_fixes.py`
```
Fix ID   | Status   | Method                           | Output
--------------------------------------------------------------------------------
FIX-01   | PASS     | llms.txt Standard Specification  | Valid Markdown hierarchy and AI agent summary blocks.
FIX-02   | PASS     | llms.txt Standard Specification  | Valid Markdown hierarchy and AI agent summary blocks.
FIX-03   | PASS     | Robots.txt Directive Check       | Includes explicit GPTBot, ClaudeBot, PerplexityBot, and Sitemap.
FIX-04   | PASS     | Schema.org Structure & JSON Syntax | Valid Schema structure with type(s): ['Organization', 'SoftwareApplication']
FIX-05   | PASS     | Schema.org Structure & JSON Syntax | Valid Schema structure with type(s): FAQPage
FIX-06   | PASS     | Schema.org Structure & JSON Syntax | Valid Schema structure with type(s): Product
FIX-07   | PASS     | Schema.org Structure & JSON Syntax | Valid Schema structure with type(s): HowTo
FIX-08   | PASS     | W3C XML Sitemap Validation       | Valid XML sitemap with 6 URL elements.
FIX-09   | PASS     | Code & Specification Verification | Verified implementation specs for: title, description
FIX-10   | PASS     | Code & Specification Verification | Verified implementation specs for: og:title, twitter:card
FIX-11   | PASS     | Code & Specification Verification | Verified implementation specs for: h1, h2, hero-title
FIX-12   | PASS     | Code & Specification Verification | Verified implementation specs for: strict-transport-security, x-content-type-options
FIX-13   | PASS     | Schema.org Structure & JSON Syntax | Valid Schema structure with type(s): DefinedTermSet
FIX-14   | PASS     | Schema.org Structure & JSON Syntax | Valid Schema structure with type(s): BreadcrumbList
FIX-15   | PASS     | Schema.org Structure & JSON Syntax | Valid Schema structure with type(s): WebPage
FIX-16   | PASS     | Code & Specification Verification | Verified implementation specs for: loading="lazy", alt=
FIX-17   | PASS     | Code & Specification Verification | Verified implementation specs for: footer, features, compare
FIX-18   | PASS     | Code & Specification Verification | Verified implementation specs for: rel="preload", font-display
FIX-19   | PASS     | Schema.org Structure & JSON Syntax | Valid Schema structure with type(s): ProfilePage
FIX-20   | PASS     | Code & Specification Verification | Verified implementation specs for: 404, error-container
```

### 3. `python -m unittest engine/test_engine.py`
```
2026-11-22 13:21:42,110 [INFO] Loading visibility records from non_existent_file.csv...
2026-11-22 13:21:42,111 [ERROR] Input file not found: non_existent_file.csv
.2026-11-22 13:21:42,113 [INFO] Loading visibility records from C:\Users\abhay\AppData\Local\Temp\tmpyq5qi6m8\mock_visibility.csv...
2026-11-22 13:21:42,116 [WARNING] Duplicate question detected and filtered: 'How to turn long videos into shorts with AI?'
2026-11-22 13:21:42,116 [INFO] Loaded 3 rows. Filtered 1 duplicates. 2 unique queries retained.
.2026-11-22 13:21:42,119 [INFO] Loading visibility records from C:\Users\abhay\AppData\Local\Temp\tmp_f0c96aa\mock_visibility.csv...
2026-11-22 13:21:42,121 [WARNING] Duplicate question detected and filtered: 'How to turn long videos into shorts with AI?'
2026-11-22 13:21:42,121 [INFO] Loaded 3 rows. Filtered 1 duplicates. 2 unique queries retained.
2026-11-22 13:21:42,121 [INFO] Computing visibility scores...
2026-11-22 13:21:42,121 [INFO] Analysis complete. IncuBrix Mention Rate: 50.0%. Answer Box Presence: 2/2 queries.
.
----------------------------------------------------------------------
Ran 3 tests in 0.017s

OK
```
