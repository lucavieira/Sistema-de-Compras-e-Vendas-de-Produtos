import csv


def dados_funcionarios():
    with open('funcionarios.csv') as funcionario:
        return [dado_funcionario for dado_funcionario in csv.DictReader(funcionario)]


def dados_produtos():
    with open('produtos.csv') as produtos:
        return [dado_produto for dado_produto in csv.DictReader(produtos)]


def verifica_login(dados, nome, senha):
    for funcionario in dados:
        if funcionario['Nome'] == nome and funcionario['Senha'] == senha and funcionario['Cargo'] == 'Admin':
            return True
        else:
            return False


def existe_produto(dados, nome_produto):
    for produto in dados:
        if produto['Nome'] == nome_produto and int(produto['Quantidade']) > 0:
            print('\033[32mProduto Adicionado com Sucesso\033[m')
            print('-' * 35)
            return True, produto
        else:
            return False, nome_produto


def mostrar_total(carrinho):
    total = 0
    print(f'\033[31m{"TOTAL".center(35)}\033[m')
    print('-' * 35)
    for produto in carrinho:
        total += float(produto['Preco'][2:])
        return total
    print('-' * 35)


def mostrar_carrinho(carrinho):
    print(f'\033[31m{"CARRINHO".center(36)}\033[m')
    print('-' * 35)
    for produto in carrinho:
        print(produto['Nome'], produto['Preco'])
    print('-' * 35)


def remove_produto(carrinho, produto_removido):
    for chave, produto in enumerate(carrinho):
        if produto['Nome'] == produto_removido:
            print('\033[32mProduto removido com sucesso!\033[m')
            print('-' * 35)
            return True, chave


def menu_login():
    print('-' * 35)
    print(f'{"LOGIN".center(35)}')
    print('-' * 35)
    nome = str(input('Nome: ')).capitalize()
    senha = str(input('Senha: ')).lower()
    print('-' * 35)
    return nome, senha


def menu_funcionario(*opcoes):
    for opcao in opcoes:
        print(opcao)
    comando = str(input('Digite o que deseja: '))
    print('-' * 35)
    return comando
