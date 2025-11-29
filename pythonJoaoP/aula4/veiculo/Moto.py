from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)

    def dirigir(self):
        return (f"A moto está fazendo uma curva.")