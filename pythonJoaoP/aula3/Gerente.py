from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario_base,bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_pagamento(self):
        return super().calcular_pagamento() + self.bonus
        
g1 = Gerente("Carlos", 3000, 1500)
g1.exibir_informacoes()
print(f"O pagamento do gerente  é: R${g1.calcular_pagamento()}") 