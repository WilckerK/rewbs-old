from __main__ import api, db
from flask import render_template

@api.route('/rank')
def rank():
    return render_template('rank.html', users=db.users)
