"""
Responsibility:
    The ONLY module in the project that calls the LLM (NVIDIA NIM / Nemotron).
    Constructs prompts from analytics data, calls the API, caches results,
    and returns generated text.

Connects to:
    analytics/services.py — facts and stats come from here; the LLM never computes.
    models.py             — reads/writes AICoachCache to avoid redundant LLM calls.
    settings              — reads NVIDIA_API_KEY, NVIDIA_BASE_URL, LLM_MODEL.

Notes:
    The LLM must NEVER be given raw player data to analyse — always pass
    pre-computed facts from analytics/services.py.
    Use the openai client pointed at NVIDIA_BASE_URL for API calls.
    Cache generated text per player + content_type; regenerate only when stale.
"""

import os
from openai import OpenAI

# Read LLM configuration from environment
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
NVIDIA_BASE_URL = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "")


def _get_client() -> OpenAI:
    """Return a configured OpenAI client pointing at the NVIDIA NIM endpoint."""
    return OpenAI(api_key=NVIDIA_API_KEY, base_url=NVIDIA_BASE_URL)


def generate_roast(player_tag: str) -> str:
    """
    Return a humorous AI roast for the given player.
    Fetches analytics facts, builds a prompt, calls the LLM,
    caches and returns the result.
    """
    # TODO:
    # 1. Call analytics/services to get player stats
    # 2. Build prompt with stats as context
    # 3. Check AICoachCache — return cached text if fresh
    # 4. Call LLM via _get_client()
    # 5. Save to cache and return text
    raise NotImplementedError("generate_roast() is not yet implemented.")


def generate_recommendations(player_tag: str) -> str:
    """
    Return AI upgrade recommendations for the given player.
    Same flow as generate_roast() but with a different prompt and content_type.
    """
    # TODO: implement
    raise NotImplementedError("generate_recommendations() is not yet implemented.")
