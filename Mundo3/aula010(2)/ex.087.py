matriz = [[], [], []]
pares = maiorValor = soma = 0

for l in range(0, 3):
    for v in range(0, 3):
        matriz[l].append((int(input(f'Digite um valor para [{l},{v}]: '))))

print('-='*30)
for l in range(0, 3):
    for v in range(0, 3):
        print(f'[{matriz[l][v]:^5}]', end='')
    print()
print('-='*30)

for v in matriz:
    for valor in v:
        if valor % 2 == 0:
            pares += valor
print(f'A soma dos números pares é: {pares}.')
for l in range(0, 3):
    soma += matriz[l][2]
print(f'A soma dos valores da última coluna é: {soma}')

for valores in matriz[1]:
    if valores > maiorValor:
        maiorValor = valores
print(f'O maior valor da segunda linha é {maiorValor}.')
