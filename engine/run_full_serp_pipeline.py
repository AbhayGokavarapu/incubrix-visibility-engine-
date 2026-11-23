import os
import sys
import csv
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.providers.serpapi_provider import SerpApiProvider
from engine.evidence_store import EvidenceStore

def run_serp_full_pipeline():
    serpapi = SerpApiProvider()
    store = EvidenceStore()

    with open('visibility/visibility.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    existing_files = os.listdir('visibility/evidence/live_runs/google_search')
    already_measured = set(f.split('_')[0] for f in existing_files if f.endswith('.json'))

    pending_rows = [r for r in rows if r['question_id'] not in already_measured]
    print(f"=== Running Full Organic SERP Measurement Pipeline ===")
    print(f"Total Questions in Dataset: {len(rows)}")
    print(f"Already Measured on Disk: {len(already_measured)}")
    print(f"Pending Collection: {len(pending_rows)}")

    successful = 0
    failed = 0

    for idx, r in enumerate(pending_rows, start=1):
        qid = r['question_id']
        qtext = r['question']
        mkt = r['market']

        print(f"[{idx}/{len(pending_rows)}] {qid} ({mkt}) \"{qtext[:45]}...\"")
        try:
            obs = serpapi.run(qtext, market=mkt)
            if obs.get("execution_status") == "SUCCESS":
                store.save_observation(qid, obs)
                cits = len(obs.get("citations", []))
                pos = obs.get("position")
                print(f"    SUCCESS | Organic Results: {cits} | IncuBrix Rank: {pos}")
                successful += 1
            else:
                print(f"    FAILED | Error: {obs.get('error_details')}")
                failed += 1
        except Exception as e:
            print(f"    ERROR | {e}")
            failed += 1

        time.sleep(1)

    print(f"\nPipeline Finished: {successful} collected, {failed} failed.")

if __name__ == "__main__":
    run_serp_full_pipeline()
