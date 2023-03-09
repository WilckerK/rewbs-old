import base64
from io import BytesIO
from flask import jsonify, request, render_template
from __main__ import admin, db

@admin.route('/race', methods=['GET', 'POST'])
def race():
	if request.method == 'GET':
		return render_template('race.html')

	# Get infos
	id = '{:03d}'.format(db.bews.count_documents({}))
	name = request.form['name']
	face_x = request.form['faceX']
	face_y = request.form['faceY']
	types = request.form['types']

	# Get image and pass to Base64
	image = ''
	if 'image' in request.files:
		image = str(base64.b64encode(request.files['image'].read())).replace('b\'', 'data:image/jpeg;base64,').replace('\'', '')

	# Pass to Json
	json = {
		'_id': id,
		'name': name,
		'face': [face_x, face_y],
		'types': types
		'image': image
	}
	db.bews.insert_one(json) # Insert
	return jsonify(json)
