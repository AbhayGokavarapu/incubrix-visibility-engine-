"""
IncuBrix Base Provider Interface
=================================
Defines the common architecture and normalized observation schema for all search
and AI assistant adapters (Google Search, ChatGPT, Gemini, Perplexity, Claude).
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

class BaseProvider(ABC):
    def __init__(self, name: str, model_id: str, api_key: Optional[str] = None):
        self.name = name
        self.model_id = model_id
        self.api_key = api_key

    @abstractmethod
    def get_status(self) -> str:
        """
        Returns one of:
        CONFIGURED, NOT CONFIGURED, CONNECTIVITY FAILED, AUTHENTICATION FAILED,
        RATE LIMITED, READY, NOT TESTED
        """
        pass

    @abstractmethod
    def run(self, question: str, market: str = "US", language: str = "en") -> Dict[str, Any]:
        """
        Executes a real query against the provider and returns a normalized observation.
        """
        pass

    def create_observation(
        self,
        question: str,
        market: str,
        raw_response: Any,
        citations: List[str],
        text_content: str,
        status: str = "SUCCESS",
        error_details: Optional[str] = None,
        execution_cost_usd: float = 0.0,
        position: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Normalizes outputs across all providers into an audited uniform schema.
        """
        # Determine mention status
        text_lower = text_content.lower()
        mentioned = "incubrix" in text_lower

        # Identify competitor mentions
        known_competitors = ["Opus Clip", "Descript", "Munch", "CapCut", "Veed.io", "Submagic", "Kapwing", "Riverside", "Vidyo.ai"]
        competitors_found = [comp for comp in known_competitors if comp.lower() in text_lower]

        return {
            "provider_name": self.name,
            "model_identifier": self.model_id,
            "question": question,
            "market": market,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "raw_response": raw_response,
            "raw_text": text_content,
            "citations": citations,
            "incubrix_mentioned": mentioned,
            "competitors_mentioned": competitors_found,
            "position": position,
            "execution_status": status,
            "error_details": error_details,
            "execution_cost_usd": execution_cost_usd,
            "collection_method": "API_AUTOMATED"
        }
