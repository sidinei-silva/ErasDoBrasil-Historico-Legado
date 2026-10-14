## Sidinei:

como em godot eu posso pegar o tamanho width de uma cena 2d via script para eu bloquear que um objeto saia da cena

---

## Claude:

Em Godot uma cena não tem largura própria. Um `Node2D` é só um ponto no espaço, então o "tamanho" que você quer é o do **viewport** (a área visível do jogo).

**Como pegar o tamanho**
- Em qualquer nó que herde de `CanvasItem` (Node2D, Sprite2D, Control...), `get_viewport_rect()` devolve um `Rect2`. O `.size` dele tem largura e altura.
- Alternativa: `get_viewport().get_visible_rect()`, que dá o mesmo resultado.
- O valor vem de Project Settings → Display → Window → Viewport Width/Height. Com stretch mode `canvas_items` ou `viewport`, ele continua sendo o tamanho base, não os pixels reais da janela. Isso é bom, porque seu código não muda se a janela for redimensionada.

**Como usar para bloquear**
Há duas abordagens, e a escolha depende do tipo de objeto.

1. **Clamp da posição.** Depois de mover o objeto, você limita `position.x` entre um mínimo e um máximo. O ponto fácil de errar: a posição é o *centro* do objeto (se o sprite estiver centralizado), então o limite tem que descontar metade da largura dele. Senão metade do sprite sai da tela antes de travar. Para saber a largura do objeto, olhe o tamanho da textura vezes a escala, ou a extensão do shape de colisão.
2. **Paredes físicas.** `StaticBody2D` com `CollisionShape2D` nas bordas, e o objeto (um `CharacterBody2D`, por exemplo) colide com elas naturalmente. Dá mais trabalho de montar, mas é o melhor caminho se você também quiser quicar ou deslizar na parede.

Para um jogo simples, o clamp costuma resolver e é o que eu tentaria primeiro. Um cuidado: se você tiver uma `Camera2D` que se move, `get_viewport_rect()` fica em coordenadas de tela, não de mundo. Nesse caso os limites precisam ser somados à posição da câmera.

**Próximo passo:** dê um `print(get_viewport_rect().size)` no `_ready()` do seu objeto e confira se o valor bate com o que você configurou. Depois escreva o clamp e me mande o que saiu, que eu reviso.

Que tipo de nó é o objeto: `CharacterBody2D`, `Area2D` ou um `Sprite2D` simples? Isso muda um pouco o detalhe do bloqueio.

---

## Sidinei:

qual a regra e convenção em godot para funções com _ e sem?

---

## Claude:

Em GDScript, o `_` no início do nome tem três usos. Só o primeiro é regra da engine; os outros dois são convenção.

**1. Callbacks virtuais da engine (regra)**
`_ready`, `_process`, `_physics_process`, `_input`, `_unhandled_input`, `_draw`, `_init`, `_enter_tree`, `_exit_tree`. O nome precisa ser exatamente esse, porque é assim que a engine sabe que deve chamá-los em cada momento do ciclo de vida do nó. Você sobrescreve, mas normalmente não chama. Se você criar uma função `_minha_coisa`, a engine não a chama sozinha, pois o underscore não tem mágica.

**2. Membros privados (convenção do style guide)**
O GDScript não tem `private` de verdade. O style guide oficial manda prefixar com `_` o que é de uso interno do script, tanto funções quanto variáveis. Nada impede outro script de chamar, é um aviso para quem lê: "isto não faz parte da API, não dependa disso". Funções sem `_` são a interface pública, o que outros nós e scripts podem chamar.

**3. Handlers de sinal (convenção, gerada pelo editor)**
Ao conectar um sinal pelo editor, o nome gerado segue o padrão `_on_<nó>_<sinal>`, por exemplo `_on_timer_timeout`. O `_` aqui segue a lógica do item 2: quem chama é a engine via sinal, não outro script.

**Um uso a mais:** parâmetro com `_` (como `_delta`) diz ao GDScript que você sabe que não vai usá-lo, e isso evita o warning de parâmetro não utilizado.

O resto do style guide segue a mesma linha: `snake_case` para funções e variáveis, `PascalCase` para classes, `CONSTANT_CASE` para constantes, e sinais no passado (`health_changed`).

Voltando ao jogo: já deu o `print` do tamanho do viewport? Se sim, me mostra o clamp que você escreveu.

---

## Sidinei:

como usar o get_vector para pegar somente esquerda e direita?

---

## Claude:

Para só esquerda e direita, o mais indicado é `Input.get_axis()`, não o `get_vector()`.

**`get_axis(negative_action, positive_action)`**
Recebe duas ações do Input Map e devolve um `float` entre -1 e 1: -1 se só a negativa está pressionada, 1 se só a positiva, 0 se nenhuma ou as duas. Como é um número e não um vetor, você não precisa extrair nada depois. Com analógico, o valor intermediário também vem (0.5 se o stick estiver no meio do caminho).

**E o `get_vector()`?**
Ele recebe quatro ações na ordem: esquerda, direita, cima, baixo (`negative_x`, `positive_x`, `negative_y`, `positive_y`), e devolve um `Vector2`. Serve para movimento em 8 direções, porque já normaliza a diagonal (senão andar na diagonal seria mais rápido) e aplica deadzone no analógico. Dá para usá-lo e ler só o `.x`, mas você estaria pedindo um vetor para descartar metade dele. Para um eixo só, essa normalização não faz diferença.

**Antes de escrever, confira:**
- As ações (`ui_left`, `ui_right` ou as suas próprias) precisam existir em Project Settings → Input Map. As `ui_*` já vêm prontas, mas as suas próprias permitem remapear depois sem mexer no código.
- O `get_axis` é lido a cada frame, então o lugar natural é o `_physics_process` (se for `CharacterBody2D`) ou o `_process`.

**Como isso se conecta ao que você já tem:** o valor do eixo vira a direção. Você multiplica pela velocidade e pelo `delta` para obter o deslocamento do frame, soma na posição e depois aplica o clamp que falamos.

**Próximo passo:** escreva o movimento horizontal usando `get_axis` e o clamp nas bordas, rode, e me mande o código junto com o que aconteceu (travou certo? sprite passou da borda?). Aí eu reviso.

---

## Sidinei:

```gdscript
extends CharacterBody2D


@export var speed = 400

func get_input():
	var input_direction = Input.get_axis("left", "right")
	velocity = input_direction * speed

func _physics_process(_delta):
	get_input()
	move_and_slide()

```

Neste codigo esta dando Nil mesmo ja mapeado as ações

---

## Claude:

O problema está na linha `velocity = input_direction * speed`. `velocity` em um `CharacterBody2D` é um `Vector2`, e `input_direction * speed` é um `float` (o `get_axis` devolve um número, não um vetor). Você está tentando guardar um número dentro de algo que espera dois valores (x e y), e o `move_and_slide()` trabalha em cima desse vetor.

**Como resolver:** em vez de substituir o vetor inteiro, atribua só ao componente horizontal dele, `velocity.x`. Como o jogo só anda na horizontal, o `y` fica como está.

**Por que o erro apareceu só ao rodar:** suas variáveis estão sem tipo (`var input_direction`, `@export var speed = 400`), então o editor não tem como avisar antes. Se você escrever `var input_direction: float` e `@export var speed: float = 400.0`, o parser passa a apontar incompatibilidades como essa enquanto você digita. Vale o hábito.

**Uma ressalva:** a mensagem exata do erro que o debugger mostrou não bate 100% com "Nil". Normalmente esse caso aparece como "Invalid assignment of property or key 'velocity' with value of type 'float'". Se depois de corrigir o `velocity.x` o erro continuar, confira:
- Se os nomes das ações no Input Map são exatamente `left` e `right`, com o mesmo case. Se não existirem, o Godot imprime que a ação não existe.
- Se o script está anexado ao nó `CharacterBody2D` certo.

Faça a correção, rode, e se ainda der erro me cole o texto completo do painel Debugger → Errors. Se funcionar, o próximo passo é o clamp nas bordas usando o tamanho do viewport.

---

## Sidinei:

speed esta vindo como null e não sei porque

---

## Claude:

Isso muda meu diagnóstico anterior. Se `speed` chega como `null`, o erro "Nil" que você viu faz sentido: `float * Nil` dá "Invalid operands 'float' and 'Nil' in operator '*'". Eu apontei o `velocity = float`, que continua sendo um bug real (precisa virar `velocity.x`), mas o `speed` nulo é provavelmente o que estava disparando o erro.

**Por que uma variável `@export` vem nula mesmo com valor padrão**
O valor que vale é o guardado na cena (`.tscn`), não o do script. O padrão do script só é usado quando a cena não tem valor salvo para aquela propriedade. Se em algum momento você exportou `speed` sem valor (`@export var speed`), o Inspector pode ter gravado `null` na cena. Depois, ao adicionar `= 400`, a cena continua mandando o `null` antigo. Isso também acontece se o script for anexado a outro nó, ou se essa cena estiver instanciada em outra que sobrescreve a propriedade.

**Como investigar, em ordem**
1. Selecione o nó `CharacterBody2D` e olhe a propriedade **Speed** no Inspector. Se o valor estiver estranho, vazio, ou com a seta de "revert" ao lado, é isso. Clique na seta para voltar ao padrão do script, ou digite o valor.
2. Dê um `print(speed)` no `_ready()` para confirmar o que o script está recebendo de fato.
3. Se a cena do player estiver instanciada dentro de outra, selecione a instância lá e veja se o Speed está sobrescrito.
4. Confirme que o script anexado ao nó é este mesmo, e não uma cópia com outro nome.

**Para evitar isso de vez:** tipar o export (`@export var speed: float = 400.0`). Com o tipo, o Inspector mostra um campo numérico e não grava `null`.

Depois de ajustar isso e o `velocity.x`, rode de novo. Qual valor apareceu no `print(speed)`? Se continuar nulo, me diga o que o Inspector mostra no campo Speed.

---
