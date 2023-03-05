from __main__ import api, db, bew, secret_key
from flask import jsonify, request

# curl -X POST -H "Content-Type: application/json" -d '{"message": "ola"}' http://localhost:5000/api/echo
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "6403ac5003f8e40841a1b105", "userId2": "6403aca303f8e40841a1b106", "bewId": "123", "bewId2": "321", "secret_key": "CHAVESUPERSECRETA321123"}' http://localhost:5000/api/trade
@api.route('/trade', methods=['POST']) # POST -> Passar valor
def trade_bews():
	data = request.json # Get request
>>>>>>> c0607c05c5e3d7b13942072916c56cfecca70f66:routes/api.py

	# Check if have necessary values
	if sorted(list(data.keys())) != ['bewId', 'bewId2', 'secret_key', 'userId', 'userId2']:
		return response_code('400')

	# Check for secret_key
	if data['secret_key'] != secret_key:
		return response_code('403')

	# Get response
	response = bew.trade_bews(data, db)
	return jsonify(response)


