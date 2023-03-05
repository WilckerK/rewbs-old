import os
from flask import Flask
from dotenv import load_dotenv # Get .env
from static.scripts.database import mongo
from static.scripts.bew import Bew
from routes import admin, api, dashboard, importRoutes

load_dotenv(dotenv_path='.env') # Load .env
secret_key = os.getenv('SECRET_KEY')
environment = os.getenv('ENVIRONMENT') # ENVIRONMENT=DEV
#O enviroment é responsavel para dizer se é desenvolvimento (DEV) ou produção (PROD)

app = Flask(__name__, instance_relative_config=True)
app.config['MONGO_URI'] = os.getenv(f'MONGO_URI_{environment}') # MONGO_URI=mongodb+srv://API:VrxAzAus26iI3tas@cluster.yruie.mongodb.net/{-> NOME DA DATABASE<-}?retryWrites=true&w=majority
# MONGO_URI_DEV é a db test / MONGO_URI_PROD é a db database
mongo.init_app(app) # inicializar o mongo
db = mongo.db


bew = Bew() # Precise inicializar por causa dos dict que estão no constructor
importRoutes() # Registra as rotas em seus respectivos caminhos

app.register_blueprint(api, url_prefix="/api") 
app.register_blueprint(dashboard, url_prefix="/dashboard")
app.register_blueprint(admin, url_prefix="/admin")

# as blueprints são para modular e separar rotas, url prefix define o prefixo q toda rota vai ter
# por exemplo uma rota "/macaco" criada dentro da blueprint de /api, será acessada com /api/macaco
# para criar uma rota dentro de uma blueprint ao invés de usar @app, se usa @nomedablueprint, exemplo @api, @dashboard

"""
from pymongo import MongoClient
client = MongoClient("mongodb+srv://API:VrxAzAus26iI3tas@cluster.yruie.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
"""

# "mongodb+srv://vako:Senha-Database321@datacluster.nqb0w6x.mongodb.net/rebtest?retryWrites=true&w=majority"

# flask_mongo é uma fusão de pymongo com flask_sqlaclhemy
# mongo.db.list_collection_names() -> Listar collections da db
# mongo.db.users.find({"online": True}) -> Achar todo obj com "online": True

# user = mongo.db.users.find_one_or_404({"_id": username}) -> Procurar por um obj, se não achar dar erro 404

# Global pra não ter que iniciar toda vez

if __name__ == '__main__':
	if environment == "DEV": app.run(debug=True)
	else: app.run()
