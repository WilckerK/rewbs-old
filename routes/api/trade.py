from __main__ import api, db, bew, secret_key
from flask import jsonify, request

# curl -X POST -H "Content-Type: application/json" -d '{"message": "ola"}' http://localhost:5000/api/echo
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "6403ac5003f8e40841a1b105", "userId2": "6403aca303f8e40841a1b106", "bewId": "123", "bewId2": "321", "secret_key": "CHAVESUPERSECRETA321123"}' http://localhost:5000/api/trade
@api.route('/trade', methods=['POST']) # POST -> Passar valor
def trade():
	data = request.json
	print(data)
	print(list(data.keys()))

	print(list(data.keys()).sort() != ['bewId', 'bewId2', 'secret_key', 'userId', 'userId2'])
	if(list(data.keys()) != ['userId', 'userId2', 'bewId', 'bewId2', 'secret_key']): # Não tem valores necessários
		return jsonify({ "status": '404' })

	if data['secret_key'] != secret_key:
		return jsonify({ "status": 'Invalid Key' })

	response = bew.trade_bews(data, db)

	# response = { "message": "Done" } # { 'message': data['message'] }

	return jsonify(response)