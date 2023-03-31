import os

from flask import Flask, request
from flask_pymongo import PyMongo
from flask_login import LoginManager

from dotenv import load_dotenv

from static.scripts.mongo import Mongo
from static.scripts.bew import Bew
from static.scripts.login import User

from routes import api, dashboard, home, admin, import_routes


# Load .env
load_dotenv(dotenv_path='.env')

# App Config
app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI_TEST')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Init db
db = Mongo(app).database()

# Flask-Login Init
user_login = User(app, db) # Eu ia chamar de login_user, mas flask_login já tem um método com esse nome

# Other files
bew = Bew(db) # Precise inicializar por causa dos dict que estão no constructor

# Register blueprints
import_routes()
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(api, url_prefix='/api') 
app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(home)


if __name__ == '__main__':
  app.run(debug=True)

"""
TODO:
- Se inputs em /login, /register, /admin/race, /admin/card, /admin/skill estiverem vazios, dar um aviso
- Verificar se as duas senhas em /register são iguais antes de fazer o reigstro
"""









"""
Python-CLI login pymongo

from pymongo import MongoClient
client = MongoClient("mongodb+srv://API:VrxAzAus26iI3tas@cluster.yruie.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
"""




"""
Pymongo useful things
# mongo.db.list_collection_names() -> Listar collections da db
# mongo.db.users.find({"online": True}) -> Achar todo obj com "online": True
# user = mongo.db.users.find_one_or_404({"_id": username}) -> Procurar por um obj, se não achar dar erro 404
"""

"""
  _   ,_,   _
 / `'=) (='` \
/.-.-.\ /.-.-.\ 
`      "      `
"""