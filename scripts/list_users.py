import sqlite3

# CONEXÃO COM O BANCO DE DADOS
conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

# BUSCAR TODOS OS USUÁRIOS
cursor.execute("SELECT id, name FROM users")
users = cursor.fetchall()

# MOSTRAR OS USUÁRIOS
for user in users:
    print(f"OS usuários cadastrados são: {user[0]} - {user[1]}")

# FECHAR CONEXÃO
conn.close()
