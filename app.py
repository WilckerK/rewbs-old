from flask import Flask, redirect, render_template, request
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://vako:Senha-Database321@datacluster.nqb0w6x.mongodb.net/rebtest?retryWrites=true&w=majority"
mongo = PyMongo(app)

# "mongodb+srv://vako:Senha-Database321@datacluster.nqb0w6x.mongodb.net/dataTest?retryWrites=true&w=majority"


# flask_pymongo is basically a fusion of flas_sqlalchemy and pymogn

# mongo.db.list_collection_names()
# mongo.db.users.find({"online": True}).
# user = mongo.db.users.find_one_or_404({"_id": username})

@app.route('/')
def index():
	user = mongo.db.users.find_one_or_404({ "discordId": '1234567890' })
	return render_template('index.html', name=user['name'])

@app.route('/bew/<string:id>')
def bews(id):
	print(id)
	user = mongo.db.users.find_one_or_404({ "discordId": id })

	return render_template('bews.html', bews=user['bews'])

@app.route('/rank/')
def rank():
	return render_template('rank.html', users=mongo.db.users)


if __name__ == '__main__':
	app.run(debug=True) # debug -> Live hot