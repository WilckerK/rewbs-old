from __main__ import api, bew
from flask import jsonify

@api.route('/summon_bew', methods=['GET']) # GET -> Pegar valor
def summon_bew():
	response = bew.summon_bew()
	return jsonify(response) # Transforma em JSON

