# Library Support System

Sistema simples de gerenciamento de empréstimos de livros em uma biblioteca universitária, desenvolvido em Python e SQLite.

# Funcionalidades

- Cadastro de usuários
- Cadastro de livros
- Empréstimo e devolução de livros
- Listagem de usuários, livros e empréstimos
- Visualização do status de devolução
- Armazenamento em banco de dados SQLite
- Scripts organizados e reutilizáveis

# Tecnologias usadas

- Python 3.10+
- SQLite (via sqlite3)
- Estrutura modular com scripts separados

# Estrutura do projeto

library-support-system/
├── database/
│ └── library.db
├── scripts/
│ ├── add_book.py
│ ├── borrow_book.py
│ ├── list_books.py
│ ├── list_loans.py
│ ├── list_users.py
│ ├── register_user.py
│ ├── return_book.py
│ └── utilities.py
├── user_manual.txt
├── README.md
└── .gitignore
