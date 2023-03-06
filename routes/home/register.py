from __main__ import app, db
from flask import flash, redirect, render_template, request, url_for

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')

	email = request.form['email']
	password = request.form['password']
	username = request.form['username']

	db.users.insert_one({
		"name": username,
		"info": { "email": email, "password": password },
		"exp": 0,
		"rewbs": 0,
		# "discordId": "0987654321",
		"bews": [],
		"cards": { "item": [] },
		"map": [],
		"answer": []
	})

	flash("pipi")
	return redirect(url_for('index'))

	# if user and request.form['password'] == user['info']['password']:
	# 	# user = User()
	# 	# user.id = email
	# 	user_login.id = email
	# 	login_user(user_login)
	# 	return redirect('dashboard')
	# return render_template('register.html')
