# Batalha
A batalha consiste em uma combate automático entre os bews. O user não decide as ações durante o conflito, ele apenas se encarrega de montar a equipe antes do confronto em si.

## Regras básicas:
- Cada user deve ter no máximo 4 bews em campo.
- É uma conflito 1x1 entre os bews, caso um seja derrotado ou recue, vem o seguinte. (Estilo pokemon e super auto pets)
- O mais rápido ataca primeiro, e em certos casos, ataca mais de uma vez.
- Ataques podem ser efetivos ou não efetivos dependendo dos tipos dos bews. Caso um ataque seja efetivo o dano aumenta em 20%, caso não efetivo o dano diminui em 20% (Vibe pokemon)
- A chance de dano crítico é de 5%, o dano crítico causa o dobro do dano e ignora se é efetivo ou não.
- Quando um Bew passa, ele entra na ultima posição do time, e ele só pode passar se tiver passado por dois turnos da luta em campo.
- Cada personalidade tem um comportamento diferente para passes.

## Regras avançadas:
- A batalha é divida em 3 fases, construção, turnos e resultado.
- O turno é divido em 3 etapas, inicial, combate e final.
- As cartas item tem seu efeito no final da **fase de construção**.
- As cartas mapas tem seu efeito durante a **etapa inicial**.
- Os marcadores (veneno, medo, paixão) tem efeito executado na **etapa final**.
- As cartas resposta podem ser ativadas durante qualquer momento da batalha, exceto na **fase de resultado**
- As habilidades podem ser ativadas durante qualquer momento da batalha.
- Um bew só pode ter um contador por vez, e ao passar ele perde o contador que tem.

# Funcionamento

Fase de Construção -> pega os objetos dos bews e põem numa filinha.

Fase de Turnos:  
- Etapa inicial -> Só é importante pra efeitos de cartas e habilidades.
- Etapa de combate -> os bews trocam dano, depois q os dois baterem a etapa passa.
- Etapa final -> Olha quem quer passar e recomeça outro turno.  

Fase de Resultado -> Dá os rewbs e exp pra quem ganhou e tira exp de quem perdeu.

##Contrução
Primeiro de tudo monta o campo, ordena os bews de acordo com a posição deles no objeto do user para ambos os jogadores, ou seja, o primeiro bew do array de bews no objeto do user também será o primeiro da fila. Enquanto ordena eles vai pegar o objeto base deles convertendo pelo bewId, e com o objeto base em mão irá adicionar certas propriedades: 
```json 
  "counter": "", 
  "original_status": {
  }, 
  "types_chart": {
    "effective":[],
    "ineffective":[]
  }, 
  "critcal_chance": 5, 
  "field_turns": 0,
```

> envent_log
