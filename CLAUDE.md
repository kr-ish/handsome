# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

[handsomekrish.live](https://www.handsomekrish.live) — a personal DJ/music site built with Flask. Each route is a standalone "page" for a specific event or vibe (DJ sets, themed pages, gifts for specific people, etc.).

## Running the app

```bash
pip install -r requirements.txt
flask run
# or
python app.py
```

## Architecture

**`app.py`** is the entire backend — one file, no blueprints. Each route corresponds to a template of the same name (e.g., `/elsewhere` → `templates/elsewhere.html`).

**Templates** extend `templates/base.html`, which provides the navbar, favicon links, and global CSS/JS. Each page has its own `{% block head %}` and `{% block body %}`.

**`static/<page>/`** directories hold per-page assets. Pages with dynamic backgrounds follow a naming convention for their media files:

```
bg-<photographer>-<filter1>-<filter2>-....mp4  (or .jpeg/.png)
```

The `load_background_and_filters()` function parses this filename to extract the image credit and filter keys, then looks up human-readable names and credits from `FILTERS_MAP` in `app.py`.

**`static/<page>/trax.csv`** powers the dual-deck SoundCloud player on DJ set pages. Columns: `track_id, artist, artist_title, track, track_title`. Two random tracks are loaded per page visit. The SoundCloud embed uses the `track_id` and the crossfader JS controls volume between the two iframes via `SC.Widget`.

**Safari/device detection** (`parse_device_info`) is used on some pages to conditionally show warnings or adjust layout — Safari has historically had autoplay/video issues.

The "false login" pattern (a button that reveals hidden content) is used to work around browser autoplay restrictions on pages with audio.

## Adding a new page

1. Add a route in `app.py` that calls `render_template('<page>.html', ...)`
2. Create `templates/<page>.html` extending `base.html`
3. If it needs dynamic backgrounds: create `static/<page>/` with `bg-<credit>-<filters>.mp4` files and register any new filter keys in `FILTERS_MAP`
4. If it needs a deck: add `static/<page>/trax.csv` with the header row `track_id,artist,artist_title,track,track_title`
