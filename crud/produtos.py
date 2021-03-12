from sistema import dados_produtos
from arquivos import cria_arquivo, exclui_arquivo


class Produtos(object):
    def __init__(self, nome_produto='', preco_produto=0.0, quantidade_produto=0):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.quantidade_produto = quantidade_produto

    # Cadastra o produto no arquivo .csv
    def cadastro(self, arquivo):
        try:
            file = open(arquivo, 'at')
        except:
            print('Erro ao abrir arquivo')
        else:
            try:
                file.write(f'{self.nome_produto},R${self.preco_produto:0.2f},{self.quantidade_produto}\n')
            except:
                print('Erro ao cadastrar produto!')
            else:
                file.close()

    # Lê o arquivo .csv e mostra os produtos
    def mostrar_produtos(self, arquivo):
        try:
            file = open(arquivo, 'rt')
        except:
            print('Erro ao ler arquivo')
        else:
            print(f'\033[31m{"LISTA DE PRODUTOS".center(35)}\033[m')
            print('-' * 35)
            print(file.read(), end='')
            print('-' * 35)
            file.close()

    def remover_produtos(self, arquivo, produto):
        lista_produtos = dados_produtos()
        for produtos in lista_produtos:
            if produto == produtos['Nome']:
                lista_produtos.remove(produtos)
                exclui_arquivo(arquivo)
        cria_arquivo(arquivo)
        for produtos in lista_produtos:
            nome = str(produtos['Nome'])
            preco = float(produtos['Preco'][2:])
            quantidade = int(produtos['Quantidade'])
            novo_produto = Produtos(nome, preco, quantidade)
            novo_produto.cadastro(arquivo)

    # Função Responsavel por diminuir a quantidade de um produto, quando o pedido for adicionado ao carrinho e fechado o pedido
    def diminui_quantidade(self, arquivo, nome_produto, quantidade_produto):
        lista_produtos = dados_produtos()
        exclui_arquivo(arquivo)
        cria_arquivo(arquivo)
        for produtos in lista_produtos:
            nome = str(produtos['Nome'])
            preco = float(produtos['Preco'][2:])
            quantidade = int(produtos['Quantidade'])
            if nome_produto == nome:
                quantidade -= quantidade_produto
            produto = Produtos(nome, preco, quantidade)
            produto.cadastro(arquivo)

    # Função que altera um produto, caso o nome, preço ou quantidade esteja errado
    def alterar_produto(self, arquivo, produto):
        lista_produtos = dados_produtos()
        exclui_arquivo(arquivo)
        cria_arquivo(arquivo)
        for produtos in lista_produtos:
            if produtos['Nome'] == produto:
                indice_produto = str(input('O que deseja alterar:\n(Nome/Preco/Quantidade): ')).capitalize()
                if indice_produto == 'Nome':
                    novo_nome = str(input('Nome: ')).capitalize()
                    produto_alterado = Produtos(novo_nome, float(produtos['Preco'][2:]), int(produtos['Quantidade']))
                elif indice_produto == 'Preco':
                    novo_preco = float(input('Preco: R$'))
                    produto_alterado = Produtos(str(produtos['Nome']), novo_preco, int(produtos['Quantidade']))
                elif indice_produto == 'Quantidade':
                    nova_quantidade = int(input('Quantidade'))
                    produto_alterado = Produtos(str(produtos['Nome']), float(produtos['Preco'][2:]), nova_quantidade)
                else:
                    produto_alterado = Produtos(str(produtos['Nome']), float(produtos['Preco'][2:]),
                                                int(produtos['Quantidade']))
                produto_alterado.cadastro(arquivo)
            else:
                produto_alterado = Produtos(str(produtos['Nome']), float(produtos['Preco'][2:]),
                                            int(produtos['Quantidade']))
                produto_alterado.cadastro(arquivo)
