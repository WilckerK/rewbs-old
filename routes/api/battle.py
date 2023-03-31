from __main__ import api, bew, db

from flask_pymongo import ObjectId
from static.scripts.api import response_code
from static.scripts.bew import Battle, BewBattle
from flask import request, jsonify

# curl -X POST -H "Content-Type: application/json" -d '{ "player1": {"id": "bababa", "team": []}, "player2": {"id": "bababa", "team": [{}]} }'

# curl -X POST -H "Content-Type: application/json" -d '{ "player1": {"id": "64049cc17ee9087557d9e1af", "team": ["VIO004M05C3BECLV1000000120724", "COR002H07D3BEKIT1S10004061131"]}, "player2": {"id": "64049d3c7ee9087557d9e1b0", "team": ["RAN011F04H1ANCAB1S30012000703", "RAN008F05H0CYFO00000004100237"]} }' http://localhost:5000/api/battle
@api.route('/battle', methods=['POST']) # POST -> Passar valor
def battle():
	data = request.json # Get request

	# Check if have necessary values
	if sorted(list(data.keys())) != ['player1', 'player2']:
		return jsonify(response_code('400'))

	player1_team = bew.query_team(data['player1']['id'], data['player1']['team'])
	player2_team = bew.query_team(data['player2']['id'], data['player2']['team'])

	if not player1_team or not player2_team:
		return jsonify(response_code('400', 'User doesn\'t exists'))


	print(player2_team)
	# Get response


	player1 = db.users.find_one({ '_id': ObjectId(data['player1']['id']) })
	player2 = db.users.find_one({ '_id': ObjectId(data['player2']['id']) })
	battle = Battle(
		[BewBattle(bew, player1) for bew in player1_team],
		[BewBattle(bew, player2) for bew in player2_team]
	)

	response = battle.start_battle()
	return jsonify(response)
