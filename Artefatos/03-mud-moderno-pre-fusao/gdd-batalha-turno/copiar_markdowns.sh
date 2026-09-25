#!/usr/bin/env bash
set -euo pipefail

# Copia todos os arquivos Markdown do projeto para a pasta todos-arquivos,
# preservando os arquivos originais e sem recriar estrutura de pastas.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_DIR="$ROOT_DIR/todos-arquivos"

mkdir -p "$DEST_DIR"

# Limpa a pasta de destino antes de copiar.
find "$DEST_DIR" -mindepth 1 -delete

find "$ROOT_DIR" \
  \( -path "$ROOT_DIR/.git" -o -path "$ROOT_DIR/.git/*" \
     -o -path "$ROOT_DIR/.github" -o -path "$ROOT_DIR/.github/*" \
     -o -path "$ROOT_DIR/web" -o -path "$ROOT_DIR/web/*" \
     -o -path "$DEST_DIR" -o -path "$DEST_DIR/*" \) -prune \
  -o -type f \( -iname "*.md" -o -iname "*.markdown" \) -print0 |
while IFS= read -r -d '' file; do
  base_name="$(basename "$file")"
  target_path="$DEST_DIR/$base_name"

  # Evita sobrescrever quando houver nomes repetidos em pastas diferentes.
  if [[ -e "$target_path" ]]; then
    name_part="${base_name%.*}"
    ext_part="${base_name##*.}"
    count=2

    if [[ "$base_name" == "$name_part" ]]; then
      while [[ -e "$DEST_DIR/${name_part}_$count" ]]; do
        ((count++))
      done
      target_path="$DEST_DIR/${name_part}_$count"
    else
      while [[ -e "$DEST_DIR/${name_part}_$count.$ext_part" ]]; do
        ((count++))
      done
      target_path="$DEST_DIR/${name_part}_$count.$ext_part"
    fi
  fi

  cp "$file" "$target_path"
done

echo "Copia concluida para: $DEST_DIR"
