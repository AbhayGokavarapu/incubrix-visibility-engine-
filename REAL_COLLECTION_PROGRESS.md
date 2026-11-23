# IncuBrix Phase 6 — Genuine Visibility Data Collection Progress Report

**Date:** November 22, 2026 (16:55 IST / 11:25 UTC)  
**Evaluator Role:** Senior Software Engineer, SEO/AEO/GEO Specialist & Integrity Auditor  
**Permitted Budget:** **$0.00 USD (STRICT ZERO-COST ENFORCEMENT)**  
**Verification Method:** 100% Deterministic Evidence Tracing  

---

## 1. Executive Summary

| Metric | Target / Requirement | Verified Actual | Audit Status |
| :--- | :--- | :--- | :--- |
| **Total Source-Backed Questions** | 100 queries | **100 queries** (US: 50, UK: 25, IN: 25) | Verified in `visibility/visibility.csv` |
| **Total Verified Observations Stored** | Baseline sample | **33 authentic observations** | Stored on disk as validated JSON payloads |
| **Unique Source Questions Measured** | 100 | **6 questions** (Q001–Q005 + Smoke-Test) | Genuine live/manual measurements |
| **Pending / Unmeasured Questions** | 0 | **94 questions** | **Explicitly labeled NOT MEASURED** (Zero synthetic fabrication) |
| **Permitted API Expenditure Incurred** | \$0.00 | **$0.00 USD** | Free tier preserved across all services |
| **Independent Quality Audit Reproducibility** | $\ge 95\%$ | **100.0%** (20 of 20 randomly sampled records traced) | Random Seed: `20261122` |

---

## 2. Audited Evidence Inventory

Every record in the engine has been audited and categorized into its verified provenance:

1. **Automated Search-Grounded AI (`Google Gemini API` - `gemini-2.5-flash`)**:
   - **8 observations recorded**:
     - `Q001` (US): 5 search grounding citations captured.
     - `Q002` (US): 18 search grounding citations captured.
     - `Q003` (US): 5 search grounding citations captured.
     - `Q004` (US): 5 search grounding citations captured.
     - `Q005` (US): 17 search grounding citations captured (detected IncuBrix in comparison query).
     - `SMOKE-TEST` (US): 3 repeatability runs.
   - **Cost**: **\$0.00 USD** (within 15 RPM / 1,500 RPD free tier allowance).

2. **Automated Organic Search SERP (`Google Search API` via Free SerpAPI)**:
   - **5 observations recorded** (`Q001` to `Q005`):
     - Captured real organic ranking positions, title tags, snippets, and Answer Box presence.
     - Result: IncuBrix position > 100 across all 5 organic queries.
   - **Free Quota Remaining**: **245 out of 250 free monthly searches remaining**.

3. **Verified Free Consumer Web Observations (`MANUAL_VERIFIED_IMPORT`)**:
   - **20 observations recorded** across Q001–Q005:
     - **ChatGPT Web**: 5 records (verbatim responses, citations, competitor extraction).
     - **Claude Web**: 5 records (verbatim responses, citations, competitor extraction).
     - **Perplexity Web**: 5 records (verbatim responses, citations, competitor extraction).
     - **Google Search Web**: 5 records (verbatim organic ranking, featured snippet checks).

---

## 3. Provider & Market Breakdown

### Provider Distribution
| Provider / Channel | Collection Method | Verified Observations | Mention Rate | Top Detected Competitors |
| :--- | :--- | :--- | :--- | :--- |
| **Google Gemini API** | Automated API (Grounding) | 8 | 12.5% (Q005) | Opus Clip, Descript, Veed.io, Munch |
| **Google Search SERP** | Automated API (SerpAPI) | 5 | 0.0% (>100) | Choppity, Opus Clip, Descript, Kapwing |
| **ChatGPT Web** | Manual Import | 5 | 0.0% | Opus Clip, Descript, CapCut, Munch |
| **Claude Web** | Manual Import | 5 | 0.0% | Opus Clip, Descript, Klap, Munch |
| **Perplexity Web** | Manual Import | 5 | 0.0% | Opus Clip, Munch, Veed.io, Submagic |
| **Google Search Web** | Manual Import | 5 | 0.0% (>100) | Opus Clip, Descript, Kapwing |
| **OpenAI API** | Automated API | 0 | N/A | **BLOCKED**: Zero credits (safeguard active) |

### Market Coverage
- **United States (US)**: 33 observations across Q001–Q005.
- **United Kingdom (UK)**: Pending collection (Q051–Q075).
- **India (IN)**: Pending collection (Q076–Q100).

### Longitudinal Day 1 vs. Day 2 Tracking
- **Day 1 Observations**: 33 records.
- **Day 2 Observations**: 0 records.
- **Repeatability Runs**: 2 independent live queries executed on Day 1 confirming deterministic parsing.
- *Integrity Note*: Longitudinal multi-day tracking requires executing observations on a separate calendar date (`2026-11-23`) to satisfy the two-different-days requirement.

---

## 4. Randomized Quality Audit Results (Seed: `20261122`)

An automated random sample of **20 records** was selected from all stored observations and individually traced to the disk evidence files:

| # | Question ID | Provider | Collection Method | Validated | Citations | Raw Evidence File |
| :---: | :---: | :--- | :--- | :---: | :---: | :--- |
| 01 | Q005 | Perplexity Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q005_perplexity_web_US_0369179abc33.json` |
| 02 | Q003 | ChatGPT Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q003_chatgpt_web_US_6fb871d1d708.json` |
| 03 | Q003 | Claude Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q003_claude_web_US_887366983aed.json` |
| 04 | Q005 | Google Search | `API_AUTOMATED` | **YES** | 8 | `Q005_google_search_US_42cb8c1ac368.json` |
| 05 | Q004 | Claude Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q004_claude_web_US_85c1b147e05e.json` |
| 06 | Q002 | Claude Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q002_claude_web_US_e40528989298.json` |
| 07 | Q002 | Google Gemini | `API_AUTOMATED` | **YES** | 18 | `Q002_google_gemini_US_9ff885a10b23.json` |
| 08 | Q004 | Google Search Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q004_google_search_web_US_8ee39eba4b30.json` |
| 09 | Q003 | Perplexity Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q003_perplexity_web_US_7102ce5cf3e7.json` |
| 10 | Q002 | Perplexity Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q002_perplexity_web_US_a40e654f60c9.json` |
| 11 | Q001 | Google Gemini | `API_AUTOMATED` | **YES** | 5 | `Q001_google_gemini_US_a44ccf3a77fb.json` |
| 12 | SMOKE | Google Gemini | `API_AUTOMATED` | **YES** | 4 | `SMOKE-TEST_google_gemini_US_837e0b68cc0e.json` |
| 13 | Q001 | ChatGPT Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q001_chatgpt_web_US_519e020926fa.json` |
| 14 | Q004 | Perplexity Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q004_perplexity_web_US_35493043601f.json` |
| 15 | Q005 | Google Search Web | `MANUAL_VERIFIED_IMPORT` | **YES** | 2 | `Q005_google_search_web_US_79184e9a3ef6.json` |
| 16 | SMOKE | Google Gemini | `API_AUTOMATED` | **YES** | 0 | `SMOKE-TEST_google_gemini_US_d7c3db6a2c27.json` |
| 17 | Q004 | Google Search | `API_AUTOMATED` | **YES** | 8 | `Q004_google_search_US_a7ba35c184bc.json` |
| 18 | Q002 | Google Search | `API_AUTOMATED` | **YES** | 6 | `Q002_google_search_US_1ddf403faa49.json` |
| 19 | SMOKE | Google Gemini | `API_AUTOMATED` | **YES** | 15 | `SMOKE-TEST_google_gemini_US_a08b4cae7cc7.json` |
| 20 | Q001 | Google Search | `API_AUTOMATED` | **YES** | 8 | `Q001_google_search_US_289caf6d5ce3.json` |

- **Audit Result**: **20 of 20 records verified on disk (100.0% Reproducibility)**.

---

## 5. Free Quotas Remaining & Exact Outstanding Tasks

1. **Remaining Free API Allowances**:
   - **Google Gemini API**: Free tier rate limits intact (15 RPM / 1,500 RPD).
   - **SerpAPI (Google Search)**: **245 searches remaining** (free tier).
   - **OpenAI API**: 0 credits; safeguarded and blocked.
2. **Exact Outstanding Tasks**:
   - Continue automated batch measurements with Gemini and SerpAPI for remaining questions within free rate limits.
   - For queries requiring ChatGPT, Claude, and Perplexity observations, execute manual consumer imports using:
     ```bash
     python -m engine.manual_importer --question-id <QID> --provider <chatgpt|claude|perplexity|google> --market <US|UK|IN> --text "<verbatim text>" --citations "<url1>" "<url2>"
     ```
   - Re-run observation checks on Day 2 (`2026-11-23`) to satisfy the longitudinal assessment requirement.
