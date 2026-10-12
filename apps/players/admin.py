"""
Responsibility:
    Register Player and PlayerSnapshot with the Django admin site
    so they can be viewed and managed via /admin/.

Connects to:
    models.py — imports Player and PlayerSnapshot.

Notes:
    Add list_display and search_fields as the project grows.
"""

from django.contrib import admin
from .models import Player, PlayerSnapshot

admin.site.register(Player)
admin.site.register(PlayerSnapshot)
