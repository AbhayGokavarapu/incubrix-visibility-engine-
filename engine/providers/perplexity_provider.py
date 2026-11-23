"""
IncuBrix Perplexity AI Provider Adapter
========================================
Integrates with the official Perplexity AI Chat Completions API (sonar / sonar-pro)
with real-time online citation tracking.
"""

import os
import json
import urllib.request
from typing import Dict, Any, List
from engine.providers.base_provider import BaseProvider

class PerplexityProvider(BaseProvider):
    def __init__(self, api_key: str = None, model: str = None):
        key = api_key or os.environ.get("PERPLEXITY_API_KEY")
        model_id = model or os.environ.get("PERPLEXITY_MODEL", "sonar")
        super().__init__(name="Perplexity", model_id=model_id, api_key=key)

    def get_status(self) -> str:
        if not self.api_key:
            return "NOT CONFIGURED"
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

        payload = {
            "model": self.model_id,
            "messages": [
                {
                    "role": "system",
                    "content": f"Location: {market}. Be precise, factual, and cite URLs for video software recommendations."
                },
                {"role": "user", "content": question}
            ]
        }

        req = urllib.request.Request(
            "https://api.perplexity.ai/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "User-Agent": "IncuBrix-Visibility-Engine/1.0"
            }
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as res:
                data = json.loads(res.read().decode("utf-8"))

            content = data["choices"][0]["message"]["content"]
            citations = data.get("citations", [])

            return self.create_observation(
                question=question,
                market=market,
                raw_response=data,
                citations=citations,
                text_content=content,
                status="SUCCESS",
                execution_cost_usd=0.001
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
