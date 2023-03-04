from __main__ import app, db
from flask import render_template

@app.route('/')
def index():
    user = db.users.find_one_or_404({ "discordId": '1234567890' })
    return render_template('index.html', name=user['name'])
