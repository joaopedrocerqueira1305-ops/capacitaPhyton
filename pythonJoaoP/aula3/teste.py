class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som():
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    
class Passaro(Animal):
    def emitir_som(self):
        return "piu piu"
    
animais = [Cachorro("Rex"), Gato("Tom"), Passaro("Pica-pau")]
for animal in animais:
    print(f"{animal.nome}: {animal.emitir_som()}")