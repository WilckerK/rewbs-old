@app.route('/api/query_user_bew', methods=['POST']) # POST -> Passar valor
def query_user_bew():
	data = request.json # Get request

	# Check if have necessary values
	if sorted(list(data.keys())) != ['bewId', 'userId']:
		return response_code('400')


	# Get response
	response = bew.query_user_bew(data, db)
	return jsonify(response)
