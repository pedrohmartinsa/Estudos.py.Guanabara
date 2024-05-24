lista = []
pares = []
impares = []

for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)

    elif n % 2 == 1:
        impares.append(n)


lista.append(impares)
lista.append(pares)
print()
print(f'Pares: {lista[1]}')
print(f'Impares: {lista[0]}')
