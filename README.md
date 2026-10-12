# ⚔️ ClashCoach AI

> AI-powered Clash of Clans analyst — roasts your neglected upgrades and tells you exactly what to fix.

Built with **Django** · **Clash of Clans API** · **NVIDIA NIM (Nemotron)**

---

## What it does

1. Look up any CoC player by tag
2. Analyze their upgrade progression against Town Hall benchmarks
3. Generate a personalized AI roast *and* a prioritized upgrade plan

---

## Architecture

Four apps, each with a single responsibility. No module calls above its layer.

```
┌─────────────────────────────────────┐
│             dashboard               │  ← assembly + rendering only, no models
└────────┬──────────┬─────────────────┘
         │          │          │
         ▼          ▼          ▼
    ┌─────────┐ ┌──────────┐ ┌──────────┐
    │ players │ │analytics │ │ ai_coach │
    └────┬────┘ └────┬─────┘ └────┬─────┘
         │           │             │
         │      reads snapshots    │
         │◄──────────┘             │
         │                         │
         │      analytics facts    │
         │◄────────────────────────┘
         │
    Clash of Clans API
```

| App | Talks to | Responsibility |
|---|---|---|
| `players` | CoC API | Fetch & cache player snapshots |
| `analytics` | `players` DB | Pure math — progression %, gaps, rankings |
| `ai_coach` | `analytics` + NVIDIA NIM | Prompt building, LLM calls, result caching |
| `dashboard` | All three above | Assemble data, render UI |

---

## Data Flow

### Player Lookup

```
User enters tag
      │
      ▼
players/fetch_player(tag)
      │
      ├── Snapshot < 60 min old? ──► return cached raw_data
      │
      └── Stale / missing ──► _call_coc_api(tag)
                                      │
                                      ▼
                              Save new PlayerSnapshot
                                      │
                                      ▼
                              return raw_data
```

### Roast / Recommendations Generation

```
User requests roast for tag
      │
      ▼
ai_coach/generate_roast(tag)
      │
      ├── AICoachCache hit? ──► return cached text
      │
      └── Cache miss
              │
              ▼
      analytics.max_level_percentages(snapshot)
      analytics.upgrade_gaps(snapshot)
      analytics.priority_ranking(snapshot)
              │
              ▼
      Build prompt with facts
              │
              ▼
      NVIDIA NIM (Nemotron)
              │
              ▼
      Save to AICoachCache
              │
              ▼
      Return generated text
```

### Player Comparison

```
User submits two tags (tag_a, tag_b)
      │
      ▼
analytics/compare_players(tag_a, tag_b)
      │
      ├── fetch_player(tag_a) ──► snapshot_a
      ├── fetch_player(tag_b) ──► snapshot_b
      │
      ▼
Side-by-side stat diff
      │
      ▼
Render analytics/compare.html
```

---

## Project Structure

```
clashcoach-ai/
├── apps/
│   ├── players/          # CoC API gateway
│   │   ├── models.py     # Player, PlayerSnapshot
│   │   └── services.py   # fetch_player, _call_coc_api
│   ├── analytics/        # Pure-Python math layer
│   │   ├── game_data.py  # Hero max levels, priority weights
│   │   └── services.py   # max_level_percentages, upgrade_gaps, …
│   ├── ai_coach/         # LLM gateway
│   │   ├── models.py     # AICoachCache
│   │   └── services.py   # generate_roast, generate_recommendations
│   └── dashboard/        # Assembly + rendering
│       └── views.py      # home view
├── config/               # Django settings, URLs, WSGI/ASGI
├── templates/            # HTML templates (extend base.html)
├── static/               # CSS, JS, images
├── docs/                 # Architecture docs
├── .env.example
├── requirements.txt
└── manage.py
```

---

## Models

```
Player
  ├── tag            CharField  (unique, e.g. #ABC123)
  ├── name           CharField
  ├── town_hall_level PositiveSmallIntegerField
  └── last_updated   DateTimeField (auto)

PlayerSnapshot
  ├── player         FK → Player
  ├── raw_data       JSONField  (full CoC API response)
  └── captured_at    DateTimeField (auto)

AICoachCache
  ├── player         FK → Player
  ├── content_type   CharField  ('roast' | 'recommendations')
  ├── generated_text TextField
  └── created_at     DateTimeField (auto)
               unique_together: (player, content_type)
```

---

## Setup

```bash
# 1. Clone & create virtual env
git clone <repo-url> && cd clashcoach-ai
python -m venv .venv && source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Fill in COC_API_TOKEN, NVIDIA_API_KEY, LLM_MODEL, DJANGO_SECRET_KEY

# 4. Apply migrations
python manage.py migrate

# 5. Run the dev server
python manage.py runserver
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `COC_API_TOKEN` | Bearer token from [developer.clashofclans.com](https://developer.clashofclans.com) |
| `NVIDIA_API_KEY` | API key from [build.nvidia.com](https://build.nvidia.com) |
| `NVIDIA_BASE_URL` | NIM endpoint — default `https://integrate.api.nvidia.com/v1` |
| `LLM_MODEL` | Nemotron model identifier string |
| `DJANGO_SECRET_KEY` | Django secret key (generate a strong random string) |
| `DJANGO_DEBUG` | `True` for development, `False` for production |

---

## Tech Stack

| Layer | Tech |
|---|---|
| Web framework | Django |
| Database | SQLite (dev) |
| CoC data | [Clash of Clans API](https://developer.clashofclans.com) |
| LLM | NVIDIA NIM — Nemotron via OpenAI-compatible client |
| HTTP client | `requests` |
| Env management | `python-dotenv` |

---

## Upgrade Priority Weights

Analytics ranks upgrade recommendations using these weights:

| Category | Weight |
|---|---|
| Heroes | 10 |
| Troops | 7 |
| Spells | 6 |
| Siege Machines | 5 |
| Pets | 4 |
| Defenses | 3 |
| Traps | 1 |

---

## Roadmap

- [ ] Implement `fetch_player()` snapshot cooldown + caching
- [ ] Implement all analytics service functions
- [ ] Fill in `TROOP_MAX_LEVELS` and `SPELL_MAX_LEVELS` in `game_data.py`
- [ ] Implement `generate_roast()` and `generate_recommendations()`
- [ ] Wire up URL routes in all four apps
- [ ] Build out all templates
- [ ] Add CSS / JS
- [ ] Pin dependency versions in `requirements.txt`
- [ ] Add sequence diagrams for fetch and roast generation flows
