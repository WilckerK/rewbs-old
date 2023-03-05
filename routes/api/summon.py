from __main__ import api, bew
from flask import jsonify


@api.route('/summon', methods=['GET']) # GET -> Pegar valor
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
