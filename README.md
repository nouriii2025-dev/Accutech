# Accutech — Website (Django + Python)

A full redesign concept for **accutech.ae**, rebuilt with a Python/Django
backend and a responsive HTML/CSS/JS frontend. The content matches the
current Accutech site (company history, full product catalog, project
verticals, brand partnerships, certifications, contact details); the visual
design is a clean, light off-white theme with navy and red accents,
dashboard/gauge-inspired detailing that ties naturally back into Accutech's
own product line (precision pressure/temperature gauges).

## Logo

The header and footer are wired to display your real logo automatically —
see `core/static/core/img/README_LOGO.txt` for the one-file drop-in step.
Until that file is added, the site gracefully falls back to a text
"ACCUTECH." wordmark so nothing looks broken in the meantime.

## Stack

- **Backend:** Python 3, Django 6, Django REST Framework (chatbot API)
- **Frontend:** HTML5, CSS3 (custom, no build step), vanilla JavaScript,
  Bootstrap 5 (grid + icons only — visuals are fully custom), Google Fonts
  (Rajdhani / Inter / JetBrains Mono)
- **Database:** SQLite by default (swap `DATABASES` in `settings.py` for
  Postgres/MySQL in production)

## Project layout

```
accutech_redesign/
├── accutech_redesign/       # project settings, root urls
├── core/                    # pages app
│   ├── content.py           # structured site copy (solutions, brands, stats)
│   ├── models.py            # ContactMessage
│   ├── forms.py             # ContactForm
│   ├── views.py / urls.py
│   ├── templates/core/      # base.html + one template per page
│   └── static/core/         # style.css, main.js
├── chatbot/                 # rule-based FAQ chatbot
│   ├── bot.py                # keyword-matching intent logic (no external API)
│   ├── models.py             # ChatLog (conversation audit trail)
│   ├── serializers.py / views.py / urls.py   # DRF endpoint: POST /api/chat/
│   └── static/chatbot/js/chatbot.js          # floating widget behaviour
├── requirements.txt
└── manage.py
```

## Pages

| Page      | URL          | Notes                                              |
|-----------|--------------|-----------------------------------------------------|
| Home      | `/`          | Hero with animated SVG accuracy gauge, solutions grid, product/project teasers, brand strip, certifications, CTA |
| About     | `/about/`    | Company history/timeline (founded 1996), mission    |
| Products  | `/products/` | Full catalog — 9 categories with subcategories, plus the full brand roster carried | 
| Solutions | `/solutions/`| All 6 measurement/calibration categories in detail  |
| Projects  | `/projects/` | MEP & District Cooling, Power/Water/Desalination, Oil & Gas |
| Brands    | `/brands/`   | ABB, WIKA, Trafag partnership detail                |
| Contact   | `/contact/`  | Django form → saved to DB, shown in Django admin     |
| Admin     | `/admin/`    | Manage contact enquiries & chat logs                 |

## Chatbot

- No external API key required — `chatbot/bot.py` is a small, deterministic
  keyword matcher covering greetings, solutions (pressure/temperature/
  force-level/flow/calibration/SF6), brand partners, certifications, company
  info, and contact details, with a friendly fallback for anything else.
- Frontend widget (bottom-right on every page) posts to `POST /api/chat/`
  with `{"message": "..."}` and renders `{"reply": "...", "quick_replies": [...]}`.
- Every exchange is logged to `ChatLog` (viewable in `/admin/`) so you can
  see what visitors are asking and extend `bot.py`'s intents over time.
- To upgrade to an AI-powered bot later, swap the body of `get_reply()` in
  `chatbot/bot.py` for a call to an LLM API — the view/serializer/frontend
  layer doesn't need to change.

## Setup

```bash
# from the accutech_redesign/ directory
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt

python3 manage.py migrate
python3 manage.py createsuperuser # optional, for /admin/

python3 manage.py runserver
```

Then open http://127.0.0.1:8000/

## Customizing content

All page copy (solutions, product categories, project verticals, brand
partners, stats, certifications, company details) lives in
`core/content.py` as plain Python dictionaries/lists — edit that one file
to update text across the whole site without touching templates.

## Production notes (not yet configured — dev server only)

- Set `DEBUG = False` and a real `SECRET_KEY` (env var) in `settings.py`
- Set `ALLOWED_HOSTS` to your real domain

  ##Access the website : https://accutech-chto.onrender.com
- Run `python3 manage.py collectstatic` and serve `staticfiles/` via
  Nginx/whitenoise
- Put SQLite behind a real database (Postgres recommended) for production traffic
- Serve via Gunicorn/uWSGI behind a reverse proxy, not `runserver`
