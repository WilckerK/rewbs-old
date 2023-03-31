import os, base64
from io import BytesIO
from flask_pymongo import ObjectId
from .api import response_code
from PIL import Image, ImageEnhance
from .mongo import Mongo


import time
from typing import Deque
from random import random, sample, choice, randint
from collections import deque
from copy import deepcopy


class Bew:
	def __init__(se,lf, db):
		self.db = db

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
			"KI": { "acronym": "KI", "name": "King",     "description": "Rei, poder político, chefe da tribo, reino, líder",    "types": [ ["SW","KI"], ["ST","RO"], ["SM","FO"] ], "emoji": '👑', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558645349535884/1.png'  },
			"SW": { "acronym": "SW", "name": "Sword",    "description": "Espada, facas, armas brancas, guerra, violência",      "types": [ ["BE","RO"], ["BO","MI"], ["MU","SM"] ], "emoji": '⚔️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558645781536868/2.png'  },
			"MU": { "acronym": "MU", "name": "Music",    "description": "Musica, arte, melodia, harmonia, ordem, esculturas",   "types": [ ["SM","MU"], ["SW","GE"], ["GO","ST"] ], "emoji": '🎵', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558646259687475/3.png'  },
			"GE": { "acronym": "GE", "name": "Gear",     "description": "Engrenagem, máquinas, fábricas, metal, robôs",         "types": [ ["CY","SW"], ["CL","CA"], ["BE","MU"] ], "emoji": '⚙️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558646754623559/4.png'  },
			"SM": { "acronym": "SM", "name": "Smile",    "description": "Sorriso, alegria, humor, juventude, festa, inocencia", "types": [ ["GO","BO"], ["KI","SW"], ["CL","GO"] ], "emoji": '🙂', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558755869425746/5.png'  },
			"GO": { "acronym": "GO", "name": "Goodness", "description": "Bondade, benevolencia, religioso, paz, santo...",      "types": [ ["KI","MI"], ["MU","SM"], ["BE","CA"] ], "emoji": '💚', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558756255318136/6.png'  },
			"BO": { "acronym": "BO", "name": "Book",     "description": "Livro, conhecimento, estudos, psiquico, mental",       "types": [ ["FO","MU"], ["BE","CY"], ["SW","MI"] ], "emoji": '📙', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558756607639763/7.png'  },
			"BE": { "acronym": "BE", "name": "Beast",    "description": "Besta, fera, animal, voraz, monstro, irracional",      "types": [ ["AN","BE"], ["GO","GE"], ["BO","ST"] ], "emoji": '🐾', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558757022875688/8.png'  },
			"RO": { "acronym": "RO", "name": "Roses",    "description": "Rosas, plantas, paixão, natureza, amor, sedução",      "types": [ ["SM","CL"], ["AN","FO"], ["CL","KI"] ], "emoji": '🌹', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831106863244/9.png'  },
			"CA": { "acronym": "CA", "name": "Catalyst", "description": "Catalizador, químico, mágico, intensificar, poções",   "types": [ ["ST","CY"], ["CA","GO"], ["GE","CA"] ], "emoji": '⚗️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831517900930/10.png' },
			"MI": { "acronym": "MI", "name": "Mistery",  "description": "Mistério, bruxaria, oculto, maligno, criminoso",       "types": [ ["CA","FO"], ["BO","AN"], ["CY","SW"] ], "emoji": '🌑', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831924748308/11.png' },
			"ST": { "acronym": "ST", "name": "Star",     "description": "Estrela, espaço, luz, planetas, fama, iluminado",      "types": [ ["MI","RO"], ["BE","MU"], ["AN","KI"] ], "emoji": '🌟', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558832373542992/12.png' },
			"CL": { "acronym": "CL", "name": "Cloud",    "description": "Nuvem, voar, ar, ventos, clima, alto, leve",           "types": [ ["GE","ST"], ["SM","RO"], ["AN","GE"] ], "emoji": '☁️', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558922551070760/13.png' },
			"CY": { "acronym": "CY", "name": "Cyber",    "description": "Cibernético, tecnologia, software, elétrico, moderno", "types": [ ["CL","AN"], ["CY","MI"], ["CY","BO"] ], "emoji": '📱', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558923054383154/14.png' },
			"FO": { "acronym": "FO", "name": "Fortune",  "description": "Fortuna, dinheiro, capital, ouro, riquezas, ganância", "types": [ ["GE","GO"], ["FO","KI"], ["FO","RO"] ], "emoji": '💰', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558923549311047/15.png' },
			"AN": { "acronym": "AN", "name": "Ancient",  "description": "Ancião, antigo, esquecido, desgastado, passado",       "types": [ ["BO","CA"], ["ST","CL"], ["MI","RO"] ], "emoji": '⏳', "image_url": 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558924056825916/16.png' },
			"TS": { "acronym": "TS", "name": "Tsunami",  "description": "Água, gelo, submarino, aquatico, frio",                "types": [], "emoji": '🌊', "image_url": ''},
			"EM": { "acronym": "EM", "name": "Ember",    "description": "typesas, Fogo, calor, quente, lava, queimar",          "types": [], "emoji": '🔥', "iamge_url": ''}
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
			"S1": { "acronym": "S1", "name": "Soberano",    "types": ['KI','AN']      },
			"S2": { "acronym": "S2", "name": "Sob Pressão", "types": ['KI','SW','ST'] },
			"C1": { "acronym": "C1", "name": "Controle",    "types": ['KI','GE','CY'] },
			"R1": { "acronym": "R1", "name": "Retorno",     "types": ['GO','CA','FO'] },
			"T1": { "acronym": "T1", "name": "Transmitir",  "types": ['GO','BO','CY'] },
			"M1": { "acronym": "M1", "name": "Manufatura",  "types": ['GE','BO','FO'] },
			"S3": { "acronym": "S3", "name": "Sucata",      "types": ['SW','GE']      },
			"R2": { "acronym": "R2", "name": "Rigidez",     "types": ['GE','ST','AN'] },
			"L1": { "acronym": "L1", "name": "Leve",        "types": ['RO','CL']      },
			"F1": { "acronym": "F1", "name": "Fluxo",       "types": ['MU','CL','CY'] },
			"E1": { "acronym": "E1", "name": "Esvair",      "types": ['MI','CL','FO'] },
			"D1": { "acronym": "D1", "name": "Dissolver",   "types": ['SM','CA','CL'] },
			"P1": { "acronym": "P1", "name": "Poesia",      "types": ['MU','BO']      },
			"E2": { "acronym": "E2", "name": "Emocional",   "types": ['SM','GO','RO'] },
			"H1": { "acronym": "H1", "name": "Hiperativo",  "types": ['SM','BE','ST'] },
			"A1": { "acronym": "A1", "name": "Assassino",   "types": ['SW','BE']      },
			"P2": { "acronym": "P2", "name": "Paixão",      "types": ['MU','RO','MI'] },
			"V1": { "acronym": "V1", "name": "Veneno",      "types": ['RO','CA','AN'] },
			"O1": { "acronym": "O1", "name": "Oculto",      "types": ['SM','AN','MI'] },
			"P3": { "acronym": "P3", "name": "Profundo",    "types": ['SW','MI','BO'] },
			"R3": { "acronym": "R3", "name": "Reproduzir",  "types": ['MU','GO','BE'] },
			"I1": { "acronym": "I1", "name": "Imunidade",   "types": ['KI','BE','CA'] },
			"B1": { "acronym": "B1", "name": "Brilhante",   "types": ['ST','CY','FO'] },
			"00": { "acronym": "00", "name": "00",          "types": []               }
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
		return choice(list(dict.keys()))

	def _find_bew_index(self, user, id):
		data = user['bews']
		for i in range(len(data)):
			if data[i]['bewId'] == id:
				return i # return index
		return None # Doesn't exist

	def _generate_bew_image(self, race, personality, color):
		race_db = self.db.bews.find_one({ '_id': str(race) }, {'face'})
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

	def summon(self, register=False, db=None):
		genre = choice(['M', 'F', 'H', 'X'])
		personality = self._random_key(self.personalities_dict) # Pegar keys e escolher uma aleatoriamente
		color =  self._random_key(self.color_dict) + str(randint(0, 3))
	
		race = list( self.db.bews.find({ '_id': randint(1, self.db.bews.count_documents({}) - 1) }))[0]
		types = [choice(race['types']), choice(race['types'])]
		
		# types = [self._random_key(self.types_dict), self._random_key(self.types_dict)]

		# Skill
		skills = ['00', '00', '00']
		if(random() <= 0.8): # 80%
			skills[0] = self._random_key(self.skills_dict)

			if(random() <= 0.5):
				skills[1] = self._random_key(self.skills_dict)

				if(random() <= 0.3):
					skills[2] = self._random_key(self.skills_dict)



		# Status and Tier
		ATK = '{:02d}'.format(randint(0, 15)) # :02d ->  01, 02, etc
		SPD = '{:02d}'.format(randint(0, 15))
		ACC = '{:02d}'.format(randint(0, 15))
		RST = '{:02d}'.format(randint(0, 45))
		STATUS = [ATK, SPD, ACC, RST]
		tier = '{:02d}'.format( int( ((int(ATK) + int(SPD) + int(ACC)) / 7 ) + (int(RST) / 13) + (3 - skills.count('00')) ) )
		
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
		image = self._generate_bew_image(race['_id'], personality, color)

		# Return
		return {
			'id': bew_id,
			'tier': tier,
			'race': race['name'],
			'height': '%sm' % (1 - (0.12 - int(tier)/100)),
			'genre': genre,
			'personality': personality,
			'color': color,
			'types': types,
			'skills': skills,
			'status': {
				"ATK": ATK,
				"SPD": SPD,
				"ACC": ACC,
				"RST": RST
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
		personality = bewId[0:3]
		color       = bewId[9:11]
		types       = bewId[11:15]
		skills      = bewId[15:21]
		status      = bewId[21:]

		race   = list( self.db.bews.find({ '_id': bewId[3:6] }) )[0]
		image  = self._generate_bew_image(race['_id'], personality, color)

		return {
			"id": bewId,
			"personality": self.personalities_dict[personality],
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
				"RST": status[6:],
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
		if ibew == None or ibew2 == None: # Não da pra usar not porque se for 0 (index 0) conta como False
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

	def query_team(self, user, team: list):
		player_team = []
		user = self.db.users.find_one({'_id': ObjectId(user) }, {'bews', 'cards'}) # Return only bews field
	
		if not user:
			return response_code('400', 'User doesn\'t exist')

		for bew_id in team:
			bew_index = self._find_bew_index(user, bew_id)

			if bew_index == None:
				return response_code('400', 'Bew %s doesn\'t exist' % bew_id)
			else:
				bew_object = user['bews'][bew_index]
				bew_object.update( self.query_bew_id(bew_id) )
				player_team.append( bew_object )



		return player_team



		

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
-> self.db.users.update_one({'discordId': '333333'}, {'$pull': {'bews': {'bewId': 'AAA'}}})

EDIT OBJECT INSIDE ARRAY
bews": [
	{
		"name": "baba",
		"bewId": "AAA",
		...
	}
]
new = {"name": "bebe", "bewId": "BBB", ...}

-> self.db.users.update_one({'discordId': '333333'}, {'$set': {'bews.INDEX': new } })
	(one field only) -> self.db.users.update_one({'discordId': '333333'}, {'$set': {'bews.INDEX.name': 'raimundin' } })


"""









"""
Algumas coisas para corrigir mais tarde
- 5w3 tecnicamente transmite debuff também, não diretamente, mas se tiver um debuff de 10 pontos e um buff de 20, tracvhjk
nsmitir vai passar 10 (a diferença)
	- Transmitir também não passa viad
				self.handle_skill('NEXT', [bew.team[0]])
- Reproduzir não passa vida

"""


class Logs:
	def __init__(self):
		self.temp_logs = []
		self.logs      = []

	def add_log(self, text):
		self.temp_logs.append(text)

	def pass_turn(self):
		self.logs.append(self.temp_logs)
		self.temp_logs = []

logs = Logs()
class Skills:
	def __init__(self):
		self.skills = {
			'NEW-BEW': {
				'E1': self.esvair,
				'I1': self.imunidade,
				'S1': self.soberano,
				'P3': self.profundo
			},

			'BEW-DIED': {
				'R3': self.reproduzir
			},

			'COMBAT': {
				'H1': self.hiperativo
			},

			# Tecnicamente podem ser ativados a qualquer momento depois do combate, mas como tem relação com combate achei melhor separar
			'AFTER-COMBAT': {
				'R2': self.rigidez,
				'R1': self.retorno,
				'S2': self.sob_pressao,
				'M1': self.manufatura,
				'S3': self.sucata,
				'F1': self.fluxo,
				'D1': self.dissolver,
				'A1': self.assassino,
				'B1': self.brilhante,
				'E2': self.emocional
			},

			'PRE-NEXT': {
				'C1': self.controle

			},

			'NEXT': {
				'T1': self.transmitir
			},


			'FINAL': {
				'L1': self.leve,
				'P1': self.poesia,

				# Marcadores
				'P2': self.paixao,
				'V1': self.veneno,
				'O1': self.oculto
			}
		}

		self.enabled_esvair = []


	def handle_skill(self, event: str, bews: list):
		for bew in bews: # This loop exists because "bews" can be one or more bews
			for skill in bew.skills:
				func = self.skills[event].get(skill)
				if func:
					logs.add_log('- Skill Usada -> %s em %s usou %s' % (bew['name'], event, skill))
					func(bew)


	def soberano(self, bew): # Ignora a redução de dano do omega, dobra a chance de crítico.
		"""
		Essa habilidade não precisa rodar aqui
		Roda em _calc_type_modifier e quando seta o crítico do bew
		"""
		pass


	def sob_pressao(self, bew): # Aumenta o atq em 50% e a SPD em 3 pts se estiver com 1/4 ou menos de RST.
		if bew.life == 0.25 * int(bew.original['status']['RST']) and bew.opponent.item != 'Pena':
			bew.atk *= 1.5
			bew.spd += 3


	def controle(self, bew): # Não permite que o oponente passe.
		bew.opponent.next = False


	def retorno(self, bew): # 1/4 de chance de retornar o dano que recebe por um ataque. 
		if random() <= 0.25:
			bew.deal_damage(bew.opponent, bew.taked_damage)


	def transmitir(self, bew): # Ao passar, os buffs vão para o BewBattle seguinte.
		"""
		Essa habilidade não roda aqui
		Roda no end_turn()
		"""
		pass


	def manufatura(self, bew): # Aumenta o ataque em 10% a cada acerto
		if bew.opponent.taked_damage:
			bew.atk *= 1.10


	def sucata(self, bew): # Sucata recupera 1/4 de RST se chegar em 1/5 uma vez por batalha.
		if bew.life < int(bew.original['status']['RST']):
			bew.life = bew.life * 1.20

			if 'Caminhão de Lixo' in bew.responses:
				bew.life += bew.life / 2
				bew.remove_response('Caminhão de Lixo')
			bew.skills.remove('S3') # Remover pra não poder usar de novo


	def rigidez(self, bew): # Devolve 1/16 de todo dano que recebe
		if bew.taked_damage:
			bew.deal_damage(bew.opponent, bew.taked_damage * 0.0625)


	def leve(self, bew): # Aumenta em1 pt de SPD por turno
		bew.spd += 1


	def fluxo(self, bew): # A cada ataque correto aumenta em 3pts o ACE.
		if bew.opponent.taked_damage:
			bew.acc += 3

	def esvair(self, bew): # Sempre que o BewBattle oponente entrar em campo diminua o ACC dele em 10 pts.
		"""
		O efeito não é causado aqui
		É causado no trigger de NEW-BEW
		Aqui vai adicionar e quando um bew entrar, na função de new_bew() vai checar se self.esvair tem algo (se tiver é porque alguém acionou)
		"""
		if bew.player_name not in self.enabled_esvair:
			self.enabled_esvair.append(bew.player_name)

	def dissolver(self, bew): # A cada dano causado recupera de vida 30% do valor do dano
		if bew.opponent.taked_damage:
			bew.life += bew.opponent.taked_damage * 0.3


	def poesia(self, bew): # 1/3 de chance por turno de retirar todos os debuffs e buffs .
		if random() <= 0.33:
			for stat in bew.status:
				if stat == 'RST':
					continue
				bew.status[stat] = int(bew.original['status'][stat])


	def emocional(self, bew): # Ganha 20% de ataque e resistencia para cada aliado derrotado.
		for _ in range( 4 - len(bew.team) ): # Se nenhum foi derrotado, o array vai estar com len 4, então o for não vai ser executado e etc
			bew.atk *= 1.20
			bew.life *= 1.20


	def hiperativo(self, bew): # 1/4 de chance de ganhar um ataque extra no turno.
		if random() <= 0.25 and bew.opponent.life > 0: # Não atacar se oponente já estiver morto
			bew.deal_damage(bew.opponent, physical_damage=True, count_acc=True)


	def assassino(self, bew): # Ganha 30% de atq para cada oponente que ele derrotar.
		# This will run in COMBAT, so this can be possible
		if bew.opponent.life <= 0:
			bew.life *= 1.30


	def paixao(self, bew): # 1/3 de deixar o seu oponente com marcador de amor ao atacar (amor faz seu oponente sempre atacar por ultimo)
		self.marker(bew, 'P2')

	def veneno(self, bew): # 1/3 de deixar um marcador de veneno no oponente ao atacar (veneno tira 8% de RST no fim de cada turno).
		self.marker(bew, 'V1')

	def oculto(self, bew): # 1/3 de deixar um marcador de medo no oponente ao atacar (medo tira 3 pts de acerto do oponente a cada turno)
		self.marker(bew, 'O1')

	def marker(self, bew, marker: str):
		marker_chance = 0.66 if bew.item == 'Cajado' else 0.33

		# Random chance / Is not immune / Do not have a marker
		if random() <= marker_chance and not bew.opponent.marker:
			bew.opponent.marker = marker


	def imunidade(self, bew): # Não pode ser colocado marcadores
		bew.marker = 'IMMUNITY'

	def profundo(self, bew): # Ignora efeito de itens. tanto seus quanto dos oponentes
		"""
		Roda em set_opponent
		"""
		pass



	# Está funcionando aparentemente
	def reproduzir(self, bew): # Ao ser derrotado, cria um clone com metade dos status e sem habs.
		if bew.life <= 0:
			clone = deepcopy(bew)
			clone.skills = ['00', '00', '00']
			for stat in bew.status:
				clone.status[stat] = round(int(bew.original['status'][stat]) / 2, 2)
			clone.bew['name'] = '%s\'s Copy' % clone['name']
			bew.team.append(clone)

	def brilhante(self, bew): # Após cada vitória você ganha 50% de Rewbs a mais.
		if bew.defeated:
			bew.rewbs_to_earn += bew.rewbs_to_earn if bew.item == 'Cálice' else bew.rewbs_to_earn * 0.5


class Responses:
	def __init__(self):
		self.responses = {
			'COMBAT': {
				'Falência': self.falencia,
				'Adestramento': self.adestramento,
				'Exorcismo': self.exorcismo,
				'Maquinofatura': self.maquinofatura
			},

			'PRE-NEXT': {
				'Estilingue': self.estilingue
			},

			'RESULTS': {
				'Mina': self.mina
			}
		}



	def handle_response(self, event: str, bews):
		for bew in bews: # This loop exists because "bews" can be one or more bews
			for response in bew.responses:
				func = self.responses[event].get(response)
				if func:
					logs.add_log('- Resposta Usada -> %s em %s usou %s' % (bew['name'], event, response))
					# print(f'- Reposta usada -> {bew.bew["name"]} em {event} usou {response}\n')
					func(bew)


	def agrotoxico(self, bew): # Quando um Bew do brasão Rosas entrar em campo, coloque um marcador de veneno dele
		"""
		Roda na checagem de quando um bew morre e quando vai passar
		"""
		pass

	def falencia(self, bew): # Quando um Bew do brasão Fortuna atacar um Bew amarelo, tire metade do RST atual dele
		if 'FO' in bew.types and bew.opponent['color']['color'] == 'YELLOW':
			bew.opponent.life /= 2
		bew.remove_response('Falência')

	def adestramento(self, bew): # Quando seu Bew do tipo fera fizer um ataque inefetivo, cause 300% de dano
		if 'BE' in bew.types and bew.opponent.taked_damage == 0.001:
			print("adestramento", bew.opponent.taked_damage)
			bew.deal_damage(bew.opponent, bew.atk * 3)
		bew.remove_response('Adestramento')


	def coroacao(self, bew): # Quando um Bew do Brasão rei chegar a menos de 1/4 de RST, tome os brasões do Bew oponente em [Rei, Rei]
		if 'KI' in bew.types:
			bew.opponent.types = ['KI', 'KI']
		bew.remove_response('Coroação')

	def espelho(self, bew): # Quando um bew receber debuff, os debuff recebidos também são colocados no oponente
		"""
		Roda em calc_debuff
		"""
		pass

	def caminhao(self, bew): # Quando seu bew ativar a habilidade sucata, recupera 1/2 do RST a mais
		"""
		Roda na habilidade de sucata
		"""
		pass

	def mina(self, bew): # Se um Bew do brasão fortuna estiver consciente em sua equipre durante a vitória, você ganah 50% de rewbs
		"""
		Como os bews que vão rodar aqui são só os que ganharam, da pra fazer um checagem individual
		"""
		if 'FO' in bew.types:
			bew.rewbs_to_earn *= 1.5
		# print(bew)
		# for bw in bew.team:
		# 	if 'FO' in bw.types:
		# 		bew.rewbs_to_earn *= 1.5


	def exorcismo(self, bew): # Quando um Bew do brasão Mistério atacar, ele sofre o dano do próprio ataque
		damage = bew.taked_damage

		if 'MI' in bew.types:
			target = bew
		elif damage and 'MI' in bew.who_attacked.types:
			target = bew.who_attacked
		else:
			return
		target.deal_damage(target, damage)
		bew.remove_response('Exorcismo')

	def maquinofatura(self, bew): # Quando um Bew oponente com hab manufatura atacar um Bew de brasão Engrenagem, os Bews com brasão de Engrenagem dobram seu ataque
		if bew.taked_damage and 'GE' in bew.types:
			bew.atk *= 2
			bew.remove_response('Maquinofatura')

	def estilingue(self, bew):
		if bew.opponent.next:
			bew.deal_damage(bew.opponent, bew.atk * 0.33)


class Maps:
	def __init__(self):
		self.bercario_stats = []

		self.academia_runned, self.lamacal_runned = False, False # Quando um bew entrar em campo
		self.bercario_run_again, self.hospital_run_again, self.pista_run_again = 2, 2, 2 # Turno sim, turno não

		# Os que estão aqui são os que eu testei
		self.maps_map = {
			'Berçário': self.bercario,
			'Manicômio': self.manicomio,
			'Hospital': self.hospital,
			'Academia': self.academia,
			'Pista': self.pista,
			'Céu': self.ceu,
			'Fábrica': self.fabrica,
			'Lamaçal': self.lamacal,
			'Cassino': self.cassino
		}


	def handle_map(self, bews):
		for bew in bews:
			func = self.maps_map[bew.map]
			if func:
				logs.add_log('- Mapa Usado -> %s usou %s' % (bew['name'], bew.map))
				func(bew)

	def reset_values(self):
		self.academia_runned, self.lamacal_runned = False, False # Quando um bew entrar em campo

	def bercario(self, bew): # ATIV: Turno sim, turno não; EFT: O Bew com maior rank em batalha tem seus status cortados pela metade até o final do turno.
		higher = bew if bew.tier > bew.opponent.tier else bew.opponent

		self.bercario_run_again -= 1

		if bew.tier == bew.opponent.tier or self.bercario_run_again > 0: # Já rodou
			return

		self.bercario_stats = [] # Por que fazer assim invés de dobrar a vida atual? Proque comoa  divisão pode não ser exata, ao dobrar os status eles podem ficar maior ou menores do que o valor original
		
		for stats in bew.status:
			mod = bew.status[stats] / 2

			higher.deal_debuff(stats, mod)
			self.bercario_stats.append(mod)

		self.bercario_run_again = 4

	def ceu(self, bew): # ATIV: Enquanto o seu time só tiver Bews de brasão Nuvem e/ou Estrela; EFT: Seus Bews não erram ataques;
		count = 0
		for bw in bew.team: # Bew team
			if 'CL' in bw.types or 'ST' in bw.types:
				count += 1

		# Count = len(player) -> Todos os bew na equipe são nuverm e/ou estrela
		for bw in bew.team:
			bw.acc = 100 if count == len(bew.team) else int(bw.original['status']['ACC'])

	def cassino(self, bew): # ATIV: Enquanto o seu time só tiver Bews de rank 7; EFT: No começo da batlha todos os seus bews ganham 7pts de buff em todos os status;
		count = 0
		for bw in bew.team: # Bew team
			if bw.tier == 7:
				count += 1

		# Count = len(player) -> Todos os bew na equipe são nuverm e/ou estrela
		if count == len(bew.team): 
			for bw in bew.team:
				for stats in bw.status:
					bw.status[stats] += 7

	def hospital(self, bew): # ATIV: Turno sim, turno não; EFT: O Bew com menor quantidade de RST em campo recupera 12% de RST atual;
		bew = bew if bew.life < bew.opponent.life else bew.opponent
		
		self.hospital_run_again -= 1 # Decrease counter, when reach 0, run
		if bew.life == bew.opponent.life or self.hospital_run_again > 0:
			return

		bew.life += round(0.12 * bew.life, 2)
		self.hospital_run_again = 4 # Reset counter

	def manicomio(self, bew): # ATIV: Continuo; EFT Os Bews com pers insano tem 50% de chance de passar no segundo turno.
		"""
		Está rodando no match case de next
		"""
		pass

	def academia(self, bew): # ATIV: Se nenhum Bew em campo for azul; EFT: Todos os Bews em campo ganham um buff 4pts em atq ao entrar em campo (tanto os seus quanto os do oponente)
		if (bew['color']['color'] != 'AQUA' and bew['color']['color'] != 'DARKBLUE')  and  (bew.opponent['color']['color'] != 'AQUA' and bew.opponent['color']['color'] != 'DARKBLUE') and not self.academia_runned:
			bew.atk          += 4
			bew.opponent.atk += 4
			self.academia_runned = True

	def pista(self, bew): # ATIV: Turno sim, turno não; EFT: A SPD e o atq dos Bews são trocados.
		self.pista_run_again -= 1

		if self.pista_run_again > 0:
			return

		bew.atk, bew.spd = bew.spd, bew.atk
		bew.opponent.atk, bew.opponent.spd = bew.opponent.spd, bew.opponent.atk

		self.pista_run_again = 4

	### Não sei se é exatamente isso que a habilidade tem que fazer
	def fabrica(self, bew): # ATIV: Se todos os Bew na sua equipe forem engrenagem; EFT: Bews de engrenagem causam dano normal aos inefetivos.
		count = 0
		for bw in bew.team: # Bew team
			if 'GE' in bw.types:
				count += 1

		# Count = len(player) -> Todos os bew na equipe são engrenagem
		for bw in bew.team:
			bw.ineffective = [] if count == len(bew.team) else bw.original['ineffective']

	def lamacal(self, bew): # ATIV: Se nenhum Bew em campo for tsunami; EFT:Todos os Bews são considerados com 10pts de SPD
		if 'TS' not in bew.types and 'TS' not in bew.opponent.types and not self.lamacal_runned:
			bew.spd          = 10
			bew.opponent.spd = 10
			self.lamacal_runned  = True





map_class = Maps() # As classes de Battle e BewBattle usam, não, não da pra fazer elas serem Chield do Map, porque senão o BewBattle criaria várias instancias dessa classe e pra funcionar precisa só de uma
class BewBattle:
	def __init__(self, bew, player):
		self.response_class = Responses() # Handle responses
		self.skill_class    = Skills() # Handle skills

		self.handle_response = self.response_class.handle_response
		self.handle_skill    = self.skill_class.handle_skill
		self.enabled_esvair  = self.skill_class.enabled_esvair


		# Used to set effeciency and inefficiency
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

		self.bew      = bew
		self.status   = self.bew['status'] # Simplify
		self.original = deepcopy(bew) # Eu fiquei HORAS da minha vida até descobrir que .copy não copia sub-list e que precisa usar o deepcopy pra isso (como deque não possui deepcopy por padrão, precisa importar)
	
		# Var that changes
		self.next                = False
		self.defeated            = False
		self.taked_attack_damage = [None, None]

		# Other things
		self.types       = [ typ['acronym'] for typ in self.bew['types'] ] # Type format (preferi fazer isso aqui porque se eu precisar das outras informações por qualquer motivo que seja, eu já vou ter)
		self.personality = self.bew['personality']
		self.skills      = [ skill['acronym'] for skill in self.bew['skills'] ]
		self.tier        = int(self.bew['tier'])


		# Setar pela classe de Battle
		self.object          = { 'team': None, 'globals': { 'rewbs': 25, 'map': None } }
		# self.team            = self.object[0]['team']
		
		self.player          = player
		self.player_name     = self.player['_id']


		self.critical_chance = 0.10 if 'S1' in self.skills else 0.05
		self.opponent        = None # Very useful
		self.new             = True


		self.map        = "Cassino"
		self.responses    = [ 'Agrotóxico', 'Falência', 'Mina' ]



		# Convert to int to counts be simpler
		for stat in self.status:
			self.status[stat] = int(self.status[stat])

		# Set types
		self.effective = []
		self.ineffective = []

		# Push effectives and ineffectives types
		for ty in self.types:
			chart = self.types_chart[ty]

			### Ajeitar isso depois, (Ps.: não sei como, e não, não é só effective = chart[0], porque como são dois tipos, ao fazer isso com o segundo vai dar overwrite)
			[self.effective.append(t) for t in chart[0]]
			[self.ineffective.append(t) for t in chart[1]]
		self.original['ineffective'] = self.ineffective
		self.original['effective']   = self.effective



	def __getitem__(self, value):
		return self.bew.get(value)

	@property
	def team(self):
		return self.object['team']
	@team.setter
	def team(self, new_team: Deque):
		self.object['team'] = new_team

	@property
	def rewbs_to_earn(self):
		return self.object['globals']['rewbs']
	@rewbs_to_earn.setter
	def rewbs_to_earn(self, new_rewbs_to_earn):
		self.object['globals']['rewbs'] = new_rewbs_to_earn

	@property
	def map(self):
		return self.object['globals']['map']
	@map.setter
	def map(self, new_map):
		self.object['globals']['map'] = new_map


	@property
	def acc(self):
		return self.status['ACC']
	@acc.setter
	def acc(self, new_acc):
		self.status['ACC'] = new_acc

	@property
	def atk(self):
		return self.status['ATK']
	@atk.setter
	def atk(self, new_atk):
		self.status['ATK'] = new_atk

	@property
	def life(self):
		return self.status['RST']
	@life.setter
	def life(self, new_life):
		self.status['RST'] = new_life

	@property
	def spd(self):
		return self.status['SPD']
	@spd.setter
	def spd(self, new_spd):
		self.status['SPD'] = new_spd


	@property
	def taked_damage(self):
		return self.taked_attack_damage[0]

	@property
	def who_attacked(self):
		return self.taked_attack_damage[1]

	def _item_status(self):
		match self.item:
			case 'Osso':
				self.life += 6
			case 'Capa':
				self.spd *= 1.20
			case 'Cálice':
				self.critical_chance *= 4
			case 'Adaga':
				self.atk +=  6


	def _calc_damage(self, target, count_acc=True):
		type_modifier = 0
		for ty in target.types:
			if ty in self.effective:
				type_modifier += 1

			if ty in self.ineffective and not 'S1' in target.skills: # If have S1 do not count ineffective
				type_modifier -= 1

		critical = True if random() <= self.critical_chance else False
		damage = ((self.atk + ((self.atk * 0.2) * type_modifier)) * 0**critical ) + (critical * 2 * self.atk)

		if count_acc:
			### Só para debug
			damage = damage if random() <= self.acc/100 else 0.001 # O dano arrendounda para 2 casas decimais, então 0.001 vai virar 0.0 e assim é um jeito de saber quando um ataque errou
			
			if damage == 0.001:
				logs.add_log("%s errou o ataque" % self['name'])

		return damage

	def _new_bew(self):
		"""
		Everything that need to run when a NEW-BEW is added
		"""

		if self.bercario:
			print(map_class.bercario_stats)

			self.atk  += map_class.bercario_stats[0]
			self.spd  += map_class.bercario_stats[1]
			self.acc  += map_class.bercario_stats[2]
			self.life += map_class.bercario_stats[3]

			map_class.bercario_stats = []
			self.bercario = False

		if ('RO' in self.types) and (self.opponent) and ('Agrotóxico' in self.opponent.responses): # self.opponent check -> porque essa função roda logo após criar o bew
			self.marker = 'V1'
			self.opponent.remove_response('Agrotóxico')


		self.marker = None
		map_class.reset_values()
		# map_class.academia_runned, map_class.lamacal_runned = False, False


		self.handle_skill('NEW-BEW', [self])
		##
		# If player2 activated esvair and player1 not / If both activated
		# esvair = [1]    # False ( 1 not in esvair  -> False and len == 1         )
		# esvair = [2]    # True  ( 1 not in esvair  -> True  and len == 1 -> True )
		# esvair = [1, 2] # True  ( False or len > 2 -> True                       )
		##
		if (self.player_name not in self.enabled_esvair and len(self.enabled_esvair) == 1) or (len(self.enabled_esvair) > 1):
			logs.add_log("%s sofreu debuff do agrtotóxico e ficou com ACC: %s" % (self['name'], self.calc_debuff(self.acc-10) ))
			self.deal_debuff('ACC', self.acc - 10)


	def set_opponent(self, opponent):
		if not self.team:
			raise TypeError('Você precisa setar o time antes disso') 

		self.opponent = opponent
		if self.new: # This things can only run if there is a opponent set
			# Status stuff
			self.profundo = self.bew['item'] if 'P3' in self.skills else False # Cópia pra devolver o item depois
			self.item     = self.bew['item'] if not self.profundo or not self.opponent.profundo else None
			self._item_status()

			# Cards things
			self.debuff_mod = 0.5 if self.item == 'Sino' else 1
			self.bercario   = False

			self._new_bew()



	def remove_response(self, response):
		self.responses.remove(response)

	def calc_debuff(self, debuff):
		return debuff / self.debuff_mod

	def deal_debuff(self, stats, debuff, target=None):
		target = self if not target else target
		debuff = self.calc_debuff(debuff)

		if 'Espelho' in self.responses:
			target.opponent.status[stats] = debuff
			self.remove_response('Espelho')

		target.status[stats] = debuff



	def reset_values(self):
		"""
		Reset values each turn
		"""
		# self._type_power_sei_la_que_nome_por_aqui_fodase() # Por causa do mapa
		self.taked_attack_damage = [None, None]
		self.dealt_damage        = 0
		self.next                = False
		self.new                 = False
		self.defeated            = False

		if not self.profundo and not self.opponent.profundo:
			self.item, self.profundo = self.profundo, False


	def deal_damage(self, target, damage: int | float | None=None, physical_damage=False, count_acc=False, trigger=False):
		"""
		Deals damage at a target

		The difference between this and attack(), this do not triggers a skill event
		"""

		if self.life <= 0:
			# print(self['name'], 'está morto e não pode atacar\n\n')
			return

		damage = self._calc_damage(target, count_acc=count_acc)
		if physical_damage:
			target.taked_attack_damage = [ damage, self ]
		target.life = round(target.life - damage, 2)

		if trigger:
			self.handle_skill('COMBAT', [self])
			self.handle_response('COMBAT', [self])
		
		logs.add_log("%s causou %s em %s \n%s ficou com RST: %s" % (self['name'], damage, target['name'], target['name'], target.life) )
		
		# Die if needed
		if target.life <= 0:
			target.die()
			self.defeated = True


	def rotate(self):
		"""
		Go to next bew
		"""
		self.handle_skill('NEXT', [self])


		## Acho que esse é o melhor jeito de se fazer isso
		if 'T1' in self.skills and len(self.team) > 1: # Ao passar os buffs vão para o bew seguinte
			new_bew = self.team[1]
			for stats in self.status:
				if stats == 'RST':
					continue
				new_bew.status[stats] += int(self.original['status'][stats]) - self.status[stats] # Se tiver diferença é um status

		self.team.rotate(-1) # -1 = [1, 2, 3] -> [2, 3, 1]
		self._new_bew()

	def die(self):
		"""
		Suicide
		"""
		self.handle_skill('BEW-DIED', [self])

		self.team.popleft() # Se fosse um array comum seria pop(0)
		logs.add_log('-> %s morreu' % self['name'])


class Battle:
	def __init__(self, player1: list, player2: list):
		self.handle_response = Responses().handle_response # Handle responses
		self.handle_skill = Skills().handle_skill # Handle skills

		# Init
		self.player1, self.player2 = deque( player1 ), deque( player2 )
		self.bews_alive = []

		self.turn = 1

	def update(self):
		# Values that might change each turn
		self.left, self.right  = self.player1[0], self.player2[0]        # Left, Right
		self.left.team, self.right.team = self.player1, self.player2     # Team

		self.left.set_opponent(self.right)
		self.right.set_opponent(self.left)

	def beggining(self):
		self.update()

		# print("Turno: ", self.turn)

		left, right = self.left, self.right
		attacker, defender = None, None

		logs.add_log('Time 1: %s' % ', '.join([bew['name'] for bew in [player for player in self.player1]]) )
		logs.add_log('Time 2: %s' % ', '.join([bew['name'] for bew in [player for player in self.player2]]) )

		# Decidindo quem vai atacar primeiro
		if left.status['SPD'] > right.status['SPD']:
			attacker, defender = left, right

			# Love marker
			if left.marker == 'P2':
				attacker, defender = right, left
		elif left.status['SPD'] < right.status['SPD']:
			attacker, defender = right, left

			# Love marker
			if right.marker == 'P2':
				attacker, defender = left, right
		else:
			attacker, defender = sample([left, right], 2) # Isso vai ordenar o array de forma aleatória

			# Attacker pass, if defender has love, it doesn't matter at all
			if attacker.marker == 'P2':
				attacker, defender = defender, attacker

		self.attacker, self.defender = attacker, defender
		self.bews_alive              = [self.attacker, self.defender]

		map_class.handle_map([self.attacker, self.defender])


		logs.add_log(f"\nAttacker: {self.attacker['name']} \nATK: {self.attacker.atk}/{self.attacker.original['status']['ATK']} \nRST: {self.attacker.life}/{self.attacker.original['status']['RST']} \nSPD: {self.attacker.spd}/{self.attacker.original['status']['SPD']} \nACC: {self.attacker.acc}/{self.attacker.original['status']['ACC']}")
		logs.add_log(f"\nDefender: {self.defender['name']} \nATK: {self.defender.atk}/{self.defender.original['status']['ATK']} \nRST: {self.defender.life}/{self.defender.original['status']['RST']} \nSPD: {self.defender.spd}/{self.defender.original['status']['SPD']} \nACC: {self.defender.acc}/{self.defender.original['status']['ACC']}")

	def combat(self):
		# Attack each other
		self.attacker.deal_damage(self.defender, physical_damage=True, count_acc=True, trigger=True)
		self.defender.deal_damage(self.attacker, physical_damage=True, count_acc=True, trigger=True)

		self.handle_skill('AFTER-COMBAT', [self.attacker, self.defender])

		# If died remove from alives
		# Pode não parecer mas isso é muito útil e ajuda muito
		[ self.bews_alive.remove(bew) for bew in self.bews_alive if bew.life <=0 ]
		


		# Passar ( "Rodar" é um nome melhor :P )
		# If is not turn 2 or higher, do not check for personalities
		if self.turn >= 2:
			for bew in self.bews_alive:
				match bew.personality:
					case 'ALE': # Se a resistência chegar a 3/4
						if bew.life <= 0.75 * int(bew.original['status']['RST']):
							bew.next = True
					case 'ATR': # Se derrotar um oponente
						if bew.opponent.life <= 0:
							bew.next = True
					case 'COR': # Nunca passa
						pass
					case 'CUR': # Se a resistência chegar em 1/4
						if bew.life <= 0.25 * int(bew.original['status']['RST']):
							bew.next = True
					case 'INS': # 25% de chance
						chance = 0.5 if bew.map == 'Manicomio' else 0.25
						if random() <= chance:
							bew.next = True
					
					case 'MED': # Se o oponente tiver mais porcentagem de resistência (porcentagem??)
						if bew.opponent.life > bew.life:
							bew.next = True

					case 'VIO': # Se deixar o oponente com metade da resistencia, força o oponente a passar
						if bew.opponent.life < int(bew.opponent.original['status']['RST']) / 2:
							bew.opponent.next = True



		# Esse precisa ser executado depois
		if self.attacker.personality == 'RAN' and self.defender.next:
			self.attacker.next = True
		elif self.defender.personality == 'RAN' and self.attacker.next:
			self.defender.next = True


	def end_turn(self):
		# Pass bews that can
		self.handle_response('PRE-NEXT', self.bews_alive)
		self.handle_skill('PRE-NEXT',  self.bews_alive)
		for bew in self.bews_alive:
			# Change before next
			if bew.next: # Life check because even if bew is dead, its value stills stored
				logs.add_log("-> %s passou com %s"  % (bew['name'], bew.personality))
				bew.rotate()
				logs.add_log("<- %s chegou"  % bew['name'])

				self.handle_skill('NEW-BEW', [bew.team[0]])


		if self.player1 and self.player2:
			self.handle_skill('FINAL', [self.attacker, self.defender])

			# Markers effects and reset_valuies
			for bew in self.bews_alive:
				match bew.marker:
					case 'V1':
						bew.deal_debuff('RST', bew.life * 0.08)
					case 'O1':
						bew.deal_debuff('ACC', bew.acc - 3)
				bew.reset_values()

			self.turn += 1
			logs.pass_turn()

	def start_battle(self):
		while self.player1 and self.player2:
			self.beggining()
			self.combat()
			self.end_turn()

		# RESULTS
		winner = self.player1 if len(self.player2) == 0 else self.player2
		loser  = self.player1 if len(self.player1) == 0 else self.player2

		self.handle_response('RESULTS', winner)
		print('Ganhador time', self.player1)
		print('Loser time', self.player2)
		print(winner[0].responses)

		print(f"\n\nPlayer {winner[0]['name']} ganhou com o time")
		print([idk['name'] for idk in [player for player in winner]])

		# if winner[0].map == 'Mina':
		# 	for bew in winner.team:
		# 		if 'FO' in bew.types:
		# 			bew.rewbs_to_earn

		print(f"Player {winner[0]['name']} ganhou {winner[0].rewbs_to_earn + (winner[0].defeated * 0.5)} Rewbs e {15*len(winner)} EXPs")
		print(f"\nPerdedor perdeu {10*len(winner)} EXPs")

		# return winner[0]['name'] + ' ganhou'
		return logs.logs
