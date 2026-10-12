"""
Responsibility:
    Tests for progression math and player ranking using fixed, known inputs.
    All tests run without database or API access.

Connects to:
    services.py  — tests max_level_percentages, upgrade_gaps, priority_ranking,
                   progress_rate, compare_players.
    game_data.py — uses hardcoded data as the expected reference.

Notes:
    Use fixed snapshot dicts as inputs (not DB objects) wherever possible.
    Tests must be deterministic and fast.
"""

from django.test import TestCase

# TODO: implement tests
