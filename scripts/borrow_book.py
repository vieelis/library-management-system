import sqlite3

# CONEXÃO COM O BANCO DE DADOS
conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

# LISTAR LIVROS DISPONÍVEIS
cursor.execute("SELECT id, title, author FROM books WHERE available = 1")
books = cursor.fetchall()

if not books:
    print("Não livros disponíveis no momento.")
    conn.close()
    exit()

print("Livros disponíveis:")
for book in books:
    print(f"{book[0]} - {book[1]} - {book[2]}")


# SOLICITAR INFORMAÇÕES DO EMPRÉSTIMO
book_id = int(input("\nDigite o ID do livro a ser emprestado:"))
user_id = int(input("Digite o ID do usuário:"))

# VERIFICAR A DISPONIBILIDADE (
cursor.execute("SELECT available FROM books WHERE id = ?", (book_id,))
result = cursor.fetchone()

if result is None:
    print("Livro não encontrado.")
elif result[0] == 0:
    print("Esse livro já está emprestado.")
else:

# INSERIR EMPRÉSTIMO NO SISTEMA
    cursor.execute("""
        INSERT INTO loans (user_id, book_id) VALUES (?,?)""", (user_id, book_id))

# ATUALIZAR STATUS DO LIVRO
    cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))

# CONFIRMAR OPERAÇÃO
    conn.commit()
    print("Empréstimo registrado com sucesso")

conn.close()
