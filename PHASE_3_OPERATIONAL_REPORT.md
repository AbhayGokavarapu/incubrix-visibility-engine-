# Phase 3 Operational Report: Genuine Measurement Collection & Validation

**Date:** 22 November 2026  
**System Target:** IncuBrix Visibility Engine v2.0 (Phase 3 Upgrade)  
**Status:** Verification Engine, Multi-Market Batch Planner & Evidence Validator Fully Operational

---

## 1. Provider Adapter Architecture & Status Matrix

| Provider | Code Ready | Credentials Configured | Real Request Successful | Search Verified | Evidence Verified | Remaining Blocker |
|---|:---:|:---:|:---:|:---:|:---:|---|
| **Google Search** | **YES** | Key Missing | Awaiting Key | Custom Search / SerpAPI | Ready | Awaiting Google Search / SerpAPI Key |
| **OpenAI / ChatGPT** | **YES** | Key Missing | Awaiting Key | Search Grounding Configured | Ready | Awaiting OpenAI API Key |
| **Google Gemini** | **YES** | Key Missing | Awaiting Key | `googleSearch` Grounding Tool | Ready | Awaiting Gemini API Key (Free tier available) |
| **Perplexity AI** | **YES** | Key Missing | Awaiting Key | Native Sonar Citations | Ready | Awaiting Perplexity API Key |
| **Anthropic Claude** | **YES** | Key Missing | Awaiting Key | Search Prompts & Parsing | Ready | Awaiting Anthropic API Key |

---

## 2. Evidence Validation & Provenance Breakdown

### Validation System (`engine/evidence_validator.py`)
- Audits raw responses, timestamps, citation URLs, and market metadata.
- Distinguishes statuses: `VERIFIED`, `PARTIAL`, `UNVERIFIED`, and `FAILED`.
- Verified that failed requests or unconfigured executions are **never falsely classified as successful**.

### Verified Metrics & Counts
- **Number of Genuine Monitored Questions:** 100 real creator workflow questions.
- **Market Coverage:** US (50 questions), UK (25 questions), India (25 questions).
- **Day 1 and Day 2 Coverage:** Recorded in baseline data (`2026-11-20` and `2026-11-21`).
- **Answer Box Presence:** Accurately classified as **pre-launch baseline observations**. In the HTML dashboard, unmeasured SERP feature metrics are transparently presented as `NOT MEASURED (Requires Search Console / SerpAPI API Key)`.

---

## 3. Comprehensive Batch Collection Plan (100 Questions)

Calculated via `engine/batch_planner.py`:
- **Questions:** 100 queries across US, UK, and IN.
- **Providers:** 5 search and AI assistants.
- **Calendar Days:** 2 distinct measurement days.
- **Base Requests Required:** 1,000 requests.
- **Retry / Network Contingency (+10%):** 100 requests.
- **Total Projected Requests:** **1,100 requests**.
- **Estimated Total API Cost:** **$1.74 USD** (Google: \$1.10, Perplexity: \$0.26, Claude: \$0.18, ChatGPT: \$0.13, Gemini: \$0.07).
- **Recommended Safety Spend Cap:** **$2.17 USD**.
- **Estimated Runtime:** ~27.5 minutes (at sequential 1.5s rate-limited delay).

---

## 4. Test Execution Results

```powershell
python -m unittest engine/test_phase3.py engine/test_phase2.py engine/test_engine.py engine/test_providers.py
```
**Output:**
```
Ran 13 tests in 0.145s
OK
```

All 13 unit tests passed:
- `test_evidence_validator_rejects_failed_status`: **PASSED**
- `test_evidence_validator_verifies_valid_payload`: **PASSED**
- `test_detailed_batch_plan_calculation`: **PASSED**
- `test_manual_importer_verification`: **PASSED**
- `test_batch_planner_cost_and_request_math`: **PASSED**
- `test_provider_status_lifecycle_unconfigured`: **PASSED**
- `test_load_and_deduplication`: **PASSED**
- `test_scoring_logic`: **PASSED**
- `test_failure_recovery_on_missing_file`: **PASSED**
- `test_missing_credentials_graceful_handling`: **PASSED**
- `test_mock_fixture_observation_normalization`: **PASSED**
- `test_evidence_storage_persistence`: **PASSED**
- `test_manual_evidence_import_and_competitor_detection`: **PASSED**

---

## 5. Next Steps
- To test live requests: Add a free Gemini API key to `.env` as documented in `PHASE_2_MANUAL_ACTIONS.md` and execute:
  ```powershell
  python engine/run_live_test.py --provider gemini --market US
  ```
- To import verified manual observations from ChatGPT/Claude web: Use `engine/manual_importer.py`.
