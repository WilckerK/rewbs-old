from flask import jsonify

def response_code(self, code, message=None):
	code_dict = {
		'200': { 'message': message or 'Sucesfully!', 'code': '200' },
		'400': { 'message': message or 'Invalid Fields', 'code': '400' },
		'403': { 'message': message or 'Invalid Key', 'code': '403' }
	}
	return code_dict[code]




