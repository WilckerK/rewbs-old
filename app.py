from flask import Flask, request, abort
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://vako:Senha-Database321@datacluster.nqb0w6x.mongodb.net/rebtest?retryWrites=true&w=majority"
mongo = PyMongo(app)

import Rotas.home_window
import Rotas.see_bew
import Rotas.see_rank

app.run(debug=True)
