# id_cliente: ultimo+1

# nome: Marcos Silva

# idade: 32

# sexo: 'M'

# email: marcos.silva@email.com

# telefone: (71)99999-1111

# endereço: Rua A, 123

# cidade: Salvador

# estado: BA

# cep: 40000-000

# data_cadastro: 2025-01-10

import sqlite3
# faz o tratamento de excecao
try:
    # cria o objeto conexao (con)
    con = sqlite3.Connection("cliente.db")
    cursor = con.cursor()
    res = cursor.execute("select name from sqlite_master ")
    print(f"Tabelas do banco cliente.db: {res.fetchone()}")
    
    # imprime o resultado: fetchone para uma linha, fetchall para varias
    res = cursor.execute("INSERT INTO cliente (id_cliente, nome, idade) "
    "values (9, 'Joao Souza', 45)")
    con.commit()
    con.close()

except Exception as e:
    print(f"Erro: {e}")
else:
    print(res.fetchall())
finally:
    # fechando o cursor
    cursor.close()
    # fechando a conexão
    con.close()