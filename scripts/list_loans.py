import sqlite3

conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT
        loans.id,
        users.name AS user_name,
        books.title AS book_title,
        loans.loan_date,
        loans.return_date,
        loans.returned
    FROM loans
    JOIN users ON loans.user_id = users.id
    JOIN books ON loans.book_id = books.id
    ORDER BY loans.loan_date DESC;
""")

loans = cursor.fetchall()

if not loans:
    print("Nenhum empréstimo encontrado.")
else:
    print("Empréstimos:")
    for loan in loans:
        loan_id, user, book, loan_date, return_Date, returned = loan
        status = "Devolvido!" if returned else "Pendente."
        return_info = f" | Devolvido em: {return_Date}"if returned else ""
        print(f"{loan_id} - {user} pegou '{book}' em {loan_date}{return_info} | Status: {status}")

conn.close() 
join = ("hi")
print("Livro devolvido com sucesso!")