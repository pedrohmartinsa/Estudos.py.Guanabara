<<<<<<< HEAD
n = 5
a = n - 1
while a > 0:
    n *= a
    a -= 1
print(n)
=======
lista = []
maiorIndex = []
menorIndex = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))


print()
menor = lista[0]
maior = lista[0]

for i, v in enumerate(lista):
    if v < menor:
        menor = v

    if v > maior:
        maior = v

    print(f'Posição {i}: {v}')

for i, v in enumerate(lista):
    if v == menor:
        menorIndex.append(i)

    if v == maior:
        maiorIndex.append(i)






print()
print(f'Os valores digitados foram: {lista}')
print(f'Maior valor digitado foi: {maior} nas posições {maiorIndex}')
print(f'Menor valor digitado foi: {menor} nas posições {menorIndex}')
>>>>>>> c315579d42381b1000aa83ac9cab488bde61cf0e
