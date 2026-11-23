import os
import sys
import time
import csv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.providers.gemini_provider import GeminiProvider
from engine.evidence_store import EvidenceStore

def run_gemini_sample():
    p = GeminiProvider()
    store = EvidenceStore()
    with open('visibility/visibility.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    target_rows = [r for r in rows if r['question_id'] in ['Q002', 'Q003', 'Q004', 'Q005']]
    for r in target_rows:
        qid = r['question_id']
        qtext = r['question']
        mkt = r['market']
        print(f"Executing Gemini for {qid} ({mkt})...")
        obs = p.run(qtext, market=mkt)
        saved = store.save_observation(qid, obs)
        status = obs.get("execution_status")
        cits = len(obs.get("citations", []))
        mentions = obs.get("incubrix_mentioned")
        print(f"  Saved: {saved} | Status: {status} | Citations: {cits} | IncuBrix: {mentions}")
        time.sleep(2)

if __name__ == "__main__":
    run_gemini_sample()
