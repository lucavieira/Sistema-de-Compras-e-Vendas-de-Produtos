import csv


def dados():
    with open('funcionarios.csv') as funcionario:
        return [dado_funcionario for dado_funcionario in csv.DictReader(funcionario)]


def verifica_login(dados, nome, senha):
    for funcionario in dados:
        if funcionario['Nome'] == nome and funcionario['Senha'] == senha and funcionario['Cargo'] == 'Admin':
            return True
        else:
            return False


def menu_login():
    print('-' * 35)
    print(f'{"LOGIN".center(35)}')
    print('-' * 35)
    nome = str(input('Nome: '))
    senha = str(input('Senha: '))
    print('-' * 35)
    return nome, senha


def menu_funcionario(*opcoes):
    print('-' * 35)
    for opcao in opcoes:
        print(opcao)
    comando = str(input('Digite o que deseja: '))
    return comando