from arquivos import *
from crud.produtos import *
from crud.funcionarios import *
from sistema import menu_login, menu_funcionario, verifica_login, mostrar_carrinho, mostrar_total, remove_produto,\
    existe, dados_funcionarios, dados_produtos

# Um dicionario com todos os arquivos
arquivos = {'arquivo_produtos': 'produtos.csv', 'arquivo_funcionarios': 'funcionarios.csv'}
# Criando os Objetos
produtos = Produtos()
funcionarios = Funcionarios()

# Para cada arquivo no dicionario, verifica se ja existe, caso não exista, cria o arquivo
for arquivo in arquivos.values():
    if not existe_arquivo(arquivo):
        cria_arquivo(arquivo)

# Menu Login
carrinho = list()
menu = menu_login()
while True:
    if len(menu) == 4:
        funcionarios = Funcionarios(menu[0], menu[2], menu[1], menu[3])
        funcionarios.cadastro(arquivos['arquivo_funcionarios'])
        print('Por gentileza, reinicie o programa para atualizar os dados.')
        break
    if verifica_login(dados_funcionarios(), menu[0], menu[1]) == 'Admin':
        print(f'Bem-Vindo {menu[0]} Admin'.center(35))
        print('-' * 35)
        menu_adm = menu_funcionario('Cadastrar Produtos (CP)', 'Cadastrar Funcionarios (CF)', 'Remover Produtos (RP)', 'Remover Funcionarios (RF)', 'Alterar Produto (AP)', 'Alterar Funcionario (AF)', 'Sair').upper()
        if menu_adm == 'CP':
            print(f'\033[31m{"CADASTRO DE PRODUTOS".center(36)}\033[m')
            print('-' * 35)
            nome = str(input('Nome do Produto: ')).capitalize()
            preco = float(input('Preco do Produto: '))
            quantidade = int(input('Quantidade: '))
            produtos = Produtos(nome, preco, quantidade)
            produtos.cadastro(arquivos['arquivo_produtos'])
            print(f'\033[32m{nome} cadastrado com sucesso!\033[m')
            print('-' * 35)
        elif menu_adm == 'CF':
            print(f'\033[31m{"CADASTRO DE FUNCIONARIOS".center(36)}\033[m')
            print('-' * 35)
            nome = str(input('Nome do Funcionario: ')).capitalize()
            cpf = int(input('CPF: '))
            senha = str(input('Senha: '))
            cargo = str(input('Cargo [Adm/Vendedor]: '))
            funcionario = Funcionarios(nome, cpf, senha, cargo)
            funcionario.cadastro(arquivos['arquivo_funcionarios'])
            print('-' * 35)
        elif menu_adm == 'RP':
            produtos.mostrar_produtos(arquivos['arquivo_produtos'])
            produto_excluido = str(input('Qual produto deseja excluir: ')).capitalize()
            print('-' * 35)
            if existe(dados_produtos(), produto_excluido)[0]:
                produtos.remover_produtos(arquivos['arquivo_produtos'], produto_excluido)
        elif menu_adm == 'RF':
            funcionarios.mostrar_funcionarios(arquivos['arquivo_funcionarios'])
            funcionario_excluido = str(input('Qual funcionario deseja excluir: ')).capitalize()
            print('-' * 35)
            if existe(dados_funcionarios(), funcionario_excluido)[0]:
                funcionarios.remover_funcionario(arquivos['arquivo_funcionarios'], funcionario_excluido)
        elif menu_adm == 'AP':
            produtos.mostrar_produtos(arquivos['arquivo_produtos'])
            produto_alterado = str(input('Qual produto deseja alterar: ')).capitalize()
            if existe(dados_produtos(), produto_alterado)[0]:
                produtos.alterar_produto(arquivos['arquivo_produtos'], produto_alterado)
        elif menu_adm == 'AF':
            funcionarios.mostrar_funcionarios(arquivos['arquivo_funcionarios'])
            funcionario_alterado = str(input('Qual funcionario deseja alterar: ')).capitalize()
            if existe(dados_funcionarios(), funcionario_alterado)[0]:
                funcionarios.alterar_funcionario(arquivos['arquivo_funcionarios'], funcionario_alterado)
        elif menu_adm == 'SAIR':
            print(f'{"ATÉ MAIS".center(35)}')
            print('-' * 35)
            break
    elif verifica_login(dados_funcionarios(), menu[0], menu[1]) == 'Vendedor':
        print(f'Bem-Vindo {menu[0]} Vendedor'.center(35))
        print('-' * 35)
        menu_vendedor = menu_funcionario('Adicionar Produto ao Carrinho (AP)', 'Remover Produto do Carrinho (RP)', 'Consultar Carrinho (CC)', 'Fechar Pedido (FP)', 'Sair').upper()
        if menu_vendedor == 'AP':
            produtos.mostrar_produtos(arquivos['arquivo_produtos'])
            produto = str(input('Qual produto deseja adicionar? ')).capitalize()
            quantidade_produto = int(input(f'Quantos {produto} você deseja levar? '))
            produto_existe = existe(dados_produtos(), produto, quantidade_produto)
            if produto_existe[0]:
                print('\033[32mProduto Adicionado com Sucesso\033[m')
                print('-' * 35)
                carrinho.append(produto_existe[1])
            else:
                print('-' * 35)
                print(f'\033[31mProduto {produto_existe[1]} inexistente, consulte a lista de Produtos\033[m')
                print('-' * 35)
        elif menu_vendedor == 'RP':
            mostrar_carrinho(carrinho, quantidade_produto)
            produto_removido = str(input('Qual produto deseja remover? ')).capitalize()
            produto_remove = remove_produto(carrinho, produto_removido)
            if produto_remove[0]:
                carrinho.pop(produto_remove[1])
        elif menu_vendedor == 'CC':
            mostrar_carrinho(carrinho, quantidade_produto)
        elif menu_vendedor == 'FP':
            mostrar_carrinho(carrinho, quantidade_produto)
            produtos.diminui_quantidade(arquivos['arquivo_produtos'], produto, quantidade_produto)
            print(f'Total R${mostrar_total(carrinho, quantidade_produto):.2f}')
            print('-' * 35)
            break
        elif menu_vendedor == 'SAIR':
            print(f'\033[31m{"ATÉ A PROXIMA".center(36)}\033[m')
            print('-' * 35)
            break
    else:
        print('Login/Senha incorretos!')
