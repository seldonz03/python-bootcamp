from flask import Flask, url_for, abort, redirect, request, render_template
app = Flask(__name__)

@app.route("/profile/<username>")
def dynamic_profile(username):
    return render_template(
        "profile.html",
        username=username)


@app.get('/login/')
def login_get():
    return render_template("index.html")

@app.route("/")
@app.route("/home/")
@app.route("/index/")
def index():

    return f"""<h1>Welcome to my page</h1>
    <i>This is a simple example of HTML in Flask</i>
    <ol>
        <li>Learn Flask</li>
        <li>Build a project</li>
    </ol>
<a href="https://flask.palletsprojects.com/">Guide</a>

<a href="{url_for('login_get', username="Ace")}">Ace</a>


"""


@app.route("/user/<username>")
def profile(username=None):
    abort(501)

@app.errorhandler(501)
def not_implemented(error):
    return"Not implemented yet"



def valid(username,email,password):
    return not (
        username == "admin"
        and password == "pass"
        and email == "admin@gmail.com"
    )

@app.post('/login/')
def login_post():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    if not valid(username, email, password):
        return "Invalid credentials!"
    else:
        return "Login successful!"


app.run()

