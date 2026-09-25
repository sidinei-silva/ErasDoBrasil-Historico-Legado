## Sidinei:

Você está me ajudando a importar o contexto de um assistente de IA para outro. Seu trabalho é analisar nossas conversas anteriores e resumir o que você sabe sobre mim.
Na resposta, evite usar pronomes na primeira pessoa (eu, meu, minha, me) e na segunda pessoa (você, seu, sua). Em vez disso, use "o usuário" ou outro termo neutro para se referir ao indivíduo com essas características.
Preserve as palavras do usuário ao pé da letra sempre que possível, especialmente para instruções e preferências.
Categorias (resposta nesta ordem):
1. Informações demográficas: como gosto que me chamem, profissão, formação acadêmica e local onde moro.
2. Interesses e preferências: coisas com que me envolvo de modo ativo e contínuo, não apenas um objeto que eu tenho ou uma compra que fiz uma vez.
3. Relacionamentos: relacionamentos confirmados e de longo prazo.
4. Eventos, projetos e planos: um registro de atividades recentes e significativas.
5. Instruções: regras que pedi explicitamente para você seguir, como "sempre faça X", "nunca faça Y" e correções no seu comportamento. Inclua apenas regras de dados de memória armazenados, não de conversas.
Formato:
Divida o conteúdo em seções rotuladas usando as categorias acima. Tente incluir citações de comandos meus que justifiquem cada resposta. Estruture cada item usando este formato:
* O nome do usuário é <name>.
    *Evidência: o usuário disse "me chame de <name>". Data: [YYYY-MM-DD].
Saída:
– Formate o resumo final como um bloco de texto.

---

## Claude:

---

```
## 1. Informações Demográficas

* O nome do usuário é Sidinei.
  Evidência: nome mencionado recorrentemente nas conversas e confirmado na memória do sistema.

* O usuário reside em Senhor do Bonfim, Bahia, Brasil.
  Evidência: dado de localização do sistema.

* O usuário trabalha como desenvolvedor fullstack sênior na empresa GamersClub (GC).
  Evidência: memória do sistema confirma "Sidinei is a fullstack senior developer working at GamersClub."

* Formação acadêmica: não há registro de dados sobre formação.

---

## 2. Interesses e Preferências

* O usuário está aprendendo Go de forma ativa e contínua por meio de um projeto pessoal.
  Evidência: memória registra "He is learning Go through the project."

* O usuário tem interesse ativo em pixel art e estética retro.
  Evidência: memória registra "interest in pixel art aesthetics."

* O usuário usa o Google Meet com virtual backgrounds temáticos.
  Evidência: memória registra criação de prompts de pixel art para Google Meet.

* O usuário participa ativamente do design e desenvolvimento de um MMORPG pessoal chamado "Eras do Brasil".
  Evidência: memória registra envolvimento contínuo desde julho de 2023.

---

## 3. Relacionamentos

* Nenhum relacionamento pessoal confirmado e de longo prazo foi registrado nas conversas ou na memória.

---

## 4. Eventos, Projetos e Planos

* O usuário está desenvolvendo solo um MMORPG de fantasia histórica chamado "Eras do Brasil", baseado na história do Brasil com sistema D20, desde julho de 2023.
  Evidência: memória descreve o projeto com 12 classes, 3 origens (Indígena, Colonial, Folclórica), full loot on death, StoryManager com eventos globais, IA de NPCs com rotinas e necessidades, e economia de crafting/lifeskills.

* O servidor do jogo é um monolito em Go com goroutines, EventBus com channels e persistência RAM-first com SQLite, definido via ADRs.
  Evidência: memória do sistema.

* O usuário configurou um ambiente WSL 2 completo do zero: Oh My Zsh com Powerlevel10k, plugins (zsh-vi-mode, zsh-autopair, zsh-completions), ferramentas modernas de CLI (eza, bat, fzf, zoxide, lazygit, lazydocker, k9s, delta, gh, yazi, btop, tlrc, direnv) e mise para gerenciamento de versões.
  Evidência: memória do sistema.

* O usuário avaliou e confirmou que manter o GitHub Copilot Student gratuito junto ao Claude Pro pago é o setup ideal para o seu fluxo de trabalho atual.
  Evidência: memória e conversa de abril de 2026 sobre tradeoffs de tooling de IA.

* O usuário mantém identidades Git e chaves SSH separadas para trabalho (GC) e projetos pessoais. GPG commit signing configurado com key ID 31B3FFB8BADC479C.
  Evidência: memória do sistema.

* O projeto "Eras do Brasil" está dividido em três repositórios (eras-do-brasil-gdd, eras-do-brasil-game e um arquivo legado), decisão arquitetural deliberada motivada por limites de token, necessidades de contexto de IA distintas e restrições de tooling.
  Evidência: memória do sistema.

---

## 5. Instruções

* "O objetivo absoluto desta interação é a verdade, o raciocínio lógico e a análise rigorosa. Aja como um analista crítico, direto e puramente objetivo: é estritamente proibido concordar comigo apenas para me agradar, ser polido ou validar minhas ideias sem embasamento."
  Evidência: conversa de março de 2026 sobre migração de preferências do Gemini para o Claude.

* "Se eu apresentar uma premissa falha, afirmar algo incorreto ou tomar uma decisão enviesada, aponte o erro imediatamente."
  Evidência: mesma conversa, março de 2026.

* "Sempre que eu sugerir uma opção, apresente primeiro os pontos negativos, as desvantagens e os possíveis furos lógicos."
  Evidência: mesma conversa, março de 2026.

* "Ao comparar ferramentas, mecânicas de jogos ou metodologias, não declare um 'vencedor absoluto' ou 'a melhor escolha para mim': liste as falhas e limitações técnicas de cada opção primeiro, de forma categorizada, e deixe a decisão final a meu cargo."
  Evidência: mesma conversa, março de 2026.

* "Se faltarem informações cruciais para uma análise rigorosa, não faça suposições — exija os dados faltantes antes de gerar uma resposta final."
  Evidência: mesma conversa, março de 2026.

* "Remova qualquer tipo de introdução, saudação, pedido de desculpas ou conclusão genérica. Inicie a resposta diretamente no cerne da questão e entregue os dados brutos."
  Evidência: mesma conversa, março de 2026.

* O usuário instrui a não misturar contextos de vida distintos: "Nunca use minha profissão ou rotina de trabalho para justificar, analisar ou criar analogias sobre meus hobbies."
  Evidência: userPreferences desta conversa.

* O usuário instrui que comentários de código em Go gerados por IA devem ser evitados; prefere explicações via chat para aprender padrões idiomáticos.
  Evidência: memória do sistema.

* Para o Project do "Eras do Brasil" no Claude, o usuário definiu uma persona de Game Designer sênior crítico e não-bajulador como system prompt.
  Evidência: conversa de abril de 2026 sobre configuração de Projects.

* O usuário prefere sincronização manual de repositórios com o Claude (via upload manual ou output do Repomix), dado que o GitHub sync do Claude Projects foi considerado não confiável.
  Evidência: memória do sistema.
```

---
