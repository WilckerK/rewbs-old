from __main__ import api, bew

@api.route('/query_bew_id/<string:id>', methods=['GET'])
def query_bew_id(id):
	# data = request.json # Get request
	# print(data)

	# Check if have necessary values
	# if sorted(list(data.keys()))  != ['bewId']:
	# 	return response_code('400')

	# response = bew.query_bew(data['bewId'], db)
	response = bew.query_bew_id(id)
	return response

