import csv
import os


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
            return True
        else:
            return False


# Verifica se o produto está cadastrado e se tem quantidade
def existe(dados, nome):
    for item in dados:
        if len(dados[0]) == 3:
            if item['Nome'] == nome and int(item['Quantidade']) > 0:
                return True, item
        else:
            if item['Nome'] == nome:
                return True, item


# Mostra o valor total das compras de um cliente
def mostrar_total(carrinho):
    total = 0
    print(f'\033[31m{"TOTAL".center(35)}\033[m')
    print('-' * 35)
    for produto in carrinho:
        total += float(produto['Preco'][2:])
        return total
    print('-' * 35)


# Mostra o carrinho de compras, quais produtos foram adicionados
def mostrar_carrinho(carrinho):
    print(f'\033[31m{"CARRINHO".center(36)}\033[m')
    print('-' * 35)
    for produto in carrinho:
        print(produto['Nome'], produto['Preco'])
    print('-' * 35)


# Remove algum produto do carrinho de compras
def remove_produto(carrinho, produto_removido):
    for chave, produto in enumerate(carrinho):
        if produto['Nome'] == produto_removido:
            print('\033[32mProduto removido com sucesso!\033[m')
            print('-' * 35)
            return True, chave


# Exclui arquivo
def exclui_arquivo(arquivo):
    os.unlink(arquivo)


# Menu para Logar no sistema como admin ou vendedor
def menu_login():
    print('-' * 35)
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
