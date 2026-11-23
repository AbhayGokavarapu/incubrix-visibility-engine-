"""
IncuBrix Manual Evidence Importer & CLI Workflow
=================================================
Allows verified recording of authentic observations from free consumer AI web interfaces
(ChatGPT Web, Claude Web, Perplexity Web, Gemini Web, and Google Search Web) with exact
provenance, question linking, verbatim citations, screenshot references, and automated validation.
"""

import os
import json
import csv
import argparse
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
from engine.evidence_store import EvidenceStore
from engine.evidence_validator import EvidenceValidator

SUPPORTED_PROVIDERS = {
    "chatgpt": {
        "display_name": "ChatGPT Web",
        "default_model": "chatgpt-free-web",
        "url": "https://chatgpt.com"
    },
    "claude": {
        "display_name": "Claude Web",
        "default_model": "claude-3-5-sonnet-web",
        "url": "https://claude.ai"
    },
    "perplexity": {
        "display_name": "Perplexity Web",
        "default_model": "perplexity-sonar-web",
        "url": "https://www.perplexity.ai"
    },
    "gemini": {
        "display_name": "Gemini Web",
        "default_model": "gemini-web",
        "url": "https://gemini.google.com"
    },
    "google": {
        "display_name": "Google Search Web",
        "default_model": "google-search-web",
        "url": "https://www.google.com"
    }
}

class ManualEvidenceImporter:
    def __init__(self, evidence_dir: str = "visibility/evidence/manual_imports"):
        self.evidence_dir = evidence_dir
        os.makedirs(self.evidence_dir, exist_ok=True)
        self.evidence_store = EvidenceStore(base_dir=self.evidence_dir)
        self.validator = EvidenceValidator(evidence_index_path=os.path.join(self.evidence_dir, "evidence_index.json"))

    def get_question_details(self, question_id: str, csv_path: str = "visibility/visibility.csv") -> Optional[Dict[str, str]]:
        if not os.path.exists(csv_path):
            return None
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("question_id") == question_id:
                    return {
                        "question_id": row.get("question_id"),
                        "question": row.get("question"),
                        "market": row.get("market", "US")
                    }
        return None

    def import_observation(
        self,
        question_id: str,
        question_text: str,
        provider_name: str,
        interface_or_model: str,
        market: str,
        observation_date_utc: str,
        raw_answer_text: str,
        citations: List[str],
        screenshot_path: Optional[str] = None,
        google_position: Optional[int] = None,
        day_identifier: str = "DAY_1"
    ) -> Dict[str, Any]:
        """
        Validates, normalizes, and stores manual observations without synthesizing data.
        """
        text_lower = raw_answer_text.lower()
        # Avoid false positives when the auditor notes "incubrix is not ranked/mentioned"
        is_negative_mention = "incubrix is not" in text_lower or "incubrix not found" in text_lower or "incubrix: not" in text_lower
        mentioned = "incubrix" in text_lower and not is_negative_mention
        
        known_competitors = ["Opus Clip", "Descript", "Munch", "CapCut", "Veed.io", "Submagic", "Kapwing", "Riverside", "Vidyo.ai"]
        competitors_found = [comp for comp in known_competitors if comp.lower() in text_lower]

        observation = {
            "provider_name": provider_name,
            "model_identifier": interface_or_model,
            "question": question_text,
            "market": market.upper(),
            "timestamp_utc": observation_date_utc,
            "collection_method": "MANUAL_VERIFIED_IMPORT",
            "execution_status": "SUCCESS",
            "incubrix_mentioned": mentioned,
            "competitors_mentioned": competitors_found,
            "position": google_position,
            "citations": citations,
            "raw_text": raw_answer_text,
            "raw_response": {
                "import_type": "manual_observation",
                "screenshot_reference": screenshot_path,
                "recorded_by": "candidate_verified",
                "day_identifier": day_identifier
            },
            "error_details": None
        }

        saved_path = self.evidence_store.save_observation(question_id, observation)
        observation["evidence_path"] = saved_path
        
        # Immediate validation check
        val_result = self.validator.validate_evidence_file(saved_path)
        observation["validation_status"] = val_result.get("status", "UNVERIFIED")
        return observation

def main():
    parser = argparse.ArgumentParser(description="IncuBrix Manual Evidence Importer CLI")
    parser.add_argument("--question-id", required=True, help="Question ID (e.g., Q001)")
    parser.add_argument("--provider", required=True, choices=["chatgpt", "claude", "perplexity", "gemini", "google"], help="Target provider")
    parser.add_argument("--market", default="US", help="Market: US, UK, IN")
    parser.add_argument("--text-file", help="Path to file containing verbatim raw response text")
    parser.add_argument("--text", help="Raw response text string")
    parser.add_argument("--citations", nargs="*", default=[], help="Citations and source URLs")
    parser.add_argument("--screenshot", help="Optional path to screenshot file")
    parser.add_argument("--position", type=int, help="SERP organic ranking position if applicable")
    parser.add_argument("--day", default="DAY_1", choices=["DAY_1", "DAY_2"], help="Observation day")
    args = parser.parse_args()

    importer = ManualEvidenceImporter()
    q_info = importer.get_question_details(args.question_id)
    if not q_info:
        print(f"Error: Question ID {args.question_id} not found in visibility/visibility.csv")
        return

    prov_cfg = SUPPORTED_PROVIDERS[args.provider]
    
    raw_content = ""
    if args.text_file and os.path.exists(args.text_file):
        with open(args.text_file, "r", encoding="utf-8") as f:
            raw_content = f.read()
    elif args.text:
        raw_content = args.text
    else:
        print(f"\nReady to collect manual observation for {args.question_id}:")
        print(f"Provider: {prov_cfg['display_name']} ({prov_cfg['url']})")
        print(f"Market: {args.market}")
        print(f"Question: \"{q_info['question']}\"")
        print("\nPlease pass --text or --text-file containing the verbatim answer.")
        return

    obs = importer.import_observation(
        question_id=args.question_id,
        question_text=q_info["question"],
        provider_name=prov_cfg["display_name"],
        interface_or_model=prov_cfg["default_model"],
        market=args.market,
        observation_date_utc=datetime.now(timezone.utc).isoformat(),
        raw_answer_text=raw_content,
        citations=args.citations,
        screenshot_path=args.screenshot,
        google_position=args.position,
        day_identifier=args.day
    )

    print("\n--- Manual Observation Successfully Imported ---")
    print(f"Question ID: {args.question_id}")
    print(f"Provider: {obs['provider_name']}")
    print(f"IncuBrix Mentioned: {obs['incubrix_mentioned']}")
    print(f"Competitors Found: {obs['competitors_mentioned']}")
    print(f"Citations Recorded: {len(obs['citations'])}")
    print(f"Validation Status: {obs['validation_status']}")
    print(f"Saved Evidence: {obs['evidence_path']}")

if __name__ == "__main__":
    main()
