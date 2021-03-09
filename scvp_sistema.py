from arquivos import *
from crud.produtos import *
from crud.funcionarios import *
from sistema import *

# Um dicionario com todos os arquivos
arquivos = {'arquivo_produtos': 'produtos.csv', 'arquivo_funcionarios': 'funcionarios.csv'}

# Para cada arquivo no dicionario, verifica se ja existe, caso não exista, cria o arquivo
for arquivo in arquivos.values():
    if not existe_arquivo(arquivo):
        cria_arquivo(arquivo)

# Menu Login
menu = menu_login()
while True:
    if verifica_login(dados(), menu[0], menu[1]):
        print(f'Bem-Vindo {menu[0]} Admin'.center(35))
        menu_adm = menu_funcionario('Cadastrar Produtos (CP)', 'Cadastrar Funcionarios (CF)', 'Sair').upper()
        if menu_adm == 'CP':
            print('-' * 35)
            nome = str(input('Nome do Produto: '))
            preco = float(input('Preco do Produto: '))
            quantidade = int(input('Quantidade: '))
            produtos = Produtos(nome, preco, quantidade)
            produtos.cadastro(arquivos['arquivo_produtos'])
            print('-' * 35)
        elif menu_adm == 'CF':
            print('-' * 35)
            nome = str(input('Nome do Funcionario: '))
            cpf = int(input('CPF: '))
            senha = str(input('Senha: '))
            cargo = str(input('Cargo [Adm/Vendedor]: '))
            funcionario = Funcionarios(nome, cpf, senha, cargo)
            funcionario.cadastro(arquivos['arquivo_funcionarios'])
            print('-' * 35)
        elif menu_adm == 'SAIR':
            print('-' * 35)
            print(f'{"ATÉ MAIS".center(35)}')
            print('-' * 35)
            break
    else:
        print(f'Bem-Vindo {menu[0]} Vendedor'.center(35))
