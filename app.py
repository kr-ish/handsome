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
        "505057155",  # track id
        "baredex-522947753",  # artist
        "baredex",  # artist title
        "as-long-as-we-got",  # track
        "as long as we got",  # track title
    ),
    (
        "859107265",  # track id
        "mehdi-dookhoo",  # artist
        "dj doog",  # artist title
        "dilemna-nelly-x-kelly-r-dj-doog-remix",  # track
        "DILEMNA NELLY x KELLY R DJ DOOG REMIX",  # track title
    ),
    (
        "1005059164",  # track id
        "lilpolotee",  # artist
        "POLO PERKS <3 <3 <3",  # artist title
        "snowpatrol-prod-goner",  # track
        "SnowPatrol Prod Goner",  # track title
    ),
    (
        "95834819",  # track id
        "daftcrew",  # artist
        "Daft Crew",  # artist title
        "modjo-lady-hear-me-tonight",  # track
        "Modjo - Lady (Hear Me Tonight)",  # track title
    ),
    (
        "1063872418",  # track id
        "ritt-momney",  # artist
        "Ritt Momney",  # artist title
        "escalator-1",  # track
        "Escalator",  # track title
    ),
    (
        "1047710704",  # track id
        "bladee1000",  # artist
        "BLADEE",  # artist title
        "i-think",  # track
        "I Think...",  # track title
    ),
    # (  # soundcloud go+ only :(
    #     "252563438",  # track id
    #     "thechemicalbrothers",  # artist
    #     "The Chemical Brothers",  # artist title
    #     "swoon-boys-noize-summer-remix",  # track
    #     "Swoon (Boys Noize Summer Remix)",  # track title
    # ),
    (
        "1141747369",  # track id
        "chvrches",  # artist
        "CHVRCHES",  # artist title
        "love-triple-j-like-a-version",  # track
        "LOVE (triple j Like A Version)",  # track title
    ),
    (
        "1071257377",  # track id
        "skrrtcord",  # artist
        "SKRRTCORD",  # artist title
        "love-feat-sphere-merchants-ko-zhone-prod-autoblush-omarevz-ko-zhone",  # track
        "LOVE (FEAT. SPHERE MERCHANTS, KØ & ZHONE) // (PROD. AUTOBLUSH, OMAREVZ, KØ & ZHONE)"  # track title
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
