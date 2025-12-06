class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.__email = email
        self.__senha = senha

    def criarNovoUsuario(self, nome, email, senha):
        nome = str(input("Digite seu nome: "))
        while True:
            email = str(input("Digite seu email: "))
            for usuarios in Usuario:
                if usuarios['email'] == email:
                    print("Email já cadastrado , por favor tente novamente")
                else:
                    return False
        
        senha = str(input("Digite sua senha: "))

        self.nome = nome
        self.__email = email
        self.__senha = senha

    def fazerLogin(self, email, senha):
        if self.__email == email and self.__senha == senha:
            return True
        else:
            return False # deve estar errado 