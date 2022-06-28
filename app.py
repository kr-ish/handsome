from flask import Flask, render_template, request
import os
import glob
import random

app = Flask(__name__)

VIDEO_PATHS = glob.glob('./static/*.mp4')
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
}

# TODO: dynamically load from playlist using soundcloud api
#  Can do this by using python API and pulling random tracks from playlist and then pulling track data.
#  Can do track metadata pulling in SC api in JS but might be easier to do it all in python.
# TODO: replace with namedtuple
TRAX = [
    (
        "294929726",  # track id
        "graphicmuzik",  # artist
        "GraphicMuzik",  # artist title
        "shrek-remix",  # track
        "Shrek Remix",  # track title
    ),
    (
        "504013449",  # track id
        "theguy-v3-because-why",  # artist
        "TheGuy V.3 (OLD)",  # artist title
        "shrek-rave-anthem",  # track
        "Shrek Rave Anthem",  # track title
    ),
    (
        "810120781",  # track id
        "countbaldor",  # artist
        "count baldor",  # artist title
        "this-is-one-dj-you-dont-want-to-fuck-with",  # track
        "This Is One DJ You Don't Want To Fuck With",  # track title
    ),
    (
        "701179420",  # track id
        "saucysantana",  # artist
        "SAUCY SANTANA",  # artist title
        "material-girl",  # track
        "Material Girl",  # track title
    ),
    (
        "1282822552",  # track id
        "callumlunneycurry",  # artist
        "Callum Lunney-Curry",  # artist title
        "livin-la-vida-loca-hardstyle",  # track
        "Livin La Vida Loca HBZ (Hardstyle Remix)",  # track title
    ),
    (
        "1202860279",  # track id
        "hikeii",  # artist
        "@hikeii",  # artist title
        "amygdala",  # track
        "ecco2k & bladee - amygdala (@hikeii flip)",  # track title
    ),
    (
        "1198775374",  # track id
        "djtravella",  # artist
        "DJ Travella",  # artist title
        "london-uwoteee",  # track
        "London Uwoteee",  # track title
    ),
]


# @app.route('/')
# def login():
#     return render_template('letmein.html')

@app.route('/')
def home():
    safari = False
    user_agent = request.headers.get('User-Agent')
    if 'Chrome' not in user_agent and 'Safari' in user_agent:
        safari = True

    video_path = random.choice(VIDEO_PATHS)
    video_name = os.path.basename(video_path)
    video_tags = os.path.splitext(video_name)[0].split('-')
    image_credit = video_tags[0]
    filter_keys = video_tags[1:]
    filters = []

    # get filters used by video by parsing filter keys from video name
    for filter_key in filter_keys:
        filter = FILTERS_MAP.get(filter_key)
        if not filter:
            app.logger.warning(f'Filter key {filter_key} not found from video path {video_path}, skipping..')
            continue
        filters.append(filter)

    # randomly pick two unique tracks to load to deck
    trax = TRAX.copy()  # make a copy so that this is reinstantiated to the full list during debugging
    # when the app is reloaded
    track1 = trax.pop(random.randrange(len(trax)))
    track2 = trax.pop(random.randrange(len(trax)))

    return render_template(
        'home.html',
        video=video_name,
        image_credit=image_credit,
        filters=filters,
        track1=track1,
        track2=track2,
        safari=safari
    )


if __name__ == '__main__':
    app.run()
