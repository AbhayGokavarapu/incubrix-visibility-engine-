# AI & Search Engine Provider Integration Report (Phase 1)

**Date:** 22 November 2026  
**System Version:** IncuBrix Visibility Engine v2.0 (Multi-Provider Architecture)  
**Status:** Architecture Implemented & Tested; Real Live Network Calls Awaiting User API Keys

---

## 1. Provider Adapter Implementation & Status Matrix

| Provider | Adapter Implemented | Adapter File Path | Model Identifier | Authentication Verified | Real Request Successful | Raw Evidence Saved | Citations Extracted | Status |
|---|:---:|---|---|:---:|:---:|:---:|:---:|:---:|
| **Google Search** | **YES** | `engine/providers/google_search_provider.py` | `customsearch-v1` | Key Missing | Awaiting Key | Supported | Supported | **NOT CONFIGURED** |
| **OpenAI / ChatGPT** | **YES** | `engine/providers/openai_provider.py` | `gpt-4o-mini` | Key Missing | Awaiting Key | Supported | Supported | **NOT CONFIGURED** |
| **Google Gemini** | **YES** | `engine/providers/gemini_provider.py` | `gemini-1.5-flash` | Key Missing | Awaiting Key | Supported | Supported | **NOT CONFIGURED** |
| **Perplexity AI** | **YES** | `engine/providers/perplexity_provider.py` | `sonar` | Key Missing | Awaiting Key | Supported | Supported | **NOT CONFIGURED** |
| **Anthropic Claude** | **YES** | `engine/providers/claude_provider.py` | `claude-3-5-haiku-20241022` | Key Missing | Awaiting Key | Supported | Supported | **NOT CONFIGURED** |

---

## 2. Exact Files Created or Modified in Phase 1

1. **`.env.example`** (Created): Configuration template documenting exact environment variable keys, endpoint parameters, and safety budget limits.
2. **`engine/providers/base_provider.py`** (Created): Abstract base class defining `run()`, status lifecycle methods, and uniform observation normalization.
3. **`engine/providers/google_search_provider.py`** (Created): Dedicated adapter for official Google Custom Search API and SerpAPI with position tracking.
4. **`engine/providers/openai_provider.py`** (Created): Dedicated adapter for OpenAI chat completions with citation regex parsing.
5. **`engine/providers/gemini_provider.py`** (Created): Dedicated adapter for Gemini API with Google Search grounding chunk extraction.
6. **`engine/providers/perplexity_provider.py`** (Created): Dedicated adapter for Perplexity Sonar API with online citation tracking.
7. **`engine/providers/claude_provider.py`** (Created): Dedicated adapter for Anthropic Claude messages API.
8. **`engine/providers/provider_status.py`** (Created): CLI health check tool to inspect configured status across all 5 providers.
9. **`engine/evidence_store.py`** (Created): Flat-file persistence module that hashes measurement metadata and saves deterministic JSON evidence.
10. **`engine/test_providers.py`** (Created): Unit test suite testing unconfigured credentials, observation normalization, and evidence persistence.
11. **`engine/visibility_engine.py`** (Modified): Upgraded to v2.0 to support both offline baseline CSV analysis and live provider execution (`execute_live_check()`).

---

## 3. Actual Terminal Test Execution Results

### Provider Status Inspection
```bash
python -m engine.providers.provider_status
```
**Output:**
```
Provider           | Model Identifier           | Status          
-----------------------------------------------------------------
Google Search      | customsearch-v1            | NOT CONFIGURED  
ChatGPT            | gpt-4o-mini                | NOT CONFIGURED  
Google Gemini      | gemini-1.5-flash           | NOT CONFIGURED  
Perplexity         | sonar                      | NOT CONFIGURED  
Anthropic Claude   | claude-3-5-haiku-20241022  | NOT CONFIGURED  
```

### Unit Test Execution
```bash
python -m unittest engine/test_engine.py engine/test_providers.py
```
**Output:**
```
Ran 6 tests in 0.136s
OK
```

### Smoke Test Execution (Unconfigured Live Execution)
```python
engine = VisibilityEngine()
res = engine.execute_live_check('Q001', 'gemini', market='US')
```
**Output:**
- Execution Status: `FAILED`
- Error Details: `Provider unconfigured: NOT CONFIGURED`
- Evidence Path Saved: `visibility/evidence/live_runs/google_gemini/Q001_google_gemini_US_fae00deb1357.json`
- **Integrity Verified:** Zero fake responses were generated; failure was captured and logged with full audit provenance.

---

## 4. Required Environment Variables

To activate live queries, copy `.env.example` to `.env` or set these in your shell:
- `GOOGLE_SEARCH_API_KEY` & `GOOGLE_SEARCH_ENGINE_ID` (or `SERPAPI_API_KEY`)
- `OPENAI_API_KEY`
- `GEMINI_API_KEY`
- `PERPLEXITY_API_KEY`
- `ANTHROPIC_API_KEY`

---

## 5. Estimated Costs & Safe Batch Limits

| Provider | Recommended Model | Est. Cost per 100 Queries | Safe Rate Limit |
|---|---|---|---|
| **Google Search** | `customsearch-v1` | Free (first 100/day) | 1 req / sec |
| **OpenAI** | `gpt-4o-mini` | ~$0.05 / 100 queries | 3 req / sec |
| **Google Gemini** | `gemini-1.5-flash` | ~$0.03 / 100 queries | 2 req / sec |
| **Perplexity** | `sonar` | ~$0.10 / 100 queries | 1 req / sec |
| **Anthropic** | `claude-3-5-haiku` | ~$0.08 / 100 queries | 2 req / sec |
| **Total Estimated Cost** | All 5 Providers | **~$0.26 / 100 queries** | |

---

## 6. What is Needed Before Processing All 100 Questions

1. Provide API keys for the providers you wish to query live (or use free tiers).
2. Once keys are configured, run batch execution via `engine.execute_live_check(question_id, provider)`.
3. If keys remain unavailable, the engine preserves full offline baseline mode without fabricating results.
