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
    nome = input("informe o nome: ")
    p1 = Pessoa(nome,'eduarda',20)
    p1.apresentar()
except ValueError:
    print("valor errado")