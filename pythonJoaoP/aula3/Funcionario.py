class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.__salario_base = salario_base

    def calcular_pagamento(self):
        return self.__salario_base
    
    def exibir_informacoes(self):
        print(f"Funcionário: {self.nome} - Salário: R${self.calcular_pagamento()}")