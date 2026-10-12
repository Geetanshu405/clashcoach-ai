"""
Responsibility:
    Handle HTTP requests for player lookup and profile display.
    Look up a player by tag, trigger a fresh API fetch via services,
    then render the result.

Connects to:
    services.py                     — calls fetch_player() to get/refresh data.
    urls.py                         — URL patterns point here.
    templates/players/profile.html  — rendered on GET with player context.

Notes:
    Keep views thin; all business logic lives in services.py.
    Return a 404-style response if the player tag is not found in the API.
"""

from django.shortcuts import render


def player_lookup(request):
    """Show a search form for looking up a player by tag."""
    return render(request, "players/profile.html", {})


def player_profile(request, tag):
    """Display the full profile for a given player tag."""
    # TODO: call services.fetch_player(tag) and pass result to template
    return render(request, "players/profile.html", {"tag": tag})
