"""
Responsibility:
    Handle HTTP requests for AI-generated roasts and recommendations.
    Retrieve (or generate) AI text via services and render it.

Connects to:
    services.py                              — calls generate_roast() / generate_recommendations().
    urls.py                                  — URL patterns point here.
    templates/ai_coach/roast.html            — rendered for roast view.
    templates/ai_coach/recommendations.html  — rendered for recommendations view.

Notes:
    Views must never call the LLM directly — always go through services.py.
    Pass the player tag from the URL, not from a form, to keep URLs bookmarkable.
"""

from django.shortcuts import render


def roast_view(request, tag):
    """Generate (or serve cached) an AI roast for the given player tag."""
    # TODO: call services.generate_roast(tag) and render
    return render(request, "ai_coach/roast.html", {"tag": tag})


def recommendations_view(request, tag):
    """Generate (or serve cached) AI upgrade recommendations for the given tag."""
    # TODO: call services.generate_recommendations(tag) and render
    return render(request, "ai_coach/recommendations.html", {"tag": tag})
