# 🧠 Estratégia de Dados e Documentação

> **Navegação:** [GDD](../README.md) · [Roadmap](02_Roadmap_Desenvolvimento.md) · [Schemas](../06_Dados_e_Assets/01_Schemas_Estruturais.md) · [Projeto](../../README.md)

Este documento define a filosofia de arquitetura de informação do projeto *Eras do Brasil*, estabelecendo como transformaremos conceitos (GDD) em código (Game).

## 1. Filosofia: "Alma vs. Lógica"

Para evitar o excesso de documentação morta ou a falta de contexto nos dados, adotamos o modelo híbrido:
> **"O Livro explica o PORQUÊ e o O QUÊ (Alma). O JSON define o QUANTO e o COMO (Lógica)."**

## 2. Classificação dos Documentos

### Grupo A: A Alma (100% Livro / 0% JSON)
*Documentos de leitura humana, inspiração e direção de arte.*
* **Enredo Principal & Lore:** História, tom, diálogos.
* **Design Visual:** Style guides, UI specs.
* **Regras Core (Conceitos):** Explicação teórica do Ciclo de Tempo, Mundo Vivo.

### Grupo B: O Híbrido (Livro Descritivo + JSON de Definição)
*Entidades que precisam de contexto narrativo E dados rígidos.*
* **Classes:**
    * *Livro (.md):* Descrição narrativa, papel na equipe, dicas de interpretação.
    * *Dados (.json):* `id`, `hp_base`, `atributos_bonus`, `lista_skills`.
* **Missões:**
    * *Livro (.md):* O drama, os diálogos, o fluxo narrativo.
    * *Dados (.json):* `id`, `gatilho_tick`, `recompensa_id`, `condicao_vitoria`.
* **Monstros/NPCs:**
    * *Livro (.md):* Ecologia, comportamento, lore.
    * *Dados (.json):* `id`, `tabela_loot`, `behavior_tree`, `stats`.

### Grupo C: O Motor (100% Dados / Referência em Tabela)
*Listas matemáticas e funcionais.*
* **Tabelas de Loot:** Probabilidades matemáticas.
* **Banco de Itens:** Lista de todos os itens com seus stats (Matriz 5x5).
* **Banco de Skills:** Fórmulas de dano, custos e cooldowns.

## 3. Fluxo de Trabalho (Pipeline)
1.  **Conceito:** Escrever no Markdown (Pasta 01, 02, 03).
2.  **Estrutura:** Definir o Schema (formato do JSON) na pasta `06_Dados_e_Assets`.
3.  **Implementação:** Popular os JSONs e structs Go no servidor (`server/data/`).
