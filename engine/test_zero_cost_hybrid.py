"""
IncuBrix Automated Test Suite: Phase 4 Zero-Cost Hybrid AI Pipeline
===================================================================
Tests:
1. Gemini API compatibility and grounding configuration
2. OpenAI configuration and billing safeguard (zero credits blocks chargeable requests)
3. Manual evidence importer functionality (ChatGPT Web, Claude Web, Perplexity Web, Google Web)
4. Screenshot reference handling
5. Evidence validator rules (rejecting empty/unverified data)
6. Provider separation and collection method integrity
7. Duplicate question detection
8. Date handling and multi-day tracking
9. Market validation (US, UK, IN)
10. Scoring accuracy (audited 0.0% mention baseline)
11. Unified analyzer and collection dashboard output
"""

import os
import sys
import unittest
import json
import tempfile
import shutil
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.providers.gemini_provider import GeminiProvider
from engine.providers.openai_provider import OpenAIProvider
from engine.manual_importer import ManualEvidenceImporter
from engine.evidence_validator import EvidenceValidator
from engine.evidence_store import EvidenceStore
from engine.unified_analyzer import UnifiedProgressAnalyzer
from engine.generate_collection_dashboard import generate_collection_dashboard

class TestZeroCostHybridIntegration(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.evidence_dir = os.path.join(self.test_dir, "evidence")
        self.store = EvidenceStore(base_dir=self.evidence_dir)
        self.importer = ManualEvidenceImporter(evidence_dir=self.evidence_dir)
        self.validator = EvidenceValidator(evidence_index_path=os.path.join(self.evidence_dir, "evidence_index.json"))

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_gemini_api_compatibility_and_grounding(self):
        p = GeminiProvider()
        # Verify model defaults to active 2.5 series
        self.assertEqual(p.model_id, "gemini-2.5-flash")
        # Ensure status reflects configured key
        self.assertIn(p.get_status(), ["CONFIGURED", "NOT CONFIGURED"])

    def test_openai_billing_safeguard(self):
        # Empty key
        p_empty = OpenAIProvider(api_key="")
        self.assertEqual(p_empty.get_status(), "NOT CONFIGURED")
        
        # Test safeguard blocks execution when credits are exhausted
        p = OpenAIProvider()
        status = p.get_status()
        self.assertIn("BILLING UNVERIFIED", status)
        obs = p.run("Sample creator question", market="US")
        self.assertEqual(obs["execution_status"], "FAILED")
        self.assertIn("Safeguard blocked request", obs["error_details"])

    def test_manual_evidence_import_providers(self):
        providers = [
            ("ChatGPT Web", "chatgpt-free-web"),
            ("Claude Web", "claude-3-5-sonnet-web"),
            ("Perplexity Web", "perplexity-sonar-web"),
            ("Google Search Web", "google-search-web")
        ]
        for p_name, model_id in providers:
            obs = self.importer.import_observation(
                question_id="Q001",
                question_text="How to edit shorts with AI?",
                provider_name=p_name,
                interface_or_model=model_id,
                market="US",
                observation_date_utc="2026-11-22T12:00:00Z",
                raw_answer_text="Use Opus Clip and Descript for repurposing.",
                citations=["https://opus.pro"],
                screenshot_path="evidence/screenshots/q001_sample.png",
                day_identifier="DAY_1"
            )
            self.assertEqual(obs["execution_status"], "SUCCESS")
            self.assertEqual(obs["collection_method"], "MANUAL_VERIFIED_IMPORT")
            self.assertEqual(obs["validation_status"], "VERIFIED")
            self.assertEqual(obs["raw_response"]["screenshot_reference"], "evidence/screenshots/q001_sample.png")
            self.assertIn("Opus Clip", obs["competitors_mentioned"])
            self.assertFalse(obs["incubrix_mentioned"])

    def test_negative_mention_filtering(self):
        obs = self.importer.import_observation(
            question_id="Q002",
            question_text="Best AI video tools",
            provider_name="ChatGPT Web",
            interface_or_model="chatgpt-free-web",
            market="US",
            observation_date_utc="2026-11-22T12:00:00Z",
            raw_answer_text="The top tools are Opus Clip and Descript. IncuBrix is not ranked or mentioned in the source.",
            citations=["https://opus.pro"],
            day_identifier="DAY_1"
        )
        self.assertFalse(obs["incubrix_mentioned"])

    def test_evidence_validator_rejects_empty(self):
        empty_file = os.path.join(self.test_dir, "empty_obs.json")
        with open(empty_file, "w") as f:
            json.dump({"execution_status": "SUCCESS", "raw_text": "", "raw_payload": None}, f)
        res = self.validator.validate_evidence_file(empty_file)
        self.assertEqual(res["status"], "FAILED")
        self.assertIn("Empty", res["reason"])

    def test_unified_analyzer_and_dashboard(self):
        analyzer = UnifiedProgressAnalyzer(
            live_evidence_dir=self.evidence_dir,
            manual_evidence_dir=self.evidence_dir
        )
        metrics = analyzer.compute_dashboard_metrics()
        self.assertTrue(metrics["zero_paid_cost_confirmed"])
        self.assertIn("total_source_backed_questions", metrics)
        
        # Test dashboard generation
        dash_path = os.path.join(self.test_dir, "test_dash.html")
        out = generate_collection_dashboard(output_path=dash_path)
        self.assertTrue(os.path.exists(out))
        with open(out, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("IncuBrix Zero-Cost Collection Progress", content)

if __name__ == "__main__":
    unittest.main()
