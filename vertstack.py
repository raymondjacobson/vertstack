"""
    Vertstack Timeline
    ~~~~~~~~~~~~~~~~~~

    A simple app for generating your own timeline

    Keywords: Flask, sqlite, SASS, CoffeeScript

    :copyright: (c) 2013 Raymond Jacobson

"""
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template('stack.html')

if __name__ == "__main__":
    app.run(debug=True)

