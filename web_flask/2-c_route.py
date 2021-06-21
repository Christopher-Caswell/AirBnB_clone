#!/usr/bin/python3
"""
Write a script that
starts a Flask web application:

Your web application must
be listening on 0.0.0.0, port 5000

Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”

followed by the value of the text variable
(replace underscore _ symbols with a space)

You must use the option
strict_slashes=False in your route definition
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def womp():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def wompo():
    return "HBNB"


@app.route('/c/<stuff>', strict_slashes=False)
def wompa(stuff):
    return "C {}".format(stuff.replace("_", " "))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
