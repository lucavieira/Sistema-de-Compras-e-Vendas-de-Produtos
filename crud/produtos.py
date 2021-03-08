class Produtos(object):
    def __init__(self, nome_produto, preco_produto, quantidade_produto):
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
            print('-' * 30)
            print(f'{"LISTA DE PRODUTOS".center(30)}')
            print('-' * 30)
            print(file.read(), end='')
            print('-' * 30)
            file.close()
