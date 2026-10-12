# Hardcoded Clash of Clans game data keyed by Town Hall level.
# IMPORTANT: verify these values against a reliable source (e.g. the official
# CoC wiki or Fandom wiki) and record the game version they reflect.
# No imports — this file is pure data.

# Max hero levels per Town Hall level
# Format: {town_hall_level: {"Barbarian King": max, "Archer Queen": max, ...}}
HERO_MAX_LEVELS = {
    1:  {"Barbarian King": 0, "Archer Queen": 0, "Grand Warden": 0, "Royal Champion": 0},
    2:  {"Barbarian King": 0, "Archer Queen": 0, "Grand Warden": 0, "Royal Champion": 0},
    3:  {"Barbarian King": 0, "Archer Queen": 0, "Grand Warden": 0, "Royal Champion": 0},
    4:  {"Barbarian King": 0, "Archer Queen": 0, "Grand Warden": 0, "Royal Champion": 0},
    5:  {"Barbarian King": 0, "Archer Queen": 0, "Grand Warden": 0, "Royal Champion": 0},
    6:  {"Barbarian King": 0, "Archer Queen": 0, "Grand Warden": 0, "Royal Champion": 0},
    7:  {"Barbarian King": 5, "Archer Queen": 0, "Grand Warden": 0, "Royal Champion": 0},
    8:  {"Barbarian King": 10, "Archer Queen": 5, "Grand Warden": 0, "Royal Champion": 0},
    9:  {"Barbarian King": 30, "Archer Queen": 30, "Grand Warden": 0, "Royal Champion": 0},
    10: {"Barbarian King": 40, "Archer Queen": 40, "Grand Warden": 0, "Royal Champion": 0},
    11: {"Barbarian King": 50, "Archer Queen": 50, "Grand Warden": 20, "Royal Champion": 0},
    12: {"Barbarian King": 65, "Archer Queen": 65, "Grand Warden": 40, "Royal Champion": 0},
    13: {"Barbarian King": 75, "Archer Queen": 75, "Grand Warden": 50, "Royal Champion": 25},
    14: {"Barbarian King": 80, "Archer Queen": 80, "Grand Warden": 55, "Royal Champion": 30},
    15: {"Barbarian King": 90, "Archer Queen": 90, "Grand Warden": 65, "Royal Champion": 40},
    16: {"Barbarian King": 95, "Archer Queen": 95, "Grand Warden": 70, "Royal Champion": 45},
}

# Priority weights for upgrade categories (higher = more important)
# Used by analytics/services.py to rank recommendations.
PRIORITY_WEIGHTS = {
    "heroes": 10,
    "troops": 7,
    "spells": 6,
    "siege_machines": 5,
    "pets": 4,
    "defenses": 3,
    "traps": 1,
}

# TODO: add per-category max troop/spell level tables keyed by town hall level.
# See HERO_MAX_LEVELS above for the expected format.
TROOP_MAX_LEVELS: dict = {}
SPELL_MAX_LEVELS: dict = {}
