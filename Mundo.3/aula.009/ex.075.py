n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tup = (n1, n2, n3, n4)
print(f'Você digitou: {tup}')
print(f'O número 9 apareceu {tup.count(9)} vez(es).')
if 3 in tup:
    print(f'O número 3 está na {tup.index(3) + 1}° posição.')
else:
    print(f'O número 3 não foi digitado.')

print(f'São pares os números: ', end=' ')
for i in range(0, len(tup)):
    if tup[i] % 2 == 0:
        print(f'{tup[i]}', end=' ')
