import sqlite3

# CONEXÃO COM O BANCO DE DADOS
conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

# RECEBER DADOS DO LIVRO
title = input('Digite o nome do livro: ')
author = input('Digite o author do livro: ')

# INSERIR DADOS AO BANCO
cursor.execute("""
    INSERT INTO books (title, author) VALUES (?,?)
""", (title, author))

# SALVAR TARNSAÇÃO E FECHAR CONEXÃO
conn.commit()
conn.close()

print(f"Livro '{title}' cadastrado com sucesso!") 