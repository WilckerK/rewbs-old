from __main__ import app, db
from flask import render_template

@app.route('/rank')
def rank():
	return render_template('rank.html', users=db.users)
