def linha(tam=42):
    return '-' * tam


def cabecalho(msg):
    print(linha())
    print(msg.center(len(linha())))
    print(linha())


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquiuvo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def leiaArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.readlines())




















