# BEWS
**Esse arquivo é uma overview do [Planilha dos Bews](https://docs.google.com/spreadsheets/d/1JtYD7HOH2AdcL9KxdH-sBE2PINgIFIMStCfiCNTYXjk/edit#gid=0) sobre os mesmos.*
## Os bews possuem propriedades: 
### Fixas:
As propriedades fixas são geradas durante o "nascimento" do bew e não podem ser alteradas, exceto **durante** as batalhas, após o término da batalha as propriedades fixas retornam ao que eram antes.

- id
- tier
- raça
- sexo
- personalidade
- cor
- brasão
- habilidades
- ataque, velocidade, acerto, resistencia

### Alteráveis:
As propriedades Alteráveis podem ser alteradas pelo user, ele pode ter a opção de escolher qual item seu bew irá segurar, ou até mesmo o nome do bew.

- nome
- imagem
- felicidade
- item

> **As váriaveis fixas só são alteradas conforme o efeito das cartas **durante a batalha**, após a batalha as fixas permanecem como estavam antes da batalha.*

## Geração dos Bews (Por Invocação)
### Id
O id do bew é definido pela junção das suas propriedades fixas, exemplo:
O id "INS001H12C1KISWS1S20015120645", significa que o bew tem:
- "INS" ou seja personalidade Insana
- "001" a raça dele é a 001
- "H" sexo hermafrodita
- "12" ele tem tier 12
- "C1" dentre as variações de cor ele é a C1 (C é vermelho e 1 de intensidade)
- "K1SW" ele tem os brasões "KI" (King) e "SW" (Sword)
- "S1S200" tem as habilidades S1 e S2. 00 é o placeholder
- "15120645" significa 15 de ataque, 12 de velocidade, 6 de acerto e 45 de resistencia

> **Todo o bew é básicamente seu id, as informações váriaveis ficam salvas no objeto do user, de resto o bew não terá o objeto salvo no banco de dados, apenas o seu id e as Aletráveis. Para saber as caracteristicas de um bew deve se converter por uma classe pelo id.*

#

### Tier
"O tier é o quão forte um bew é", é um calculo feito após os dados do bew estiverem prontos, sendo:
`((ataque + velocidade + acerto) / 7) + (resitencia / 13) + quantidadeDeHabilidades`
O resultado dessa conta sempre resultará entre 0 a 12. O tier também e responsável pela tamanho do bew, sendo 0 o menor e 13 o maior.

#

### Raça
As raças dos bews ficam salvas no banco de dados, ao gerar um bew se deve escolher uma raça aleatória entre elas. Eles são representados por 3 dígitos. (001, 002, ..., 045, ..., 245, etc...)

#

### Sexo
Os bews podem ter 4 váriações de sexo:
"M" para macho, "F" para fêmea, "H" para hermafrodita, "X" para assexuado.

Para haver a reprodução, bews de sexos opostos devem cruzar, sendo o hermafrodita capaz de se passar por qualquer papel e o assexuado incapaz de realizar qualquer reprodução.

#

### Personalidade
A personalidade influencia no rosto dele.
(Construção...)

#

### Cor
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

#

### Brasão
Existem 16 brasões no total, cada bew possui dois brasões e cada carta possuí um brasão.
| Sigla | Nome | Descrição |
| ------ | -------- | ------------- |
| **KI** | King | Rei, monarquia, poder político, chefe da tribo, reino, líder...
| **SW** | Sword | Espada, facas, armas brancas, guerra, violência, agressão, revolta...
| **MU** | Music | Musica, arte, melodia, harmonia, ordem, esculturas...
| **GE** | Gear | Engrenagem, máquinas, fábricas, armas de fogo, metal, robôs...
| **SM** | Smile | Sorriso, alegria, humor, juventude, inocencia...
| **GO** | Goodness | Bondade, benevolencia, anjelical, religioso, santo...
| **BO** | Book | Livro, conhecimento, estudos, psiquico, mental...
| **BE** | Beast | Besta, fera, animal, voraz, irracional...
| **RO** | Roses | Rosas, plantas, paixão, natureza, amor, sedução...
| **CA** | Catalyst | Catalizador, químico, mágico, intensificar, poções...
| **MI** | Mistery | Mistério, bruxaria, oculto, maligno, criminoso...
| **ST** | Star | Estrela, espaço, luz, planetas, divino, iluminado...
| **CL** | Cloud | Nuvem, voar, ar, ventos, clima, alto, leve...
| **CY** | Cyber | Cibernético, tecnologia, software, elétrico, moderno...
| **FO** | Fortune | Fortuna, dinheiro, capital, ouro, riquezas, ganâmcia...
| **AN** | Ancient | Ancião, velho, antigo, esquecido, desgastado, sábio...

#

### Habilidades
Cada bew pode ter entre 0 a 3 habilidades, elas interagem durante a batalha. As habilidades tendem a ser referentes ao brasão na hora da invocação, por exemplo, um bew do brasão "RO" (Roses), vir com as habilidades paixão e emocional. 

#

### Status
- **Ataque** (0 a 15): Quanto de força esse bew tem.
- **Velocidade** (0 a 15): O bew mais rápido sempre ataca primeiro, caso um bew tenha o dobro da velocidade de outro ele bate duas vezes, o triplo três vezes, etc...
- **Acerto** (0 a 15): A chance que um bew tem de acerto adicional.
- **Resistência** (0 a 45): Quanto ele tem de vida antes de ser nocauteado.

#

### Nome
O bew vem com um nome aleatório, mas o user deve conseguir alterar o nome dele.

#

### Imagem
A imagem ficará guardada em BASE64 e deve ser convertida na hora de mostrar ao user.

#

### Felicidade
O bew perde felicidade após perder batalhas e conforme o tempo passa, o user pode aumentar a felicidade de formas variadas.  
(Construção...)

#

### Item
Cada bew poderá segurar uma carta de item que o afetará durante as batalhas.


# =-=-=-=-=-=-=-=-= CONSTRUÇÃO =-=-=-=-=-=-=-=-=
