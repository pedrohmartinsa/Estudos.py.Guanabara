lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    r = input('Deseja continuar? [S/N]')
    if r not in 'SsNn':
        r = input('Deseja continuar? [S/N]')
    if r in 'Nn':
        break



print()
a = lista[:]
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores na lista')
print(f'Os valores digitados foram: {a}')
print(f'Os valores digitados, em ordem decrescente, foram: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')
