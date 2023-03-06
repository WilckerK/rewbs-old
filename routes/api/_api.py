from flask import jsonify

def response_code(code, message=None):
	code_dict = {
		'400': { 'message': message or 'Invalid Fields', 'code': '400' },
		'403': { 'message': message or 'Invalid Key', 'code': '403' }
	}
	return jsonify(code_dict[code])




