"""
IncuBrix Provider Status & Health Check Tool
============================================
Checks API configuration, credentials, and environment status across all 5 providers.
"""

from engine.providers import (
    GoogleSearchProvider,
    OpenAIProvider,
    GeminiProvider,
    PerplexityProvider,
    ClaudeProvider
)

def check_all_providers():
    providers = [
        GoogleSearchProvider(),
        OpenAIProvider(),
        GeminiProvider(),
        PerplexityProvider(),
        ClaudeProvider()
    ]

    print(f"{'Provider':<18} | {'Model Identifier':<26} | {'Status':<16}")
    print("-" * 65)
    for p in providers:
        print(f"{p.name:<18} | {p.model_id:<26} | {p.get_status():<16}")

if __name__ == "__main__":
    check_all_providers()
