from flask import Flask, render_template
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
# TODO: add list of song urls


@app.route('/')
def home():
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

    return render_template('home.html', video=video_name, filters=filters)


if __name__ == '__main__':
    app.run()
