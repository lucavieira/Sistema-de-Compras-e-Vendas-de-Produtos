class Produtos(object):
    def __init__(self, nome_produto='', preco_produto=0.0, quantidade_produto=0):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.quantidade_produto = quantidade_produto

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
                print(f'{self.nome_produto} cadastrado com sucesso!')
                file.close()

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
