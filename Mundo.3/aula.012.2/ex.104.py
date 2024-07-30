def readInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return valor


n = readInt('Digite um número inteiro: ')
print(f'Você digitou {n}')
