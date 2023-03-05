from __main__ import api, bew
from flask import jsonify


@api.route('/summon', methods=['GET']) # GET -> Pegar valor
def summon():
	response = bew.summon_bew()
	return jsonify(response) # Transforma em JSON