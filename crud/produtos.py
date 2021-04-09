from sistema import dados_produtos
from arquivos import cria_arquivo, exclui_arquivo
import pandas as pd


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
                file.write(f'{self.nome_produto},R${self.preco_produto:.2f},{self.quantidade_produto}\n')
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
        lista_produtos = pd.read_csv(arquivo)
        for indice in lista_produtos.index:
            if lista_produtos.loc[indice, 'Nome'] == produto:
                lista_produtos.drop(indice, inplace=True)
            lista_produtos.to_csv(arquivo, index=False)

    # Função Responsavel por diminuir a quantidade de um produto, quando o pedido for adicionado ao carrinho e fechado o pedido
    def diminui_quantidade(self, arquivo, nome_produto, quantidade_produto):
        lista_produtos = pd.read_csv(arquivo)
        for indice in lista_produtos.index:
            if lista_produtos.loc[indice, 'Nome'] == nome_produto:
                lista_produtos.loc[indice, 'Quantidade'] -= quantidade_produto
            lista_produtos.to_csv(arquivo, index=False)

    # Função que altera um produto, caso o nome, preço ou quantidade esteja errado
    def alterar_produto(self, arquivo, produto):
        lista_produtos = pd.read_csv(arquivo)
        for indice in lista_produtos.index:
            if lista_produtos.loc[indice, 'Nome'] == produto:
                indice_produto = str(input('O que deseja alterar:\n(Nome/Preco/Quantidade): ')).capitalize()
                if indice_produto == 'Nome':
                    novo_nome = str(input('Nome: ')).capitalize()
                    lista_produtos.loc[indice, indice_produto] = novo_nome
                elif indice_produto == 'Preco':
                    novo_preco = float(input('Preco: R$'))
                    lista_produtos.loc[indice, indice_produto] = f'R${novo_preco:.2f}'
                elif indice_produto == 'Quantidade':
                    nova_quantidade = int(input('Quantidade: '))
                    lista_produtos.loc[indice, indice_produto] = nova_quantidade
                else:
                    print('-' * 35)
                    print('\033[31mNenhum dado foi alterado\033[m')
                    print('-' * 35)
                lista_produtos.to_csv(arquivo, index=False)
