def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        else:
            return n

def readFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido.')
            continue
        else:
            return n


i = readInt('Digite um número inteiro: ')
r = readFloat('Digite um número real: ')
print(f'Você digitou {i} como inteiro e {r} como real.')
