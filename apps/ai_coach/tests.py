"""
Responsibility:
    Tests for prompt construction, LLM response handling, and cache behaviour.
    The LLM must always be mocked — never call the real API in tests.

Connects to:
    services.py — tests generate_roast() and generate_recommendations().
    models.py   — verifies AICoachCache is created/returned correctly.

Notes:
    Key scenarios to cover:
      - Cache miss: LLM is called, result stored in AICoachCache.
      - Cache hit: LLM is NOT called, cached text returned directly.
      - Prompt content: assert that known analytics facts appear in the prompt.
      - LLM error: service raises/propagates exception cleanly.
"""

from django.test import TestCase

# TODO: implement tests
