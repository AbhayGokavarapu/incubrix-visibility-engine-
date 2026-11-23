"""
Unit tests for the IncuBrix Visibility Engine.
Tests cover data ingestion, duplicate filtering, schema validation, and error recovery.
"""

import unittest
import os
import tempfile
import csv
from engine.visibility_engine import VisibilityEngine

class TestVisibilityEngine(unittest.TestCase):
    def setUp(self):
        # Create a temporary mock CSV
        self.temp_dir = tempfile.TemporaryDirectory()
        self.mock_csv = os.path.join(self.temp_dir.name, "mock_visibility.csv")
        
        self.headers = [
            "question_id", "question", "intent", "source_type", "market",
            "google_position", "answer_box_or_ai_overview", "chatgpt", "gemini", "perplexity"
        ]
        
        self.sample_rows = [
            {
                "question_id": "T001",
                "question": "How to turn long videos into shorts with AI?",
                "intent": "Informational",
                "source_type": "Google",
                "market": "US",
                "google_position": ">100",
                "answer_box_or_ai_overview": "AI Overview Present",
                "chatgpt": "Not Mentioned",
                "gemini": "Not Mentioned",
                "perplexity": "Not Mentioned"
            },
            {
                "question_id": "T002",
                "question": "How to turn long videos into shorts with AI?",  # Duplicate question
                "intent": "Informational",
                "source_type": "Google",
                "market": "US",
                "google_position": ">100",
                "answer_box_or_ai_overview": "AI Overview Present",
                "chatgpt": "Not Mentioned",
                "gemini": "Not Mentioned",
                "perplexity": "Not Mentioned"
            },
            {
                "question_id": "T003",
                "question": "Best video repurposing software in 2026?",
                "intent": "Commercial",
                "source_type": "Reddit",
                "market": "UK",
                "google_position": ">100",
                "answer_box_or_ai_overview": "Featured Snippet",
                "chatgpt": "Mentioned IncuBrix",
                "gemini": "Not Mentioned",
                "perplexity": "Not Mentioned"
            }
        ]
        
        with open(self.mock_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(self.sample_rows)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_and_deduplication(self):
        engine = VisibilityEngine(input_csv=self.mock_csv)
        self.assertTrue(engine.load_and_validate())
        # Should detect that T002 is a duplicate of T001
        self.assertEqual(engine.metrics["total_queries"], 3)
        self.assertEqual(engine.metrics["unique_queries"], 2)

    def test_scoring_logic(self):
        engine = VisibilityEngine(input_csv=self.mock_csv)
        engine.load_and_validate()
        metrics = engine.calculate_scores()
        
        # 1 out of 2 unique items has a mention -> 50%
        self.assertEqual(metrics["incubrix_mentions"], 1)
        self.assertEqual(metrics["visibility_score"], 50.0)
        self.assertEqual(metrics["answer_box_presence"], 2)

    def test_failure_recovery_on_missing_file(self):
        bad_engine = VisibilityEngine(input_csv="non_existent_file.csv")
        # Should gracefully return False without crashing
        self.assertFalse(bad_engine.load_and_validate())

if __name__ == "__main__":
    unittest.main()
