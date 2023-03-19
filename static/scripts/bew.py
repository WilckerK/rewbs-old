import random, os, base64
from io import BytesIO
from flask_pymongo import ObjectId
from .api import response_code
from PIL import Image, ImageEnhance
from .mongo import Mongo


class Bew:
	def __init__(self, db):
		self.db = db # COMO QUE EU NUNCA PENSEI NISSO?????

		self.personalities_dict = {
			"ALE": "Alegre",
			"ATR": "Atrevido",
			"COR": "Corajoso",
			"CUR": "Curioso",
			"INS": "Insano",
			"MED": "Medroso",
			"RAN": "Rancoroso",
			"VIO": "Violento"
		}

		self.types_dict = {
			"KI": { "name": "King",     "description": "Rei, poder político, chefe da tribo, reino, líder",    "types": [ ["SW","KI"], ["ST","RO"], ["SM","FO"] ], "emoji": '👑', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558645349535884/1.png'  },
			"SW": { "name": "Sword",    "description": "Espada, facas, armas brancas, guerra, violência",      "types": [ ["BE","RO"], ["BO","MI"], ["MU","SM"] ], "emoji": '⚔️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558645781536868/2.png'  },
			"MU": { "name": "Music",    "description": "Musica, arte, melodia, harmonia, ordem, esculturas",   "types": [ ["SM","MU"], ["SW","GE"], ["GO","ST"] ], "emoji": '🎵', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558646259687475/3.png'  },
			"GE": { "name": "Gear",     "description": "Engrenagem, máquinas, fábricas, metal, robôs",         "types": [ ["CY","SW"], ["CL","CA"], ["BE","MU"] ], "emoji": '⚙️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558646754623559/4.png'  },
			"SM": { "name": "Smile",    "description": "Sorriso, alegria, humor, juventude, festa, inocencia", "types": [ ["GO","BO"], ["KI","SW"], ["CL","GO"] ], "emoji": '🙂', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558755869425746/5.png'  },
			"GO": { "name": "Goodness", "description": "Bondade, benevolencia, religioso, paz, santo...",      "types": [ ["KI","MI"], ["MU","SM"], ["BE","CA"] ], "emoji": '💚', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558756255318136/6.png'  },
			"BO": { "name": "Book",     "description": "Livro, conhecimento, estudos, psiquico, mental",       "types": [ ["FO","MU"], ["BE","CY"], ["SW","MI"] ], "emoji": '📙', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558756607639763/7.png'  },
			"BE": { "name": "Beast",    "description": "Besta, fera, animal, voraz, monstro, irracional",      "types": [ ["AN","BE"], ["GO","GE"], ["BO","ST"] ], "emoji": '🐾', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558757022875688/8.png'  },
			"RO": { "name": "Roses",    "description": "Rosas, plantas, paixão, natureza, amor, sedução",      "types": [ ["SM","CL"], ["AN","FO"], ["CL","KI"] ], "emoji": '🌹', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831106863244/9.png'  },
			"CA": { "name": "Catalyst", "description": "Catalizador, químico, mágico, intensificar, poções",   "types": [ ["ST","CY"], ["CA","GO"], ["GE","CA"] ], "emoji": '⚗️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831517900930/10.png' },
			"MI": { "name": "Mistery",  "description": "Mistério, bruxaria, oculto, maligno, criminoso",       "types": [ ["CA","FO"], ["BO","AN"], ["CY","SW"] ], "emoji": '🌑', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831924748308/11.png' },
			"ST": { "name": "Star",     "description": "Estrela, espaço, luz, planetas, fama, iluminado",      "types": [ ["MI","RO"], ["BE","MU"], ["AN","KI"] ], "emoji": '🌟', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558832373542992/12.png' },
			"CL": { "name": "Cloud",    "description": "Nuvem, voar, ar, ventos, clima, alto, leve",           "types": [ ["GE","ST"], ["SM","RO"], ["AN","GE"] ], "emoji": '☁️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558922551070760/13.png' },
			"CY": { "name": "Cyber",    "description": "Cibernético, tecnologia, software, elétrico, moderno", "types": [ ["CL","AN"], ["CY","MI"], ["CY","BO"] ], "emoji": '📱', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558923054383154/14.png' },
			"FO": { "name": "Fortune",  "description": "Fortuna, dinheiro, capital, ouro, riquezas, ganância", "types": [ ["GE","GO"], ["FO","KI"], ["FO","RO"] ], "emoji": '💰', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558923549311047/15.png' },
			"AN": { "name": "Ancient",  "description": "Ancião, antigo, esquecido, desgastado, passado",       "types": [ ["BO","CA"], ["ST","CL"], ["MI","RO"] ], "emoji": '⏳', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558924056825916/16.png' },
			"TS": { "name": "Tsunami",  "description": "Água, gelo, submarino, aquatico, frio",                "types": [], "emoji": '🌊', "image_url": ''},
			"EM": { "name": "Ember",    "description": "typesas, Fogo, calor, quente, lava, queimar",          "types": [], "emoji": '🔥', "iamge_url": ''}
		}

		self.types_chart = { # Type / Effective / Ineffective
			"KI": [["KI", "SW", "FO"], ["ST", "RO", "GO"]],
			"SW": [["SM", "BE", "MI"], ["GE", "BO"]],
			"MU": [["SM", "GO"],       ["BO", "AN", "GE"]],
			"GE": [["CL", "CY"],       ["MU", "BO", "FO"]],
			"SM": [["AN", "RO"],       ["SW", "GO"]],
			"GO": [["KI", "ST"],       ["SW", "SM"]],
			"BO": [["MI", "SW"],       ["KI", "MU"]],
			"BE": [["BE", "FO", "CY"], ["AN", "CL", "SM"]],
			"RO": [["TS", "CA", "ST"], ["GE", "EM"]],
			"CA": [["ST", "MU", "FO"], ["MI", "GO"]],
			"MI": [["CA", "EM", "GO"], ["ST", "MU"]],
			"ST": [["MI", "TS", "CL"], ["CA", "EM"]],
			"EM": [["RO", "BO", "GE"], ["TS", "CL", "MI"]],
			"TS": [["EM", "BO"],       ["BE", "RO", "CA"]],
			"CL": [["RO", "MU"],       ["CL", "TS", "CY"]],
			"CY": [["AN", "BO", "CA"], ["FO", "TS", "SM"]],
			"FO": [["GO", "SW"],       ["FO", "BE"]],
			"AN": [["SM", "GE"],       ["KI", "AN", "CY"]],
		}


		self.skills_dict = {
			"S1": { "name": "Soberano",    "types": ['KI','AN']      },
			"S2": { "name": "Sob Pressão", "types": ['KI','SW','ST'] },
			"C1": { "name": "Controle",    "types": ['KI','GE','CY'] },
			"R1": { "name": "Retorno",     "types": ['GO','CA','FO'] },
			"T1": { "name": "Transmitir",  "types": ['GO','BO','CY'] },
			"M1": { "name": "Manufatura",  "types": ['GE','BO','FO'] },
			"S3": { "name": "Sucata",      "types": ['SW','GE']      },
			"R2": { "name": "Rigidez",     "types": ['GE','ST','AN'] },
			"L1": { "name": "Leve",        "types": ['RO','CL']      },
			"F1": { "name": "Fluxo",       "types": ['MU','CL','CY'] },
			"E1": { "name": "Esvair",      "types": ['MI','CL','FO'] },
			"D1": { "name": "Dissolver",   "types": ['SM','CA','CL'] },
			"P1": { "name": "Poesia",      "types": ['MU','BO']      },
			"E2": { "name": "Emocional",   "types": ['SM','GO','RO'] },
			"H1": { "name": "Hiperativo",  "types": ['SM','BE','ST'] },
			"A1": { "name": "Assassino",   "types": ['SW','BE']      },
			"P2": { "name": "Paixão",      "types": ['MU','RO','MI'] },
			"V1": { "name": "Veneno",      "types": ['RO','CA','AN'] },
			"O1": { "name": "Oculto",      "types": ['SM','AN','MI'] },
			"P3": { "name": "Profundo",    "types": ['SW','MI','BO'] },
			"R3": { "name": "Reproduzir",  "types": ['MU','GO','BE'] },
			"I1": { "name": "Imunidade",   "types": ['KI','BE','CA'] },
			"B1": { "name": "Brilhante",   "types": ['ST','CY','FO'] },
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

	def _generate_bew_image(self, race, personality, color):
		race_db = self.db.bews.find_one({ '_id': race }, {'face'})
		x = race_db['face'][0]
		y = race_db['face'][1]
		path = 'static/images/bew_base'


		# Make base
		img = Image.new('RGBA', (320, 320))

		# Load body
		body = Image.open('%s/bodies/%s.png' % (path, race))

		# Get color if needed
		r, g, b, a = body.split()

		# Switch case
		p = int(color[1]) # Pontecia
		match color[0]:
			case 'A':
				enhancer = ImageEnhance.Brightness(body)
				body = enhancer.enhance( ((p+10) - (p*3)) / 10 )
			case 'B':
				enhancer = ImageEnhance.Brightness(body)
				body = enhancer.enhance( ((p+10) + (p*3)) / 10 )
			case 'C':
				r = r.point(lambda i: i * ((p + 10) + (p*3)) / 10 )
			case 'D':
				b = b.point(lambda i: i * ((p + 10) - (p*3)) / 10 )
			case 'E':
				g = b.point(lambda i: i * ((p + 10) + (p*3)) / 10 )
			case 'F':
				r = b.point(lambda i: i * ((p + 10) - (p*3)) / 10 )
			case 'G':
				b = r.point(lambda i: i * ((p + 10) + (p*3)) / 10 )
			case 'H':
				g = r.point(lambda i: i * ((p + 10) - (p*3)) / 10 )

		body = Image.merge('RGBA', (r, g, b, a))
		img.paste(body, (0, 0), body)

		face = Image.open('%s/faces/%s.png' % (path, personality))
		img.paste(face, (x, y), face)

		# Save and convert to base64 (Não sei como fazer de um jeito que não precisa salvar antes)
		buffered = BytesIO()
		img.save(buffered, format="PNG")
		return str(base64.b64encode(buffered.getvalue())).replace('b\'', 'data:image/jpeg;base64,').replace('\'', '')

	def summon(self, register=False):
		genre = random.choice(['M', 'F', 'H', 'X'])
		personality = self._random_key(self.personalities_dict) # Pegar keys e escolher uma aleatoriamente
		color =  self._random_key(self.color_dict) + str(random.randint(0, 3))
	
		race = self.db.bews.find()[random.randint(1, self.db.bews.count_documents({}) - 1)]
		types = [random.choice(race['types']), random.choice(race['types'])]
		
		# types = [self._random_key(self.types_dict), self._random_key(self.types_dict)]

		# Skill
		skills = ['00', '00', '00']
		if(random.random() <= 0.8): # 80%
			skills[0] = self._random_key(self.skills_dict)

			if(random.random() <= 0.5):
				skills[1] = self._random_key(self.skills_dict)

				if(random.random() <= 0.3):
					skills[2] = self._random_key(self.skills_dict)



		# Status and Tier
		ATK = random.randint(0, 15) # :02d ->  01, 02, etc
		SPD = random.randint(0, 15)
		ACC = random.randint(0, 15)
		RST = random.randint(0, 45)
		STATUS = [ATK, SPD, ACC, RST]
		tier = '{:02d}'.format( int( ((ATK + SPD + ACC) / 7 ) + (RST / 13) + (3 - skills.count('00')) ) )
		
		# Make Id
		bew_id = personality + race['_id'] + genre + tier + color + ''.join(types) + ''.join(skills) + ''.join(str(STATUS))

		# Check if bewId exist
		for id in self.db.bews.find_one({ '_id': '000' })['registered']:
			if bew_id == id:
				return response_code('400', 'Poisé nego, se fudeu')

		# If not, register
		if register:
			self.db.bews.update_one({ '_id': '000' }, { '$push': { # Pare remover um item do array é só trocar o "$push" por "$pull"
					'registered': bew_id
				}
			})

		# Gen image
		image = self._generate_bew_image(race['_id'], personality, color, self.db)

		# Return
		return {
			'id': bew_id,
			'tier': tier,
			'race': race['name'],
			'height': '%dm' % (1 - (0.12 - int(tier)/100)),
			'genre': genre,
			'personality': personality,
			'color': color,
			'types': types,
			'skills': skills,
			'status': {
				"ATK": f'{(ATK + 10):02d}',
				"SPD": f'{(SPD + 10):02d}',
				"ACC": f'{(ACC + 80):02d}',
				"RST": f'{(RST + 80):02d}'
			},
			'name': race['name'],
			'image': str(image),
			'item': None,
			'feli': 100
		}

	def release(self, bewId, userId):
		# Remove from registered
		self.db.bews.update_one({ '_id': '000' }, { '$pull': {
				'registered': bewId
			}
		})

		# Search for bew in user obj
		for bew in self.db.users.find_one({ '_id': ObjectId(userId) }):
			# Found and remove
			if bew['bewId'] == bewId:
				self.db.users.update_one({'_id': ObjectId(userId)}, {'$pull': {'bews': {'bewId': bewId}}})
				return response_code('200', 'Released!')
		return response_code('400', 'Bew not found!')



	def query_bew_id(self, bewId):
		color = bewId[9:11]
		types = bewId[11:15]
		skills = bewId[15:21]
		status = bewId[21:]
		race = self.db.bews.find()[bewId[3:6]]['name']
		personality = self.personalities_dict[bewId[0:3]]
		image = self._generate_bew_image(race, personality, color)

		return {
			"personality": personality,
			"race": race,
			"genre": self.genre_dict[bewId[6:7]],
			"tier": bewId[7:9],
			"color": {
				'color': self.color_dict[color[0]],
				'intensity': color[1]
			},
			"types": [ self.types_dict[types[0:2]], self.types_dict[types[2:]] ],
			"skills": [ self.skills_dict[skills[0:2]],  self.skills_dict[skills[2:4]], self.skills_dict[skills[4:]] ],
			"status": {
				"ATK": status[0:2],
				"SPD": status[2:4],
				"ACC": status[4:6],
				"RST": status[6:]
			},
			"image": str(image)
		}


	# Só para debug
	def query_user_bew(self, data):
		user = self.db.users.find_one({'_id': ObjectId(data['userId']) }) # Return only bews field

		if not user:
			return response_code('400', 'User doesn\'t exist')

		ibew = self._find_bew_index(user, data['bewId'])
		if not ibew:
			return response_code('400', 'Bew was not found')

		return {
			"owner_name": user['name'],
			"bews": user['bews'][self._find_bew_index]
		}


	def trade_bews(self, data):
		# Get users
		user = self.db.users.find_one({'_id': ObjectId(data['userId']) })#, { 'bews' }) # Return only bews field
		user2 = self.db.users.find_one({'_id': ObjectId(data['userId2']) })#, { 'bews' })

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
		self.db.users.update_one({'_id': ObjectId(data['userId'])}, {'$set': {'bews.%c' % str(ibew): bew } })
		self.db.users.update_one({'_id': ObjectId(data['userId2'])}, {'$set': {'bews.%c' % str(ibew2): bew2 } })

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