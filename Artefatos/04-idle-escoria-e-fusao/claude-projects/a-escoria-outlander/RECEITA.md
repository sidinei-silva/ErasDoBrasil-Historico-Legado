# A Receita

> Como se trabalha neste projeto. Se você voltar depois de um mês sem tocar, leia só isto.

## As cinco peças

| Peça | O que é | Vive onde | Muda? |
| --- | --- | --- | --- |
| **Regra** | o quê o jogo faz. Numerada, testável | `gdd/` | sim — vira regra nova |
| **Prosa** | por quê, tom, ficção. Não testável | `gdd/` | quando der vontade |
| **Spec** | como esta entrega acontece | `specs/` | **morre no fim** |
| **Teste** | a regra, executável | junto do código | não desincroniza |
| **ADR** | por que decidimos assim | `docs/adr/` | **nunca** — só nova |

Só a spec é efêmera. Só a ADR é imutável.

---

## Passo 1 — Escrever a regra no GDD

**Quando:** antes de qualquer código. Se não há regra escrita, não há o que construir.

**Como:** abra o arquivo do sistema em `gdd/sistemas/`. Se não existir, crie. Separe prosa de
regra fisicamente.

```markdown
# Têmpera

A arma esquenta com uso. Trocar é largar o metal antes da hora — não destrói
nada, mas apaga o forno. É o que faz presença valer mais que calendário.

## Regras

- **R-TEM-01** — sobe apenas com ação ativa da arma equipada
- **R-TEM-02** — congela offline: não sobe nem decai
- **R-TEM-03** — reseta ao valor base quando a arma equipada muda
- **R-TEM-04** — multiplica ganho de Fama; não altera dano
```

**O teste que separa regra de prosa:**

> *"O Guia parou perto do T8 por medo"* → prosa. Não testável, e não deve ser.
> *"Têmpera reseta na troca"* → regra. Numerada, testável.

**Cuidado com o falso terceiro tipo.** "Nome entre 3 e 20 caracteres" **não é regra de jogo** —
é validação de software. Não ganha ID, não vai pro GDD. Vive na spec da entrega.

Pergunta que decide: *se eu trocasse Go por Rust e web por mobile, isso continuaria valendo?*
Sim → regra. Não → encanamento, fica na spec.

---

## Passo 2 — Escrever a spec da entrega

**Quando:** quando as regras que ela implementa já existem.

**Tamanho:** uma entrega que você consegue **terminar e demonstrar**. Se não couber em um bloco
de trabalho seu, quebre em duas. "Criação de personagem" é uma spec. "Fatia 1" não é.

**Como:** um arquivo em `specs/`, quatro seções. As regras são **citadas, nunca reescritas**.

```markdown
# S-003 · Criação de personagem

## Regras que esta entrega implementa
- R-JOG-01 — o jogador tem um nome escolhido por ele
- R-JOG-02 — o jogador está sempre em exatamente uma zona
- R-JOG-03 — jogador novo nasce em A Ressaca

## Comportamento de software
Não é regra de jogo; é o que o GDD nunca vai dizer.

- Nome entre 3 e 20 caracteres, com erro visível ao usuário
- Recarregar a página mantém o jogador logado e na zona correta
- Nome vazio não cria jogador

## Como demonstro que funcionou
- Informo um nome, confirmo, e vejo a tela de A Ressaca
- Recarrego a página e continuo lá
- Tento confirmar vazio e vejo o erro

## Fora de escopo
- Executar ações na zona — S-004
- Inventário, equipamento, Fama
```

**Escopo negativo não é opcional.** É ele que impede a entrega de inchar.

---

## Passo 3 — Escrever os testes, falhando

**Quando:** antes do código. O teste é a spec deixando de ser texto.

**Como:** cada regra citada vira ao menos um teste que **nomeia o ID**.

```
Test_R_JOG_03_JogadorNovoNasceEmARessaca

  // DADO   nenhum jogador existente
  // QUANDO  crio um jogador chamado "Sidinei"
  // ENTÃO   a zona atual dele é A Ressaca
```

O comportamento de software também vira teste, mas **sem ID** — não é regra do jogo.

Rode. Tem que falhar. Se passar sem código, o teste está errado.

---

## Passo 4 — Escrever o código

Até os testes passarem. Nada além disso.

Se você precisar de uma decisão que a spec não responde — como estruturar, onde validar, que
biblioteca — **decida você**. É por isso que a spec para no comportamento.

Se a decisão for **arquitetural e difícil de reverter**, anote para o Passo 5.

---

## Passo 5 — Fechar

Quatro coisas, nesta ordem:

**1. Regra descoberta volta pro GDD.**
Construindo, você vai esbarrar em algo que ninguém decidiu: *"e se a zona sumir do JSON?"*
Isso é regra nova. Escreve no GDD com ID novo, escreve o teste. **Não pode morrer com a spec.**

É assim que o GDD cresce: por descoberta, não por antecipação.

**2. Decisão relevante vira ADR.**

```markdown
# ADR-014 — Sessão por cookie assinado, não token no cliente

**Data:** 2026-08-20
**Status:** aceita

## Contexto
A PoC não tem autenticação real, mas o jogador precisa sobreviver a um refresh.

## Decisão
Cookie de sessão assinado pelo servidor.

## Consequência
O cliente não guarda identidade. Quando a autenticação real entrar, troca-se o
conteúdo do cookie sem mexer nas outras rotas. Custo: não funciona para um
cliente nativo depois, e aí precisará de outra ADR.

## Regras afetadas
nenhuma
```

**ADR nunca é editada.** Mudou de ideia? ADR nova, com `Status: substitui ADR-014`. A antiga
fica, com `Status: substituída por ADR-021`. O histórico é o valor.

**3. A spec morre.** `git mv specs/S-003-criacao-personagem.md specs/arquivo/`
Ela não é mantida, não é sincronizada, não é lida de novo. Cumpriu a função.

**4. Um commit com tudo.** Regra, teste, código, ADR. Junto.

---

## Onde cada coisa mora

```
gdd/
├── sistemas/          um arquivo por sistema que tem REGRAS
│   ├── tempera.md         R-TEM-*
│   ├── litania.md         R-LIT-*
│   ├── loadout.md         R-LOD-*
│   ├── jogador.md         R-JOG-*
│   ├── zonas.md           R-ZON-*
│   └── tutorial.md        R-TUT-*
├── mundo/             prosa: geografia, facções, cosmologia
├── narrativa/         prosa: enredo, personagens, tom
└── README.md          índice de sistemas e prefixos

specs/
├── S-003-criacao-personagem.md      ativa
├── S-004-tela-de-zona.md            ativa
└── arquivo/                         mortas, nunca mais lidas

docs/adr/
├── ADR-001-litania-tres-camadas.md
└── ADR-014-sessao-por-cookie.md

data/                 as instâncias: zonas, mobs, armas, diálogos
server/  web/         código e testes
```

**Por sistema, não por funcionalidade.** Um sistema é algo com regras próprias que outros
sistemas consultam. O prefixo do ID espelha o arquivo — achar regra vira `grep R-TEM`.

**Arquivo de sistema é curto.** Prosa em parágrafos, regras em lista. Se passar de duas telas,
provavelmente são dois sistemas.

---

## Convenções

| | Formato | Exemplo |
| --- | --- | --- |
| Regra | `R-<SISTEMA>-<NN>` | `R-TEM-03` |
| Spec | `S-<NNN>-<slug>` | `S-003-criacao-personagem` |
| ADR | `ADR-<NNN>-<slug>` | `ADR-014-sessao-por-cookie` |

Numeração sempre cresce, nunca é reaproveitada. Regra aposentada some do GDD, mas o número
não volta a ser usado.

---

## Regras de bolso

**Regra sem teste é decoração.** Se não vale um teste, não vale um ID — é prosa.

**Não escreva spec para o óbvio.** Ajustar um número, adicionar item ao JSON, corrigir texto:
vai direto ao código. Spec existe para reduzir incerteza; onde não há incerteza, é cerimônia.

**Se escrever a spec demora mais que fazer a coisa, não escreva a spec.**

**Nunca reescreva uma regra na spec.** Cite o ID. Duplicou, dessincronizou.

**Se não há regra para citar, a entrega não está pronta para começar.** Volte ao Passo 1.

**Uma spec por vez.** Duas abertas significa que nenhuma vai fechar.

---

## Verificação

Um script que cruza os IDs do `gdd/` com os dos testes:

- **Regra sem teste** → ou é decoração, ou é buraco
- **Teste com ID inexistente** → a regra sumiu, o teste ficou órfão

Escreva quando tiver umas quinze regras. Antes disso, o olho dá conta.

O que ele **não** verifica: se o texto da regra diz o mesmo que o teste afirma. Isso é humano —
mas o modo de falha encolhe de "desync silencioso em qualquer lugar" para "editaram uma regra e
não mexeram no teste dela".

---

## O ciclo, inteiro

```
    ┌─────────────────────────────────────────┐
    │                                         │
    ▼                                         │
  GDD ──cita IDs──► SPEC ──vira──► TESTES ──► CÓDIGO
 (regras)         (efêmera)      (permanentes)  │
    ▲                 │                         │
    │                 ▼                         │
    │              arquivo/                     │
    │                                           │
    └──── regra descoberta ─────────────────────┤
                                                │
                          ADR ◄── decisão ──────┘
                       (em pedra)
```

**Morre:** a spec.
**Fica:** regra, teste, código, ADR.
**Sincronização manual:** nenhuma.

---

## Por onde começar hoje

Se você está na primeira vez, faça exatamente nesta ordem — e só isto:

1. Crie `gdd/sistemas/jogador.md` e `gdd/sistemas/zonas.md`. Escreva **três regras em cada**,
   lendo do Notion. Não migre o resto ainda.
2. Escreva `specs/S-001-criacao-personagem.md` no template acima.
3. Escreva os testes. Rode. Veja falhar.
4. Escreva o código até passarem.
5. Feche: spec para `arquivo/`, ADR se houve decisão, um commit.

Terminou o ciclo uma vez. Agora você sabe o que a receita significa, e pode discordar dela com
fundamento.
