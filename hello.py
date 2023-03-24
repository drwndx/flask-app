from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from datetime import datetime
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route("/<name>")
def slash_name(name):
    return url_for('static', filename=name)


# @app.route('/hello')
# def hello():
#     return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/layout/')
def layout():
    return render_template('layout.html')


@app.route('/indexx')
def indexx():
    return render_template('indexx.html')


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

