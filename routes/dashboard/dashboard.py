import flask_login
from __main__ import dashboard, db
from flask import render_template
from flask_login import current_user

@dashboard.route('/')
def dashboard():
	print(current_user.id)
	print(current_user.email)
	print(current_user.name)
	print(current_user.is_admin)
	print(db.users.find_one({ '_id': current_user.id }))
	return f'<h1> Hello, {current_user.name}</h1>'


"""


curl -X POST \
      'https://api.mercadopago.com/users/test' \
      -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
      -H 'Content-Type: application/json' -d '{ "site_id": "MLA", "description": "a description" }'


"""