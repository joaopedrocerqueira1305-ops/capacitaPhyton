from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, sexo, raca):
        super().__init__(nome, sexo)
        self.raca = raca

    def emitir_som(self):
        return (f"O cachorro {self.nome} da raça {self.raca} faz: Au Au")
    
c1 = Cachorro("Rex","Macho","Pastor Alemão")
print(c1.emitir_som())