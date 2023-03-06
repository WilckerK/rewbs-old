from __main__ import dashboard, db
from flask import render_template

@dashboard.route('/rank')
def rank():
	return render_template('rank.html', users=db.users)
