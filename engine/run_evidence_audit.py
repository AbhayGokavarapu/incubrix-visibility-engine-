import os
import sys
import random
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.unified_analyzer import UnifiedProgressAnalyzer
from engine.evidence_validator import EvidenceValidator

def run_random_evidence_audit(sample_size: int = 20, seed: int = 20261122):
    random.seed(seed)
    analyzer = UnifiedProgressAnalyzer()
    all_obs = analyzer.scan_stored_observations()
    validator = EvidenceValidator()

    print(f"=== IncuBrix Phase 6 Randomized Quality Audit ===")
    print(f"Random Seed: {seed}")
    print(f"Total Available Genuine Observations: {len(all_obs)}")
    
    # We sample up to sample_size, or all if fewer exist
    actual_sample_size = min(sample_size, len(all_obs))
    sampled_records = random.sample(all_obs, actual_sample_size)
    print(f"Sampled Records for Deep Trace: {actual_sample_size}\n")

    reproducible_count = 0
    audit_results = []

    for idx, obs in enumerate(sampled_records, start=1):
        fpath = obs.get("_file_path")
        val = validator.validate_evidence_file(fpath)
        is_reproducible = (val.get("status") == "VERIFIED") and os.path.exists(fpath)
        if is_reproducible:
            reproducible_count += 1

        qid = obs.get("question_id", "N/A")
        prov = obs.get("provider_name", "N/A")
        ts = obs.get("timestamp_utc", "N/A")
        method = obs.get("collection_method", "N/A")
        cits = len(obs.get("citations", []))

        audit_results.append({
            "sample_index": idx,
            "question_id": qid,
            "provider": prov,
            "method": method,
            "file_path": fpath,
            "timestamp": ts,
            "citations_count": cits,
            "reproducible": is_reproducible
        })

        print(f"[{idx:02d}] {qid} | {prov:<20} | Method: {method:<22} | Valid: {is_reproducible} | Citations: {cits} | File: {os.path.basename(fpath)}")

    pct = round((reproducible_count / actual_sample_size * 100), 2)
    print(f"\nAudit Summary: {reproducible_count}/{actual_sample_size} records successfully traced to raw evidence on disk.")
    print(f"Reproducibility Rate: {pct}%\n")
    return {
        "seed": seed,
        "sample_size": actual_sample_size,
        "reproducible_count": reproducible_count,
        "reproducibility_pct": pct,
        "records": audit_results
    }

if __name__ == "__main__":
    run_random_evidence_audit()
