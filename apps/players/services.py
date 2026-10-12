"""
Responsibility:
    The ONLY module in the project that calls the Clash of Clans API.
    Fetches player data by tag, caches results in the database,
    and enforces a one-hour cooldown before saving a new snapshot.

Connects to:
    models.py — reads/writes Player and PlayerSnapshot.
    settings   — reads COC_API_TOKEN for API authentication.

Notes:
    Always use this module (not raw requests) when you need player data.
    The API base URL is https://api.clashofclans.com/v1.
    Player tags must be URL-encoded (replace '#' with '%23').
    One-hour cooldown: if the most recent snapshot is less than 60 minutes
    old, return it instead of hitting the API again.
"""

import os
import requests
from datetime import timedelta
from django.utils import timezone

# Read the API token from settings/environment
COC_API_TOKEN = os.getenv("COC_API_TOKEN", "")
COC_API_BASE = "https://api.clashofclans.com/v1"
SNAPSHOT_COOLDOWN_MINUTES = 60


def fetch_player(tag: str) -> dict:
    """
    Return player data for the given tag.
    Uses a cached snapshot if one exists within the cooldown window;
    otherwise hits the CoC API and saves a new snapshot.
    """
    # TODO: implement full fetch + cache logic
    # 1. Look up Player by tag in DB
    # 2. Check latest PlayerSnapshot age against SNAPSHOT_COOLDOWN_MINUTES
    # 3. If fresh, return raw_data from snapshot
    # 4. Otherwise, call _call_coc_api(tag) and save new snapshot
    raise NotImplementedError("fetch_player() is not yet implemented.")


def _call_coc_api(tag: str) -> dict:
    """Make an authenticated GET request to the CoC API for a single player."""
    encoded_tag = tag.replace("#", "%23")
    url = f"{COC_API_BASE}/players/{encoded_tag}"
    headers = {"Authorization": f"Bearer {COC_API_TOKEN}"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()
