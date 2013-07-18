"""
    Vertstack Timeline
    ~~~~~~~~~~~~~~~~~~

    A simple app for generating your own timeline

    Keywords: Flask, sqlite, SASS, CoffeeScript

    :copyright: (c) 2013 Raymond Jacobson

"""
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack

from lib import get_formatted_date, get_media_html

# Configuration
DB = '/tmp/vertstack.db'
DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('VERTSTACK_SETTINGS', silent=True)
app.debug = True

def init_db():
    """Creates db tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens db connection if none."""
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        sqlite_db = sqlite3.connect(app.config['DB'])
        sqlite_db.row_factory = sqlite3.Row
        top.sqlite_db = sqlite_db
    return top.sqlite_db

@app.teardown_appcontext
def close_db(exception):
    """Closes the db connection."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

@app.route("/")
def show_timeline():
    db = get_db()
    cur = db.execute('select * from events order by happened_at desc')
    events = cur.fetchall()
    fixed_events = []
    for event in events:
        print event
        fixed_event = {
            'content': event['content'],
            'happened_at': get_formatted_date(event['happened_at']),
            'media_resource': get_media_html(event['media_resource'],
                                             event['media_type'])
        }
        fixed_events.append(fixed_event)
    return_vals = {
        'events': fixed_events,
        'title': 'Vertstack Timeline',
        'subtitle': 'Express a story in time, vertically. Reach for the sky.',
    }
    return render_template('stack.html', return_vals=return_vals)

@app.route("/add", methods=['POST'])
def add_event():
    db = get_db()
    forms = [request.form['happened_at'],
             request.form['content'],
             request.form['media_type'],
             request.form['media_resource']]
    db.execute('insert into events (happened_at, content, \
        media_type, media_resource) values (?, ?, ?, ?)', forms)
    db.commit()
    flash('New event posted')
    return redirect(url_for('show_timeline'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

