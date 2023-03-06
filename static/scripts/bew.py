import random
from flask_pymongo import ObjectId
from .api import response_code

class Bew:
	def __init__(self):
		self.personalities_dict = {
			"ALE": "Alegre",
			"MED": "Medroso",
			"COR": "Corajoso",
			"ATR": "Atrevido",
			"CUR": "Curioso",
			"RAN": "Rancoroso",
			"VIO": "Violento",
			"INS": "Insano"
		}

		self.brasoes_dict = {
			"KI" :{ "name": "King",     "bras": [ ["SW","KI"], ["ST","RO"], ["SM","FO"] ], "emoji": '👑', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558645349535884/1.png'  },
			"SW" :{ "name": "Sword",    "bras": [ ["BE","RO"], ["BO","MI"], ["MU","SM"] ], "emoji": '⚔️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558645781536868/2.png'  },
			"MU" :{ "name": "Music",    "bras": [ ["SM","MU"], ["SW","GE"], ["GO","ST"] ], "emoji": '🎵', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558646259687475/3.png'  },
			"GE" :{ "name": "Gear",     "bras": [ ["CY","SW"], ["CL","CA"], ["BE","MU"] ], "emoji": '⚙️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558646754623559/4.png'  },
			"SM" :{ "name": "Smile",    "bras": [ ["GO","BO"], ["KI","SW"], ["CL","GO"] ], "emoji": '🙂', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558755869425746/5.png'  },
			"GO" :{ "name": "Goodness", "bras": [ ["KI","MI"], ["MU","SM"], ["BE","CA"] ], "emoji": '💚', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558756255318136/6.png'  },
			"BO" :{ "name": "Book",     "bras": [ ["FO","MU"], ["BE","CY"], ["SW","MI"] ], "emoji": '📙', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558756607639763/7.png'  },
			"BE" :{ "name": "Beast",    "bras": [ ["AN","BE"], ["GO","GE"], ["BO","ST"] ], "emoji": '🐾', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558757022875688/8.png'  },
			"RO" :{ "name": "Roses",    "bras": [ ["SM","CL"], ["AN","FO"], ["CL","KI"] ], "emoji": '🌹', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831106863244/9.png'  },
			"CA" :{ "name": "Catalyst", "bras": [ ["ST","CY"], ["CA","GO"], ["GE","CA"] ], "emoji": '⚗️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831517900930/10.png' },
			"MI" :{ "name": "Mistery",  "bras": [ ["CA","FO"], ["BO","AN"], ["CY","SW"] ], "emoji": '🌑', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831924748308/11.png' },
			"ST" :{ "name": "Star",     "bras": [ ["MI","RO"], ["BE","MU"], ["AN","KI"] ], "emoji": '🌟', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558832373542992/12.png' },
			"CL" :{ "name": "Cloud",    "bras": [ ["GE","ST"], ["SM","RO"], ["AN","GE"] ], "emoji": '☁️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558922551070760/13.png' },
			"CY" :{ "name": "Cyber",    "bras": [ ["CL","AN"], ["CY","MI"], ["CY","BO"] ], "emoji": '📱', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558923054383154/14.png' },
			"FO" :{ "name": "Fortune",  "bras": [ ["GE","GO"], ["FO","KI"], ["FO","RO"] ], "emoji": '💰', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558923549311047/15.png' },
			"AN" :{ "name": "Ancient",  "bras": [ ["BO","CA"], ["ST","CL"], ["MI","RO"] ], "emoji": '⏳', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558924056825916/16.png' }
		}

		self.skills_dict = {
			"S1": { "name": "Soberano",    "bras": ['KI','AN']      },
			"S2": { "name": "Sob Pressão", "bras": ['KI','SW','ST'] },
			"C1": { "name": "Controle",    "bras": ['KI','GE','CY'] },
			"R1": { "name": "Retorno",     "bras": ['GO','CA','FO'] },
			"T1": { "name": "Transmitir",  "bras": ['GO','BO','CY'] },
			"M1": { "name": "Manufatura",  "bras": ['GE','BO','FO'] },
			"S3": { "name": "Sucata",      "bras": ['SW','GE']      },
			"R2": { "name": "Rigidez",     "bras": ['GE','ST','AN'] },
			"L1": { "name": "Leve",        "bras": ['RO','CL']      },
			"F1": { "name": "Fluxo",       "bras": ['MU','CL','CY'] },
			"E1": { "name": "Esvair",      "bras": ['MI','CL','FO'] },
			"D1": { "name": "Dissolver",   "bras": ['SM','CA','CL'] },
			"P1": { "name": "Poesia",      "bras": ['MU','BO']      },
			"E2": { "name": "Emocional",   "bras": ['SM','GO','RO'] },
			"H1": { "name": "Hiperativo",  "bras": ['SM','BE','ST'] },
			"A1": { "name": "Assassino",   "bras": ['SW','BE']      },
			"P2": { "name": "Paixão",      "bras": ['MU','RO','MI'] },
			"V1": { "name": "Veneno",      "bras": ['RO','CA','AN'] },
			"O1": { "name": "Oculto",      "bras": ['SM','AN','MI'] },
			"P3": { "name": "Profundo",    "bras": ['SW','MI','BO'] },
			"R3": { "name": "Reproduzir",  "bras": ['MU','GO','BE'] },
			"I1": { "name": "Imunidade",   "bras": ['KI','BE','CA'] },
			"B1": { "name": "Brilhante",   "bras": ['ST','CY','FO'] },
			"00": 'None'
		}

		self.color_dict = {
			'A': '0x000000', # Preto
			'B': '0xFFFFFF', # Branco
			'C': 'RED',
			'D': 'YELLOW',
			'E': 'GREEN',
			'F': 'AQUA',
			'G': 'DARKBLUE',
			'H': 'PURPLE',
		}

		self.genre_dict = {
			'M': 'Male',
			'F': 'Female',
			'H': 'Hemaphrodite',
			'X': 'Assexual'
		}

	def _random_key(self, dict):
		return random.choice(list(dict.keys()))

	def _find_bew_index(self, user, id):
		data = user['bews']
		for i in range(len(data)):
			if data[i]['bewId'] == id:
				return i # return index
		return None # Doesn't exist


	def summon_bew(self):
		"""
		id
		tier
		raça
		sexo: M, F, H, X
		personalidade
		cor
		brasão
		habilidades
		ataque, velocidade, acerto, resistencia

		"""
		# id, [raçaId, sexo, raça, genero], Rank, personalidade, [cor, brasões], habs, {ATQ, VEL, ACE, RES}, nome, link

	
		genre = random.choice(['M', 'F', 'H', 'X'])
		personality = self._random_key(self.personalities_dict) # Pegar keys e escolher uma aleatoriamente
		brasoes = [self._random_key(self.brasoes_dict), self._random_key(self.brasoes_dict)]
		color =  self._random_key(self.color_dict) + str(random.randint(1, 4))

		# Skill
		skills = ['00', '00', '00']
		if(random.random() <= 0.8): # 80%
			skills[0] = self._random_key(self.skills_dict)
			print('1', skills)

			if(random.random() <= 0.5):
				skills[1] = self._random_key(self.skills_dict)
				print('2', skills)

				if(random.random() <= 0.3):
					skills[2] = self._random_key(self.skills_dict)
					print('3', skills)

		# Status and Tier
		ATK = f'{random.randint(0, 15):02d}'
		VEL = f'{random.randint(0, 15):02d}'
		ACR = f'{random.randint(0, 15):02d}'
		RES = f'{random.randint(0, 45):02d}'
		STATUS = [ATK, VEL, ACR, RES]
		tier = '{:02d}'.format( int( ((int(ATK) + int(VEL) + int(ACR)) / 7 ) + (int(RES) / 13) + (3 - skills.count('00')) ) )
		

		race = f'{random.randint(1, 255):03d}' # :03d ->  001, 002, etc



		return {
			'id': personality + race + genre + tier + color + ''.join(brasoes) + ''.join(skills) + ''.join(STATUS),
			'tier': tier,
			'race': race,
			'genre': genre,
			'personality': personality,
			'color': color,
			'brasao': brasoes,
			'skills': skills,
			'status': {
				"ATK": ATK,
				"VEL": VEL,
				"ACR": ACR,
				"RES": RES
			},
			'name': None,
			'image': None,
			'item': None,
			'feli': 100
		}

	def query_bew_id(self, bewId):
		# ID -> personality + race + genre + tier + color + brasoes + skills + status
		color = bewId[9:11]
		brasoes = bewId[11:15]
		skills = bewId[15:21]
		status = bewId[21:]
		return {
			"personality": self.personalities_dict[bewId[0:3]],
			"race": bewId[3:6],
			"genre": self.genre_dict[bewId[6:7]],
			"tier": bewId[7:9],
			"color": {
				'color': self.color_dict[color[0]],
				'intensity': color[1]
			},
			"brasoes": [ self.brasoes_dict[brasoes[0:2]], self.brasoes_dict[brasoes[2:]] ],
			"skills": [ self.skills_dict[skills[0:2]],  self.skills_dict[skills[2:4]], self.skills_dict[skills[4:]] ],
			"status": {
				"ATK": status[0:2],
				"VEL": status[2:4],
				"ACR": status[4:6],
				"RES": status[6:],

			}
		}



	def query_user_bew(self, data, db):
		user = db.users.find_one({'_id': ObjectId(data['userId']) }) # Return only bews field

		if not user:
			return response_code('400', 'User doesn\'t exist')

		ibew = self._find_bew_index(user, data['bewId'])
		if not ibew:
			return response_code('400', 'Bew was not found')

		return {
			"owner_name": user['name'],
			"bews": user['bews'][self._find_bew_index]
		}


	def trade_bews(self, data, db):
		# Get users
		user = db.users.find_one({'_id': ObjectId(data['userId']) })#, { 'bews' }) # Return only bews field
		user2 = db.users.find_one({'_id': ObjectId(data['userId2']) })#, { 'bews' })

		# Check if exist
		if not user or not user2:
			return response_code('400', 'User doesn\'t exist')

		# Get bews index
		ibew = self._find_bew_index(user, data['bewId'])
		ibew2 = self._find_bew_index(user2, data['bewId2'])

		# Check if exist
		if ibew == None or ibew2 == None:
			return response_code('400', 'Bew doesn\'t exist')

		# Get bews
		bew = user['bews'][ibew]
		bew2 = user2['bews'][ibew2]

		# Swap values
		bew, bew2 = bew2, bew 

		# Update bews, aka trade
		db.users.update_one({'_id': ObjectId(data['userId'])}, {'$set': {'bews.%c' % str(ibew): bew } })
		db.users.update_one({'_id': ObjectId(data['userId2'])}, {'$set': {'bews.%c' % str(ibew2): bew2 } })

		return response_code('200', 'Trade done!')

"""
{"name":"AAA","discordId":"333333","bews":[{"bewId":"ESSAPIRANHA","item":"Pena","image":"adefeqjo8hfoeunfajldnfoeqhafunaefuiaegfyagdbjfhcaejbjlakelnflandhu==","name":"Rebew","feli":100},{"bewId":"CUR001F03G2ETFER3000002011502","item":None,"image":"gjkjefgeqfsgsfgsgsfhjo8hgjfoegnfoeqhjkkgfyagdbjfhcaegjkgjjbjlasfghsu==","name":"Myra","feli":75}]}
{'bewId': 'AAAA', 'item': None, 'image': 'AA==', 'name': 'MMM', 'feli': 00}


REMOVE OBJECT INSIDE ARRAY
"bews": [
	{
		"name": "baba",
		"bewId": "AAA",
		...
	}
]
-> db.users.update_one({'discordId': '333333'}, {'$pull': {'bews': {'bewId': 'AAA'}}})

EDIT OBJECT INSIDE ARRAY
bews": [
	{
		"name": "baba",
		"bewId": "AAA",
		...
	}
]
new = {"name": "bebe", "bewId": "BBB", ...}

-> db.users.update_one({'discordId': '333333'}, {'$set': {'bews.INDEX': new } })
	(one field only) -> db.users.update_one({'discordId': '333333'}, {'$set': {'bews.INDEX.name': 'raimundin' } })


"""