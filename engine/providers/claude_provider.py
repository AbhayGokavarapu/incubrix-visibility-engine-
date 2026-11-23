"""
IncuBrix Anthropic Claude Provider Adapter (v2.0)
=================================================
Integrates with the official Anthropic Messages API (claude-3-5-haiku / claude-3-5-sonnet)
with web search research instructions and citation parsing.
"""

import os
import json
import urllib.request
import re
from typing import Dict, Any, List
from engine.providers.base_provider import BaseProvider

class ClaudeProvider(BaseProvider):
    def __init__(self, api_key: str = None, model: str = None):
        key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        # Updated to modern Claude model
        model_id = model or os.environ.get("ANTHROPIC_MODEL", "claude-3-5-haiku-latest")
        super().__init__(name="Anthropic Claude", model_id=model_id, api_key=key)

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
            "max_tokens": 1024,
            "system": f"You are a creator economy research analyst. User location: {market}. Search and synthesize information on creator workflows, providing objective recommendations and URLs.",
            "messages": [
                {"role": "user", "content": question}
            ]
        }

        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "User-Agent": "IncuBrix-Visibility-Engine/2.0"
            }
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as res:
                data = json.loads(res.read().decode("utf-8"))

            content_blocks = data.get("content", [])
            text_content = " ".join([b.get("text", "") for b in content_blocks if b.get("type") == "text"])
            citations = re.findall(r'https?://[^\s)"]+', text_content)

            return self.create_observation(
                question=question,
                market=market,
                raw_response=data,
                citations=citations,
                text_content=text_content,
                status="SUCCESS",
                execution_cost_usd=0.0008
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
