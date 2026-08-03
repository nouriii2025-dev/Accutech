Place the official Accutech logo file here as:

    logo.png

The site templates already reference `core/img/logo.png` in the nav bar and
footer (see `core/templates/core/base.html`). Until this file exists, the
site automatically falls back to a text "ACCUTECH." wordmark, so nothing
breaks — but for an exact match to the original site, drop the real logo
file (ideally a transparent PNG or SVG, roughly 200x60px or similar
aspect ratio) in this folder using the exact filename above.

If you'd rather use an SVG, save it as `logo.svg` instead and update the
two `src="{% static 'core/img/logo.png' %}"` references in
`core/templates/core/base.html` to `core/img/logo.svg`.
