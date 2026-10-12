"""
Responsibility:
    Tests for the Clash of Clans API service layer and the snapshot
    cooldown rule.

Connects to:
    services.py — tests fetch_player() and _call_coc_api().
    models.py   — creates Player and PlayerSnapshot fixtures.

Notes:
    All HTTP calls to the CoC API must be mocked (use unittest.mock.patch).
    Never hit the real API in tests.
    Key scenarios to cover:
      - Fresh fetch: no existing snapshot → API is called, snapshot saved.
      - Cooldown: snapshot < 60 min old → API is NOT called, cached data returned.
      - Stale: snapshot >= 60 min old → API is called, new snapshot saved.
      - API error: requests raises an exception → service propagates it.
"""

from django.test import TestCase

# TODO: implement tests
