import os
import sys
import csv
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.providers.serpapi_provider import SerpApiProvider
from engine.evidence_store import EvidenceStore

def run_google_serp_batch():
    p = SerpApiProvider()
    store = EvidenceStore()
    with open('visibility/visibility.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    for r in rows[:5]:
        qid = r['question_id']
        qtext = r['question']
        mkt = r['market']
        obs = p.run(qtext, market=mkt)
        saved = store.save_observation(qid, obs)
        cits = len(obs.get("citations", []))
        pos = obs.get("position")
        ab = obs.get("has_serp_answer_box")
        print(f"SerpAPI Google saved for {qid}: {saved} | Organic results: {cits} | Pos: {pos} | AnswerBox: {ab}")
        time.sleep(1)

if __name__ == "__main__":
    run_google_serp_batch()
