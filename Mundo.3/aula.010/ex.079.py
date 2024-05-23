lista = []

while True:
    n = int(input('Digite uma valor: '))

    if n in lista:
        print('Valor ja digitado, não adicionado.')

    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')

    r = input('Deseja continuar ? [S/N]')
    while r not in 'SsNn':
        r = input('Deseja continuar ? [S/N]')
    if r in 'Nn':
        break



print(f'Os valores digitados foram: {lista}')
print('FIM.')