usuarios = []
ui = 0

def novo_usuario(self, nome,senha):
    self.nome = str(input("Digite o nome do novo usuário: "))
    self.senha = str(input("Digite a senha do novo usuário: "))
    usuarios[ui] = {self.nome: self.senha}
    ui += 1
    print("Usuário criado com sucesso!")

def login():
    try:
        print("Digite o que deseja fazer!")
        print("1 - entrar")
        print("2 - criar novo usuario")
        print("3 - sair\n")
        opcao = int(input())
        if opcao >3 or opcao <1:
            raise ValueError
        elif opcao == 1:
            pass
        elif opcao == 2:
            novo_usuario()
        elif opcao == 3:
            print("Saindo...")
            exit()

    except ValueError:
        print("Valor inválido!\n Digite os números comforme cada opção\n digite 1 para entrar, 2 para criar novo usuario e 3 para sair")

while True:
    login()
    try:
        print(usuarios[0])
    except IndexError:
        pass