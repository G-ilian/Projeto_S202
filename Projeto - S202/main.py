from Model.pa import Pa
from Model.martelo import Martelo
from Model.alicate import Alicate
from Model.carrinho_compras import Carrinho
import random

# Variáveis de controle do sistema
cart=Carrinho()

# Criando Produtos
print('------------------ Seja bem vindo (a) a Loja ------------------')
print('É um prazer termos você em nosso sistema')

# Funções auxiliares
def cabecalho():
    print('\n----- Lojas de ferramentas -----')
    print('''- Oferecemos os seguintes produtos -
        1 - Pá
        2 - Martelo
        3 - Alicate
    ''')

def mostrar_opcoes_de_compra_pa():
    print('''
        Pás 
        Opções: 
        [1] 
            Pá hiper forte
            Material : Aço
            Marca: Paraboni
            Valor[Unitário] : R$ 46.22
            
        [2] 
            Pá ultramega
            Material : Aço
            Marca: Tramontina
            Valor[Unitário] : R$ 43.50 
    ''')


def mostrar_opcoes_de_compra_martelo():
    print('''
        Martelo
        Opções: 
        [1] 
            Martelo mega blaster
            Material : Aço
            Marca: SpecOps
            Valor[Unitário] : R$ 294,12
            Peso: 0,625 kg

        [2] 
            Martelo mega poderoso
            Material : Aço
            Marca: Stanley
            Valor[Unitário] : R$ 43.50 
            Peso: 0,800 kg
    ''')


def mostrar_opcoes_de_compra_alicate():
    print('''
        Alicates
        Opções: 
        [1] 
            Alicate brabo 3000
            Marca: Tramontina
            Valor[Unitário] : R$ 38.00

        [2] 
            Alicate diferenciado 4000
            Marca: MTX
            Valor[Unitário] : R$ 27.80
    ''')


def cria_produtos(tProduto):

    if (tProduto == 1):
        idProduto=random.randint(1,10000)
        mostrar_opcoes_de_compra_pa()

        opcao=int(input('Digite a super pá que deseja: '))

        if(opcao==1):
            quant=int(input('Quantidade de pás: ')) # Cliente informa a quantidade de pás que ele deseja
            pa = Pa(idProduto, 'Paraboni', 'aço', 'Pá hiper forte',quant, 46.22)
            cart.adicionarProdutos(pa)

        if(opcao==2):
            quant2=int(input('Quantidade de pás: ')) # Cliente informa a quantidade de pás que ele deseja
            pa2 = Pa(idProduto, 'Tramontina', 'aço','Pá ultramega',quant2,43.50)
            cart.adicionarProdutos(pa2)

    if (tProduto==2):
        idProduto = random.randint(1, 10000)
        mostrar_opcoes_de_compra_martelo()

        opcao = int(input('Digite o martelo que deseja: '))

        if (opcao == 1):
            quant = int(input('Quantidade de martelos: '))  # Cliente informa a quantidade de pás que ele deseja
            cor=input('Cor do martelo: ')
            martelo= Martelo(idProduto,'SpecOps',cor,0.625,'Martelo mega blaster',quant,294.12)
            cart.adicionarProdutos(martelo)

        if (opcao == 2):
            quant2 = int(input('Quantidade de martelos: '))  # Cliente informa a quantidade de pás que ele deseja
            cor = input('Cor do martelo: ')
            martelo2 = Martelo(idProduto,'Stanley',cor,0.800,'Martelo mega poderoso',quant2,43.50)
            cart.adicionarProdutos(martelo2)

    if(tProduto==3):
        idProduto = random.randint(1, 10000)
        mostrar_opcoes_de_compra_alicate()

        opcao=int(input('Digite o alicate que deseja: '))

        if (opcao == 1):
            quant = int(input('Quantidade de alicates: '))  # Cliente informa a quantidade de pás que ele deseja
            cor=input('Cor do alicate: ')
            alicate=Alicate(idProduto,'Tramontina',cor,'Alicate brabo 3000',quant,38.00)
            cart.adicionarProdutos(alicate)

        if (opcao == 2):
            quant2 = int(input('Quantidade de alicates: '))  # Cliente informa a quantidade de pás que ele deseja
            cor=input('Cor do alicate: ')
            alicate2=Alicate(idProduto,'MTX',cor,'Alicate diferenciado 4000',quant2,27.80)
            cart.adicionarProdutos(alicate2)



while(1):
    print('''
        MENU:

        [C] - Adicionar novo produto ao carrinho
        [R] - Ver os produtos no carrinho
        [U] - Atualizar os produtos que estão no carrinho
        [D] - Excluir produtos no carrinho
        [S] - Sair
    ''')

    op=input('Digite a operação que você deseja: ')

    if(op.upper()=='C'):
        
        cabecalho()
        tProduto=int(input('Digite sua opção: '))
        cria_produtos(tProduto)


    if(op.upper()=='R'):
        cart.mostrarItens()

    if(op.upper()=='U'):
        print('---- ATUALIZANDO QUANTIDADE DE PRODUTOS ----')
        id=int(input('Id do produto que deseja atualizar: '))
        quantidade=int(input('Nova quantidade de produtos que deseja: '))
        cart.atualizarItens(id, quantidade)


    if(op.upper()=='D'):
        print('---- Deletando produtos ----')
        id=int(input('Id do produto que deseja deletar: '))
        cart.excluirItens(id)

    if(op.upper()=='S'):
        break

