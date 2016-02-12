from flask import (Flask, render_template, redirect, 
                  url_for, request, make_response, 
                  flash)
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)


@app.route('/')
def index():
	return render_template("login.html", html_title="Login | Spotipy")

@app.route('/index.html', methods=['GET', 'POST'])
def discoverView():
	if request.method == 'POST':
		username = request.form['login_info_username']
		password = request.form['login_info_password']

		if attempt_login(username, password):
			flash("Hey presto! Away you go")
			return render_template("index.html")
		else:
			flash("Oops, looks like those were the wrong details!")
			return redirect(url_for('index'))

	else:
		return render_template("loginock_screen.html")

def attempt_login(username,	password):
	#Login Logic
	return True

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port = 8000)