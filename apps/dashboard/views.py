"""
Responsibility:
    Assemble and render the main dashboard home page.
    Gathers player cards, progression stats, and AI insights from the
    three service modules and passes them to the template.

Connects to:
    apps.players.services    — fetches player data.
    apps.analytics.services  — computes progression stats for display.
    apps.ai_coach.services   — retrieves AI insights (cached or fresh).
    templates/dashboard/home.html — rendered with assembled context.
    urls.py                  — home URL points here.

Notes:
    Dashboard has no models — it only reads from other modules.
    Handle missing/new players gracefully (show empty state, not an error).
"""

from django.shortcuts import render


def home(request):
    """Render the dashboard home page with player cards and stats."""
    # TODO: fetch tracked players, get their stats and AI insights, pass to template
    context = {
        "players": [],
    }
    return render(request, "dashboard/home.html", context)
