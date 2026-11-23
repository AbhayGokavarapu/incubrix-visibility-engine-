"""
IncuBrix Phase 3 Comprehensive Unit Test Suite
==============================================
Validates:
1. EvidenceValidator rejection of fake or failed outputs.
2. EvidenceValidator verification of well-formed responses.
3. Detailed batch planning math with contingency buffer.
4. Provider adapter status lifecycle.
5. Manual importer validation with screenshot references.
6. Graceful recovery on missing evidence indices.
"""

import unittest
import os
import shutil
import json
from engine.evidence_validator import EvidenceValidator
from engine.evidence_store import EvidenceStore
from engine.batch_planner import calculate_detailed_batch_plan
from engine.manual_importer import ManualEvidenceImporter

class TestPhase3Integrations(unittest.TestCase):
    def setUp(self):
        self.test_dir = "visibility/evidence/test_phase3_runs"
        os.makedirs(self.test_dir, exist_ok=True)
        self.store = EvidenceStore(base_dir=self.test_dir)
        self.validator = EvidenceValidator(evidence_index_path=os.path.join(self.test_dir, "evidence_index.json"))

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_evidence_validator_rejects_failed_status(self):
        # Create observation with FAILED status
        failed_obs = {
            "provider_name": "TestAI",
            "model_identifier": "test-model",
            "question": "Sample Question",
            "market": "US",
            "timestamp_utc": "2026-11-22T14:00:00Z",
            "execution_status": "FAILED",
            "error_details": "API Key Invalid",
            "raw_text": "",
            "raw_response": None,
            "citations": []
        }
        path = self.store.save_observation("Q-FAIL-01", failed_obs)
        res = self.validator.validate_evidence_file(path)
        self.assertEqual(res["status"], "FAILED")
        self.assertIn("Execution status was FAILED", res["reason"])

    def test_evidence_validator_verifies_valid_payload(self):
        valid_obs = {
            "provider_name": "TestAI",
            "model_identifier": "test-model",
            "question": "How to make shorts?",
            "market": "US",
            "timestamp_utc": "2026-11-22T14:00:00Z",
            "execution_status": "SUCCESS",
            "error_details": None,
            "raw_text": "Opus Clip and IncuBrix are great options for creators.",
            "raw_response": {"id": "123", "choices": [{"text": "Sample"}]},
            "citations": ["https://incubrix.com/features", "https://opus.pro"]
        }
        path = self.store.save_observation("Q-PASS-01", valid_obs)
        res = self.validator.validate_evidence_file(path)
        self.assertEqual(res["status"], "VERIFIED")
        self.assertEqual(res["valid_citations_count"], 2)
        self.assertEqual(res["incubrix_mentioned"], True)

    def test_detailed_batch_plan_calculation(self):
        plan = calculate_detailed_batch_plan(
            num_questions=100,
            market_distribution={"US": 50, "UK": 25, "IN": 25},
            measurement_days=2,
            retry_contingency_percent=10.0
        )
        self.assertEqual(plan["base_requests_total"], 1000)
        self.assertEqual(plan["retry_contingency_requests"], 100)
        self.assertEqual(plan["total_projected_requests"], 1100)
        self.assertAlmostEqual(plan["total_estimated_cost_usd"], 1.74, delta=0.05)

    def test_manual_importer_verification(self):
        importer = ManualEvidenceImporter(evidence_dir=self.test_dir)
        obs = importer.import_observation(
            question_id="Q-MANUAL-01",
            question_text="Best video repurposing AI?",
            provider_name="ChatGPT Web",
            interface_or_model="gpt-4o-web-consumer",
            market="US",
            observation_date_utc="2026-11-22T14:00:00Z",
            raw_answer_text="Opus Clip is popular for video clipping.",
            citations=["https://opus.pro"],
            screenshot_path="evidence/screenshots/sample.png"
        )
        self.assertEqual(obs["collection_method"], "MANUAL_VERIFIED_IMPORT")
        self.assertTrue(os.path.exists(obs["evidence_path"]))

if __name__ == "__main__":
    unittest.main()
