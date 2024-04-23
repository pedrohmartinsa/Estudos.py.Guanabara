print('*' * 65)
print('Soma entre os número ímpares que são múltiplos de 3 entre 1 e 500')
print('*' * 65)
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma dos {cont} valores solicitados é {soma}')
