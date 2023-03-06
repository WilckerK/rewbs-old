from __main__ import app, user_login
from flask import render_template, request, redirect, url_for
from flask_login import login_user


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')

	email = request.form['email']
	print(email)
	print(request.form['password'])

	user = user_login.check_for_password(email)
	if user and request.form['password'] == user['info']['password']:
		# user = User()
		# user.id = email
		user_login.id = email
		login_user(user_login)
		return redirect('dashboard')
	return render_template('login.html')
