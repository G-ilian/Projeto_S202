from Model.produto import Produto

class Martelo(Produto):
    # Construtor
    def __init__(self,idProduto,marca,cor,peso,nome,quantidade,valor):
        super().__init__(nome, quantidade, valor)
        self.id=idProduto
        self.marca=marca
        self.cor=cor
        self.peso=peso