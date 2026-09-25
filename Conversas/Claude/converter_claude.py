import json
import sys


def load_messages(path):
    """Le um export de conversa do Claude (formato chat_messages, ja linear,
    sem arvore de branches como no ChatGPT). Mantem so blocos de texto visiveis
    de human/assistant; descarta thinking, tool_use, tool_result e
    injected_prompt_block (ruido interno de execucao de ferramentas)."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    messages = []
    for msg in data.get("chat_messages", []):
        sender = msg.get("sender")
        if sender not in ("human", "assistant"):
            continue
        pieces = []
        for block in msg.get("content") or []:
            if block.get("type") == "text":
                text = block.get("text", "").strip()
                if text:
                    pieces.append(text)
        seen_files = set()
        for att in msg.get("attachments") or []:
            name = att.get("file_name", "anexo")
            if name in seen_files:
                continue
            seen_files.add(name)
            size = att.get("file_size")
            pieces.append(f"[Anexo: {name}{f' ({size} bytes)' if size else ''}]")
        for f in msg.get("files") or []:
            name = f.get("file_name", "arquivo")
            if name in seen_files:
                continue
            seen_files.add(name)
            pieces.append(f"[Arquivo anexado: {name}]")
        text = "\n\n".join(pieces).strip()
        if not text:
            continue
        messages.append((sender, text))

    return data.get("name", ""), data.get("created_at"), messages


def to_markdown(messages):
    lines = []
    for sender, text in messages:
        autor = "Sidinei" if sender == "human" else "Claude"
        lines.append(f"## {autor}:\n")
        lines.append(f"{text}\n")
        lines.append("---\n")
    return "\n".join(lines)


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    title, created_at, messages = load_messages(src)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(to_markdown(messages))
    print(f"OK: {src} -> {dst} ({len(messages)} mensagens)")
