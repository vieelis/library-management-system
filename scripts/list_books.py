import sqlite3

# CONEXÃO COM O BANCO
conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

# BUSCAR TODOS OS LIVROS
cursor.execute("SELECT id, title, author, available FROM books")
books = cursor.fetchall()

# MOSTRAR OS LIVROS
print('Livros cadastrados:')
for book in books:
    status = "Disponível" if book[3] == 1 else "Emprestado"
    print(f"{book[0]} - {book[1]} - {book[2]} - {status}")

# FECHAR CONEXÃO
conn.close()