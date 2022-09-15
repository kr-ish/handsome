from flask import Flask, render_template, request
import os
import glob
import random
from user_agents import parse

app = Flask(__name__)

BG_PATHS = glob.glob('./static/bg-*')
FILTERS_MAP = {
    'breakdown': ('Breakdown', 'justinwlaurent'),
    '90stethic': ('𝟡𝟘𝕤𝕥𝕖𝕥𝕙𝕚𝕔', 'demiandrou'),
    'blvckpvris': ('BLVCK PVRI$', 'demiandrou'),
    'inlightning': ('Lightning', 'instagram'),
    'chromaticpulse': ('Chromatic Pulse', 'instagram'),
    'lightning': ('lightning', 'demiandrou'),
    'vhsstyle': ('V H S Style', 'demiandrou'),
    'camcorder': ('𝕔𝕒𝕞𝕔𝕠𝕣𝕕𝕖𝕣', 'demiandrou'),
    'ledsthetic': ('𝕝𝕖𝕕𝕤𝕥𝕙𝕖𝕥𝕚𝕔', 'demiandrou'),
    'discoglam': ('𝕕𝕚𝕤𝕔𝕠 𝕘𝕝𝕒𝕞♕', 'demiandrou'),
    'cyberblue': ('cyberblue', 'demiandrou'),
    'allyouneed': ('all you need', 'justinwlaurent'),
    'mixedpersonalities': ('Mixed Personalities', 'justinwlaurent'),
    'technicolor': ('Technicolor', 'liamo.studio'),
    'flowerpower': ('Flower Power', 'chrispelk'),
    'watery': ('Watery', 'alwayscodingsomething'),
    '<3u': ('<3 U', 'justinwlaurent'),
    'wind': ('Wind', 'justinwlaurent'),
    '90slove': ('90sLove', 'liamo.studio'),
    'bathingwithshrek': ('Bathing with Shrek', 'ryleevigor'),
    'shrekislove': ('Shrek is love', 'ryleevigor'),
    'shrek&fiona': ('shrek&fiona', 'pityzza'),
    'spiral': ('SPIRAL 🌀🌀🌀', 'liamo.studio'),
    'handycamera': ('Handy Camera', 'solar.w'),
}

# TODO: dynamically load from playlist using soundcloud api
#  Can do this by using python API and pulling random tracks from playlist and then pulling track data.
#  Can do track metadata pulling in SC api in JS but might be easier to do it all in python.
# TODO: replace with namedtuple
TRAX = [
    (
        "518465847",  # track id
        "kawaiiton",  # artist
        "𝕂𝔸𝕎𝔸𝕀𝕀𝕋𝕆ℕ",  # artist title
        "anuel-x-chico-sonido-la-noche-oscura-x-christine",  # track
        "ANUEL - La noche oscura x christine",  # track title
    ),
    (
        "794804059",  # track id
        "krypt",  # artist
        "krypt",  # artist title
        "bladee-lovestory-feat-ecco2k-krypt-rmx",  # track
        "Bladee — Lovestory (krypt remix)",  # track title
    ),
    (
        "1274960959",  # track id
        "djanimebby",  # artist
        "Dj Animebby",  # artist title
        "dj-animebby-ki55-m3",  # track
        "Dj Animebby - Ki55 M3",  # track title
    ),
    (
        "1215934435",  # track id
        "lynyofficial",  # artist
        "LYNY",  # artist title
        "danny-l-harle-on-a-mountain-lyny-remix",  # track
        "Danny L Harle - On a Mountain (LYNY Remix)",  # track title
    ),
    # (
    #     "1301438497",  # track id
    #     "flume",  # artist
    #     "FLUME",  # artist title
    #     "hollow-feat-emma-louise-2",  # track
    #     "Hollow (Logic1000 Remix)",  # track title
    # ),
    (
        "1261559698",  # track id
        "flume",  # artist
        "FLUME",  # artist title
        "dhlc",  # track
        "DHLC",  # track title
    ),
]


# @app.route('/')
# def login():
#     return render_template('letmein.html')

@app.route('/')
def home():
    is_safari = False
    ua_string = request.headers.get('User-Agent')
    if 'Chrome' not in ua_string and 'Safari' in ua_string:
        is_safari = True

    user_agent = parse(ua_string)
    is_computer = user_agent.is_pc

    bg_path = random.choice(BG_PATHS)
    bg_name = os.path.basename(bg_path)
    bg_tags, bg_ext = os.path.splitext(bg_name.lstrip('bg-'))
    bg_is_video = bg_ext == '.mp4'
    bg_tags = bg_tags.split('-')
    image_credit = bg_tags[0]
    filter_keys = bg_tags[1:]
    filters = []

    # get filters used by video by parsing filter keys from video name
    for filter_key in filter_keys:
        filter = FILTERS_MAP.get(filter_key)
        if not filter:
            app.logger.warning(f'Filter key {filter_key} not found from background media path {bg_path}, skipping..')
            continue
        filters.append(filter)

    # randomly pick two unique tracks to load to deck
    trax = TRAX.copy()  # make a copy so that this is reinstantiated to the full list during debugging
    # when the app is reloaded
    track1 = trax.pop(random.randrange(len(trax)))
    track2 = trax.pop(random.randrange(len(trax)))

    # set flag to show main text
    show_text = bg_name in ['bg-kr_______________-lottafruta.jpeg', 'bg-kr_______________-leasebk.png']

    return render_template(
        'home.html',
        background=bg_name,
        bg_is_video=bg_is_video,
        image_credit=image_credit,
        filters=filters,
        show_text=show_text,
        track1=track1,
        track2=track2,
        is_safari=is_safari,
        is_computer=is_computer,
    )

@app.route('/shirt')
def shirt():
    return render_template('shirt.html')


if __name__ == '__main__':
    app.run()
