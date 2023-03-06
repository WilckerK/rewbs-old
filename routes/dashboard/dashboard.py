import flask_login
from __main__ import dashboard, db
from flask import render_template
from flask_login import current_user

@dashboard.route('/')
def dashboard():
	return f'<h1> Hello, {current_user.id}</h1>'


