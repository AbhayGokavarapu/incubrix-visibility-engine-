import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.providers.serpapi_provider import SerpApiProvider
from engine.evidence_store import EvidenceStore

def test_new_question():
    q = "What are the best automated AI video clipping tools for Twitch streamers in 2026?"
    print(f"Running new question test: \"{q}\"")
    serp = SerpApiProvider()
    store = EvidenceStore()
    obs = serp.run(q, market="US")
    saved = store.save_observation("NEW-Q-TEST", obs)
    print(f"New question executed: Status={obs['execution_status']} | Results={len(obs.get('citations', []))} | Saved={saved}")

if __name__ == "__main__":
    test_new_question()
