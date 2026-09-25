import os
from bs4 import BeautifulSoup

# Lista dos seus arquivos HTML para converter
arquivos_html = [
    'RPG Eras do Brasil.html',
    'Setor de Arte.html',
    'Setor Enredo Narrativa.html',
    'Setor Livro de Regras e Sistema.html',
    'Setor Missões e Eventos.html',
    'Setores para Desenvolvimento Eras.html'
]

for nome_arquivo_html in arquivos_html:
    if not os.path.exists(nome_arquivo_html):
        print(f"Aviso: Arquivo '{nome_arquivo_html}' não encontrado. Pulando.")
        continue

    print(f"Processando '{nome_arquivo_html}'...")

    # Gera o nome do novo arquivo .md
    nome_arquivo_md = os.path.splitext(nome_arquivo_html)[0] + '_convertido.md'

    with open(nome_arquivo_html, 'r', encoding='utf-8') as f:
        conteudo_html = f.read()

    soup = BeautifulSoup(conteudo_html, 'html.parser')

    # Encontra todas as mensagens na conversa
    mensagens = soup.find_all('pre', class_='message')

    with open(nome_arquivo_md, 'w', encoding='utf-8') as f_md:
        for msg in mensagens:
            autor_div = msg.find('div', class_='author')

            # O conteúdo da mensagem está no próximo 'div' após o autor
            conteudo_div = autor_div.find_next_sibling('div')

            if autor_div and conteudo_div:
                # Limpa o nome do autor
                autor = autor_div.get_text(strip=True)
                if 'user' in autor.lower():
                    autor = "Sidinei" # Você pode mudar aqui se o nome de usuário for outro

                # Limpa o conteúdo da mensagem
                conteúdo = conteudo_div.get_text(strip=True)

                # Escreve no formato Markdown
                f_md.write(f"## {autor}:\n\n")
                f_md.write(f"{conteúdo}\n\n")
                f_md.write("---\n\n")

print("Conversão concluída!")