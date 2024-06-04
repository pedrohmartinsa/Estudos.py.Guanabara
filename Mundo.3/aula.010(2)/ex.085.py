lista = []
pares = []
impares = []

for c in range(0, 7):
<<<<<<< HEAD
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

=======
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
>>>>>>> 66f043079c6629d4e12eb1fe8685dff286ebde34
