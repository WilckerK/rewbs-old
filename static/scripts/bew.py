import random
from flask_pymongo import ObjectId


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
			"KI" :["King",     ["EP","RE"],["ET","RO"],["SO","FO"], '👑', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558645349535884/1.png'],
			"SW" :["Sword",    ["FE","RO"],["LI","MI"],["MU","SO"], '⚔️', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558645781536868/2.png'],
			"MU" :["Music",    ["SO","MU"],["EP","EN"],["BO","ET"], '🎵', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558646259687475/3.png'],
			"GE" :["Gear",     ["CI","EP"],["NU","CA"],["FE","MU"], '⚙️', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558646754623559/4.png'],
			"SM" :["Smile",    ["BO","LI"],["RE","EP"],["NU","BO"], '🙂', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558755869425746/5.png'],
			"GO" :["Goodness", ["RE","MI"],["MU","SO"],["FE","CA"], '💚', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558756255318136/6.png'],
			"BO" :["Book",     ["FO","MU"],["FE","CI"],["EP","MI"], '📙', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558756607639763/7.png'],
			"BE" :["Beast",    ["AN","FE"],["BO","EN"],["LI","ET"], '🐾', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558757022875688/8.png'],
			"RO" :["Roses",    ["SO","NU"],["AN","FO"],["NU","RE"], '🌹', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831106863244/9.png'],
			"CA" :["Catalyst", ["ET","CI"],["CA","BO"],["EN","CA"], '⚗️', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831517900930/10.png'],
			"MI" :["Mistery",  ["CA","FO"],["LI","AN"],["CI","EP"], '🌑', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558831924748308/11.png'],
			"ST" :["Star",     ["MI","RO"],["FE","MU"],["AN","RE"], '🌟', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558832373542992/12.png'],
			"CL" :["Cloud",    ["EN","ET"],["SO","RO"],["AN","EN"], '☁️', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558922551070760/13.png'],
			"CY" :["Cyber",    ["NU","AN"],["CI","MI"],["CI","LI"], '📱', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558923054383154/14.png'],
			"FO" :["Fortune",  ["EN","BO"],["FO","RE"],["FO","RO"], '💰', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558923549311047/15.png'],
			"AN" :["Ancient",  ["LI","CA"],["ET","NU"],["MI","RO"], '⏳', 'https://cdn.discordapp.com/attachments/1030554748664946809/1030558924056825916/16.png']
		}

		self.skills_dict = {
			"S1": ["Soberano",    ['RE','AN']],
			"S2": ["Sob Pressão", ['RE','EP','ET']],
			"C1": ["Controle",    ['RE','EN','CI']],
			"R1": ["Retorno",     ['BO','CA','FO']],
			"T1": ["Transmitir",  ['BO','LI','CI']],
			"M1": ["Manufatura",  ['EN','LI','FO']],
			"S3": ["Sucata",      ['EP','EN']],
			"R2": ["Rigidez",     ['EN','ET','AN']],
			"L1": ["Leve",        ['RO','NU']],
			"F1": ["Fluxo",       ['MU','NU','CI']],
			"E1": ["Esvair",      ['MI','NU','FO']],
			"D1": ["Dissolver",   ['SO','CA','NU']],
			"P1": ["Poesia",      ['MU','LI']],
			"E2": ["Emocional",   ['SO','BO','RO']],
			"H1": ["Hiperativo",  ['SO','FE','ET']],
			"A1": ["Assassino",   ['EP','FE']],
			"P2": ["Paixão",      ['MU','RO','MI']],
			"V1": ["Veneno",      ['RO','CA','AN']],
			"O1": ["Oculto",      ['SO','AN','MI']],
			"P3": ["Profundo",    ['EP','MI','LI']],
			"R3": ["Reproduzir",  ['MU','BO','FE']],
			"I1": ["Imunidade",   ['RE','FE','CA']],
			"B1": ["Brilhante",   ['ET','CI','FO']]
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

	def _random_key(self, dict):
		return random.choice(list(dict.keys()))

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
			'id': f"{personality}-{race}-{genre}-{tier}-{color}-{''.join(brasoes)}-{''.join(skills)}-{''.join(STATUS)}",
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

	def trade_bews(self, data, db):
		user = db.users.find_one({'_id': ObjectId(data['userId']) })
		user2 = db.users.find_one({'_id': ObjectId(data['userId2']) })


		return {
			"user": user['name'],
			"user2": user2['name']
		}

