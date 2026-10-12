"""
Responsibility:
    Cache model for AI-generated text (roasts, recommendations, comparisons).
    Keyed by player tag and content type, with a timestamp so stale content
    can be regenerated when player data changes.

Connects to:
    players/models.py    — links each cache entry to a Player.
    analytics/services.py — AI text is generated from analytics output;
                            the model stores the result, not the inputs.

Notes:
    content_type examples: 'roast', 'recommendations', 'comparison'.
    Check the timestamp before serving cached text; regenerate if stale.
"""

from django.db import models
from apps.players.models import Player


class AICoachCache(models.Model):
    # The player this AI text was generated for
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="ai_cache")
    # Type of content stored (e.g. 'roast', 'recommendations')
    content_type = models.CharField(max_length=50)
    # The generated text from the LLM
    generated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # One cache entry per player + content type combination
        unique_together = [("player", "content_type")]

    def __str__(self):
        return f"{self.content_type} for {self.player.tag}"
