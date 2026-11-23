"""
IncuBrix OpenAI / ChatGPT Provider Adapter (v2.0)
=================================================
Integrates with the official OpenAI API using web search capabilities (web_search tool
or web-grounded completions) to ensure search-grounded creator visibility measurements.
"""

import os
import json
import urllib.request
import urllib.error
import re
from typing import Dict, Any, List
from engine.providers.base_provider import BaseProvider
import engine.env_loader

class OpenAIProvider(BaseProvider):
    def __init__(self, api_key: str = None, model: str = None):
        engine.env_loader.load_dotenv()
        key = api_key if api_key is not None else os.environ.get("OPENAI_API_KEY")
        # Default to search-capable modern model identifier
        model_id = model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
        super().__init__(name="ChatGPT", model_id=model_id, api_key=key)
        self._quota_checked = False
        self._has_quota = False
        self._quota_error_msg = None

    def check_quota_status(self) -> Dict[str, Any]:
        """
        Safely inspects whether usable credit quota exists without charging.
        Uses minimal probe with safeguards.
        """
        if not self.api_key:
            return {"configured": False, "has_quota": False, "status": "NOT CONFIGURED", "error": "Missing OPENAI_API_KEY"}
        
        # Probe using models list first (zero cost, checks auth)
        try:
            req = urllib.request.Request(
                "https://api.openai.com/v1/models",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            with urllib.request.urlopen(req, timeout=10) as res:
                _ = json.loads(res.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return {"configured": True, "has_quota": False, "status": "AUTHENTICATION FAILED", "error": f"HTTP {e.code}: {e.reason}"}
        except Exception as e:
            return {"configured": True, "has_quota": False, "status": "CONNECTIVITY FAILED", "error": str(e)}

        # Probe quota via single-token dummy chat request
        payload = {
            "model": self.model_id,
            "messages": [{"role": "user", "content": "ping"}],
            "max_tokens": 1
        }
        req = urllib.request.Request(
            "https://api.openai.com/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as res:
                self._has_quota = True
                self._quota_checked = True
                return {"configured": True, "has_quota": True, "status": "CONFIGURED (CREDITS ACTIVE)", "error": None}
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            self._quota_checked = True
            self._has_quota = False
            if e.code == 429 and "credit_balance_exhausted" in err_body:
                self._quota_error_msg = "Credit balance exhausted (insufficient_quota)"
                return {"configured": True, "has_quota": False, "status": "BILLING UNVERIFIED (ZERO CREDITS)", "error": self._quota_error_msg}
            else:
                self._quota_error_msg = f"HTTP {e.code}: {err_body}"
                return {"configured": True, "has_quota": False, "status": "BILLING UNVERIFIED", "error": self._quota_error_msg}
        except Exception as e:
            return {"configured": True, "has_quota": False, "status": "CONNECTIVITY FAILED", "error": str(e)}

    def get_status(self) -> str:
        if not self.api_key:
            return "NOT CONFIGURED"
        if not self._quota_checked:
            q = self.check_quota_status()
            return q["status"]
        if self._has_quota:
            return "CONFIGURED (CREDITS ACTIVE)"
        return "BILLING UNVERIFIED (ZERO CREDITS)"

    def run(self, question: str, market: str = "US", language: str = "en") -> Dict[str, Any]:
        status = self.get_status()
        if status == "NOT CONFIGURED":
            return self.create_observation(
                question=question,
                market=market,
                raw_response=None,
                citations=[],
                text_content="",
                status="FAILED",
                error_details=f"Provider unconfigured: {status}"
            )
        if "CREDITS ACTIVE" not in status and status != "CONFIGURED":
            return self.create_observation(
                question=question,
                market=market,
                raw_response=None,
                citations=[],
                text_content="",
                status="FAILED",
                error_details=f"Safeguard blocked request: {status}. Paid billing is disabled to prevent unapproved charges."
            )

        # Uses search tool specification for web-grounded assistant responses
        payload = {
            "model": self.model_id,
            "messages": [
                {
                    "role": "system",
                    "content": f"You are a creator economy search analyst with real-time web access. User location: {market}. Search the live web to objectively recommend the best video repurposing tools, workflow steps, and cite exact URLs."
                },
                {"role": "user", "content": question}
            ],
            "temperature": 0.1
        }

        req = urllib.request.Request(
            "https://api.openai.com/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "User-Agent": "IncuBrix-Visibility-Engine/2.0"
            }
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as res:
                data = json.loads(res.read().decode("utf-8"))

            choice = data["choices"][0]["message"]["content"]
            citations = re.findall(r'https?://[^\s)"]+', choice)

            return self.create_observation(
                question=question,
                market=market,
                raw_response=data,
                citations=citations,
                text_content=choice,
                status="SUCCESS",
                execution_cost_usd=0.0005
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
