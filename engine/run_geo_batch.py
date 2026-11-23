import os
import sys
import csv
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.providers.gemini_provider import GeminiProvider
from engine.providers.serpapi_provider import SerpApiProvider
from engine.evidence_store import EvidenceStore

def run_geographic_batch():
    gemini = GeminiProvider()
    serpapi = SerpApiProvider()
    store = EvidenceStore()

    with open('visibility/visibility.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    # Pick 2 UK questions and 2 IN questions
    target_qids = ['Q026', 'Q027', 'Q051', 'Q052']
    target_rows = [r for r in rows if r['question_id'] in target_qids]

    print(f"=== Running Geographic Free-Tier Measurements for {len(target_rows)} questions ===")

    for r in target_rows:
        qid = r['question_id']
        qtext = r['question']
        mkt = r['market']
        print(f"\n--- Processing {qid} ({mkt}) ---")
        print(f"Query: \"{qtext}\"")

        # 1. Gemini Grounded API Call
        print("Executing Gemini 2.5 Flash Grounding...")
        g_obs = gemini.run(qtext, market=mkt)
        g_saved = store.save_observation(qid, g_obs)
        print(f"  Gemini Saved: {g_saved} | Status: {g_obs['execution_status']} | Citations: {len(g_obs.get('citations', []))}")
        time.sleep(2)

        # 2. SerpAPI Organic SERP Call
        print(f"Executing Google Search SERP (gl={mkt.lower()})...")
        s_obs = serpapi.run(qtext, market=mkt)
        s_saved = store.save_observation(qid, s_obs)
        print(f"  Google Saved: {s_saved} | Status: {s_obs['execution_status']} | Organic results: {len(s_obs.get('citations', []))} | Pos: {s_obs.get('position')}")
        time.sleep(1)

    print("\nGeographic batch complete.")

if __name__ == "__main__":
    run_geographic_batch()
