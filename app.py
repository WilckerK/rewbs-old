import os
from flask import Flask
from flask_pymongo import PyMongo
from static.scripts.bew import Bew
from dotenv import load_dotenv # Get .env

load_dotenv(dotenv_path='.env') # Load .env
secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI_TEST')
db = PyMongo(app).db


bew = Bew() # Precise inicializar por causa dos dict que estão no constructor

import routes.index, routes.see_bew, routes.see_rank, routes.api


# "mongodb+srv://vako:Senha-Database321@datacluster.nqb0w6x.mongodb.net/rebtest?retryWrites=true&w=majority"
# "mongodb+srv://API:VrxAzAus26iI3tas@cluster.yruie.mongodb.net/?retryWrites=true&w=majority"

# flask_mongo é uma fusão de pymongo com flask_sqlaclhemy
# mongo.db.list_collection_names() -> Listar collections da db
# mongo.db.users.find({"online": True}) -> Achar todo obj com "online": True
# user = mongo.db.users.find_one_or_404({"_id": username}) -> Procurar por um obj, se não achar dar erro 404


# Global pra não ter que iniciar toda vez


if __name__ == '__main__':
	app.run(debug=True)
