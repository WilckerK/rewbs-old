<<<<<<< HEAD
from __main__ import home, user_login
=======
from __main__ import app, user_login
>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d
from flask import render_template, request, redirect, url_for
from flask_login import login_user


<<<<<<< HEAD
@home.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('home/login.html')
=======
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d

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
<<<<<<< HEAD
	return render_template('home/login.html')
=======
	return render_template('login.html')
>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d
