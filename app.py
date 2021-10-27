from flask import Flask, render_template, request
import os
import glob
import random

app = Flask(__name__)

VIDEO_PATHS = glob.glob('./static/*.mp4')
FILTERS_MAP = {
    'breakdown': ('Breakdown', 'justinwlaurent'),
    'chromaticvortex': ('Chromatic Vortex', 'sergiooturano'),
    'radialblur': ('Radial Blur', 'iamcraiglewis2'),
    'takeaway': ('TAKEAWAY', 'liamo.studio'),
    '90stethic': ('𝟡𝟘𝕤𝕥𝕖𝕥𝕙𝕚𝕔', 'demiandrou'),
    'colorfilm': ('カラーフィルム - Color Film', 'bma_japan'),
    'muybridge': ('Muybridge', 'argitendo'),
}

# TODO: dynamically load from playlist using soundcloud api
#  Can do this by using python API and pulling random tracks from playlist and then pulling track data.
#  Can do track metadata pulling in SC api in JS but might be easier to do it all in python.
# TODO: replace with namedtuple
TRAX = [
    (
        "1071257377",  # track id
        "skrrtcord",  # artist
        "SKRRTCORD",  # artist title
        "love-feat-sphere-merchants-ko-zhone-prod-autoblush-omarevz-ko-zhone",  # track
        "LOVE (FEAT. SPHERE MERCHANTS, KØ & ZHONE) // (PROD. AUTOBLUSH, OMAREVZ, KØ & ZHONE)"  # track title
    ),
    (
        "915067819",  # track id
        "sglily",  # artist
        "@sglilyy",  # artist title
        "let-me-go",  # track
        "Let Me Go (+ Kidtrash)",  # track title
    ),
    (
        "1028860690",  # track id
        "brianx-018",  # artist
        "BrianX",  # artist title
        "brianx-018/pissy-pamper",  # track
        "Pissy pamper",  # track title
    ),
    # (  # track was deleted
    #     "1046985679",  # track id
    #     "bigboihefner",  # artist
    #     "Bigboi Hefner",  # artist title
    #     "playboi-carti-rip-mike-dean-intro-prod-bigboi-hefner-ig-bigboi_hefner",  # track
    #     "playboi carti - rip + mike dean intro prod. bigboi hefner",  # track title
    # ),
    (
        "1122427504",  # track id
        "shigecki",  # artist
        "shigecki",  # artist title
        "stars-r-blind-wet-dream-remix",  # track
        "staRs r bLind (wet dream remix)",  # track title
    ),
    (
        "264537168",  # track id
        "magsbeats",  # artist
        "MAGS",  # artist title
        "mybooedit",  # track
        "my b00 (mag$ body roll edit)",  # track title
    ),
    (
        "1086800347",  # track id
        "emma_etc",  # artist
        "emma etc",  # artist title
        "security07112021-42-127x",  # track
        "security07112021-4.2-1.27x",  # track title
    ),
    (
        "942426532",  # track id
        "elf_z",  # artist
        "｡*.☆ELFZ☆.*｡",  # artist title
        "e-v-r-y-t-h-i-n-g-i-w-n-t-e-d",  # track
        ".・゜2 anyone who might care゜・．",  # track title
    ),
    (
        "985408600",  # track id
        "plnt99",  # artist
        "Planet 1999",  # artist title
        "touch-my-body-silence-debut-fin-live-at-pop-carol",  # track
        "Touch My Body (Live at Pop Carol)",  # track title
    ),
    (
        "976949422",  # track id
        "skreetghost",  # artist
        "skreetghost",  # artist title
        "velvet-glue-rit",  # track
        "velvet glue (rit)",  # track title
    ),
    (
        "823125895",  # track id
        "i9u",  # artist
        "<<##33",  # artist title
        "monkee",  # track
        "i9bonsai - funee monkee gif [reup]",  # track title
    ),
    (
        "851298181",  # track id
        "archoninfinity",  # artist
        "A R C H O N I N F I N I T Y",  # artist title
        "archoninfinity-abyss",  # track
        "abyss",  # track title
    ),
    (
        "725843302",  # track id
        "duke-deuce-live",  # artist
        "Duke Deuce",  # artist title
        "crunk-aint-dead",  # track
        "CRUNK AIN'T DEAD",  # track title
    ),
    (
        "857089711",  # track id
        "kiddiegoggles",  # artist
        "Kiddiegoggles",  # artist title
        "party4u-kiddiegoggles-remix",  # track
        "party4u[kiddiegoggles.remix].wav",  # track title
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
    filters = []

    # get filters used by video by parsing filter keys from video name
    for filter_key in os.path.splitext(video_name)[0].split('_'):
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
        filters=filters,
        track1=track1,
        track2=track2,
        safari=safari
    )


if __name__ == '__main__':
    app.run()
