from Model.produto import Produto

class Alicate(Produto):
    # Construtor
    def __init__(self,idProduto,marca,cor,nome,quantidade,valor):
        super().__init__(nome, quantidade, valor)
        self.id=idProduto
        self.marca=marca
        self.cor=cor