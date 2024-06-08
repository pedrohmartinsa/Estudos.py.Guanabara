lista = []
pares = []
impares = []

for c in range(0, 7):

    n = int(input(f'Digite o {c+1}o valor: '))
    lista.append(n)

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
print(f'Os números pares digitados foram: {pares}')
impares.sort()
print(f'Os números impares digitados foram: {impares}')
