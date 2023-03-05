from __main__ import api, db
from flask import render_template

@api.route('/bew/<string:id>')
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
