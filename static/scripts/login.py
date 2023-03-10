# from __main__ import login_manager
from flask_login import LoginManager, UserMixin

"""
Ignora, ainda estou trabalhando nisso
"""


"""
- Decidir onde colocar esse código do flask_login
- Decidir como armazenar email e senha na db
	- Ajeitar no index.py
- Decidir se vai ter uma página só pra login
- 
"""

# class User(UserMixin):
# 	pass

class User(UserMixin):
	def __init__(self, app, db):
		self.db = db
<<<<<<< HEAD
		self.admins = ['email@gmail.com']
=======
		self.admins = ['raimundo@gmail.com']
>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d

		# Init
		login_manager = LoginManager()
		login_manager.init_app(app)

		# Configure user_loader
		@login_manager.user_loader
		def user_loader(email):
			user = self.check_for_password(email)
			if not user:
				return

			# user = User()
			# user.id = email
<<<<<<< HEAD
			self.id = user['_id']
			self.email = email
			self.name = user['name']
=======
			self.id = email
>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d
			self.is_admin = True if email in self.admins else False
			return self

	def check_for_password(self, email):
		users = list(self.db.users.find())
		for user in users:
			if user['info']['email'] == email:
				return user # Exist
		return False

