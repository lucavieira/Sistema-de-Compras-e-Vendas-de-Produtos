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
        file.close()
        try:
            file = open(arquivo, 'at')
        except:
            print('Erro ao abrir arquivo')
        else:
            if arquivo == 'produtos.csv':
                file.write('Nome,Preco,Quantidade\n')
                file.close()
            else:
                file.write('Nome,CPF,Senha,Cargo\n')
                file.close()
