class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.__email = email
        self.__senha = senha

    def criarNovoUsuario(self, nome, email, senha):
        while True:
            nome = str(input("Digite seu nome: "))
        
            email = str(input("Digite seu email: "))
            for usuarios in Usuario:
                if usuarios['email'] == email:
                    print("Email já cadastrado , por favor tente novamente")
                    break
                else:
                    i += 1
                    if i == len(usuarios):
                        return False
        
            senha = str(input("Digite sua senha: "))

            return Usuario(nome, email, senha)
            

    def fazerLogin(self, nome, email, senha):
        if self.__email == email and self.__senha == senha:
            return True
        else:
            return False # deve estar errado 