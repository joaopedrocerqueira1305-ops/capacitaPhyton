class Veiculo:
    def __init__(self,nome):
        self.nome = nome

    def dirigir(self):
        return(f"O veículo está se movendo")

    def descricao(self):
        print(f"{self.__class__.__name__}:{self.dirigir()}")