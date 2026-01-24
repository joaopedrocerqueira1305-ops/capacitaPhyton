import sqlite3

# =========================
# CONEXÃO COM O BANCO
# =========================


def abrir_conexao():
    conn = sqlite3.connect("escola.db")
    cursor = conn.cursor()
    return conn, cursor


def fechar_conexao(conn):
    conn.close()


# abre conexão global
conn, cursor = abrir_conexao()


# =========================
# CADASTROS (CREATE)
# =========================

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    cpf = input("cpf do aluno: ")
    data_nascimento = input("data de nascimento do aluno: ")
    cursor.execute("INSERT INTO alunos (nome) VALUES (?)", (nome,))
    conn.commit()
    print("Aluno cadastrado com sucesso!")


def cadastrar_professor():
    nome = input("Nome do professor: ")
    cursor.execute(
        "INSERT INTO professores (nome, contrato) VALUES (?, ?)",
        (nome, None)
    )
    conn.commit()
    print("Professor cadastrado com sucesso!")


def cadastrar_curso():
    nome = input("Nome do curso: ")
    cursor.execute(
        "INSERT INTO cursos (nome, professor_id) VALUES (?, ?)",
        (nome, None)
    )
    conn.commit()
    print("Curso cadastrado com sucesso!")


# =========================
# CONSULTAS (READ)
# =========================

def listar_alunos():
    cursor.execute("SELECT id, nome FROM alunos")
    alunos = cursor.fetchall()

    print("\n--- ALUNOS ---")
    for a in alunos:
        print(a)


def listar_professores():
    cursor.execute("SELECT id, nome, contrato FROM professores")
    professores = cursor.fetchall()

    print("\n--- PROFESSORES ---")
    for p in professores:
        print(p)


def listar_cursos():
    cursor.execute("""
        SELECT *
        FROM curso
    """)
    cursos = cursor.fetchall()

    print("\n--- CURSOS ---")
    for c in cursos:
        print(c)


# =========================
# REGRAS DE NEGÓCIO
# =========================

def matricular_aluno():
    listar_alunos()
    aluno_id = int(input("ID do aluno: "))

    listar_cursos()
    curso_id = int(input("ID do curso: "))

    cursor.execute(
        "INSERT INTO matriculas (aluno_id, curso_id) VALUES (?, ?)",
        (aluno_id, curso_id)
    )
    conn.commit()
    print("Aluno matriculado com sucesso!")


def designar_professor():
    listar_professores()
    professor_id = int(input("ID do professor: "))

    listar_cursos()
    curso_id = int(input("ID do curso: "))

    cursor.execute(
        "UPDATE cursos SET professor_id = ? WHERE id = ?",
        (professor_id, curso_id)
    )
    conn.commit()
    print("Professor designado ao curso!")


def atribuir_contrato():
    listar_professores()
    professor_id = int(input("ID do professor: "))

    contrato = input("Tipo de contrato (CLT / PJ / Horista): ")

    cursor.execute(
        "UPDATE professores SET contrato = ? WHERE id = ?",
        (contrato, professor_id)
    )
    conn.commit()
    print("Contrato atribuído com sucesso!")


# =========================
# MENU PRINCIPAL (SWITCH CASE)
# =========================

def menu():
    while True:
        print("\n=== SISTEMA ESCOLAR (SQLite) ===")
        print("1 - Cadastrar aluno")
        print("2 - Cadastrar professor")
        print("3 - Cadastrar curso")
        print("4 - Listar alunos")
        print("5 - Listar professores")
        print("6 - Listar cursos")
        print("7 - Matricular aluno em curso")
        print("8 - Designar professor ao curso")
        print("9 - Atribuir contrato ao professor")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_aluno()
            case "2":
                cadastrar_professor()
            case "3":
                cadastrar_curso()
            case "4":
                listar_alunos()
            case "5":
                listar_professores()
            case "6":
                listar_cursos()
            case "7":
                matricular_aluno()
            case "8":
                designar_professor()
            case "9":
                atribuir_contrato()
            case "0":
                print("Encerrando sistema...")
                fechar_conexao(conn)
                break
            case _:
                print("Opção inválida!")


# =========================
# EXECUÇÃO
# =========================

menu()