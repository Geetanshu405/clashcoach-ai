"""
Responsibility:
    Define the Player and PlayerSnapshot database models.
    Player stores core identity (tag, name, town hall level).
    PlayerSnapshot stores a point-in-time copy of stats fetched from the API.

Connects to:
    analytics/services.py  — reads snapshots to compute progression.
    admin.py               — registers these models for the Django admin.

Notes:
    A new snapshot should only be saved if one doesn't already exist
    within the last hour (cooldown enforced in services.py).
    Use 'tag' as the unique identifier for a player (e.g. '#ABC123').
"""

from django.db import models


class Player(models.Model):
    # Unique Clash of Clans player tag, e.g. '#ABC123'
    tag = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    town_hall_level = models.PositiveSmallIntegerField(default=1)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.tag})"


class PlayerSnapshot(models.Model):
    # Links back to the Player this snapshot belongs to
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="snapshots")
    # Raw JSON data returned by the Clash of Clans API
    raw_data = models.JSONField()
    captured_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-captured_at"]

    def __str__(self):
        return f"Snapshot of {self.player.tag} at {self.captured_at}"
