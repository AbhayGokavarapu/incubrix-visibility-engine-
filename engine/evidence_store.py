"""
IncuBrix Real Evidence Storage & Evidence Indexer
=================================================
Persists raw responses, normalized metadata, and citations into an audited flat-file
evidence store with unique deterministic identifiers.
"""

import os
import json
import hashlib
from datetime import datetime, timezone
from typing import Dict, Any, Optional

class EvidenceStore:
    def __init__(self, base_dir: str = "visibility/evidence/live_runs"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        self.index_file = os.path.join(self.base_dir, "evidence_index.json")

    def _generate_measurement_id(self, question_id: str, provider: str, market: str, timestamp_str: str) -> str:
        raw_key = f"{question_id}_{provider}_{market}_{timestamp_str}"
        return hashlib.sha256(raw_key.encode("utf-8")).hexdigest()[:12]

    def save_observation(self, question_id: str, observation: Dict[str, Any]) -> str:
        """
        Saves normalized observation and raw response payload.
        Returns the relative file path to the saved evidence.
        """
        provider_safe = observation["provider_name"].lower().replace(" ", "_")
        market = observation["market"].upper()
        ts = observation.get("timestamp_utc", datetime.now(timezone.utc).isoformat())
        
        meas_id = self._generate_measurement_id(question_id, provider_safe, market, ts)
        filename = f"{question_id}_{provider_safe}_{market}_{meas_id}.json"
        
        provider_dir = os.path.join(self.base_dir, provider_safe)
        os.makedirs(provider_dir, exist_ok=True)
        file_path = os.path.join(provider_dir, filename)

        # Detect mention if not explicitly defined
        raw_text_full = observation.get("raw_text", "") or observation.get("raw_text_summary", "")
        mentioned = observation.get("incubrix_mentioned")
        if mentioned is None:
            mentioned = "incubrix" in raw_text_full.lower()

        record = {
            "measurement_id": meas_id,
            "question_id": question_id,
            "timestamp_utc": ts,
            "provider_name": observation["provider_name"],
            "model_identifier": observation["model_identifier"],
            "question": observation["question"],
            "market": market,
            "collection_method": observation.get("collection_method", "API_AUTOMATED"),
            "execution_status": observation.get("execution_status", "SUCCESS"),
            "incubrix_mentioned": bool(mentioned),
            "competitors_mentioned": observation.get("competitors_mentioned", []),
            "position": observation.get("position"),
            "citations": observation.get("citations", []),
            "raw_text_summary": raw_text_full,
            "raw_payload": observation.get("raw_response"),
            "error_details": observation.get("error_details")
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2)

        # Update index
        self._update_index(question_id, meas_id, file_path)
        return file_path

    def _update_index(self, question_id: str, measurement_id: str, path: str):
        index = {}
        if os.path.exists(self.index_file):
            try:
                with open(self.index_file, "r", encoding="utf-8") as f:
                    index = json.load(f)
            except Exception:
                index = {}

        if question_id not in index:
            index[question_id] = []
        index[question_id].append({
            "measurement_id": measurement_id,
            "evidence_path": path,
            "recorded_at": datetime.now(timezone.utc).isoformat()
        })

        with open(self.index_file, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=2)
