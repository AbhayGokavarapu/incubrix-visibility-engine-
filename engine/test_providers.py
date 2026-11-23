"""
IncuBrix Provider Integration Unit Tests (Test Fixtures)
========================================================
Tests all 5 provider interfaces, handling of missing credentials, payload normalization,
citation parsing, and evidence storage using explicitly labeled test fixtures.
"""

import unittest
from engine.providers.base_provider import BaseProvider
from engine.providers.google_search_provider import GoogleSearchProvider
from engine.providers.openai_provider import OpenAIProvider
from engine.providers.gemini_provider import GeminiProvider
from engine.providers.perplexity_provider import PerplexityProvider
from engine.providers.claude_provider import ClaudeProvider
from engine.evidence_store import EvidenceStore

class TestProviderIntegrations(unittest.TestCase):
    def test_missing_credentials_graceful_handling(self):
        providers = [
            GoogleSearchProvider(api_key=""),
            OpenAIProvider(api_key=""),
            GeminiProvider(api_key=""),
            PerplexityProvider(api_key=""),
            ClaudeProvider(api_key="")
        ]
        for p in providers:
            status = p.get_status()
            self.assertIn("NOT CONFIGURED", status)
            obs = p.run("How to turn long videos into shorts with AI?", market="US")
            self.assertEqual(obs["execution_status"], "FAILED")
            self.assertIn("unconfigured", obs["error_details"].lower())

    def test_mock_fixture_observation_normalization(self):
        # Create a mock provider subclass explicitly for fixture validation
        class MockSearchProvider(BaseProvider):
            def get_status(self): return "CONFIGURED"
            def run(self, question, market="US", language="en"):
                return self.create_observation(
                    question=question,
                    market=market,
                    raw_response={"mock_items": [{"link": "https://opus.pro"}]},
                    citations=["https://opus.pro"],
                    text_content="Opus Clip and Descript are great for shorts.",
                    status="SUCCESS"
                )

        mock_p = MockSearchProvider(name="Mock Engine", model_id="fixture-v1")
        obs = mock_p.run("Best AI tools for video repurposing?", market="UK")
        
        self.assertEqual(obs["provider_name"], "Mock Engine")
        self.assertEqual(obs["market"], "UK")
        self.assertEqual(obs["incubrix_mentioned"], False)
        self.assertIn("Opus Clip", obs["competitors_mentioned"])
        self.assertIn("Descript", obs["competitors_mentioned"])
        self.assertEqual(obs["citations"], ["https://opus.pro"])

    def test_evidence_storage_persistence(self):
        store = EvidenceStore(base_dir="visibility/evidence/test_runs")
        sample_obs = {
            "provider_name": "TestProvider",
            "model_identifier": "test-model-1",
            "question": "Sample Question?",
            "market": "US",
            "timestamp_utc": "2026-11-22T13:30:00Z",
            "raw_response": {"status": "ok"},
            "raw_text": "Sample answer text mentioning Opus Clip.",
            "citations": ["https://test.com"],
            "incubrix_mentioned": False,
            "competitors_mentioned": ["Opus Clip"],
            "execution_status": "SUCCESS"
        }
        path = store.save_observation("TEST-Q001", sample_obs)
        import os
        self.assertTrue(os.path.exists(path))
        # Cleanup test file
        if os.path.exists(path):
            os.remove(path)

if __name__ == "__main__":
    unittest.main()
