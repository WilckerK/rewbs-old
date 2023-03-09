import random
from flask import jsonify
from __main__ import api, db

def remove_key(d):
	r = dict(d)
	del r['_id']
	return r

@api.route('/booster', methods=['GET'])
def booster():
	cards = list(db.cards.find())
	response = [ remove_key(random.choice(cards)), remove_key(random.choice(cards)) ]
	return jsonify(response)

