import os
from flask import Blueprint, redirect, url_for
from flask_login import current_user

# Create Blueprints
api = Blueprint('api', __name__)
<<<<<<< HEAD
dashboard = Blueprint('dashboard', __name__, static_folder='static', template_folder='templates/dashboard')
home = Blueprint('home', __name__, template_folder='templates/home')
admin = Blueprint("admin", __name__, template_folder='admin')
=======
dashboard = Blueprint('dashboard', __name__, template_folder='templates/dashboard')
admin = Blueprint("admin", __name__, template_folder='templates/admin')
>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d

# Executado antes de ir para qualquer página do dashboard
@dashboard.before_request
def restrict_to_logged_users():
	print(current_user.is_authenticated)
	if not current_user.is_authenticated: # Not logged in
		return redirect(url_for('index'))

@admin.before_request
def restrict_to_admins():
	print(current_user.is_admin)
	if not current_user.is_authenticated or not current_user.is_admin: # Not logged in
		return redirect(url_for('index'))

# Precisa ser em uma função, não sei explicar, mas precisa ser numa função, senão da erro, porque não importou tudo primeiro
def import_routes():
	for root, dirs, files in os.walk('routes'):
		for file in files:

			# Ignore self and functions file
			if str(file).startswith('_'):
				continue

			# print(file)
			if file.endswith('.py'):
				# Get path to routes
				route_path = os.path.join(root, file[:-3]).replace('/', '.')
				# print(route_path)

				# Import routes
				__import__(f'{route_path}', fromlist=[''])
