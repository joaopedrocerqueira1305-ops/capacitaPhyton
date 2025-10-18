class Pessoa:
    def __init__(self,nome,sobrenome,idade):
        if nome!="":
            self.nome = nome
        else:
            raise ValueError
        self.sobrenome = sobrenome
        self.idade = idade

    def apresentar(self):
        print(f"nome: {self.nome} sobrenome: {self.sobrenome}\nidade: {self.idade}")
try:
    p1 = Pessoa('','eduarda',20)
    p1.apresentar()
except ValueError:
    print("valor errado")