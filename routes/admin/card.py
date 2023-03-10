from flask import jsonify, request, render_template
from __main__ import admin, db

@admin.route('/card', methods=['GET', 'POST'])
def card():
	if request.method == 'GET':
		return render_template('admin/card.html')

	json = {
		'name': request.form['name'],
		'category': request.form['category'],
		'effect': request.form['effect']
	}
	response = jsonify(json) # Por algum motivo da erro se eu não por numa variavel e tentar retornar direto


	db.cards.insert_one(json)
	return response
