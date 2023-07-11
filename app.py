from flask import Flask, render_template

app = Flask(__name__) # creates a new Flask app or a new Flask object, and it gives it a name that is unique
# dunder name is always unique in Python

@app.route("/")
def render_html_template():
    return render_template("first_pg.html")

@app.route("/second")
def render_second_template():
    return render_template("second_pg.html")


@app.route("/hello_world")
def hello_world():
    return "Hello, world!"


@app.route("/hello")
def html_hello():
    return """
    <html>
    <body>
    <h1>Greetings!</h1>
    <p>Hello, world!</p>
    <p>Hello, world!</p>
    </body>
    </html>
    """