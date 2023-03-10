from __main__ import dashboard, db
from flask import render_template

@dashboard.route('/bew/<string:id>')
def bews(id):
	print(id)
	user = db.users.find_one_or_404({ "discordId": id })

	return render_template('bews.html', bews=user['bews'])

