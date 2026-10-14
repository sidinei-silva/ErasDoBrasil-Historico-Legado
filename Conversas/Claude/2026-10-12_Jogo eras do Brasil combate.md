## Sidinei:

Estou fazendo esse jogo: https://github.com/sidinei-silva/eras-do-brasil

Veja as regras de combate https://github.com/sidinei-silva/eras-do-brasil/blob/b365e32c1add767e9efcc144d12573b186b9ef2b/docs/mecanicas/combate.md

Neste exato momento estou escrevendo o core, e criado os tipo, estou fazendo o tipo de configs da luta quero deixar configuravel quantas linhas paralelas vai ter a luta e quantas casas de movimento vai ter. E mais alguns tipo quais nomes deu para a variaveis?

---

## Claude:

Li as regras de combate. Seguem os nomes que eu usaria, em inglês (é o padrão mais comum em código), com o motivo de cada um para você decidir.

## As duas que você pediu

**Filas → `laneCount`**
"Lane" é o termo usado em jogos para uma fila paralela onde as coisas andam em linha reta, como em Plants vs Zombies ou nas lanes de MOBA. Eu evitaria `rows` e `lines`. `row` sugere uma grade genérica em que você anda em qualquer direção, e no seu jogo ninguém muda de fila andando. `line` é ambíguo demais.

**Casas de movimento → `laneLength`**
Seu doc já chama cada casa de "passo", então a unidade é *step*. A posição dentro da fila fica `step`, e o tamanho da fila fica `laneLength`. Outra opção é `stepsPerLane`, que é mais explícito, mas fica mais longo. Prefiro `laneLength` porque se lê como uma propriedade da lane.

Com isso, a posição de alguém na área de combate fica `{ lane, step }`. Evite `x/y`: além de genérico demais, você vai confundir qual eixo é qual na hora de calcular distância.

## Outros valores do doc que valem virar config

| Nome | Vem de qual regra |
|---|---|
| `oppositeLanePenalty` | "Fila oposta soma +1" na distância |
| `stepsPerTurn` | Movimento comum de 1 passo por turno |
| `playerStartLane` / `playerStartStep` | Jogador começa na fila central, no canto esquerdo |
| `rangedPointBlankPenalty` | Dano que a arma à distância perde colada no alvo (ainda em aberto, ótimo candidato a config) |
| `turnTimeLimitMs` | PvP tem limite de turno. No PvE fica `null`, que comunica "sem limite" melhor que `0` |
| `fleeChanceMin` / `fleeChanceMax` | Piso e teto da chance de fuga |
| `fleeProtectionDurationMs` | Tempo protegido depois de fugir |

## Dois problemas que a configurabilidade cria

**1. "Fila central" e "fila oposta" só fazem sentido com 3 filas.** Com `laneCount = 4` não existe centro, e com 5 a ideia de "oposta" fica vaga. Você tem dois caminhos:
- Calcular a partir da regra: centro é `floor(laneCount / 2)` e a penalidade passa a ser por diferença de filas, algo como `laneDiff > 1 ? penalty : 0`. Nesse caso o nome vira `farLanePenalty` ou `laneCrossPenalty`.
- Validar que `laneCount` é ímpar e manter a regra como está.

Decida isso antes de nomear, porque o nome da penalidade depende da regra.

**2. Não guarde a fila central como config.** `playerStartLane` costuma ser derivado de `laneCount`. Se virar um campo à parte, os dois podem ficar inconsistentes (`laneCount: 3, playerStartLane: 4`). Prefira um campo opcional que, se ausente, cai no centro calculado, ou uma função.

## Sobre organização

Eu separaria em dois tipos: um que descreve o **terreno** (`BattlefieldConfig`, com `laneCount`, `laneLength`, posições iniciais) e outro com as **regras** (`CombatRulesConfig`, com penalidades, fuga, tempo de turno). O terreno pode variar por encontro (um boss numa arena maior, por exemplo), enquanto as regras variam por modo (PvE, PvP). Misturar os dois te obriga a duplicar regras toda vez que quiser um mapa diferente.

Em que linguagem está o core? Se for Go, os nomes mudam um pouco por causa da convenção de exportação, como `LaneCount` em vez de `laneCount`.

---

## Sidinei:

Isso faz sentido?


```typescript
type CombatState = {
  combatants: Combatant[];
  battlefieldConfig: BattlefieldConfig;
  combatConfig: CombatConfig;
  currentTurn: number;
  battlefield: {
    lanes: {
      [laneIndex: number]: {
        positions: (Combatant | null)[];
      };
    };
  };
};

```

---

## Claude:

Faz sentido na intenção, mas tem um problema estrutural e alguns ajustes menores.

## O principal: duas fontes da verdade

Hoje o mesmo combatente aparece em dois lugares: no array `combatants` e dentro de `positions`. Quando ele anda, você precisa atualizar os dois. Quando ele morre, também. Na primeira vez que esquecer um dos lados, o grid vai dizer que tem alguém numa casa onde o combatente já não está, e esse tipo de bug é chato de achar.

A saída mais simples é a posição ser um dado **do combatente**: cada `Combatant` tem `lane` e `step`, e o grid deixa de existir no estado. Quando você precisar saber "quem está na casa X?" (para bloqueio, por exemplo), calcula a partir da lista. Com 3 filas e poucos inimigos, percorrer o array é barato e não justifica manter uma estrutura paralela.

Se mais tarde quiser o grid por performance ou conveniência, faça ele guardar **ids**, não o objeto, e trate como índice derivado, reconstruído a partir dos combatentes, nunca editado direto.

## Ajustes menores

**`lanes` como objeto com chave numérica.** `{ [laneIndex: number]: ... }` é um array com ergonomia pior: você perde `.length`, `.map` e a garantia de que os índices são contínuos. E o wrapper `{ positions }` não acrescenta nada. Se mantiver o grid, um array de arrays basta.

**`currentTurn` é ambíguo.** Pelo doc, cada combatente age na sua vez, em ordem de iniciativa. Então existem duas coisas diferentes:
- o **round**, um contador que sobe quando todo mundo agiu;
- **de quem é a vez agora**, que precisa da ordem sorteada mais um índice ou id.

Isso importa já: o doc diz que o cooldown "diminui a cada turno". Você vai ter que decidir se é a cada round ou a cada vez do próprio combatente, e o estado precisa ter as duas informações para isso funcionar.

**Configs dentro do estado.** Pode ficar, e tem uma vantagem real: o estado vira autocontido, e você consegue serializar, reproduzir ou fazer replay de uma luta sem depender de nada externo. Só tenha claro que esses dois campos nunca mudam durante a luta. O resto do estado é o que muda.

## O que vai faltar logo

Sem precisar resolver agora, mas o doc já cobra:
- se o jogador fez alguma ação manual, porque isso muda o preço da morte;
- o loot acumulado na luta, que se perde na fuga.

Quer mandar o `Combatant` depois? A decisão de onde fica a posição pesa mais lá do que aqui.

---
