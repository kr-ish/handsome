import csv
from flask import Flask, render_template, request
import os
import glob
import random
from user_agents import parse

app = Flask(__name__)

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


def parse_device_info(request):
    """
    Parses and returns info on the device sending the request.
    """
    is_safari = False
    ua_string = request.headers.get('User-Agent')
    if 'Chrome' not in ua_string and 'Safari' in ua_string:
        is_safari = True

    user_agent = parse(ua_string)
    is_computer = user_agent.is_pc

    return is_safari, is_computer


def load_background_and_filters(page):
    """
    Returns page background images/videos and associated filter and credit info.
    """
    bg_paths = glob.glob(f'./static/{page}/bg-*')
    bg_path = random.choice(bg_paths)
    bg_path_in_static = bg_path.split('static/')[1]
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

    return bg_path_in_static, bg_name, bg_is_video, image_credit, filters


def load_trax(page):
    """
    Loads trax onto the deck 🎚️
    """
    # TODO: write script to auto populate trax csvs using SC api
    #       + ad hoc- doesn't need to be hit all the time, can be run whenever playlist is updated
    #       + get track metadata SC api in JS but might be easier to do it all in python but would
    #         rather populate all at once.
    trax_path = f'./static/{page}/trax.csv'
    trax = []
    with open(trax_path, newline='') as f:
        # TODO: would be more readble in the html if DictReader is used here to parse header
        csvreader = csv.reader(f, delimiter=',')
        next(csvreader)  # skip hesder
        for row in csvreader:
            # print(row)  # debug
            trax.append(row)

    # randomly pick two unique tracks to load to deck
    track1 = trax.pop(random.randrange(len(trax)))
    track2 = trax.pop(random.randrange(len(trax)))

    return track1, track2


@app.route('/elsewhere')
def elsewhere():
    page = 'elsewhere'
    is_safari, is_computer = parse_device_info(request)
    bg_path_in_static, bg_name, bg_is_video, image_credit, filters = load_background_and_filters(page)
    track1, track2 = load_trax(page)

    return render_template(
        f'{page}.html',
        video=bg_path_in_static,
        image_credit=image_credit,
        filters=filters,
        track1=track1,
        track2=track2,
        safari=is_safari
    )


@app.route('/spook')
def spook():
    page = 'spook'
    is_safari, is_computer = parse_device_info(request)
    bg_path_in_static, bg_name, bg_is_video, image_credit, filters = load_background_and_filters(page)
    track1, track2 = load_trax(page)

    return render_template(
        f'{page}.html',
        video=bg_path_in_static,
        image_credit=image_credit,
        filters=filters,
        track1=track1,
        track2=track2,
        safari=is_safari
    )


@app.route('/peaceandlove')
def peaceandlove():
    page = 'peaceandlove'
    is_safari, is_computer = parse_device_info(request)
    bg_path_in_static, bg_name, bg_is_video, image_credit, filters = load_background_and_filters(page)
    track1, track2 = load_trax(page)

    return render_template(
        f'{page}.html',
        video=bg_path_in_static,
        image_credit=image_credit,
        filters=filters,
        track1=track1,
        track2=track2,
        safari=is_safari
    )


@app.route('/shrek')
def shrek():
    page = 'shrek'
    is_safari, is_computer = parse_device_info(request)
    bg_path_in_static, bg_name, bg_is_video, image_credit, filters = load_background_and_filters(page)
    track1, track2 = load_trax(page)

    return render_template(
        f'{page}.html',
        video=bg_path_in_static,
        image_credit=image_credit,
        filters=filters,
        track1=track1,
        track2=track2,
        safari=is_safari
    )


@app.route('/atl')
def atl():
    page = 'atl'
    is_safari, is_computer = parse_device_info(request)
    bg_path_in_static, bg_name, bg_is_video, image_credit, filters = load_background_and_filters(page)
    track1, track2 = load_trax(page)
    # set flag to show main text
    show_text = bg_name in ['bg-kr_______________-lottafruta.jpeg', 'bg-kr_______________-leasebk.png']

    return render_template(
        f'{page}.html',
        background=bg_path_in_static,
        bg_is_video=bg_is_video,
        image_credit=image_credit,
        filters=filters,
        show_text=show_text,
        track1=track1,
        track2=track2,
        is_safari=is_safari,
        is_computer=is_computer,
    )


@app.route('/thankgod')
def thankgod():
    page = 'thankgod'
    # is_safari, is_computer = parse_device_info(request)
    bg_path_in_static, bg_name, bg_is_video, image_credit, filters = load_background_and_filters(page)
    # track1, track2 = load_trax(page)

    return render_template(
        f'{page}.html',
        background=bg_path_in_static,
        # bg_is_video=bg_is_video,
        # image_credit=image_credit,
        # filters=filters,
        # track1=track1,
        # track2=track2,
        # is_safari=is_safari,
        # is_computer=is_computer,
    )


@app.route('/hamster')
@app.route('/hampster')
def hampster():
    page = 'hampster'
    return render_template(
        f'{page}.html',
    )


@app.route('/prom')
@app.route('/homecoming')
def promposal():
    page = 'promposal'
    return render_template(f'{page}.html',)


@app.route('/please')
def please():
    page = 'please'
    return render_template(f'{page}.html',)


@app.route('/shrek2')
def shrek2():
    page = 'shrek2'
    # is_safari, is_computer = parse_device_info(request)
    # bg_path_in_static, bg_name, bg_is_video, image_credit, filters = load_background_and_filters(page)
    # track1, track2 = load_trax(page)

    return render_template(
        f'{page}.html',
        # background=bg_path_in_static,
        # bg_is_video=bg_is_video,
        # image_credit=image_credit,
        # filters=filters,
        # track1=track1,
        # track2=track2,
        # is_safari=is_safari,
        # is_computer=is_computer,
    )


@app.route('/shirt')
def shirt():
    _, is_computer = parse_device_info(request)
    return render_template(
        'shirt.html',
        is_computer=is_computer,
    )

@app.route('/home')
def home():
    page = 'home'
    return render_template(
        f'{page}.html',
    )

@app.route('/join')
def join():
    page = 'join'
    return render_template(
        f'{page}.html',
    )

@app.route('/harmony')
def harmony():
    page = 'harmony'
    return render_template(
        f'{page}.html',
    )

@app.route('/oracle')
def oracle():
    page = 'oracle'
    return render_template(
        f'{page}.html',
    )

@app.route('/generator')
def generator():
    page = 'generator'
    return render_template(
        f'{page}.html',
    )

@app.route('/offline')
def offline():
    page = 'offline'
    return render_template(
        f'{page}.html',
    )

@app.route('/offline/tushar')
def offline_tushar():
    page = 'offline_tushar'
    return render_template(
        f'{page}.html',
    )

@app.route('/offline/amel')
def offline_amel():
    page = 'offline_amel'
    return render_template(
        f'{page}.html',
    )

@app.route('/offline/andrew')
def offline_andrew():
    page = 'offline_andrew'
    return render_template(
        f'{page}.html',
    )

@app.route('/offline/jack')
def offline_jack():
    page = 'offline_jack'
    return render_template(
        f'{page}.html',
    )

@app.route('/nice')
def nice():
    page = 'nice'
    return render_template(
        f'{page}.html',
    )

@app.route('/')
@app.route('/staytuned')
def staytuned():
    page = 'staytuned'
    return render_template(
        f'{page}.html',
    )


if __name__ == '__main__':
    app.run()
