# Banco de Dados
As únicas informações salvas no banco de dados deve ser o objeto do user, como exemplificado no [Rewbs Readme](https://github.com/WilckerK/rewbs/blob/main/README.md#objeto-do-user), as raças dos bews e as cartas.
As informações dos bews devem ser retiradas do próprio id dele.

## Collections
### User: 
A collection de usuário deve conter as informações de todos as pessoas que se cadastrarem dentro de objetos. Exemplo de objeto do user: 
```json
{
	"_id": "lfhgolsnvoh8u494hfkjf466sh",
	"nome": "Iberê",
	"email": "manualdomundo@gmail.com",
	"senha": "3fw4fwrffwefsddff3aw2",
	"discordId": "34534536363456",
	"exp": 87987,
	"rewbs": 1340,
	"bews":[
		{
			"nome":"Rebew", 
			"bewId":"INS000H12C1REEPS1S2I115151545", 
			"feli": 100,
			"item": "Pena",
			"image": "adefeqjo8hfoeunfajldnfoeqhafunaefuiaegfyagdbjfhcaejbjlakelnflandhu=="
		},
		{
			"nome":"Myra", 
			"bewId":"CUR001F03G2ETFER3000002011502", 
			"feli": 75,
			"item": "",
			"image": "gjkjefgeqfsgsfgsgsfhjo8hgjfoegnfoeqhjkkgfyagdbjfhcaegjkgjjbjlasfghsu=="
		}
	],
	"cartas":{
			"resposta": ["Coroação", "Agrotóxico", "Coroação", "Adestrar"],
			"mapa": ["Berçário", "Mina"],
			"item": ["Adaga", "Livro"]
		}
}
```

### Bews:
Aqui se deve guardar os ids dos bews existentes e as raças, o primeiro registro (000) deve guardar todosos bews registrados, caso algum bew deixe de existir o id dele de ser deletado da lista. A collection de bews também deve guardar todas as raças de bews possiveis (001 em diante). Os objetos seguintes devem conter a imagem base da raça, o nome da raça, registro da raça e a posição onde o rosto de encontra.
```json
{
  "_id": "000"
  "bewsRegistrados": [
  	"INS000H12C1KISWS1S2I115151545",
  	"CUR001F03G2STBER3000002011502",
  	"ALE004X12D4CLCYB1000011071226",
  	"..."
  ]
},
{
  "_id": "001",
  "nome": "Psytal",
  "bras": ["KI", "SW"],
  "rosto": [100, 200],
  "imagem": "sfsgset4wrgsrkgjoush97fsg8yfbisugebfiy7sg86egfsiyebfi7ygefiku="
},
{
  "_id": "002",
  "nome": "Rulio",
  "bras": ["BE", "KI"],
  "rosto": [400, 80],
  "imagem": "sfadfadfarkgjoush97fsg8yfbisasfasfi7ygefiku="
},
"..."
```

### Cartas:
A de cartas deve conter o nome da carta, o tipo de carta e o efeito salvo em string.
```json
{
  "nome": "Agrotóxico",
  "tipo": "Resposta",
  "efeito":
}
```

#

<details> 
	<summary><b>LINK PARA CONECTAR AO BANCO DE DADOS</b></summary>
    <mark>mongodb+srv://API:VrxAzAus26iI3tas@cluster.yruie.mongodb.net/{NOMEDADATABASE}?retryWrites=true&w=majority</mark>
</details>


