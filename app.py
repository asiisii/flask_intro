from flask import Flask

app = Flask(__name__) # creates a new Flask app or a new Flask object, and it gives it a name that is unique
# dunder name is always unique in Python

@app.route("/")
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