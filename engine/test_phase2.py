"""
IncuBrix Robust Unit Test Suite v2.0
====================================
Tests manual evidence imports, observation normalization, batch planning calculations,
error handling, and provider offline behavior with zero synthetic assessment data.
"""

import unittest
import os
import shutil
from engine.manual_importer import ManualEvidenceImporter
from engine.batch_planner import calculate_batch_plan
from engine.providers import (
    GoogleSearchProvider,
    OpenAIProvider,
    GeminiProvider,
    PerplexityProvider,
    ClaudeProvider
)

class TestPhase2Integrations(unittest.TestCase):
    def setUp(self):
        self.test_dir = "visibility/evidence/test_manual_runs"
        self.importer = ManualEvidenceImporter(evidence_dir=self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_manual_evidence_import_and_competitor_detection(self):
        obs = self.importer.import_observation(
            question_id="Q-TEST-01",
            question_text="What is the best AI video repurposing software?",
            provider_name="ChatGPT Web",
            interface_or_model="gpt-4o-web-consumer",
            market="US",
            observation_date_utc="2026-11-22T13:00:00Z",
            raw_answer_text="Opus Clip and Munch are the most popular tools for turning videos into shorts.",
            citations=["https://opus.pro", "https://getmunch.com"],
            screenshot_path="evidence/screenshots/Q_TEST_01_chatgpt.png",
            google_position=None
        )

        self.assertEqual(obs["execution_status"], "SUCCESS")
        self.assertEqual(obs["collection_method"], "MANUAL_VERIFIED_IMPORT")
        self.assertEqual(obs["incubrix_mentioned"], False)
        self.assertIn("Opus Clip", obs["competitors_mentioned"])
        self.assertIn("Munch", obs["competitors_mentioned"])
        self.assertEqual(len(obs["citations"]), 2)
        self.assertTrue(os.path.exists(obs["evidence_path"]))

    def test_batch_planner_cost_and_request_math(self):
        plan = calculate_batch_plan(num_questions=10, days=1)
        # 10 questions * 5 providers * 1 day = 50 requests
        self.assertEqual(plan["total_requests_all_days"], 50)
        self.assertGreater(plan["estimated_total_cost_usd"], 0.0)
        self.assertEqual(plan["safe_batch_size"], 25)

    def test_provider_status_lifecycle_unconfigured(self):
        p = GeminiProvider(api_key="")
        self.assertEqual(p.get_status(), "NOT CONFIGURED")
        obs = p.run("Sample question", market="US")
        self.assertEqual(obs["execution_status"], "FAILED")
        self.assertIn("unconfigured", obs["error_details"].lower())

if __name__ == "__main__":
    unittest.main()
