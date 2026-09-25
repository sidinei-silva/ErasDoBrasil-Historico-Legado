import json
import sys
import html


def extract_canvas_doc(content):
    """Extrai o conteúdo de um documento criado/editado via canvas (canmore).
    O payload vem como uma string JSON (com entidades HTML) dentro de parts[0]."""
    parts = content.get("parts", [])
    if not parts or not isinstance(parts[0], str):
        return None
    try:
        payload = json.loads(html.unescape(parts[0]))
    except (json.JSONDecodeError, TypeError):
        return None
    name = payload.get("name", "documento")
    body = payload.get("content")
    if body:
        return f'[Documento criado/atualizado no canvas: "{name}"]\n\n{body}'
    # update_textdoc costuma vir como lista de patches, não um "content" completo
    updates = payload.get("updates")
    if updates:
        pieces = [u.get("replacement", "") for u in updates if u.get("replacement")]
        if pieces:
            return f'[Atualização de documento no canvas: "{name}"]\n\n' + "\n\n".join(pieces)
    return None


def load_linear_messages(path):
    """Segue o mapping do export do ChatGPT (JSON) do current_node até a raiz,
    reconstruindo a conversa linear visível (ignora ramos alternativos/editados)."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    mapping = data["mapping"]
    current = data.get("current_node")

    chain = []
    node_id = current
    seen = set()
    while node_id and node_id in mapping and node_id not in seen:
        seen.add(node_id)
        chain.append(node_id)
        node_id = mapping[node_id].get("parent")
    chain.reverse()

    messages = []
    for node_id in chain:
        node = mapping[node_id]
        msg = node.get("message")
        if not msg:
            continue
        role = msg.get("author", {}).get("role")
        if role not in ("user", "assistant"):
            continue
        content = msg.get("content", {})
        if content.get("content_type") != "text":
            continue
        recipient = msg.get("recipient")
        # canmore.create_textdoc/update_textdoc = documento real escrito no canvas
        # (conteúdo de valor, ex: capítulos de regras); demais recipients != "all"
        # são chamadas de ferramenta (python, bio, browser, etc.), sem texto de conversa
        if recipient in ("canmore.create_textdoc", "canmore.update_textdoc"):
            doc_text = extract_canvas_doc(content)
            if doc_text:
                messages.append((role, doc_text))
            continue
        if recipient not in ("all", None):
            continue
        if msg.get("metadata", {}).get("is_visually_hidden_from_conversation"):
            continue
        parts = content.get("parts", [])
        text = "\n".join(p for p in parts if isinstance(p, str)).strip()
        if not text:
            continue
        messages.append((role, html.unescape(text)))

    return data.get("title", ""), data.get("create_time"), messages


def to_markdown(messages):
    lines = []
    for role, text in messages:
        autor = "Sidinei" if role == "user" else "ChatGPT"
        lines.append(f"## {autor}:\n")
        lines.append(f"{text}\n")
        lines.append("---\n")
    return "\n".join(lines)


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    title, create_time, messages = load_linear_messages(src)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(to_markdown(messages))
    print(f"OK: {src} -> {dst} ({len(messages)} mensagens)")
