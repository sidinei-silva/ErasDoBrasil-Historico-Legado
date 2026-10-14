# Memória do Project do Claude — Eras do Brasil - Arquivado 2

Resumo e arquivos de memória que o Claude mantinha para este Project (export de 14/10/2026). É texto gerado pelo Claude a partir das conversas, não documento escrito pelo Sidinei.

## Arquivo de memória `/index.md` (atualizado 2026-09-14)

---
name: "Eras do Brasil"
description: Eras do Brasil
---

## Arquivo de memória `/ways-of-working.md` (atualizado 2026-09-25)

---
name: ways-of-working
description: Como o Sidinei trabalha neste projeto — o que ele espera das respostas e o que já está fechado como método
sources: [chat]
---

## O papel deste projeto

- [stated] Aqui ele estuda e projeta: arquitetura de servidor, balanceamento, game design e pesquisa histórica para conteúdo de era
- [stated] Não é onde o jogo é escrito. O código ele escreve à mão no repositório, lendo, entendendo e adaptando — muitas vezes com estrutura diferente da discutida. É intencional e é como ele aprende
- [stated] Em 21/09/2026: o Project Knowledge está com o conector de GitHub do repositório eras-do-brasil sincronizado (pastas backend/data/design/docs/tools), mas só da branch `main` e só quando ele aperta "Sincronizar" — não é automático a cada push. Branch fora da main não é coberta; precisa do link direto

## O que ele espera

- [stated] Ensinar, não entregar: arquitetura primeiro, depois responsabilidade de cada componente, depois o código, depois o fluxo. Nunca bloco grande sem explicação
- [stated] Código como exemplo pequeno e didático, que não serve para colar
- [stated] Ser corrigido quando estiver errado, sem concordância para agradar
- [stated] Nunca inferir: se não souber, pesquisar ou perguntar; hipótese tem que ser declarada como hipótese
- [stated] Sem complexidade antecipada — nada de Redis, Kafka, microserviço ou sharding por precaução
- [stated] É iniciante em Blender
- [stated] Entre 22 e 24/09/2026 reorganizou os docs (via ChatGPT) para o repositório ser a fonte única de verdade, independente de IA: a instrução de qualquer Project de IA só descreve comportamento e aponta para o repo, sem copiar conteúdo. Está decidindo em qual IA/Project continuar e pensa em usar Sonnet em vez de Opus pelo custo
- [stated] Em 21/09/2026, após gostar do formato de resposta ajustado, decidiu incluir na instrução do Project duas regras novas: diagrama pequeno por ideia (não um grande só no fim) e resposta do tamanho da pergunta (não reabrir a arquitetura inteira para dúvida pontual)

## Regras de método fixadas

- [stated] Decisão registrada é decisão: antes de reabrir algo fechado, dizer o que mudou. Ele tende a revisitar as mesmas questões e isso lhe custa semanas
- [stated] Arquitetura definitiva em escala reduzida, nunca desenho descartável "porque é PoC"
- [stated] Material feito com IA vale como mockup ou brainstorm, nunca texto final; o que sobreviver é reescrito por ele
- [stated] Toda constante de jogo mora em arquivo de dados, nunca em código; servidor e simulador leem o mesmo arquivo
- [stated] Não poetizar mecânica: nome de sistema usa termo comum de MMORPG. Item e habilidade podem ter nome próprio; mecânica não. E nome de sistema global não pode vir de uma era nem de uma facção, já que o jogo tem várias

## Vocabulário morto

- [stated] Não existem mais: Lastro, panteões e deuses dentro de armas, gank por adjacência, as zonas A Ressaca/A Bigorna/O Verde Surdo/A Costela, combate D20, e as classes como classes. Se aparecer em material antigo, é resíduo
- [stated] Termos renomeados em 14/09/2026, também resíduo se aparecerem: Litania (virou Árvore do Destino), Sopro (virou Essência), Têmpera (virou Afinidade), doutrina de combate (virou regras de combate), e as bandas de risco firme/trêmula/rachada (viraram segura/disputada/mortal, mais selvagem no continente 2)
