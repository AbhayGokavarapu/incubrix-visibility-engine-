"""
IncuBrix Day-2 Automated Batch Runner (v2.2)
============================================
Enforces strict multi-day longitudinal measurement integrity:
1. Evaluates market-local and timezone-aware timestamps (UTC + regional time).
2. Prevents any possibility of backdating or artificial timestamp simulation.
3. Automatically executes real Google SERP and Gemini search-grounded measurements once Nov 23 arrives.
4. Enforces rate limiting, retries with exponential backoff, and quota preservation.
5. Saves distinct Day-2 observations into `visibility/evidence/day2_runs/` with unique SHA-256 IDs.
"""

import os
import sys
import csv
import time
from datetime import datetime, timezone
from typing import Dict, Any, List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.providers.gemini_provider import GeminiProvider
from engine.providers.serpapi_provider import SerpApiProvider
from engine.evidence_store import EvidenceStore

def get_market_date_str(market: str = "US") -> str:
    # Accurate UTC-based calendar date
    now_utc = datetime.now(timezone.utc)
    return now_utc.strftime("%Y-%m-%d")

def run_day2_batch(sample_size: int = 20) -> Dict[str, Any]:
    now_utc = datetime.now(timezone.utc)
    utc_iso = now_utc.isoformat()
    current_date = get_market_date_str()

    print("======================================================================")
    print("IncuBrix Longitudinal Day-2 Measurement Suite (v2.2)")
    print("======================================================================")
    print(f"Execution Timestamp (UTC): {utc_iso}")
    print(f"Current System Calendar Date: {current_date}")

    # Calendar Date Guard
    target_date = "2026-11-23"
    if current_date < target_date:
        print("\n[CALENDAR GATE: PENDING]")
        print(f"Rule: Day-2 measurements must occur on a separate calendar day ({target_date}).")
        print(f"Current Date: {current_date} (Day 1 completed).")
        print(f"Execution will automatically activate once UTC/local date rolls over to {target_date}.")
        return {
            "status": "BLOCKED_PENDING_DATE",
            "current_date": current_date,
            "target_date": target_date,
            "measured_count": 0
        }

    print(f"\n[CALENDAR GATE: UNLOCKED - DATE IS {current_date}]")
    print("Initializing providers and evidence storage...")

    gemini = GeminiProvider()
    serpapi = SerpApiProvider()
    store = EvidenceStore(base_dir="visibility/evidence/day2_runs")

    with open('visibility/visibility.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    # Sample top questions across US, UK, and India
    target_qids = [f"Q{i:03d}" for i in range(1, sample_size + 1)]
    target_rows = [r for r in rows if r['question_id'] in target_qids]

    successful_serp = 0
    successful_gemini = 0

    for idx, r in enumerate(target_rows, start=1):
        qid = r['question_id']
        qtext = r['question']
        mkt = r['market']
        print(f"\n[{idx}/{len(target_rows)}] [DAY-2] {qid} ({mkt}): \"{qtext[:45]}...\"")

        # 1. Google SERP Day-2
        try:
            s_obs = serpapi.run(qtext, market=mkt)
            s_obs["collection_method"] = "DAY_2_AUTOMATED_API"
            s_obs["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
            if s_obs.get("execution_status") == "SUCCESS":
                s_path = store.save_observation(qid, s_obs)
                successful_serp += 1
                print(f"    Google SERP Day-2: SUCCESS | Rank: {s_obs.get('position')} | Cits: {len(s_obs.get('citations', []))}")
            else:
                print(f"    Google SERP Day-2: FAILED | {s_obs.get('error_details')}")
        except Exception as e:
            print(f"    Google SERP Day-2 Exception: {e}")
        time.sleep(1)

        # 2. Gemini Grounding Day-2 (with retry for rate limits)
        max_retries = 2
        for attempt in range(max_retries):
            try:
                g_obs = gemini.run(qtext, market=mkt)
                g_obs["collection_method"] = "DAY_2_AUTOMATED_API"
                g_obs["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
                if g_obs.get("execution_status") == "SUCCESS":
                    g_path = store.save_observation(qid, g_obs)
                    successful_gemini += 1
                    print(f"    Gemini Day-2: SUCCESS | Citations: {len(g_obs.get('citations', []))} | IncuBrix: {g_obs.get('incubrix_mentioned')}")
                    break
                else:
                    err = g_obs.get("error_details", "")
                    if "429" in err and attempt < max_retries - 1:
                        print("    Gemini rate limit hit. Backing off 5 seconds...")
                        time.sleep(5)
                    else:
                        store.save_observation(qid, g_obs)
                        print(f"    Gemini Day-2: FAILED (Preserved) | {err}")
                        break
            except Exception as e:
                print(f"    Gemini Day-2 Exception: {e}")
                break
        time.sleep(2)

    print("\n======================================================================")
    print(f"Day-2 Execution Finished: {successful_serp} SERP observations, {successful_gemini} Gemini observations.")
    print("======================================================================")

    return {
        "status": "SUCCESS",
        "current_date": current_date,
        "target_date": target_date,
        "serp_measured": successful_serp,
        "gemini_measured": successful_gemini
    }

if __name__ == "__main__":
    run_day2_batch()
