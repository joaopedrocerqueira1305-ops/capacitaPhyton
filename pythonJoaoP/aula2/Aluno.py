class Aluno:
    def __init__(self,nome,nota1,nota2):
        if isinstance(nome,str) and len(nome)>0:
            self.nome = nome
        else:
            raise ValueError("Nome invalido")
        
        if isinstance(nota1,(int,float)) and 0 <= nota1 <= 10:
            self.nota1 = nota1
        else:
            raise ValueError("Nota invalida")
        if isinstance(nota2,(int,float)) and 0 <= nota2 <= 10:
            self.nota2 = nota2
        else:
            raise ValueError("Nota invalida")

    def calcularMedia(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def situacao(self):
        if self.media >= 6:
            print(f"O aluno {self.nome} foi Aprovado com media {self.media:.2f}")
        else:
            print(f"O aluno {self.nome} foi Reprovado com media {self.media} , muito burro!")
        
nome = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

a1 = Aluno(nome, nota1, nota2)
a1.calcularMedia()
a1.situacao()