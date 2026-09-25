# 🎨 Documento de Design Visual — Eras do Brasil

Este documento define o **design system visual** do jogo *Eras do Brasil*, incluindo estilo gráfico, arte de UI, fontes, proporções e direções gerais para sprites, HUD, narrativa e apresentação. Ele serve como base para manutenção de consistência visual e como guia para futuras gerações de assets e componentes.

---

## 🧭 Estilo Visual Geral

- **Estilo gráfico:** Pixel Art moderna
- **Paleta principal:** Tons terrosos, madeira, palha, dourado envelhecido, verdes profundos, azuis místicos e roxos espirituais
- **Atmosfera:** Rústica, espiritual, mística, conectada à natureza e aos ciclos
- **Referências:** *Sea of Stars*, *Wartales*, *Solasta*, *Pathfinder* (em pixel art), arte brasileira artesanal

### 📐 Proporção e Resolução

- **Grid base:** 32x32px para elementos interativos e icônicos
- **Resolução alvo:** 1920x1080 (redimensionável com 9-slice e escalonamento)

---

## 🖼️ UI e HUD

### 🎮 Componentes

- Molduras com textura de madeira, detalhes em cordas, entalhes e penas
- Botões com estados `idle`, `hover` e `pressed`, seguindo o mesmo estilo tribal
- Painéis de informações com ornamentos discretos inspirados em pergaminhos ou artefatos
- Barras de vida e durabilidade com molduras entalhadas e preenchimento temático

### 🌟 Elementos visuais

- HUD contextual (aparece por bloco)
- Mini log de eventos e tempo (tick)
- Setas para movimentação com arte integrada ao ambiente
- Componentes diegéticos sempre que possível (ex: painel de atributos como pergaminho)

---

## 🧩 Estilo de Ícones

### 📊 Atributos

- Pixel art em 32x32 px
- Simbologia tribal e clara
- Ex: Coração para Vigor, Braço para Força Bruta, Máscara para Astúcia

### 🧪 Proficiências de Vida

- 32x32 px, fundo transparente
- Design temático por tipo:
    - 🌿 **Coleta:** natureza, rastros, minerais, visões
    - ⚙️ **Refinamento:** couro, fornalhas, ferramentas, trocas
    - 🔨 **Produção:** caldeirões, bigornas, talismãs, tecidos

### 🧿 Efeitos e Status

- Icônes simples, animados quando aplicável (ex: envenenado, buff, maldição)

---

## 📖 Tipografia

### Fontes avaliadas:

- **Londrina Solid:** para títulos e menus principais
- **TinyUnicode:** para textos menores com suporte PT-BR
- **Press Start 2P:** como opção estilizada e nostálgica, se apropriado

### Características desejadas

- Total suporte a PT-BR (acentos, cedilha, pontuação)
- Boa legibilidade em 14px e 18px (escalonável)
- Versão de título com maior destaque visual

---

## 🧱 Arte de Cenário e Blocos

- Estilo de "cenas conectadas" com caminhos e cenários modulares
- Cada bloco é uma tela com fundo ilustrado em pixel art detalhado
- Elementos clicáveis (NPCs, coleta, evento) ficam sobrepostos com sprites de 32-64px
- Blocos "vazios" (trilhas, estradas) têm ambientação suave mas com possibilidade de eventos e recursos

---

## ⚔️ Combate e Grid

- Combate em modo tático isométrico, estilo *Solasta*
- Grid em perspectiva 5x5 ou superior
- HUD de combate com ações: Atacar, Habilidade, Fugir, Item
- Preenchimentos coloridos nos tiles para alcance (azul = movimento, vermelho = ataque)

---

## 📦 Exportação e Formatos

- Todos os assets devem ser exportados em:
    - `.png` com fundo transparente
    - Escalonamento múltiplo de 16 ou 32 px
    - Quando aplicável, considerar uso de **9-slice** para componentes de UI

---

## 📚 Recomendações finais

- Todos os elementos devem priorizar **clareza visual + identidade cultural brasileira**
- A pixel art deve ser responsiva, adaptando-se tanto a exploração quanto ao combate
- O estilo deve permitir transição para versões futuras (2.5D ou HD art) sem perder a essência

---

Este documento pode ser estendido com diretrizes de animação, feedback sonoro e comportamento visual (interações).