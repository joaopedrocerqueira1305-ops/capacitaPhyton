class Retangulo:
    def __init__(self,altura,largura):
        self.__altura = altura
        self.__largura = largura

    def area(self):
        return self.__altura * self.__largura        

    def perimetro(self):
        return (self.__altura*2)+(self.__largura*2)
    
    def set_largura(self,nova_largura):
        self.__largura = nova_largura
    def get_largura(self):
        return self.__largura
    
    def set_altura(self, nova_altura):
        self.__altura = nova_altura
    def get_altura(self):
        return self.__altura
    

try:
    retangulo = Retangulo(6,4)
    print(f"Área: {retangulo.area()}")
    print(f"Perímetro: {retangulo.perimetro()}")
    retangulo.set_altura(8)
    retangulo.set_largura(10)
    print(f"Área: {retangulo.area()}")
    print(f"Perímetro: {retangulo.perimetro()}")
except Exception as e:
    print(f"Erro {e}")