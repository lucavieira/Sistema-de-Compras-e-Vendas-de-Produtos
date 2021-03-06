import csv


# Pega os dados dos funcionarios
def dados_funcionarios():
    with open('funcionarios.csv') as funcionario:
        return [dado_funcionario for dado_funcionario in csv.DictReader(funcionario)]


# Pega os dados dos produtos
def dados_produtos():
    with open('produtos.csv') as produtos:
        return [dado_produto for dado_produto in csv.DictReader(produtos)]


# Verifica o login, se é admin ou vendedor
def verifica_login(dados, nome, senha):
    for funcionario in dados:
        if funcionario['Nome'] == nome and funcionario['Senha'] == senha and funcionario['Cargo'] == 'Admin':
            return 'Admin'
        elif funcionario['Nome'] == nome and funcionario['Senha'] == senha and funcionario['Cargo'] == 'Vendedor':
            return 'Vendedor'
        else:
            return False


# Verifica se o produto está cadastrado e se tem quantidade
def existe(dados, nome, quantidade_produto=0):
    for item in dados:
        if len(dados[0]) == 3:
            if item['Nome'] == nome and int(item['Quantidade']) >= quantidade_produto:
                return True, item
        else:
            if item['Nome'] == nome:
                return True, item


# Mostra o valor total das compras de um cliente
def mostrar_total(carrinho, quantidade_produto):
    total = 0
    print(f'\033[31m{"TOTAL".center(35)}\033[m')
    for produto in carrinho:
        total += (float(produto['Preco'][2:]) * quantidade_produto)
    print('-' * 35)
    return total


# Mostra o carrinho de compras, quais produtos foram adicionados
def mostrar_carrinho(carrinho, quantidade_produto):
    print(f'\033[31m{"CARRINHO".center(36)}\033[m')
    print('-' * 35)
    for produto in carrinho:
        print(produto['Nome'], produto['Preco'], quantidade_produto)
    print('-' * 35)


# Remove algum produto do carrinho de compras
def remove_produto(carrinho, produto_removido):
    for chave, produto in enumerate(carrinho):
        if produto['Nome'] == produto_removido:
            print('\033[32mProduto removido com sucesso!\033[m')
            print('-' * 35)
            return True, chave


# Menu para Logar no sistema como admin ou vendedor
def menu_login():
    print('-' * 100)
    if len(dados_funcionarios()) == 0:
        print('Olá, bem-vindo ao sistema de vendas, essa é sua primeira vez, então cadastre um login de Admin\n'
              'para poder utilizar o sistema por completo.')
        print('-' * 100)
        nome = str(input('Nome: ')).capitalize()
        senha = str(input('Senha: ')).lower()
        cpf = int(input('CPF: '))
        print('-' * 35)
        return nome, senha, cpf, 'Admin'
    else:
        print(f'{"LOGIN".center(35)}')
        print('-' * 35)
        nome = str(input('Nome: ')).capitalize()
        senha = str(input('Senha: ')).lower()
        print('-' * 35)
        return nome, senha


# Menu com as opções de admin e vendedor
def menu_funcionario(*opcoes):
    for opcao in opcoes:
        print(opcao)
    comando = str(input('Digite o que deseja: '))
    print('-' * 35)
    return comando
