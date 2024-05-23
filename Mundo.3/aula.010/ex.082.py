lista = []
listaPar = []
listaImpar = []

while True:
    valor = int(input('Digite um valor:'))
    lista.append(valor)

    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)

    r = input('Deseja continuar ?[S/N] ')
    while r not in 'SsNn':
        r = input('Deseja continuar ?[S/N] ')
    if r in 'Nn':
        break


print()
print(f'Os valores digitados foram: {lista}')
print(f'Pares: {listaPar}')
print(f'Ímpares: {listaImpar}')
