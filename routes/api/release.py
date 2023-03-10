from __main__ import api, bew, db
from flask_login import current_user

@api.route('/release/<string:id>', methods=['GET'])
def release(id):
	response = bew.release(id, current_user.id,db)
	return response

