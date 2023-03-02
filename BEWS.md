# BEWS
**Esse arquivo é uma overview do (Planilha dos Bews)[https://docs.google.com/spreadsheets/d/1JtYD7HOH2AdcL9KxdH-sBE2PINgIFIMStCfiCNTYXjk/edit#gid=0] sobre os mesmos.*
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

> **As váriaveis fixas só são alteradas conforme o efeito das cartas **durante a batalha**, após a batalha as fixas permanecem como estavam antes da batalha.*

## Geração dos Bews (Por Invocação)
### id
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

### rank
(Construção...)

### raça
As raças dos bews ficam salvas no banco de dados, ao gerar um bew se deve escolher uma raça aleatória entre elas. Eles são representados por 3 dígitos. (001, 002, ..., 045, ..., 245, etc...)

### sexo
Os bews podem ter 4 váriações de sexo:
"M" para macho.
"F" para fêmea
"H" para hermafrodita
"X" para assexuado

Para haver a reprodução, bews de sexos opostos devem cruzar, sendo o hermafrodita capaz de se passar por qualquer papel e o assexuado incapaz de realizar qualquer reprodução.

### personalidade
(Construção...)

###cor
Pode váriar entre 8 váriações, e cada variação existe 4 níveis de intensidade.
| Letra | Cor | Descrição |
| ------ | -------- | ------------- |
| **A** | Preto | Diminuir o brilho
| **B** | Branco | Aumentar o brilho
| **C** | Vermelho | RGB(alto, zero, zero)
| **D** | Amarelo | RGB(alto, alto, zero)
| **E** | Verde | RGB(zero, alto, zero)
| **F** | Ciano | RGB(zero, alto, alto)
| **G** | Azul | RGB(zero, zero, alto)
| **H** | Lilás | RGB(alto, zero, alto)

# =-=-=-=-=-=-=-=-= CONSTRUÇÃO =-=-=-=-=-=-=-=-=
