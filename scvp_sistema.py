from arquivos import *
from crud.produtos import *
from crud.funcionarios import *

# Um dicionario com todos os arquivos
arquivos = {'arquivo_produtos': 'produtos.csv', 'arquivo_funcionarios': 'funcionarios.csv'}

# Para cada arquivo no dicionario, verifica se ja existe, caso não exista, cria o arquivo
for arquivo in arquivos.values():
    if not existe_arquivo(arquivo):
        cria_arquivo(arquivo)

produto = Produtos('Carro', 500000, 5)
produto.cadastro(arquivos['arquivo_produtos'])
produto.mostrar_produtos(arquivos['arquivo_produtos'])