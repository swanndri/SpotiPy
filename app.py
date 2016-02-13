from flask import (Flask, render_template, redirect,
                   url_for, request, make_response,
                   flash)
from youtube import Youtube_API
import os

import os

app = Flask(__name__)

app.secret_key = os.urandom(24)
youtube_api = Youtube_API()


@app.route('/')
def index():
    return render_template("basic.html")
	# return render_template("login.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        qeury_string = request.form['query_string']
        results = youtube_api.youtube_search(qeury_string)
        return render_template("basic_list.html", videos=results)
    else:
        return "Search failed"


@app.route('/play/<id>')
def play(id):
    filename = youtube_api.youtube_download(id)
    return render_template('basic_player.html', url=filename)


@app.route('/index.html', methods=['GET', 'POST'])
def discoverView():
    if request.method == 'POST':
        username = request.form['login_info_username']
        password = request.form['login_info_password']

        if attempt_login(username, password):
            flash("Hey presto! Away you go")
            return render_template("layout.html")
        else:
            flash("Oops, looks like those were the wrong details!")
            return redirect(url_for('index'))

    else:
        return render_template("loginock_screen.html")


def attempt_login(username, password):
    # Login Logic
    return True


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
