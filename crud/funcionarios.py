import pandas as pd


class Funcionarios(object):
    def __init__(self, nome='', cpf=00000, senha='', cargo=''):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.cargo = cargo

    # Cadastra um funcionario no arquivo .csv
    def cadastro(self, arquivo):
        try:
            file = open(arquivo,  'at')
        except:
            print('Erro ao abrir o arquivo')
        else:
            try:
                file.write(f'{self.nome},{self.cpf},{self.senha},{self.cargo}\n')
            except:
                print('Erro ao cadastrar funcionario')
            else:
                file.close()

    # Lê o arquivo .csv e mostra todos funcionarios cadastrados
    def mostrar_funcionarios(self, arquivo):
        try:
            file = open(arquivo, 'rt')
        except:
            print('Erro ao ler arquivo')
        else:
            print(f'\033[31m{"LISTA DE FUNCIONARIOS".center(35)}\033[m')
            print('-' * 35)
            print(file.read(), end='')
            print('-' * 35)
            file.close()

    # Função que remove um funcionario do arquivo .csv
    def remover_funcionario(self, arquivo, funcionario):
        lista_funcionarios = pd.read_csv(arquivo)
        for indice in lista_funcionarios.index:
            if lista_funcionarios.loc[indice, 'Nome'] == funcionario:
                lista_funcionarios.drop(indice, inplace=True)
            lista_funcionarios.to_csv(arquivo, index=False)

    # Função que altera algum dado do Funcionario
    def alterar_funcionario(self, arquivo, funcionario):
        lista_funcionarios = pd.read_csv(arquivo)
        for indice in lista_funcionarios.index:
            if lista_funcionarios.loc[indice, 'Nome'] == funcionario:
                indice_funcionario = str(input('\nO que deseja alterar:\n(Nome/Cpf/Senha/Cargo) -> ')).capitalize()
                if indice_funcionario == 'Nome':
                    novo_nome = str(input('Nome: ')).capitalize()
                    lista_funcionarios.loc[indice, indice_funcionario] = novo_nome
                elif indice_funcionario == 'Cpf':
                    novo_cpf = int(input('CPF: '))
                    lista_funcionarios.loc[indice, indice_funcionario] = novo_cpf
                elif indice_funcionario == 'Senha':
                    nova_senha = int(input('Senha: '))
                    lista_funcionarios.loc[indice, indice_funcionario] = nova_senha
                elif indice_funcionario == 'Cargo':
                    novo_cargo = int(input('Cargo: '))
                    lista_funcionarios.loc[indice, indice_funcionario] = novo_cargo
                else:
                    print('-' * 35)
                    print('\033[31mNenhum dado foi alterado!\033[m')
                    print('-' * 35)
                lista_funcionarios.to_csv(arquivo, index=False)
