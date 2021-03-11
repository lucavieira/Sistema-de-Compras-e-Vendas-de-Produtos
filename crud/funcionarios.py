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
