# Estilo Visual, Arte e Técnica

Diretrizes de direção artística, interface e exportação de assets para *Eras do Brasil*.

---

## Direção de Arte

- **Estilo gráfico:** Pixel Art moderna.
- **Paleta principal:** Tons terrosos, madeira, palha, dourado envelhecido, verdes profundos, azuis místicos e roxos espirituais.
- **Atmosfera:** Rústica, espiritual, mística, conectada à natureza e aos ciclos.
- **Referências:** *Sea of Stars*, *Wartales*, *Solasta*, *Pathfinder* (em pixel art), arte brasileira artesanal.
- **Grid base:** 32×32 px para elementos interativos e icônicos.
- **Resolução alvo:** 1920×1080 (redimensionável com 9-slice e escalonamento).

---

## Componentes de UI

- **Estilo:** Molduras com textura de madeira, detalhes em cordas, entalhes e penas.
- **Botões:** Estados visuais claros — `idle`, `hover`, `pressed` — no estilo tribal.
- **Painéis:** Apresentados com ornamentos discretos inspirados em pergaminhos ou artefatos.
- **Barras:** Barras de vida e durabilidade com molduras entalhadas e preenchimento temático.

## HUD

- **HUD Contextual:** Aparece por bloco, evitando poluição visual.
- **Log:** Mini log de eventos e tempo para feedback imediato.
- **Navegação:** Setas de movimentação com arte integrada ao ambiente.
- **Diegese:** Componentes diegéticos sempre que possível (ex: atributos representados como pergaminho físico).

## Tipografia

- **Londrina Solid** — títulos e menus principais.
- **TinyUnicode** — textos menores com suporte a PT-BR (acentos, cedilha).
- **Press Start 2P** — opção estilizada para momentos específicos.
- Requisito: suporte completo a PT-BR, boa legibilidade em 14–18 px.

---

## Assets, Ícones e Cenários

### Arte de Cenário

- **Conceito:** Cenas conectadas com caminhos e cenários modulares.
- **Blocos:** Cada bloco é uma tela com fundo ilustrado em pixel art detalhado.
- **Elementos interativos** (NPCs, coleta, evento): sprites sobrepostos de 32–64 px.
- **Blocos de travessia:** Ambientação suave com possibilidade de eventos e recursos.

### Ícones

| Categoria | Tamanho | Exemplos |
|-----------|---------|----------|
| Atributos | 32×32 px | Coração (Vigor), Braço (Força Bruta), Máscara (Astúcia) |
| Proficiências | 32×32 px, fundo transparente | Coleta: natureza, rastros, minerais; Produção: caldeirões, bigornas |
| Status/Efeitos | 32×32 px, animado quando aplicável | Bolhas (envenenado), brilho (buff) |

### Combate e Grid

- **Perspectiva:** Combate tático isométrico (estilo *Solasta*), grid 5×5 ou superior.
- **HUD de Combate:** Ações claras — Atacar, Habilidade, Fugir, Item.
- **Feedback Visual:** Preenchimento de tiles por tipo — azul (movimento), vermelho (ataque).

---

## Exportação e Requisitos Técnicos

- **Formato:** `.png` com fundo transparente.
- **Escala:** Múltiplo de 16 ou 32 px; UI com 9-slice para redimensionamento.
- **Identidade:** Clareza visual aliada à identidade cultural brasileira.
- **Responsividade:** Funciona tanto na exploração (blocos) quanto no combate.
- **Escalabilidade:** Estilo compatível com transição futura para 2.5D ou HD art.
