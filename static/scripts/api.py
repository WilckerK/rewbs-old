from flask import jsonify

def response_code(code, message=None):
	code_dict = {
		'200': { 'message': message or 'Sucesfully!', 'code': '200' },
		'400': { 'message': message or 'Invalid Scopes', 'code': '400' },
		'403': { 'message': message or 'Invalid Key', 'code': '403' }
	}
	return code_dict[code]
