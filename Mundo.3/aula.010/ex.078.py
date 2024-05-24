lista = []
maiorIndex = []
menorIndex = []

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

print()
menor = lista[0]
maior = lista[0]

for v in lista:
    if v < menor:
        menor = v

    if v > maior:
        maior = v

for i, v in enumerate(lista):
    if v == menor:
        menorIndex.append(i)

    if v == maior:
        maiorIndex.append(i)


print()
print(f'Os valores digitados foram: {lista}')
print(f'Maior valor digitado foi: {maior} nas posições: {maiorIndex}')
print(f'Menor valor digitado foi: {menor} nas posições: {menorIndex}')
