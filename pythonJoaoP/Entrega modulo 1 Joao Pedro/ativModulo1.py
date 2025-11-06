import os
import time

usuarios = []
filmes = []
i=0
home = 0
home_opcao = 0

def Home():
    global home_opcao
    print(f"-- Bem vindo ao sistema de avaliar filmes {nome}! --\n")
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
                pass

            if home_opcao == 2:
                pass

            if home_opcao == 3:
                print("Lista de usuários cadastrados:")
                for usuario in usuarios:
                    print(f" - {usuario['nome']}")
                time.sleep(1.0)
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
        print("Opção inválido! Digíte a opção corretamente\n")