import os
import sys
import csv
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.providers.gemini_provider import GeminiProvider
from engine.providers.serpapi_provider import SerpApiProvider
from engine.evidence_store import EvidenceStore

def run_collection_batch(qids):
    gemini = GeminiProvider()
    serpapi = SerpApiProvider()
    store = EvidenceStore()

    with open('visibility/visibility.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    target_rows = [r for r in rows if r['question_id'] in qids]
    print(f"=== Running Batch for {len(target_rows)} Questions ===")

    for r in target_rows:
        qid = r['question_id']
        qtext = r['question']
        mkt = r['market']
        print(f"\n[{qid}] ({mkt}) \"{qtext[:50]}...\"")

        # 1. Gemini Grounding
        try:
            g_obs = gemini.run(qtext, market=mkt)
            g_path = store.save_observation(qid, g_obs)
            print(f"  Gemini: {g_obs['execution_status']} | Cits: {len(g_obs.get('citations', []))} | IncuBrix: {g_obs.get('incubrix_mentioned')}")
        except Exception as e:
            print(f"  Gemini Error: {e}")
        time.sleep(2)

        # 2. SerpAPI
        try:
            s_obs = serpapi.run(qtext, market=mkt)
            s_path = store.save_observation(qid, s_obs)
            print(f"  Google SERP: {s_obs['execution_status']} | Pos: {s_obs.get('position')} | Cits: {len(s_obs.get('citations', []))}")
        except Exception as e:
            print(f"  SerpAPI Error: {e}")
        time.sleep(1)

    print("\nBatch complete.")

if __name__ == "__main__":
    batch_qids = ['Q006', 'Q007', 'Q008', 'Q009', 'Q010', 'Q028', 'Q029', 'Q053', 'Q054', 'Q055']
    run_collection_batch(batch_qids)
