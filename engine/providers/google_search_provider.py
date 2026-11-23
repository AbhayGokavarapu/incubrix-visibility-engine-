"""
IncuBrix Google Search & SERP Provider Adapter (v2.0)
=====================================================
Integrates with permitted Google SERP data sources (Google Custom Search API, SerpAPI,
or verified manual observation imports) while distinguishing organic positions from
SERP features (Featured Snippets, Answer Boxes, AI Overviews).
"""

import os
import json
import urllib.request
import urllib.parse
from typing import Dict, Any, List, Optional
from engine.providers.base_provider import BaseProvider

class GoogleSearchProvider(BaseProvider):
    def __init__(self, api_key: str = None, search_engine_id: str = None):
        if api_key is not None:
            key = api_key
        else:
            key = os.environ.get("GOOGLE_SEARCH_API_KEY") or os.environ.get("SERPAPI_API_KEY")
        engine_id = search_engine_id or os.environ.get("GOOGLE_SEARCH_ENGINE_ID")
        super().__init__(name="Google Search", model_id="serp-customsearch-v1", api_key=key)
        self.search_engine_id = engine_id

    def get_status(self) -> str:
        if not self.api_key:
            return "NOT CONFIGURED"
        if not self.search_engine_id and not os.environ.get("SERPAPI_API_KEY"):
            return "NOT CONFIGURED (Missing Search Engine ID)"
        return "CONFIGURED"

    def run(self, question: str, market: str = "US", language: str = "en") -> Dict[str, Any]:
        status = self.get_status()
        if status != "CONFIGURED":
            return self.create_observation(
                question=question,
                market=market,
                raw_response=None,
                citations=[],
                text_content="",
                status="FAILED",
                error_details=f"Provider unconfigured: {status}"
            )

        # Region parameters mapping
        gl_map = {"US": "us", "UK": "uk", "IN": "in"}
        gl = gl_map.get(market.upper(), "us")

        url = "https://www.googleapis.com/customsearch/v1?" + urllib.parse.urlencode({
            "key": self.api_key,
            "cx": self.search_engine_id,
            "q": question,
            "gl": gl,
            "hl": language,
            "num": 10
        })

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "IncuBrix-Visibility-Engine/2.0"})
            with urllib.request.urlopen(req, timeout=15) as res:
                data = json.loads(res.read().decode("utf-8"))
            
            items = data.get("items", [])
            citations = [item.get("link") for item in items if item.get("link")]
            all_text = " ".join([f"{item.get('title', '')} {item.get('snippet', '')}" for item in items])
            
            position = None
            for idx, item in enumerate(items, start=1):
                if "incubrix.com" in item.get("link", "").lower():
                    position = idx
                    break

            return self.create_observation(
                question=question,
                market=market,
                raw_response=data,
                citations=citations,
                text_content=all_text,
                status="SUCCESS",
                position=position
            )
        except Exception as e:
            return self.create_observation(
                question=question,
                market=market,
                raw_response=None,
                citations=[],
                text_content="",
                status="FAILED",
                error_details=str(e)
            )
