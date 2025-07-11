import sqlite3

# CONEXÃO COM O BANCO DE DADOS
conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

# BUSCAR LIVROS EMPRESTADOS
cursor.execute("""
    SELECT b.id, b.title, u.name
    FROM books AS b
    JOIN loans AS l ON b.id = l.book_id
    JOIN users AS u ON l.user_id = u.id
    WHERE b.available = 0 AND l.returned = 0
""")

borrowed_books = cursor.fetchall()

# VERIFICAR SE EXISTEM LIVROS EMPRESTADOS 
if not borrowed_books:
    print("Nenhum livro emprestado no momento.")
    conn.close()
    exit()
    
# MOSTRAR LIVROS EMPRESTADOS
print("Livros emprestados:")
for book in borrowed_books:
    print(f"{book[0]} - {book[1]} (emprestado por {book[2]})")

# PEDIR ID DO LIVRO A SER DEVOLVIDO 
book_id = int(input("Digite o ID do livro a ser devolvido: "))

# VERIFICAR SE FOI EMPRESTADO MESMO
cursor.execute("""
    SELECT id FROM loans
    WHERE book_id = ? AND returned = 0
    ORDER BY loan_date DESC LIMIT 1
""", (book_id,))

loan = cursor.fetchone()

if loan is None:
    print("Esse livro não está emprestado ou já foi devolvido")
else:
    # ATUALIZAR O STATUS DO EMPRESTIMO COMO DEVOLVIDO
    cursor.execute("""
        UPDATE loans
        SET return_date = CURRENT_TIMESTAMP,
            returned = 1
        WHERE id = ?
""", (loan[0],))
    

# TORNAR LIVRO DISPONIVEL
    cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,)) 

    conn.commit()
    print("Livro devolvido com sucesso!")

conn.close()

    
