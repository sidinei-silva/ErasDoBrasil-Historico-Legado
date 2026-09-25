# 🖼️ UI – Fase 1: Exploração e Combate Estático

Este documento define a interface de usuário (UI) e a experiência de usuário (UX) para a **Fase 1 (Protótipo / RPG de Mesa Digital)** de *Eras do Brasil*.

Nesta fase, o jogo não possui movimentação livre de personagens nem grids táticos. A experiência é focada em **tomada de decisão, gestão de recursos e narrativa visual**, assemelhando-se a um jogo de tabuleiro digital avançado ou um "RPG de Texto Visual".

---

## 1. Layout Geral e HUD (Heads-Up Display)

A interface principal deve passar a sensação de estar olhando para uma mesa de jogo organizada ou um diário de aventura interativo.

### 🧱 O Painel de Gestão (Topo da Tela)
Inspirado em jogos de gestão (*Idle RPGs* e *Azure Dragon's Treasure*), o topo da tela exibe constantemente os recursos vitais do jogador.

* **Estilo:** Barra de madeira escura com ícones em pixel art 32x32.
* **Elementos (Esquerda para Direita):**
    1.  **Retrato do Personagem:** Rosto do personagem + Barra de PV (Vermelha) e Barra de XP (Azul/Amarela).
    2.  **Recursos de Coleta (Resumo):** Ícones pequenos de Madeira, Pedra, Ervas e Couro com seus contadores numéricos.
    3.  **Moeda:** Ícone de Ouro/UC e valor total.
    4.  **Relógio do Jogo:** Um ícone de sol/lua que gira ou muda conforme o tempo avança, indicando o período do dia (Manhã, Tarde, Noite, Madrugada).

---

## 2. Interface de Exploração (Mapa de Nós)

Na Fase 1, não há um "mundo aberto" contínuo. O mundo é representado por um **Mapa de Nós** (Node Map), similar a *Slay the Spire* ou *Sorcery!*.

### 🗺️ O Mapa de Trilhas
* **Visual:** Um pergaminho ou mapa desenhado à mão (pixel art) ocupa o centro da tela.
* **Os "Blocos":** Locais são representados por **Ícones/Nós** conectados por linhas pontilhadas.
    * **Ícone de Interrogação (?)**: Local inexplorado.
    * **Ícone de Fogueira:** Local de descanso/acampamento.
    * **Ícone de Caveira:** Combate obrigatório.
    * **Ícone de Cidade/Casa:** Vila ou NPC importante.
* **Interação:** O jogador clica no próximo Nó disponível.
* **Feedback de Movimento:** Ao clicar, uma animação rápida do personagem (token ou miniatura) se move pela linha pontilhada, e o "Relógio do Jogo" no topo avança conforme o tempo de viagem.

---

## 3. Interface de Evento e Interação (Cena)

Quando o jogador chega em um Nó (Bloco), a tela muda para o **Modo de Cena**.
*Referência principal: Roadwarden.*

### 📐 Layout de Tela Dividida (Split Screen)
* **Lado Esquerdo (A Imersão):** Uma ilustração grande em Pixel Art (alta qualidade) representando o local (ex: "A Clareira Sagrada"). Esta imagem é estática, mas pode ter efeitos climáticos leves (chuva, folhas caindo).
* **Lado Direito (A Narrativa):**
    * **Título:** Nome do Local (ex: "Clareira do Pajé").
    * **Texto Descritivo:** "Você encontra o velho Pajé sentado sob a árvore..." (Texto rolável).
    * **Menu de Ações (Botões Grandes):** Uma lista vertical de escolhas estilo *Button Choice*.
        * `[1] Conversar com o Pajé`
        * `[2] (Sabedoria) Pedir Benção`
        * `[3] Coletar Ervas (~5 min)`
        * `[4] Seguir Viagem`

---

## 4. Interface de Combate Estático (Turnos)

O combate na Fase 1 não usa grid. Ele foca na escolha tática de habilidades.
*Referência principal: Path of Adventure / JRPGs Clássicos.*

### ⚔️ A Tela de Batalha
* **Centro Superior:** Sprites dos Inimigos (estáticos ou com animação de "respiro"). Se houver 3 lobos, mostram-se 3 sprites lado a lado.
* **Centro Inferior:** O Personagem do Jogador (visto de costas ou lateral).
* **Barra de Ações (Hotbar):** No rodapé da tela, substituindo o texto narrativo.
    * Botões grandes e claros: **ATACAR**, **HABILIDADE**, **ITEM**, **DEFENDER/FUGIR**.
* **Log de Combate (Lateral ou Sobreposto):** Uma caixa de texto translúcida que narra o resultado matemático:
    * *"Você rolou 15 (Astúcia) + 2 = 17. Acerto! Lobo sofre 6 de dano."*
    * *"Lobo ataca! Sua defesa absorveu 2 de dano."*

### Feedback Visual
* **Dano:** Números "pulam" (pop-up) sobre a cabeça dos sprites quando atingidos.
* **Status:** Ícones pequenos (veneno, atordoado) aparecem flutuando ou ao lado da barra de vida do alvo.

---

## 5. Estética e Materiais

Seguindo a identidade visual do projeto:

* **Molduras:** Madeira rústica e entalhada para as janelas de texto.
* **Fundos de Texto:** Textura de papel envelhecido ou pergaminho amarelado (leitura escura sobre fundo claro) ou pedra escura (leitura clara sobre fundo escuro) para menus.
* **Botões:** Devem parecer peças de madeira ou pedra com relevo (efeito de "clique" físico).
* **Detalhes Culturais:** O uso de penas, cordas e grafismos marajoaras/indígenas para decorar as bordas da UI é encorajado.