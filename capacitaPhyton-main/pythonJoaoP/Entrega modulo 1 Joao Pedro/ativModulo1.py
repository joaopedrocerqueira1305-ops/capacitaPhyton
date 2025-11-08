import os
import time

usuarios = []
filmes = []
i=0
home = 0

def Home():
    global home_opcao
    print(f"-- Bem vindo ao sistema de avaliar filmes, {nome}! --\n")
    print("1 - adicionar Filme")
    print("2 - avaliar e ver filmes")
    print("3 - ver usuários")
    print("4 - logout")
    print("5 - sair do sistema\n")
    home_opcao = int(input())

while True:
    try: 
        if home != 1:
            print("| Sistema de avaliar filmes |\n")
            print("Digite o que deseja fazer!")
            print("1 - entrar")
            print("2 - criar novo usuario")
            print("3 - sair\n")
            opcao = int(input())
            if opcao >3 or opcao <1:
                raise ValueError
            
            elif opcao == 1:
                if usuarios == []:
                    print("Nenhum usuário cadastrado! Crie um novo usuário.\n")
                    continue
                nome = str(input("Digíte o seu nome :\n")).strip()
                senha = str(input("Digíte a sua senha :\n")).strip()
                for usuario in usuarios:
                    if usuario['nome'] == nome and usuario['senha'] == senha:
                        os.system('cls' if os.name == 'nt' else 'clear') # comando para limpar a tela
                        print("Login realizado com sucesso!")
                        home = 1
                    else:
                        i += 1
                        if i == len(usuarios):
                            print("Usuário ou senha incorretos!")
                i=0
            
            elif opcao == 2:
                nome = str(input("Digíte o nome do novo usuário:\n")).strip()
                senha = str(input("Digíte a senha do novo usuário:\n")).strip()
                usuarios.append({'nome': nome, 'senha': senha})
                os.system('cls' if os.name == 'nt' else 'clear') # comando para limpar a tela
                print("Usuário CASDASTRADO com sucesso!")
    
            elif opcao == 3:
                print("Saindo...")
                exit()

    except ValueError:
        print("Valor inválido! Digíte a opção corretamente\n")
    try:
        while home == 1:
            Home()
            if home_opcao == 1:
                print("-+- Adicionar um novo filme -+-")
                titulo = str(input("título: ")).strip()
                data = int(input("Ano de lançamento: "))
                genero = str(input("Gênero: ")).strip()
                notaUsuarios = []
                notaGeral = 0 # sum(notaUsuarios) / len(notaUsuarios)
                filmes.append({'titulo': titulo, 'data': data, 'genero':genero, 'notaGeral':notaGeral, 'notaUsuarios':notaUsuarios})
                
                os.system('cls' if os.name == 'nt' else 'clear') # comando para limpar a tela

                print("filme CASDASTRADO com sucesso! digíte 2 para avalia-lo")

            elif home_opcao == 2:
                print("- _Lista de filmes do sistema_ -")

                for filme in filmes:
                    i+=1
                    print(f"{i} - {filme['titulo']}")
                    print(f"Ano de lançamento: {filme['data']}  ,  Gênero: {filme['genero']}")
                    if filme['notaGeral'] == 0:
                        print(f"Nota -/10")
                    else:
                        print(f"Nota {filme['notaGeral']}/10")
                    if filme['notaUsuarios'] == 0:
                        print(f"Sua Nota -")
                    else:
                        print(f"Sua Nota {filme['notaUsuarios']}\n")
                                    
                i=0
                opcao_filme = input("Digíte o número correspndente ao filme para avalial-lo ou 'V' para voltar\n")
                if opcao_filme == "v":
                    continue
                else:
                    for filme in filmes:
                        i+=1
                        if i == opcao_filme:
                            print(f"{i} - {filme['titulo']}")
                            print(f"Ano de lançamento: {filme['data']}  ,  Gênero: {filme['genero']}")
                            nota = int(input("Digíte um nota de 1 a 10"))
                            filme['notaUsuarios'] = (nome, nota)
                            notaGeral = sum(filme['notaUsuarios']) / len(filme['notaUsuarios'])

            elif home_opcao == 3:
                print("Lista de usuários cadastrados:")
                for usuario in usuarios:
                    if usuario['nome'] == nome:
                        print(f" -> {usuario['nome']}")
                    else:
                        print(f" - {usuario['nome']}")
                time.sleep(1.8)
                print("\n")

            elif home_opcao == 4:
                print("Fazendo logout...\n")
                home = 0

            elif home_opcao == 5:
                print("Saindo...")
                exit()

            elif home_opcao >5 or home_opcao <1:
                raise ValueError
    except ValueError:
        print("Valor inválido! Digíte corretamente\n")