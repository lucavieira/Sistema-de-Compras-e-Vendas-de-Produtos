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
                print(f'{self.nome} cadastrado com sucesso!')
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
