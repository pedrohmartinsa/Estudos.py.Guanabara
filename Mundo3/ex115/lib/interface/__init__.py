from time import sleep


def erro(msg):
    print(f'\033[31m{msg}\033[m', end='')
    for c in range(0, 3):
        print(f'\033[31m{'.'}\033[m', end='')
        sleep(1)
    print()


def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(msg):
    print(linha())
    print(msg.center(len(linha())))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = readInt('Sua Opção: ')
    return opc















