"""
Responsibility:
    Optional cache models for storing pre-computed analytics results.
    Avoids recalculating expensive stats on every request.
    May stay empty until caching is needed.

Connects to:
    players/models.py — analytics are always tied to a specific Player.

Notes:
    If you add models here, link them to Player via a ForeignKey.
    Computed fields should always be re-derivable from PlayerSnapshot data.
"""

from django.db import models

# No models defined yet — add cache models here when needed.
