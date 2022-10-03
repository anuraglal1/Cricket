from pycricbuzz import Cricbuzz
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/score', methods=['POST'])
def score():
    c = Cricbuzz()
    matches = c.matches()

    posts = {
        1: request.form.get('live score'),
        2: request.form.get('commentary'),
        3: request.form.get('scorecard')
    }

    for post_id in posts.keys():
        x = []
        cnt = 0
        for match in matches:
            x.append(json.dumps(c.commentary(match['id']), indent=4))
            cnt += 1
        return render_template('score.html', y=x, count=cnt, id=post_id)

    return None


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
