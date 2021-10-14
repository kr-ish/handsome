from flask import Flask, render_template
import os
import glob
import random

app = Flask(__name__)

video_paths = glob.glob('./static/*.mp4')
filters = [
    ('Breakdown', 'justinwlaurent'),
    ('Chromatic Vortex', 'sergiooturano'),
    ('Radial Blur', 'iamcraiglewis2'),
    ('TAKEAWAY', 'liamo.studio'),
    ('𝟡𝟘𝕤𝕥𝕖𝕥𝕙𝕚𝕔', 'demiandrou'),
    ('カラーフィルム - Color Film', 'bma_japan'),
]
# TODO: add list of song urls
# TODO: come up with way to only show filters used in the current video?


@app.route('/')
def home():  # put application's code here
    video_path = random.choice(video_paths)
    video = os.path.basename(video_path)
    return render_template('home.html', video=video, filters=filters)


if __name__ == '__main__':
    app.run()
