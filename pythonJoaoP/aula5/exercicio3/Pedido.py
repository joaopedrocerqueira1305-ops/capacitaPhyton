class QuantidadeInvalidaErro(Exception):
    def __init__(self,quantidade):
        super().__init__(f"quantidade inválida: ")
        

class Pedido:
    def __init__(self,item,quantidade):
        self.item =  item
        self.quantidade = quantidade

    def definirQuantidade(self,quantidade):
        if quantidade <= 0:
            raise QuantidadeIvaladaErro(quantidade)
        
    def resumo(self):
        return (f"O pedido é {self.item} e a quantidade é {self.quantidade}")
