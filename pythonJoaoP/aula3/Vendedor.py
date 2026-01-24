from Funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        super().__init__(nome, salario_base)
        self.comissao = comissao

    def calcular_pagamento(self):
        return super().calcular_pagamento() + self.comissao
    
v1 = Vendedor("Mariana", 4000, 800)
f1 = Funcionario("Pedro", 1000)
f1.exibir_informacoes()
v1.exibir_informacoes()
print(f"O pagamento do vendedor é: R${v1.calcular_pagamento()}")