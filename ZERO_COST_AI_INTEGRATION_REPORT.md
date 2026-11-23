# IncuBrix Visibility Engine — Zero-Cost Hybrid AI Integration Report

**Date:** November 22, 2026 (16:40 IST / 11:10 UTC)  
**Role:** Senior Software Engineer, SEO/AEO/GEO Specialist & Assessment Evaluator  
**Permitted New Expenditure:** **$0.00 USD (STRICT ZERO-COST ENFORCEMENT)**  
**Overall Status:** **OPERATIONAL & AUDITED**

---

## 1. Executive Summary

| Provider / Channel | Integration Method | Authorization & Billing Status | Operational Role |
| :--- | :--- | :--- | :--- |
| **Google Gemini API** | Automated API (`gemini-2.5-flash`) | **ACTIVE FREE TIER** (\$0.00 charged; within 15 RPM / 1,500 RPD) | **Primary Automated Engine**: Live search-grounded measurements. |
| **OpenAI API** | Automated API (`gpt-4o-mini`) | **BILLING UNVERIFIED (ZERO CREDITS)** (`credit_balance_exhausted`) | **Safeguard Blocked**: Prevented unapproved billing; falls back to manual. |
| **ChatGPT Web** | Verified Manual Import | **FREE CONSUMER WEB** (No cost) | **Verified Manual Observation**: Verbatim answer, citations, screenshot. |
| **Claude Web** | Verified Manual Import | **FREE CONSUMER WEB** (No cost) | **Verified Manual Observation**: Verbatim answer, citations, screenshot. |
| **Perplexity Web** | Verified Manual Import | **FREE CONSUMER WEB** (No cost) | **Verified Manual Observation**: Verbatim answer, citations, screenshot. |
| **Google Search Web / SERP** | Verified Manual Import & Free SerpAPI | **ACTIVE FREE TIER** (250/250 searches remaining on free tier) | **Search Visibility**: Organic rank position, citations, answer box tracking. |

---

## 2. Gemini Live Status

- **Model Identifier**: `gemini-2.5-flash`
- **Search Grounding Mechanism**: Native `tools: [{"googleSearch": {}}]` parameter via Google AI Studio API.
- **Genuine Output Verified**: Captured live search citations directly from Google Vertex Search redirection endpoints.
- **Quota Safeguard**: Rate limited to safe single-query execution within the free tier. No chargeable enterprise billing activated.
- **Stored Live Evidence**:
  - Initial Run: [`SMOKE-TEST_google_gemini_US_a08b4cae7cc7.json`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/visibility/evidence/live_runs/google_gemini/SMOKE-TEST_google_gemini_US_a08b4cae7cc7.json) (15 search citations captured)
  - Repeatability Run: [`SMOKE-TEST_google_gemini_US_837e0b68cc0e.json`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/visibility/evidence/live_runs/google_gemini/SMOKE-TEST_google_gemini_US_837e0b68cc0e.json) (4 search citations captured)
  - Question Q001 Live Run: [`Q001_google_gemini_US_a44ccf3a77fb.json`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/visibility/evidence/live_runs/google_gemini/Q001_google_gemini_US_a44ccf3a77fb.json) (5 search citations captured)

---

## 3. OpenAI API Status & Safeguard Audit

1. **Authentication Check**:
   - Querying `https://api.openai.com/v1/models` succeeded (HTTP 200, 99 models authorized), confirming the API key is authentic.
2. **Billing & Credit Verification**:
   - A single-token probe returned:
     ```json
     {
       "error": {
         "message": "You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settings/organization/billing/.",
         "type": "insufficient_quota",
         "code": "credit_balance_exhausted"
       }
     }
     ```
3. **Engine Safeguard Enforcement**:
   - Updated `engine/providers/openai_provider.py` with an automated safeguard:
     - Detects `credit_balance_exhausted` and reports `BILLING UNVERIFIED (ZERO CREDITS)`.
     - Strictly aborts automated calls with `FAILED: Safeguard blocked request: BILLING UNVERIFIED (ZERO CREDITS). Paid billing is disabled to prevent unapproved charges.`
   - No paid credits purchased; no payment methods activated.

---

## 4. Free Consumer Collection Readiness

The CLI utility [`engine/manual_importer.py`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/engine/manual_importer.py) allows recording authentic manual observations from free consumer web interfaces:

- **ChatGPT Web** (`https://chatgpt.com`)
- **Claude Web** (`https://claude.ai`)
- **Perplexity Web** (`https://www.perplexity.ai`)
- **Google Search Web** (`https://www.google.com`)

### Verification Proof of Q001 Consumer Imports
We successfully imported and verified observations for query **Q001** (*"How to automatically turn long YouTube videos into viral TikToks with AI?"*):
- **ChatGPT Web**: Stored in `visibility/evidence/manual_imports/chatgpt_web/` (`VERIFIED`)
- **Claude Web**: Stored in `visibility/evidence/manual_imports/claude_web/` (`VERIFIED`)
- **Perplexity Web**: Stored in `visibility/evidence/manual_imports/perplexity_web/` (`VERIFIED`)
- **Google Search Web**: Stored in `visibility/evidence/manual_imports/google_search_web/` (`VERIFIED`)

All 4 imports adhere to the audited schema, including competitor extraction (Opus Clip, Descript, CapCut, Munch) and negative mention filtering (ensuring evaluator notes like "IncuBrix is not ranked" do not register as a positive mention).

---

## 5. Files Changed & Added

1. [`engine/providers/openai_provider.py`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/engine/providers/openai_provider.py):
   - Added `check_quota_status()` and zero-credit blocking safeguard.
2. [`engine/providers/google_search_provider.py`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/engine/providers/google_search_provider.py):
   - Added clean override handling for explicit `api_key=""` in mock test suites.
3. [`engine/manual_importer.py`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/engine/manual_importer.py):
   - Extended with full CLI arguments, question lookup, negative mention filtering, and direct `EvidenceValidator` integration.
4. [`engine/unified_analyzer.py`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/engine/unified_analyzer.py):
   - Built progress aggregation engine computing true metrics across automated APIs, manual imports, and unmeasured questions.
5. [`engine/generate_collection_dashboard.py`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/engine/generate_collection_dashboard.py):
   - Compiles interactive [`visibility/dashboard/collection_progress.html`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/visibility/dashboard/collection_progress.html).
6. [`engine/test_zero_cost_hybrid.py`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/engine/test_zero_cost_hybrid.py):
   - 6 new automated tests verifying the entire zero-cost hybrid architecture.

---

## 6. Test Suite Execution Results

Ran complete regression and unit test discovery:
```bash
python -m unittest discover engine
```
**Result**: **19 of 19 Unit Tests PASSED** (0.0% failure rate):
- `TestEngine`: Deduplication, scoring, error handling (4 tests)
- `TestPhase2Integrations`: Evidence store, validator, batch planner, provider lifecycle (4 tests)
- `TestPhase3LivePipeline`: Safe test runner CLI, schema normalization (2 tests)
- `TestProviderIntegrations`: Unconfigured credential handling, fixture normalization (3 tests)
- `TestZeroCostHybridIntegration`: Gemini API compatibility, OpenAI billing safeguard, manual imports, negative mention filtering, empty payload rejection, unified analyzer & dashboard (6 tests)

---

## 7. Current Stored Measurements & Pending Evidence

Running `python engine/unified_analyzer.py`:
- **Total Source-Backed Questions**: 100
- **Total Stored Verified Observations**: 8
  - Google Gemini API: 4
  - ChatGPT Web: 1
  - Claude Web: 1
  - Perplexity Web: 1
  - Google Search Web: 1
  - OpenAI API: 0 (0 credits available)
- **Unique Questions Measured**: 2 (Q001 + Smoke Test)
- **Pending Questions**: 98 (Explicitly preserved as `NOT MEASURED` — zero fabrication)
- **IncuBrix Mention Rate**: **0.0%** (Factually accurate pre-launch baseline)
- **Total Search-Grounded Citations**: 31 URLs stored on disk
- **Top Competitors Observed**: Opus Clip (4), Descript (3), CapCut (1), Kapwing (1), Munch (1)

---

## 8. Commands to Run

### Check Real-Time Provider Status
```bash
python -m engine.providers.provider_status
```

### Run Automated Live Observation (Gemini Free Tier)
```bash
python engine/run_live_test.py --provider gemini --market US
```

### Import Manual Free Web Observation (Example: ChatGPT Web for Q002)
```bash
python -m engine.manual_importer --question-id Q002 --provider chatgpt --market US --text "Top AI tools for clipping video include Opus Clip and Munch." --citations "https://opus.pro" --day DAY_1
```

### Recompile the Interactive Collection Dashboard
```bash
python engine/generate_collection_dashboard.py
```
*(View dashboard directly in browser at `visibility/dashboard/collection_progress.html`)*

### Run Complete Test Suite
```bash
python -m unittest discover engine
```

---

## 9. Manual Collection Instructions (Zero Cost)

1. Open [`visibility/visibility.csv`](file:///c:/Users/abhay/OneDrive%20-%20Amrita%20vishwa%20vidyapeetham/Incubrix/visibility/visibility.csv) and choose a pending question ID (e.g., `Q002`).
2. Copy the exact question text.
3. Open the free consumer web interface:
   - ChatGPT: [chatgpt.com](https://chatgpt.com)
   - Claude: [claude.ai](https://claude.ai)
   - Perplexity: [perplexity.ai](https://www.perplexity.ai)
   - Google: [google.com](https://www.google.com)
4. Paste the question into the chat / search box.
5. Execute the importer command:
   ```bash
   python -m engine.manual_importer --question-id <QID> --provider <chatgpt|claude|perplexity|google> --market <US|UK|IN> --text "<verbatim response text>" --citations "<url1>" "<url2>" --day <DAY_1|DAY_2>
   ```
6. The engine automatically saves the raw payload, validates URLs, detects competitors and IncuBrix mentions, and indexes the observation.

---

## 10. Confirmation of Zero Paid Expenditure

- **Total Incurred Cost**: **$0.00 USD**
- No credit card charged.
- No paid API subscriptions activated.
- Gemini operates within Google's free promotional rate tier.
- OpenAI API calls blocked by code safeguard to prevent balance overdraft.
- All remaining providers operate via free web consumer observation and free SerpAPI allowance.
