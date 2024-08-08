lista = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}o. valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
print(f'Os números pares digitados foram: {lista[0]}')
lista[1].sort()
print(f'Os números impares digitados foram: {lista[1]}')
