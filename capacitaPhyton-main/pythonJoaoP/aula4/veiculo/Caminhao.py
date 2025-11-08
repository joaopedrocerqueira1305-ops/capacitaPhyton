from Veiculo import Veiculo


class Caminhao(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)

    def dirigir(self):
        return (f"O caminhão está transportando carga.")