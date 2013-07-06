"""
    Vertstack Timeline
    ~~~~~~~~~~~~~~~~~~

    A simple app for generating your own timeline

    Keywords: Flask, sqlite, Isotope

    :copyright: (c) 2013 Raymond Jacobson

"""
from flask import (
    Flask,
    render_template,
)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('vertstack.html')

if __name__ == "__main__":
    app.run(debug=True)
