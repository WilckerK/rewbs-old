from __main__ import api, db, bew, secret_key
from flask import jsonify, request

<<<<<<< HEAD:routes/api/trade.py
# curl -X POST -H "Content-Type: application/json" -d '{"message": "ola"}' http://localhost:5000/api/echo
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "6403ac5003f8e40841a1b105", "userId2": "6403aca303f8e40841a1b106", "bewId": "123", "bewId2": "321", "secret_key": "CHAVESUPERSECRETA321123"}' http://localhost:5000/api/trade
@api.route('/trade', methods=['POST']) # POST -> Passar valor
def trade():
	data = request.json
	print(data)
	print(list(data.keys()))
=======
def response_code(code):
	code_dict = {
		'404': { 'message': 'Invalid Fields', 'code': '400' },
		'403': { 'message': 'Invalid Key', 'code': '403' }
	}

	return jsonify(code_dict[code])


@app.route('/api/summon_bew', methods=['GET']) # GET -> Pegar valor
def summon_bew():
	response = bew.summon_bew()
	return jsonify(response) # Transforma em JSON


# curl -X POST -H "Content-Type: application/json" -d '{"userId": "64049cc17ee9087557d9e1af", "bewId": "CUR001F03G2ETFER3000002011502"}' http://localhost:5000/api/query_user_bew
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "64049d3c7ee9087557d9e1b0", "bewId": "SANTOCRISTO"}' http://localhost:5000/api/query_suer_bew
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "64049cc17ee9087557d9e1af", "bewId": "SANTOCRISTO"}' http://localhost:5000/api/query_user_bew
@app.route('/api/query_user_bew', methods=['POST']) # POST -> Passar valor
def query_user_bew():
	data = request.json # Get request

	# Check if have necessary values
	if sorted(list(data.keys())) != ['bewId', 'userId']:
		return response_code('400')


	# Get response
	response = bew.query_user_bew(data, db)
	return jsonify(response)

# Query bew's id
@app.route('/api/query_bew_id/<string:id>', methods=['GET'])
def query_bew_id(id):
	# data = request.json # Get request
	# print(data)

	# Check if have necessary values
	# if sorted(list(data.keys()))  != ['bewId']:
	# 	return response_code('400')

	# response = bew.query_bew(data['bewId'], db)
	response = bew.query_bew_id(id)
	return response


# curl -X POST -H "Content-Type: application/json" -d '{"message": "ola"}' http://localhost:5000/api/echo
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "64049cc17ee9087557d9e1af", "userId2": "64049d3c7ee9087557d9e1b0", "bewId": "CUR001F03G2ETFER3000002011502", "bewId2": "SANTOCRISTO", "secret_key": "CHAVESUPERSECRETA321123"}' http://localhost:5000/api/trade_bews
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "64049d3c7ee9087557d9e1b0", "userId2": "64049cc17ee9087557d9e1af", "bewId": "CUR001F03G2ETFER3000002011502", "bewId2": "SANTOCRISTO", "secret_key": "CHAVESUPERSECRETA321123"}' http://localhost:5000/api/trade_bews
@app.route('/api/trade_bews', methods=['POST']) # POST -> Passar valor
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


