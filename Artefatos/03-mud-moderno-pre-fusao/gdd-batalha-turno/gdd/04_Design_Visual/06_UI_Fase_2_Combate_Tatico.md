# 🖼️ UI – Fase 2: Combate Tático e Grid

Este documento define a interface para a **Fase 2 (Jogo Completo)** de *Eras do Brasil*, onde o sistema de "Combate Tático" (Capítulo 4 do Livro de Regras) é ativado.

A visualização muda de "Cenas Estáticas" para uma **visão isométrica ou top-down com grid**, focada em posicionamento, alcance e estratégia espacial.

---

## 1. O Grid Tático (Visualização no Mundo)

O grid não deve ser invasivo. Ele deve parecer integrado ao terreno (como em *Stoneshard* ou *Wartales*).

### 🟦 Feedback de Movimento e Alcance
Quando o jogador seleciona seu personagem ou uma habilidade, o grid se ilumina para mostrar as possibilidades:

* **Tiles Azuis (Borda ou Preenchimento Leve):** Área de movimentação disponível com os Pontos de Movimento atuais.
* **Tiles Vermelhos:** Alcance de ataque ou área de efeito de uma magia ofensiva.
* **Tiles Amarelos/Laranjas:** Área de perigo (ex: terreno difícil, fogo, zona de ataque de oportunidade).
* **Linha de Visão (LoS):** Inimigos ou áreas bloqueadas por obstáculos (árvores, muros) devem ficar escurecidos ou com silhueta (Fog of War tático).

### 🛡️ Indicadores de Cobertura
* **Ícone de Escudo:** Aparece sobre a cabeça do personagem ou inimigo quando ele está adjacente a uma cobertura (muro, tronco), indicando bônus de Defesa.
    * **Escudo Meio Cheio:** Cobertura Parcial (+2 Defesa).
    * **Escudo Cheio:** Cobertura Total (Não pode ser alvo).

---

## 2. HUD de Combate Tático

A interface de combate evolui para dar controle total sobre as ações complexas.

### ⚔️ A Barra de Ações (Hotbar)
Localizada na parte inferior central.
* **Slots 1-5:** Habilidades Ativas da Classe e da Arma.
* **Botões Fixos:**
    * **Mover:** (Ativa o grid azul).
    * **Ação Bônus:** (Se disponível).
    * **Fim de Turno:** (Botão de destaque para passar a vez).
    * **Inventário Rápido:** Acesso a poções/itens sem abrir o menu completo.

### ⏱️ Trilha de Iniciativa (Turn Order)
Localizada no topo ou lateral da tela.
* Uma lista horizontal/vertical de retratos mostrando a ordem de quem age.
* **Destaque:** O retrato do personagem atual brilha ou pulsa.
* **Previsão:** Ao passar o mouse sobre um inimigo na trilha, o grid mostra o alcance de movimento *dele*, permitindo ao jogador planejar.

---

## 3. Feedback de Ação (Pré-visualização)

Antes de confirmar uma ação, o jogador deve ver as consequências matemáticas (Math-transparent UI).

* **Ao mirar um ataque:**
    * Uma janela flutuante (tooltip) aparece ao lado do alvo.
    * **Chance de Acerto:** "85% de chance" (Baseado em 1D20 + Mod vs Defesa).
    * **Dano Estimado:** "4-9 de Dano" (Baseado na Arma).
    * **Vantagem/Desvantagem:** Ícones claros (seta verde para cima / vermelha para baixo) indicando se há modificadores ativos.

* **Ataque de Oportunidade:**
    * Se o jogador traçar uma rota de movimento que passa pela área de ameaça de um inimigo, o tile correspondente pisca em vermelho com um ícone de "Espada Cruzada", alertando que ele levará um ataque se passar por ali.

---

## 4. Estética da Fase 2

Mantém a identidade "Rústica/Colonial" da Fase 1, mas adaptada para não obstruir a visão tática.

* **Grid:** Linhas finas e translúcidas, não grades grossas.
* **Retratos e Menus:** Mantêm a moldura de madeira e corda, mas em escala menor para maximizar a área de visão do mapa.
* **Dano e Texto Flutuante:** Pixel art nítida com contorno forte para leitura rápida sobre o cenário colorido.