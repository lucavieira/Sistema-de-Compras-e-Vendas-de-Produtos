from arquivos import *

# Um dicionario com todos os arquivos
arquivos = {'arquivo_produtos': 'produtos.txt', 'arquivo_funcionarios': 'funcionarios.txt'}

# Para cada arquivo no dicionario, verifica se ja existe, caso não exista, cria o arquivo
for arquivo in arquivos.values():
    if not existe_arquivo(arquivo):
        cria_arquivo(arquivo)
