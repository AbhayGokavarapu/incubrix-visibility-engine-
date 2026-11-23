"""
IncuBrix Google Gemini Provider Adapter (v2.1)
==============================================
Integrates with the Google Gemini API (gemini-2.0-flash / gemini-1.5-pro / gemini-1.5-flash)
with official Google Search grounding and metadata chunk extraction.
Automatically loads .env configuration.
"""

import os
import json
import urllib.request
from typing import Dict, Any, List
from engine.providers.base_provider import BaseProvider
import engine.env_loader  # Ensures .env is loaded if present

class GeminiProvider(BaseProvider):
    def __init__(self, api_key: str = None, model: str = None):
        engine.env_loader.load_dotenv()
        key = api_key if api_key is not None else os.environ.get("GEMINI_API_KEY")
        # Default to gemini-2.5-flash (fast, search-grounded) with fallback to gemini-1.5-flash
        model_id = model or os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
        super().__init__(name="Google Gemini", model_id=model_id, api_key=key)

    def get_status(self) -> str:
        if not self.api_key:
            return "NOT CONFIGURED"
        return "CONFIGURED"

    def verify_models_available(self) -> Dict[str, Any]:
        """
        Queries the Gemini API models.list endpoint to verify authentication and model availability.
        """
        if not self.api_key:
            return {"authenticated": False, "models": [], "error": "Missing GEMINI_API_KEY"}

        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={self.api_key}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "IncuBrix-Visibility-Engine/2.1"})
            with urllib.request.urlopen(req, timeout=10) as res:
                data = json.loads(res.read().decode("utf-8"))
            models = [m.get("name", "").replace("models/", "") for m in data.get("models", [])]
            return {"authenticated": True, "models": models, "error": None}
        except Exception as e:
            return {"authenticated": False, "models": [], "error": str(e)}

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

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_id}:generateContent?key={self.api_key}"
        
        # Grounding tool specification per Google Gemini documentation
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"User location: {market}. Search the web and answer the following creator workflow question objectively, citing the leading tools and verified URLs: {question}"
                }]
            }],
            "tools": [{"googleSearch": {}}],  # Official Google Search Grounding tool
            "generationConfig": {
                "temperature": 0.1,
                "maxOutputTokens": 1024
            }
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "IncuBrix-Visibility-Engine/2.1"}
        )

        try:
            with urllib.request.urlopen(req, timeout=20) as res:
                data = json.loads(res.read().decode("utf-8"))

            candidates = data.get("candidates", [])
            text_content = ""
            citations = []
            grounding_executed = False
            
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                text_content = " ".join([p.get("text", "") for p in parts])
                
                # Extract Google Search Grounding metadata and cited web URIs
                grounding = candidates[0].get("groundingMetadata", {})
                if grounding:
                    grounding_executed = bool(grounding.get("webSearchQueries")) or bool(grounding.get("groundingChunks")) or bool(grounding.get("searchEntryPoint"))
                    for chunk in grounding.get("groundingChunks", []):
                        web = chunk.get("web", {})
                        if web.get("uri"):
                            citations.append(web["uri"])
                    
                    # Also extract direct redirect URIs from searchEntryPoint HTML chips if present
                    entry_point = grounding.get("searchEntryPoint", {}).get("renderedContent", "")
                    if "href=\"" in entry_point:
                        import re
                        urls = re.findall(r'href="([^"]+)"', entry_point)
                        for u in urls:
                            if u not in citations:
                                citations.append(u)

            obs = self.create_observation(
                question=question,
                market=market,
                raw_response=data,
                citations=citations,
                text_content=text_content,
                status="SUCCESS",
                execution_cost_usd=0.0003
            )
            obs["search_grounding_executed"] = grounding_executed
            return obs
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
