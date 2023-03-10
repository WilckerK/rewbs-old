from flask import jsonify

<<<<<<< HEAD
def response_code(code, message=None):
	code_dict = {
		'200': { 'message': message or 'Sucesfully!', 'code': '200' },
		'400': { 'message': message or 'Invalid Scopes', 'code': '400' },
		'403': { 'message': message or 'Invalid Key', 'code': '403' }
	}
	return code_dict[code]
=======
def response_code(self, code, message=None):
	code_dict = {
		'200': { 'message': message or 'Sucesfully!', 'code': '200' },
		'400': { 'message': message or 'Invalid Fields', 'code': '400' },
		'403': { 'message': message or 'Invalid Key', 'code': '403' }
	}
	return code_dict[code]




>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d
