# BEWS
## Os bews possuem propriedades: 
### Fixas:
- id
- rank
- raça
- sexo
- personalidade
- cor
- brasão
- habilidades
- ataque
- velocidade
- acerto
- resistencia

### Alteráveis:
- nome
- imagem
- felicidade
- equipamento

> **As váriaveis fixas só são alteradas conforme o efeito das cartas **durante a batalha**, após a batalha as fixas permanecem estáticas.*

## Geração dos Bews
O id do bew é definido pela junção das suas propriedades fixas, exemplo:
O id "INS001H12C1KISWS1S20015120645", significa que o bew tem:
- "INS" ou seja personalidade Insana
- "001" a raça dele é a 001
- "H" sexo hermafrodita
- "12" ele tem rank 12
- "C1" dentre as variações de cor ele é a C1 (C é vermelho e 1 de intensidade)
- "K1SW" ele tem os brasões "KI" (King) e "SW" (Sword)
- "S1S200" tem as habilidades S1 e S2. 00 é o placeholder
- "15120645" significa 15 de ataque, 12 de velocidade, 6 de acerto e 45 de resistencia

> **Todo o bew é básicamente seu id, as informações váriaveis ficam salvas no objeto do user, de resto o bew não terá o objeto salvo no banco de dados, apenas o seu id e as Aletráveis. Para saber as caracteristicas de um bew deve se converter por uma classe pelo id.*

# =-=-=-=-=-=-=-=-= CONSTRUÇÃO =-=-=-=-=-=-=-=-=