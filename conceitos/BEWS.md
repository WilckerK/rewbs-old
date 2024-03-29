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
- tipos
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
O id "INS-001-H-12-C1-KISW-S1S200-15120645", significa que o bew tem:
- "INS" ou seja personalidade Insana
- "001" a raça dele é a 001
- "H" sexo hermafrodita
- "12" ele tem tier 12
- "C1" dentre as variações de cor ele é a C1 (C é vermelho e 1 de intensidade)
- "K1SW" ele tem os tipos "KI" (King) e "SW" (Sword)
- "S1S200" tem as habilidades S1 e S2. 00 é o placeholder
- "15120645" significa 15 de ataque, 12 de velocidade, 6 de acerto e 45 de resistencia

> - **Todo o bew é básicamente seu id, as informações váriaveis ficam salvas no objeto do user, de resto o bew não terá o objeto salvo no banco de dados, apenas o seu id e as Aletráveis. Para saber as caracteristicas de um bew deve se converter por uma classe pelo id.*<br>
> - **DB para armazenar IDs para fazer query**
#

### Tier
"O tier é o quão forte um bew é", é um calculo feito após os dados do bew estiverem prontos, sendo:  
```((ataque + velocidade + acerto) / 7) + (resitencia / 13) + quantidadeDeHabilidades```  
O resultado dessa conta sempre resultará entre 0 a 12. O tier também e responsável pela tamanho do bew, sendo 0 o menor e 12 o maior.

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
A personalidade influencia no rosto dele. E na interação que eles irão ter sobre passar.
- **INSANO**: 25% de chance de passar a cada turno.
- **ALEGRE**: A resistencia dele chegar em 3/4 ele passa.
- **CORAJOSO**: Fica até o final.
- **MEDROSO**: Se o oponente tiver mais porcentagem de resistencia que ele, ele passa.
- **ATREVIDO**: Se derrotar um oponente, ele passa passa.
- **CUIROSO**: Se a resistÊcia chega a 1/4 ele passa
- **RANCOROSO**: Se o oponente passar ele também passa
- **VIOLENTO**: Se ele deixar o oponente com metade da resistencia força o oponente a passar.

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

### Types

Existem 18 tipos no total, cada bew possui dois tipos e cada carta possuí um tipos.  
[Tipos Conceito](https://github.com/WilckerK/rewbs/blob/main/conceitos/TIPOS.md)


#

### Habilidades
Cada bew pode ter entre 0 a 3 habilidades, elas interagem durante a batalha. As habilidades tendem a ser referentes ao tipos na hora da invocação, por exemplo, um bew do tipos "RO" (Roses), vir com as habilidades paixão e emocional. 

#

### Status
Os status são os pontos adicionais que cada bew tem que vai ser acrescentado ao status base. Por exemplo: Um bew com 12 pontos em ataque teria efeticamente 22 pontos durante a batalha, sendo 10 (base) somado a 12 (pontos adicionais).
- **Ataque** (0 a 15): Quanto de força esse bew tem. Status base: 10.
- **Velocidade** (0 a 15): O bew mais rápido ataca primeiro, caso um bew tenha o dobro da velocidade do oponente ele bate duas vezes, o triplo três vezes, etc. Status base: 10.
- **Acerto** (0 a 15): A chance que um bew tem de acerto adicional. Status base: 80.
- **Resistência** (0 a 45): Quanto ele tem de vida antes de ser nocauteado.  Status base: 80.

#

### Nome
O bew vem com um nome aleatório, mas o user deve conseguir alterar o nome dele.

#

### Imagem
A imagem ficará guardada em BASE64 e deve ser convertida na hora de mostrar ao user.

#

### Felicidade
O bew perde felicidade após perder batalhas e conforme o tempo passa, o user pode aumentar a felicidade de formas variadas. 

#

### Item
Cada bew poderá segurar uma carta de item que o afetará durante as batalhas.

## Variações visuais dos bews:
- **Raça**: Cada raça tem sua forma base definida.
- **Cor**: Sendo 8 cores diferentes e 4 variações de intensidade de cada.
- **Rosto**: Cada personalidade é referente a um rosto, totalizando 8.
- **Tamanho**: O tamanho do bew é referente ao seu rank, quanto maior o rank, maior o bew será.
