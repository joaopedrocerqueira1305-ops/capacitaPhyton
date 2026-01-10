from Carro import Carro
from Caminhao import Caminhao
from Moto import Moto

vlista = []
cr1 = Carro("carro A")
vlista.append(cr1)
c1 = Caminhao("caminhao A")
vlista.append(c1)
m1 = Moto("moto A")
vlista.append(m1) 
for veiculo in vlista:
    veiculo.descricao()