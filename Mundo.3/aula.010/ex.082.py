lista = []
listaPar = []
listaImpar = []

while True:
    valor = int(input('Digite um valor:'))
    lista.append(valor)

    r = input('Deseja continuar ?[S/N] ')
    while r not in 'SsNn':
        r = input('Deseja continuar ?[S/N] ')
    if r in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    elif v % 2 == 1:
        listaImpar.append(v)

print()
print(f'Os valores digitados foram: {lista}')
print(f'Pares: {listaPar}')
print(f'Ímpares: {listaImpar}')
