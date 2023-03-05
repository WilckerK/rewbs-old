from __main__ import api, db, bew, secret_key
from flask import jsonify, request

@api.route('/api/user', methods=['POST']) # POST -> Passar valor
def user():
	data = request.json # Get request

	# Check if have necessary values
	if sorted(list(data.keys())) != ['bewId', 'userId']:
		return response_code('400')

	# Get response
	response = bew.query_user_bew(data, db)
	return jsonify(response)
