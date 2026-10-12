"""
Root URL configuration for clashcoach-ai.
Each app owns its own urls.py; routes are included here.
"""

from django.contrib import admin
from django.urls import path, include

# URL patterns — admin plus one include per app
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.dashboard.urls")),
    path("players/", include("apps.players.urls")),
    path("analytics/", include("apps.analytics.urls")),
    path("ai_coach/", include("apps.ai_coach.urls")),
]
