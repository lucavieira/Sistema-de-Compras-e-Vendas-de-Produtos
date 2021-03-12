from sistema import dados_funcionarios, exclui_arquivo
from arquivos import cria_arquivo


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

    def remover_funcionarios(self, arquivo, funcionario):
        lista_funcionarios = dados_funcionarios()
        for funcionarios in lista_funcionarios:
            if funcionario == funcionarios['Nome']:
                lista_funcionarios.remove(funcionarios)
                exclui_arquivo(arquivo)
        cria_arquivo(arquivo)
        for funcionarios in lista_funcionarios:
            if not funcionarios['Nome'] in dados_funcionarios()[0]['Nome']:
                nome = str(funcionarios['Nome'])
                cpf = int(funcionarios['CPF'])
                senha = str(funcionarios['Senha'])
                cargo = str(funcionarios['Cargo'])
                novo_funcionario = Funcionarios(nome, cpf, senha, cargo)
                novo_funcionario.cadastro(arquivo)

    def alterar_funcionario(self, arquivo, funcionario):
        lista_funcionarios = dados_funcionarios()
        exclui_arquivo(arquivo)
        cria_arquivo(arquivo)
        for funcionarios in lista_funcionarios:
            if funcionarios['Nome'] == funcionario:
                indice_funcionario = str(input('O que deseja alterar:\n(Nome/Cpf/Senha/Cargo)')).capitalize()
                if indice_funcionario == 'Nome':
                    novo_nome = str(input('Nome: ')).capitalize()
                    funcionario_alterado = Funcionarios(novo_nome, int(funcionarios['CPF']), str(funcionarios['Senha']), str(funcionarios['Cargo']))
                elif indice_funcionario == 'Cpf':
                    novo_cpf = int(input('CPF: '))
                    funcionario_alterado = Funcionarios(str(funcionarios['Nome']), novo_cpf, str(funcionarios['Senha']), str(funcionarios['Cargo']))
                elif indice_funcionario == 'Senha':
                    nova_senha = str(input('Senha: ')).lower()
                    funcionario_alterado = Funcionarios(str(funcionarios['Nome']), int(funcionarios['CPF']), nova_senha, str(funcionarios['Cargo']))
                elif indice_funcionario == 'Cargo':
                    novo_cargo = str(input('Cargo: ')).capitalize()
                    funcionario_alterado = Funcionarios(str(funcionarios['Nome']), int(funcionarios['CPF']), str(funcionarios['Senha']), novo_cargo)
                else:
                    funcionario_alterado = Funcionarios(str(funcionarios['Nome']), int(funcionarios['CPF']), str(funcionarios['Senha']), str(funcionarios['Cargo']))
                funcionario_alterado.cadastro(arquivo)
            else:
                if not funcionarios['Nome'] in dados_funcionarios()[0]['Nome']:
                    funcionario_alterado = Funcionarios(str(funcionarios['Nome']), int(funcionarios['CPF']), str(funcionarios['Senha']), str(funcionarios['Cargo']))
                    funcionario_alterado.cadastro(arquivo)
