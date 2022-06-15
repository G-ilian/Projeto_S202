from database.database import Database
from Model.pa import Pa
import pprint

db=Database("ProjetoS202","Produtos",None)

class Carrinho():
    lista_produtos=[]
    def __init__(self) -> None:
        pass

    def adicionarProdutos(self,object):
        self.lista_produtos.append(object)
        for produto in self.lista_produtos:

            if(len(self.lista_produtos)>0):
                if(produto.nome.startswith('Pá')):
                    print('\n---- Cadastrando Pá ----')
                    if(produto.quantidade>0):
                        db.create_product_shovel(produto.nome,produto.quantidade,produto.id,produto.marca,produto.material_fabri,produto.valor)
                    else:
                        print('A quantidade de itens deve ser maior que 0')

                if(produto.nome.startswith('Alicate')):
                    print('\n---- Cadastrando Alicate ----')
                    if(produto.quantidade>0):
                        db.create_product_pliers(produto.nome,produto.quantidade,produto.id,produto.marca,produto.cor,produto.valor)
                    else:
                        print('A quantidade de itens deve ser maior que 0')

                if(produto.nome.startswith('Martelo')):
                    print('\n---- Cadastrando Martelo ----')
                    if(produto.quantidade>0):
                        db.create_product_hammer(produto.nome,produto.quantidade,produto.id,produto.marca,produto.cor,produto.peso,produto.valor)
                    else:
                        print('A quantidade de itens deve ser maior que 0')
                self.lista_produtos.pop()
            else:
                print('Lista vazia, não foi possível adicionar nenhum produto !! ')

    def mostrarItens(self):
        print('--- Itens presentes em seu carrinho ---')
        itens=db.read_product()
        for item in itens:
            print(item)

    def atualizarItens(self,id,quantidade):
        print('--- Atualizando itens ---')
        if(quantidade>0):
            db.update_product(id,quantidade)
        else:
            print('A quantidade de itens deve ser maior que 0')

    def excluirItens(self,id):
        print('--- Excluindo itens ---')
        db.delete_product(id)