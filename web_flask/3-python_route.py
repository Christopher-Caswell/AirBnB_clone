#!/usr/bin/python3
"""
mandatory
Write a script that
starts a Flask web application:

Your web application must
be listening on 0.0.0.0, port 5000

Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the
value of the text variable
(replace underscore _ symbols with a space )

/python/(<text>): display “Python ”,
followed by the value of the text variable
(replace underscore _ symbols with a space )

The default value of text is “is cool”

You must use the option
strict_slashes=False in your route definition
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def womp():
    """HTML indicates an exchange of information is forthcoming"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def wompo():
    """Return the HBNB web?"""
    return "HBNB"


@app.route('/c/<stuff>', strict_slashes=False)
def wompa(stuff):
    """Return the url of the page?"""
    return "C {}".format(stuff.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def wompu(text="is cool"):
    """Just saying, cool people don't say they're cool"""
    return "Python %s" % text.replace('_', ' ')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
