"""
IncuBrix Multi-Market Batch Collection Planner (Phase 3)
========================================================
Calculates exact request matrices and cost models for:
- 100 questions across 3 markets (US, UK, IN)
- 5 providers (Google Search, ChatGPT, Gemini, Perplexity, Claude)
- 2 measurement days
- Explicit retry buffer (10% contingency)
- Per-market question allocations
"""

from typing import Dict, Any, List

def calculate_detailed_batch_plan(
    num_questions: int = 100,
    market_distribution: Dict[str, int] = None,
    providers: List[str] = None,
    measurement_days: int = 2,
    retry_contingency_percent: float = 10.0,
    days: int = None
) -> Dict[str, Any]:
    
    if days is not None:
        measurement_days = days

    if market_distribution is None:
        market_distribution = {"US": 50, "UK": 25, "IN": 25}

    if providers is None:
        providers = ["google", "chatgpt", "gemini", "perplexity", "claude"]
    
    # Modern API rates per request (in USD)
    PROVIDER_RATES = {
        "google": 0.005,      # Google Custom Search API / SerpAPI
        "chatgpt": 0.0006,    # gpt-4o-mini with search grounding
        "gemini": 0.0003,     # gemini-2.0-flash with googleSearch tool
        "perplexity": 0.0012, # sonar online search
        "claude": 0.0008      # claude-3-5-haiku with search
    }

    # Base requests per day = num_questions * len(providers)
    requests_per_day = num_questions * len(providers)
    
    # Total for measurement_days across all markets
    base_requests_total = requests_per_day * measurement_days
    contingency_requests = int(base_requests_total * (retry_contingency_percent / 100.0))
    total_projected_requests = base_requests_total + contingency_requests

    # Calculate exact per-provider costs
    cost_breakdown = {}
    total_cost_usd = 0.0

    for p in providers:
        rate = PROVIDER_RATES.get(p.lower(), 0.001)
        p_base = num_questions * measurement_days
        p_with_retry = int(p_base * (1.0 + retry_contingency_percent / 100.0))
        p_cost = p_with_retry * rate
        cost_breakdown[p] = {
            "requests": p_with_retry,
            "rate_usd": rate,
            "subtotal_usd": round(p_cost, 4)
        }
        total_cost_usd += p_cost

    runtime_seconds = total_projected_requests * 1.5
    runtime_minutes = round(runtime_seconds / 60.0, 1)

    return {
        "num_questions": num_questions,
        "market_distribution": market_distribution,
        "providers_count": len(providers),
        "measurement_days": measurement_days,
        "base_requests_total": base_requests_total,
        "retry_contingency_requests": contingency_requests,
        "total_requests_all_days": base_requests_total, # For backwards compatibility
        "total_projected_requests": total_projected_requests,
        "cost_breakdown_by_provider": cost_breakdown,
        "total_estimated_cost_usd": round(total_cost_usd, 2),
        "estimated_total_cost_usd": round(total_cost_usd, 2), # For backwards compatibility
        "estimated_runtime_minutes": runtime_minutes,
        "safe_batch_size": 25,
        "recommended_spend_cap_usd": round(total_cost_usd * 1.25, 2)
    }

# Backwards compatibility alias
calculate_batch_plan = calculate_detailed_batch_plan

def print_detailed_plan():
    plan = calculate_detailed_batch_plan()
    print("=" * 70)
    print("IncuBrix Phase 3 Comprehensive Batch Collection Plan")
    print("=" * 70)
    print(f"Monitored Questions: {plan['num_questions']}")
    print(f"Providers: {plan['providers_count']} search & AI engines")
    print(f"Measurement Days: {plan['measurement_days']} distinct calendar dates")
    print(f"Total Projected Requests: {plan['total_projected_requests']}")
    print(f"Estimated Sequential Runtime: {plan['estimated_runtime_minutes']} minutes")
    print(f"Total Estimated API Cost: ${plan['total_estimated_cost_usd']:.2f} USD")
    print(f"Recommended Safety Spend Cap: ${plan['recommended_spend_cap_usd']:.2f} USD")
    print("=" * 70)

if __name__ == "__main__":
    print_detailed_plan()
