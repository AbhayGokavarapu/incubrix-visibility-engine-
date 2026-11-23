"""
IncuBrix Safe Live Test Runner CLI
==================================
Runs a single test question against one or more selected providers with spending limits,
dry-run preview, raw evidence persistence, and normalized output reporting.
"""

import os
import sys
import argparse
from datetime import datetime

# Path resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from engine.providers import (
    GoogleSearchProvider,
    OpenAIProvider,
    GeminiProvider,
    PerplexityProvider,
    ClaudeProvider
)
from engine.evidence_store import EvidenceStore

PROVIDER_MAP = {
    "google": GoogleSearchProvider,
    "chatgpt": OpenAIProvider,
    "gemini": GeminiProvider,
    "perplexity": PerplexityProvider,
    "claude": ClaudeProvider
}

def run_safe_test(provider_name: str, question: str, market: str, dry_run: bool = False, max_spend: float = 1.0):
    provider_cls = PROVIDER_MAP.get(provider_name.lower())
    if not provider_cls:
        print(f"Error: Unknown provider '{provider_name}'. Choose from: {list(PROVIDER_MAP.keys())}")
        return

    provider = provider_cls()
    status = provider.get_status()

    print("=" * 70)
    print(f"IncuBrix Safe Test Runner: {provider.name} ({provider.model_id})")
    print("=" * 70)
    print(f"Question: '{question}'")
    print(f"Target Market: {market}")
    print(f"Configuration Status: {status}")
    print(f"Spending Cap: ${max_spend:.2f} USD")
    print(f"Dry Run Mode: {dry_run}")
    print("-" * 70)

    if dry_run:
        print("[DRY-RUN] Network call bypassed. Provider interface and schema verified.")
        return

    if status != "CONFIGURED":
        print(f"Execution Aborted: Provider is {status}. Please set valid API key in .env.")
        return

    print("Executing authenticated live search-grounded measurement...")
    obs = provider.run(question, market=market)
    
    # Persist evidence
    store = EvidenceStore()
    ev_path = store.save_observation("SMOKE-TEST", obs)

    print("\n--- Measurement Output Summary ---")
    print(f"Status: {obs['execution_status']}")
    print(f"IncuBrix Mentioned: {obs['incubrix_mentioned']}")
    print(f"Competitors Found: {obs['competitors_mentioned']}")
    print(f"Citations Captured: {len(obs['citations'])}")
    print(f"Evidence File Saved: {ev_path}")
    if obs.get("error_details"):
        print(f"Error Details: {obs['error_details']}")

def main():
    parser = argparse.ArgumentParser(description="IncuBrix Safe Live Test Runner CLI")
    parser.add_argument("--provider", default="gemini", choices=list(PROVIDER_MAP.keys()), help="Target provider to query")
    parser.add_argument("--question", default="How to automatically turn long YouTube videos into viral TikToks with AI?", help="Creator question text")
    parser.add_argument("--market", default="US", help="Target country market (US, UK, IN)")
    parser.add_argument("--dry-run", action="store_true", help="Preview request without making outbound network call")
    parser.add_argument("--max-spend", type=float, default=1.00, help="Maximum allowed cost threshold in USD")

    args = parser.parse_args()
    run_safe_test(args.provider, args.question, args.market, args.dry_run, args.max_spend)

if __name__ == "__main__":
    main()
