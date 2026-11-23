import os
import sys
import json
import urllib.request
import urllib.parse
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from engine.providers.base_provider import BaseProvider
import engine.env_loader

class SerpApiProvider(BaseProvider):
    def __init__(self, api_key: str = None):
        engine.env_loader.load_dotenv()
        key = api_key if api_key is not None else os.environ.get("SERPAPI_API_KEY")
        super().__init__(name="Google Search", model_id="serpapi-google-engine", api_key=key)

    def get_status(self) -> str:
        if not self.api_key:
            return "NOT CONFIGURED"
        return "CONFIGURED"

    def run(self, question: str, market: str = "US", language: str = "en") -> dict:
        if not self.api_key:
            return self.create_observation(
                question=question,
                market=market,
                raw_response=None,
                citations=[],
                text_content="",
                status="FAILED",
                error_details="SerpAPI key not configured"
            )

        gl_map = {"US": "us", "UK": "uk", "IN": "in"}
        gl = gl_map.get(market.upper(), "us")

        params = {
            "api_key": self.api_key,
            "engine": "google",
            "q": question,
            "gl": gl,
            "hl": language,
            "num": 10
        }
        url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "IncuBrix-Visibility-Engine/2.1"})
            with urllib.request.urlopen(req, timeout=15) as res:
                data = json.loads(res.read().decode("utf-8"))

            organic = data.get("organic_results", [])
            citations = [item.get("link") for item in organic if item.get("link")]
            all_text = " ".join([f"{item.get('title', '')} {item.get('snippet', '')}" for item in organic])

            position = None
            for idx, item in enumerate(organic, start=1):
                if "incubrix.com" in item.get("link", "").lower():
                    position = idx
                    break

            # Answer box or AI overview detection
            has_answer_box = bool(data.get("answer_box")) or bool(data.get("ai_overview")) or bool(data.get("knowledge_graph"))

            obs = self.create_observation(
                question=question,
                market=market,
                raw_response=data,
                citations=citations,
                text_content=all_text,
                status="SUCCESS",
                position=position
            )
            obs["has_serp_answer_box"] = has_answer_box
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

if __name__ == "__main__":
    p = SerpApiProvider()
    print("SerpAPI Provider Status:", p.get_status())
    res = p.run("How to automatically turn long YouTube videos into viral TikToks with AI?", market="US")
    print("Execution:", res["execution_status"])
    print("Organic results:", len(res["citations"]))
    print("Answer Box:", res.get("has_serp_answer_box"))
    print("Top citation:", res["citations"][0] if res["citations"] else "None")
