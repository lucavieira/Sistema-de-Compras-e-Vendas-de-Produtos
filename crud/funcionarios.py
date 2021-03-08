class Funcionarios(object):
    def __init__(self, nome, cpf, senha, cargo):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.cargo = cargo

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

    def mostrar_funcionarios(self, arquivo):
        try:
            file = open(arquivo, 'rt')
        except:
            print('Erro ao ler arquivo')
        else:
            print('-' * 30)
            print(f'{"LISTA DE FUNCIONARIOS".center(30)}')
            print('-' * 30)
            print(file.read(), end='')
            print('-' * 30)
            file.close()
