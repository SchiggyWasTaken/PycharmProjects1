from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>. Es gibt folgende Optionen: /hello /user/username /projects /about"

if __name__ == '__main__':
    app.run(debug = True)

@app.route("/hello")
def hello():
    return 'Hello, World!!!!!!!!!'

@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)
# TO-DO: TEMPLATE ERSTELLEN!!!

@app.route("/user/<username>")
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'

'''
Mehrere URLS zurselben Funktion
@app.route('/item/<int:appitemid>/')
@app.route('/item/<int:appitemid>/<path:anythingcanbehere>')
def show_item(appitemid, anythingcanbehere=None):
'''

''' REROUTEN VON URLS!
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
'''

'''
TEMPLATES ERSTELLEN!!!
'''
