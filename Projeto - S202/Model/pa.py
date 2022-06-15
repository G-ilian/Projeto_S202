from Model.produto import Produto


class Pa(Produto):
    # Construtor
    def __init__(self,idProduto,marca,material,nome,quantidade,valor):
        super().__init__(nome,quantidade,valor)
        self.id=idProduto
        self.marca=marca
        self.material_fabri=material

