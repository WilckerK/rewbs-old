from __main__ import dashboard, db
from flask import render_template
from flask_pymongo import ObjectId
from flask_login import current_user

@dashboard.route('/bews')
def bewss():
	user = db.users.find_one_or_404({ "_id": ObjectId(current_user.id) })

	return render_template('dashboard/bews.html', bews=user['bews'])

