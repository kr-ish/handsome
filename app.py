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
    'vhsstlye': ('V H S Style', 'demiandrou'),
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
}

# TODO: dynamically load from playlist using soundcloud api
#  Can do this by using python API and pulling random tracks from playlist and then pulling track data.
#  Can do track metadata pulling in SC api in JS but might be easier to do it all in python.
# TODO: replace with namedtuple
TRAX = [
    # (
    #     "976949422",  # track id
    #     "skreetghost",  # artist
    #     "skreetghost",  # artist title
    #     "velvet-glue-rit",  # track
    #     "velvet glue (rit)",  # track title
    # ),
    # (
    #     "851298181",  # track id
    #     "archoninfinity",  # artist
    #     "A R C H O N I N F I N I T Y",  # artist title
    #     "archoninfinity-abyss",  # track
    #     "abyss",  # track title
    # ),
    # (
    #     "725843302",  # track id
    #     "duke-deuce-live",  # artist
    #     "Duke Deuce",  # artist title
    #     "crunk-aint-dead",  # track
    #     "CRUNK AIN'T DEAD",  # track title
    # ),
    (
        "1004480833",  # track id
        "osno1",  # artist
        "laura les",  # artist title
        "haunted-1",  # track
        "Haunted",  # track title
    ),
    (
        "1140757354",  # track id
        "ashnikko",  # artist
        "Ashnikko ",  # artist title
        "halloweenie-iv-innards",  # track
        "Halloweenie IV: Innards",  # track title
    ),
    (
        "21792166",  # track id
        "skrillex",  # artist
        "Skrillex ",  # artist title
        "scary-monsters-and-nice",  # track
        "SCARY MONSTERS AND NICE SPRITES",  # track title
    ),
    (
        "823111990",  # track id
        "danger-incorporated",  # artist
        "Danger Incorporated",  # artist title
        "frankenstein",  # track
        "Frankenstein",  # track title
    ),
    (
        "242616127",  # track id
        "danger-incorporated",  # artist
        "Danger Incorporated",  # artist title
        "graveyard-ft-yung-ghoul",  # track
        "Graveyard (feat. Yung Ghoul)",  # track title
    ),
    (
        "516371775",  # track id
        "yungearle",  # artist
        "¥ung 3arle ",  # artist title
        "goosebumps",  # track
        "Goosebumps (Yung Earle Remix)",  # track title
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
    video_tags = os.path.splitext(video_name)[0].split('_')
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
