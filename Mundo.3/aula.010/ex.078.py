lista = []

for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))


print()

for i, v in enumerate(lista):
    print(f'{i+1}º posição: {v}')


lista.sort()
print()
print(f'Os valores digitados foram: {lista}')
print(f'Maior valor digitado foi: {lista[0]}')
print(f'Menor valor digitado foi: {lista[-1]}')
