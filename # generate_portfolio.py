# generate_portfolio.py
# -----------------------------------------
# Gera um index.html para um portfólio dark mode
# -----------------------------------------

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Portfólio</title>
    <style>
        :root {{
            --bg: #0d1117;
            --card-bg: #161b22;
            --text: #c9d1d9;
            --accent: #58a6ff;
        }}

        body {{
            background-color: var(--bg);
            color: var(--text);
            font-family: "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 0;
        }}

        header {{
            text-align: center;
            padding: 3rem 1rem 2rem;
        }}

        header h1 {{
            font-size: 2.5rem;
            color: var(--accent);
            margin-bottom: 0.3rem;
        }}

        header p {{
            font-size: 1.1rem;
            color: #8b949e;
        }}

        section {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem 1rem;
        }}

        h2 {{
            color: var(--accent);
            border-bottom: 1px solid #30363d;
            padding-bottom: 0.3rem;
        }}

        .projects {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }}

        .project-card {{
            background-color: var(--card-bg);
            border-radius: 10px;
            padding: 1.2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .project-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
        }}

        .project-card h3 {{
            margin-top: 0;
            color: var(--accent);
        }}

        .project-card p {{
            font-size: 0.95rem;
            color: #adbac7;
        }}

        .project-card a {{
            display: inline-block;
            margin-top: 0.8rem;
            text-decoration: none;
            color: var(--accent);
            font-weight: bold;
        }}

        footer {{
            text-align: center;
            padding: 2rem 1rem;
            font-size: 0.9rem;
            color: #8b949e;
        }}

        .contact a {{
            margin: 0 0.6rem;
            color: var(--accent);
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <header>
        <h1>{nome}</h1>
        <p>{descricao}</p>
    </header>

    <section>
        <h2>Sobre mim</h2>
        <p>{sobre_mim}</p>
    </section>

    <section>
        <h2>Projetos</h2>
        <div class="projects">
            {projetos_html}
        </div>
    </section>

    <section>
        <h2>Contato</h2>
        <p class="contact">
            <a href="{linkedin}" target="_blank">LinkedIn</a> |
            <a href="{github}" target="_blank">GitHub</a> |
            <a href="mailto:{email}">E-mail</a>
        </p>
    </section>

    <footer>
        © {ano} {nome}. Todos os direitos reservados.
    </footer>
</body>
</html>
"""

# ==============================
# 🔧 Edite suas informações aqui
# ==============================

import datetime
ano = datetime.datetime.now().year

nome = "Gabriela Lopes"
descricao = "Desenvolvedora Python | Data & Automation"
sobre_mim = """Economista e Contadora, apaixonada por transformar ideias em soluções eficientes.
Atualmente, trabalho em projetos de automação, dados e visualização.
Gosto de aprender novas tecnologias e compartilhar conhecimento."""

projetos = [
    {
        "titulo": "TAX Scan Mapeamento de Legislação Tributária",
        "descricao": "TAX Scan é uma ferramenta de automação desenvolvida em Python com interface gráfica (PySide6) que permite buscar e mapear trechos de legislação tributária com base em tributo, estado/cidade e palavras-chave. O objetivo é agilizar a pesquisa em arquivos de textos legislativos e facilitar o estudo de normas tributárias.",
        "link": "https://github.com/gabrieladll/TAX_Scan"
    },
    {
        "titulo": "Dashboard Automático",
        "descricao": "Este projeto automatiza o preenchimento de um dashboard em PowerPoint (PPTX) com base em um arquivo Excel contendo dados de vendas. O script lê a planilha, realiza cálculos e atualiza automaticamente textos e gráficos em um modelo de slide existente, gerando uma apresentação final atualizada.",
        "link": "https://github.com/gabrieladll/Dashboard_automatico"
    }
]

linkedin = "https://www.linkedin.com/in/gabrieladelimalopes/"
github = "https://github.com/gabrieladll"
email = "gabidelimalopes@hotmail.com"

# ==============================
# 🔨 Geração automática do HTML
# ==============================

projetos_html = ""
for p in projetos:
    projetos_html += f"""
        <div class="project-card">
            <h3>{p['titulo']}</h3>
            <p>{p['descricao']}</p>
            <a href="{p['link']}" target="_blank">Ver no GitHub →</a>
        </div>
    """

html_final = html_template.format(
    nome=nome,
    descricao=descricao,
    sobre_mim=sobre_mim,
    projetos_html=projetos_html,
    linkedin=linkedin,
    github=github,
    email=email,
    ano=ano
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_final)

print("✅ Arquivo 'index.html' gerado com sucesso! Agora é só enviar para seu repositório github.io.")


