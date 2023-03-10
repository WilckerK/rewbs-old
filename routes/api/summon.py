from __main__ import api, bew, db
from flask import jsonify

@api.route('/summon', methods=['GET']) # GET -> Pegar valor
def summon():
	response = bew.summon(False, db)
	return jsonify(response) # Transforma em JSON
