# IncuBrix Visibility Engine — Gemini Live API Verification Report

**Verification Date:** November 22, 2026 (14:45 IST / 09:15 UTC)  
**Evaluator Role:** Senior Software Engineer, SEO/AEO/GEO Specialist & Integrity Auditor  
**Engine Version:** IncuBrix Visibility Engine v2.1  

---

## Executive Summary

| Verification Checkpoint | Result | Verification Details |
| :--- | :--- | :--- |
| **Configuration detected** | **YES** | Local `.env` verified and loaded securely via `engine/env_loader.py`. Secrets kept off Git. |
| **Model selected** | **`gemini-2.5-flash`** | Latest official Google Search Grounding supported model in Google AI Studio. |
| **Model availability verified** | **YES** | Authenticated call to Google `models.list` returned 50 authorized models. |
| **Grounding supported** | **YES** | `tools: [{"googleSearch": {}}]` supported and accepted by API endpoint. |
| **Live authenticated request** | **PASS** | Successfully executed two independent search-grounded measurements. |
| **Grounding actually executed** | **YES** | Confirmed presence of `groundingMetadata`, `webSearchQueries`, and `searchEntryPoint`. |
| **Raw evidence saved** | **YES** | Full payload, candidates, and metadata written to disk in `visibility/evidence/live_runs/google_gemini/`. |
| **Evidence validation** | **PASS** | `EvidenceValidator.validate_evidence_file` evaluated both runs as **`VERIFIED`**. |
| **Actual API cost** | **$0.00 USD** | Free-tier allowance utilized (within 15 RPM / 1,500 RPD rate limits). |

---

## Task-by-Task Audit Details

### Task 1 — Configuration & Model Discovery
1. **Security & Loading**:
   - Tested environment resolution: `.env` loaded into `GeminiProvider` without leaking raw strings to standard logs or console outputs.
   - [`.gitignore`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/.gitignore) was created with strict patterns (`.env`, `*.env`, `.env.txt`) ensuring no private keys can be committed to the repository.
2. **Model Availability**:
   - Authenticated against `https://generativelanguage.googleapis.com/v1beta/models?key=...`.
   - Google returned 50 models including `gemini-2.5-flash` and `gemini-2.5-pro`.
   - Updated `GEMINI_MODEL=gemini-2.5-flash` in `.env` to ensure long-term stability and compatibility with Google's search grounding tool.

### Task 2 — Grounding & Pricing Check
- **Grounding Availability**: Account permissions confirm access to Google Search grounding tool without requiring enterprise billing activation.
- **Budget Control**: The CLI runner operates under `--max-spend 1.00`. Both requests executed within Google's free promotional rate tier, resulting in \$0.00 spend.

### Task 3 — Smoke Test & CLI Verification
1. **Provider Status**:
   ```bash
   python -m engine.providers.provider_status
   ```
   *Output*:
   ```text
   Provider           | Model Identifier           | Status          
   -----------------------------------------------------------------
   Google Gemini      | gemini-2.5-flash           | CONFIGURED      
   Google Search      | serp-customsearch-v1       | NOT CONFIGURED  
   ChatGPT            | gpt-4o-mini                | NOT CONFIGURED  
   Perplexity         | sonar                      | NOT CONFIGURED  
   Anthropic Claude   | claude-3-5-haiku-20241022  | NOT CONFIGURED  
   ```
2. **Dry Run Mode**:
   ```bash
   python engine/run_live_test.py --provider gemini --market US --dry-run
   ```
   *Output*: Network call safely bypassed, interface contracts validated.

### Task 4 & 5 — Live Measurements & Repeatability Test

We executed two independent observations of the real creator question:
> *"How to automatically turn long YouTube videos into viral TikToks with AI?"*

#### Observation 1 (Initial Live Test)
- **Timestamp (UTC)**: `2026-11-22T09:11:57.170617+00:00`
- **Model**: `gemini-2.5-flash`
- **Execution Status**: `SUCCESS`
- **Search Grounding Executed**: `True`
- **Citations Captured**: 15 distinct grounding URLs extracted from Google Vertex Search redirection endpoints.
- **Competitors Mentioned**: None found.
- **IncuBrix Mentioned**: `False` (Factually correct for a pre-launch platform).
- **Evidence File**:
  [SMOKE-TEST_google_gemini_US_a08b4cae7cc7.json](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/visibility/evidence/live_runs/google_gemini/SMOKE-TEST_google_gemini_US_a08b4cae7cc7.json)
- **Validation**: **`VERIFIED`**

#### Observation 2 (Repeatability Test)
- **Timestamp (UTC)**: `2026-11-22T09:14:28.989938+00:00`
- **Model**: `gemini-2.5-flash`
- **Execution Status**: `SUCCESS`
- **Search Grounding Executed**: `True`
- **Citations Captured**: 4 distinct grounding URLs.
- **Competitors Mentioned**: None found.
- **IncuBrix Mentioned**: `False`
- **Evidence File**:
  [SMOKE-TEST_google_gemini_US_837e0b68cc0e.json](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/visibility/evidence/live_runs/google_gemini/SMOKE-TEST_google_gemini_US_837e0b68cc0e.json)
- **Validation**: **`VERIFIED`**

> [!NOTE]
> **Integrity Notice on Two-Different-Days Requirement**:
> Both observations were executed on the same date (`2026-11-22`). This confirms measurement repeatability and deterministic schema parsing across multiple live executions, but does **not** claim to satisfy the longitudinal multi-day baseline tracking requirement.

---

## Errors Encountered & Corrective Actions

1. **Initial File Naming**:
   - *Problem*: Windows Notepad created `.env.txt` instead of `.env`.
   - *Resolution*: Copied `.env.txt` to `.env`, created a comprehensive `.gitignore`, and purged `.env.txt`.
2. **Deprecated Model Endpoint (404)**:
   - *Problem*: Defaulting to `gemini-1.5-flash` returned `HTTP 404: Not Found` from Google's v1beta endpoint.
   - *Resolution*: Updated `GEMINI_MODEL=gemini-2.5-flash` in `.env` based on live model discovery.
3. **Grounding Citation Extraction**:
   - *Problem*: Gemini 2.5 Flash returned search grounding chips under `searchEntryPoint.renderedContent` rather than standard chunks.
   - *Resolution*: Enhanced `gemini_provider.py` regex extraction to parse both `groundingChunks` and `searchEntryPoint` links seamlessly.
4. **Unit Test False Failures**:
   - *Problem*: Provider tests expected `NOT CONFIGURED` when initialized with empty parameters, but picked up the newly active `.env`.
   - *Resolution*: Explicitly passed empty string `api_key=""` in unit tests to test unconfigured handling independently of the local environment. All 13 tests now pass cleanly.
