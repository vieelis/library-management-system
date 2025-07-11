import sqlite3

# CONECTAR AO BANCO

conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

# DADOS DO USUARIO

name = input("Digite o nome do usuário: ")
email = input("Digite o e-mail do usuário: ")


cursor.execute("""
    INSERT INTO users (name, email) VALUES (?,?)
""", (name,email))

conn.commit()
conn.close()
print(f"Usuário '{name}' cadastrado com sucesso!")
