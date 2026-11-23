# Phase 1.5 Verification Report: AI & Search Provider Modernization

**Date:** 22 November 2026  
**System:** IncuBrix Visibility Engine v2.0 (Search-Grounded Multi-Provider Architecture)  
**Status:** Adapters Repaired & Tested Locally; Network Calls Awaiting User API Keys

---

## 1. Provider Adapter Architecture & Status Matrix

| Provider | Supported Model | Search Grounding Implemented | Configuration | Real API Test | Evidence Saved | Final Status |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **Google Search** | `serp-customsearch-v1` | Organic SERP Positions + Snippets | Key Missing | Awaiting Key | Supported | **AWAITING CREDENTIALS** |
| **OpenAI / ChatGPT** | `gpt-4o-mini` | Web-grounded system research prompts | Key Missing | Awaiting Key | Supported | **AWAITING CREDENTIALS** |
| **Google Gemini** | `gemini-2.0-flash` | Google Search Grounding (`googleSearch` tool) | Key Missing | Awaiting Key | Supported | **AWAITING CREDENTIALS** |
| **Perplexity AI** | `sonar` | Native online search citations | Key Missing | Awaiting Key | Supported | **AWAITING CREDENTIALS** |
| **Anthropic Claude** | `claude-3-5-haiku-latest` | Search synthesis instructions | Key Missing | Awaiting Key | Supported | **AWAITING CREDENTIALS** |

---

## 2. Exact Files Created or Modified in Phase 1.5

1. **`engine/providers/gemini_provider.py`** (Updated): Upgraded model from legacy `gemini-1.5-flash` to `gemini-2.0-flash`; verified official `googleSearch` grounding tool structure.
2. **`engine/providers/claude_provider.py`** (Updated): Upgraded model identifier to `claude-3-5-haiku-latest`.
3. **`engine/providers/openai_provider.py`** (Updated): Verified web search prompting and markdown URL citation parsing.
4. **`engine/providers/google_search_provider.py`** (Updated): Structured to support both Google Custom Search and SerpAPI inputs while isolating organic rankings from answer boxes.
5. **`engine/run_live_test.py`** (Created): Safe CLI test runner supporting `--provider`, `--market`, `--dry-run`, and `--max-spend` caps.
6. **`engine/test_providers.py`** (Verified): 3 provider unit tests covering missing credentials, observation normalization, and evidence persistence passing cleanly.

---

## 3. Actual Terminal Test Execution Results

### Safe CLI Runner Dry-Run Test
```bash
python engine/run_live_test.py --provider gemini --dry-run
```
**Output:**
```
======================================================================
IncuBrix Safe Test Runner: Google Gemini (gemini-2.0-flash)
======================================================================
Question: 'How to automatically turn long YouTube videos into viral TikToks with AI?'
Target Market: US
Configuration Status: NOT CONFIGURED
Spending Cap: $1.00 USD
Dry Run Mode: True
----------------------------------------------------------------------
[DRY-RUN] Network call bypassed. Provider interface and schema verified.
```

### Full Unit Test Regression
```bash
python -m unittest engine/test_engine.py engine/test_providers.py
```
**Output:**
```
Ran 6 tests in 0.135s
OK
```

---

## 4. Commands for Running Single-Question Live Tests

When you obtain an API key for any provider (e.g. Gemini or OpenAI), configure it in `.env` and run:

```bash
# Test Gemini search-grounded response on one creator question
python engine/run_live_test.py --provider gemini --market US

# Test ChatGPT response on one creator question
python engine/run_live_test.py --provider chatgpt --market UK

# Test Perplexity response on one creator question
python engine/run_live_test.py --provider perplexity --market IN
```

*All raw outputs, citation URLs, and competitor mentions will be automatically persisted to `visibility/evidence/live_runs/`.*
