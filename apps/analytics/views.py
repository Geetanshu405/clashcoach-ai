"""
Responsibility:
    Handle HTTP requests for player comparison analytics.
    Accept two player tags, compute stats via services, and render results.

Connects to:
    services.py                       — calls comparison and progression functions.
    urls.py                           — URL patterns point here.
    templates/analytics/compare.html  — rendered with comparison context.

Notes:
    Keep views thin; all calculation logic lives in services.py.
"""

from django.shortcuts import render


def compare_players(request):
    """Compare two players' progression stats side by side."""
    # TODO: read tags from query params, call services.compare(), render
    return render(request, "analytics/compare.html", {})
