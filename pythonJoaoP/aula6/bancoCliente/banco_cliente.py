# importa a biblioteca sqlite
import sqlite3
# faz o tratamento de excecao
try:
    # cria o objeto conexao (con)
    con = sqlite3.Connection("cliente.db")
    # cria o cursor com a conexao (envia comandos)
    cursor = con.cursor()
    # variavel que armazena comando de criacao da tabela
    sql_create_cliente = '''-- Criação da tabela cliente
    CREATE TABLE if not exists cliente (
        id_cliente INT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT,
        sexo CHAR(1),
        email VARCHAR(150),
        telefone VARCHAR(20),
        endereco VARCHAR(200),
        cidade VARCHAR(100),
        estado CHAR(2),
        cep VARCHAR(10),
        data_cadastro DATE
    );
    '''
    # executando o sql com o cursor
    cursor.execute(sql_create_cliente)

    # variavel que armazena comando de insercao de dados na tabela
    sql_insert_cliente = '''-- Inserção de dados fictícios
    INSERT INTO cliente (id_cliente, nome, idade, sexo, email, telefone, endereco, cidade, estado, cep, data_cadastro) VALUES
    (1, 'Ana Paula Ferreira', 28, 'F', 'ana.paula@email.com', '11987654321',
    'Rua das Flores, 120', 'São Paulo', 'SP', '04567-900', '2025-01-10'),

    (2, 'Carlos Eduardo Silva', 34, 'M', 'carlossilva@email.com', '11999887766',
    'Av. Paulista, 1500', 'São Paulo', 'SP', '01310-200', '2025-02-05'),

    (3, 'Mariana Lopes', 22, 'F', 'marilopes@email.com', '21988776655',
    'Rua das Acácias, 45', 'Rio de Janeiro', 'RJ', '22030-001', '2025-02-12'),

    (4, 'Rafael Gomes', 40, 'M', 'rafaelgomes@email.com', '31999884422',
    'Rua Goiás, 300', 'Belo Horizonte', 'MG', '30160-040', '2025-03-01'),

    (5, 'Beatriz Santos', 31, 'F', 'biasantos@email.com', '41988774466',
    'Rua das Araucárias, 77', 'Curitiba', 'PR', '82560-900', '2025-03-15'),

    (6, 'João Batista', 29, 'M', 'joaobatista@email.com', '51988774433',
    'Av. Borges de Medeiros, 900', 'Porto Alegre', 'RS', '90020-040', '2025-04-01'),

    (7, 'Julia Andrade', 26, 'F', 'julia.andrade@email.com', '61999885544',
    'QS 11 Conjunto 4', 'Brasília', 'DF', '72025-111', '2025-04-10');
    '''
    cursor.execute(sql_insert_cliente)
# captura excecao, se houver
except Exception as e:
    # desfaz a operacao
    con.rollback()
    # imprime a execao, se houver
    print(f"Erro: {e}")
else:
    con.commit()
finally:
    # fecha o cursor
    cursor.close()
    # fecha a conexão
    con.close()
