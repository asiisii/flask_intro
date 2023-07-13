from flask import Flask, render_template

app = Flask(__name__) # creates a new Flask app or a new Flask object, and it gives it a name that is unique
# dunder name is always unique in Python

@app.route("/")
def render_html_template():
    return render_template("first_pg.html")

@app.route("/jinja")
def render_jinja_pg():
    return render_template("jinja_intro.html", name="Habibi Malla", template_name="jinja2") #template_name="Django"

@app.route("/expressions")
def render_expressions():
    #Interpolation
    color="black"
    animal_one="fox"
    animal_two="cat"
    #addition
    orange_amount=10
    apple_amount=20
    donate_amount=15
    #string concatenation
    first_name="habibi"
    last_name="puku"
    kwargs = {
        #Interpolation
        "color" : color,
        "animal_one" : animal_one,
        "animal_two" : animal_two,
        #addition
        "orange_amount" : orange_amount,
        "apple_amount" : apple_amount,
        "donate_amount" : donate_amount,
        #string concatenation
        "first_name" : first_name,
        "last_name" : last_name
    }
    return render_template("expressions.html", **kwargs)

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