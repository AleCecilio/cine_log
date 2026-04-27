# 🎬 CineLog

Sistema desktop de registro e avaliação de filmes desenvolvido em Python, com interface gráfica moderna e arquitetura em camadas — criado como demonstração de conceitos de Engenharia de Software.

---

## 📋 Objetivo

Permitir que o usuário registre os filmes que assistiu, atribua notas e gerencie uma watchlist — tudo por meio de uma interface gráfica intuitiva, com dados persistidos localmente em JSON.

---

## 📁 Estrutura do Projeto

```
cine_log/
├── data/
│   └── cinelog.json             # Banco de dados (JSON)
├── dist/
│   ├── CineLog.exe              # Executável final (gerado pelo PyInstaller)
│   └──data/
│      └── cinelog.json             # Banco de dados (JSON)
├── src/
│   ├── main.py                  # Ponto de entrada (GUI)
│   ├── main_terminal.py         # Ponto de entrada (Terminal)
│   ├── model/
│   │   ├── config.py            # Configuração de caminhos e ambiente
│   │   ├── database_handler.py  # Leitura e escrita no arquivo JSON
│   │   └── repository.py        # Acesso lógico aos dados
│   ├── services/
│   │   ├── engine.py            # Regras de negócio e orquestração
│   │   └── rules.py             # Validações de título, data e nota
│   └── view/
│       ├── __init__.py
│       ├── app.py               # Orquestrador da Interface Gráfica
│       ├── components/          # Peças reutilizáveis da UI
│       │   ├── __init__.py
│       │   ├── tabela.py        # Classe TabelaEstilizada
│       │   └── modais.py        # Janelas de formulário (Pop-ups)
│       ├── tabs/                # Telas/Abas principais
│       │   ├── __init__.py
│       │   ├── aba_diario.py    # Lógica da aba Diário
│       │   └── aba_watchlist.py # Lógica da aba Watchlist
│       ├── terminal/            # Interface antiga (Modo Texto)
│       │   ├── __init__.py
│       │   ├── forms.py         # Formulários do terminal
│       │   ├── menu.py          # Menus do terminal
│       │   ├── reports.py       # Relatórios do terminal
│       │   └── io_helpers.py    # Utilitários de entrada/saída
│       └── utils/                # Telas/Abas principais
│           ├── __init__.py
│           ├── theme.py             # Central de cores e estilos (CORES)
│           └── image.py             # Carrega o Logo do app
├── CineLog.spec                 # Arquivo de configuração do PyInstaller
├── README.md                    # Documentação do projeto
└── requirements.txt             # Dependências (customtkinter, etc.)
```

---

## ✨ Funcionalidades

- 📝 **Diário de filmes** — registre título, data assistida e nota (0.5 a 5.0 em incrementos de 0.5)
- ⭐ **Avaliação com estrelas** — notas exibidas visualmente com `★`, `½` e `☆`
- 📋 **Watchlist** — adicione e remova filmes que deseja assistir
- 📊 **Relatórios** — visualize seu histórico de filmes assistidos
- 🌙 **Tema escuro** — interface com paleta dark usando CustomTkinter
- 💾 **Persistência local** — dados salvos em JSON, sem necessidade de banco externo
- 📦 **Executável standalone** — distribuível via `.exe` gerado com PyInstaller
- 🖥️ **Modo terminal (CLI)** — versão alternativa para rodar diretamente no terminal, sem interface gráfica

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura em **3 camadas** bem definidas:

```
View (app.py, forms.py, menu.py...)
    ↓  chama apenas
Services (engine.py, rules.py)
    ↓  chama apenas
Model (repository.py, database_handler.py)
```

- **View** — responsável exclusivamente pela interface e captura de eventos. Nunca acessa o model diretamente.
- **Services** — contém toda a lógica de negócio e validações. Orquestra as operações entre view e model.
- **Model** — responsável pela persistência: leitura e escrita no arquivo `cinelog.json`.

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-1F6FEB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-4B4B4B?style=for-the-badge&logo=python&logoColor=white)

---

## 🚀 Como Usar

### Opção 1 — Executável (sem instalar Python)

Baixe o arquivo `CineLog.exe` na pasta `dist/` e execute diretamente.

### Opção 2 — Interface Gráfica (GUI)

**1. Clone o repositório**
```bash
git clone <url-do-repositorio>
cd cine_log
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Execute a aplicação**
```bash
python src/main.py
```

### Opção 3 — Terminal (CLI)

Prefere rodar sem interface gráfica? Use o modo terminal. Os passos 1 a 3 são os mesmos da Opção 2, apenas o comando de execução muda:

```bash
python src/main_terminal.py
```

> Não requer instalação do CustomTkinter — funciona em qualquer ambiente com Python puro.

---

## 📈 Validações Implementadas

| Campo   | Regra                                              |
|---------|----------------------------------------------------|
| Título  | Não pode ser vazio ou apenas espaços               |
| Data    | Formato `dd/mm/aaaa`, não permite datas futuras    |
| Nota    | Entre `0.5` e `5.0`, em incrementos de `0.5`      |
| Watchlist | Não permite títulos duplicados                   |

---

## 📌 Observações

- Os dados ficam salvos em `data/cinelog.json` — não apague esse arquivo para preservar seu histórico.
- O executável `.exe` já embute o arquivo de dados e funciona de forma portátil.

---

## 👤 Autor

<div align="center">

**Alessandro Moreira Cecilio**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AleCecilio)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alessandro-cecilio/)


</div>


## 📌 Status do Projeto

![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Python](https://img.shields.io/badge/python-3.13+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
