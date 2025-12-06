class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir_informacoes(self):
        print(f"Carro da marca {self.marca} modelo {self.modelo} do ano de {self.ano}")
    def ligar(self):
        print(f"O {self.marca} esta ligado!")

c1 = Carro("Ford","Ka",2020)
c2 = Carro("Chevrolet","Onix",2021)
c1.exibir_informacoes()
c1.ligar()
c2.ligar()