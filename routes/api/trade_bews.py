from __main__ import app, api, bew, db
from static.scripts.api import response_code
from flask import request, jsonify


# curl -X POST -H "Content-Type: application/json" -d '{"message": "ola"}' http://localhost:5000/api/echo
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "64049cc17ee9087557d9e1af", "userId2": "64049d3c7ee9087557d9e1b0", "bewId": "CUR001F03G2ETFER3000002011502", "bewId2": "SANTOCRISTO", "secret_key": "CHAVESUPERSECRETA321123"}' http://localhost:5000/api/trade_bews
# curl -X POST -H "Content-Type: application/json" -d '{"userId": "64049d3c7ee9087557d9e1b0", "userId2": "64049cc17ee9087557d9e1af", "bewId": "CUR001F03G2ETFER3000002011502", "bewId2": "SANTOCRISTO", "secret_key": "CHAVESUPERSECRETA321123"}' http://localhost:5000/api/trade_bews
@api.route('/trade_bews', methods=['POST']) # POST -> Passar valor
def trade_bews():
	data = request.json # Get request

	# Check if have necessary values
	if sorted(list(data.keys())) != ['bewId', 'bewId2', 'secret_key', 'userId', 'userId2']:
		return response_code('400')

	# Check for secret_key
	if data['secret_key'] != app.config['SECRET_KEY']:
		return jsonify(response_code('403'))

	# Get response
	response = bew.trade_bews(data, db)
	return jsonify(response)

