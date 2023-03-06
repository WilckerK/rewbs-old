from __main__ import admin
from flask_login import current_user

@admin.route('/')
def admin():
	return f'<h1>Olá {current_user.id}</h1>'