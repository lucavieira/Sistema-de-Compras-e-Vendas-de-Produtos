# Verifica se o arquivo existe
def existe_arquivo(arquivo):
    try:
        file = open(arquivo, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


# Cria o arquivo
def cria_arquivo(arquivo):
    try:
        file = open(arquivo, 'wt+')
    except:
        print('Erro ao criar arquivo')
    else:
        print('Arquivo criado com Sucesso')
