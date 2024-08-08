#DIZENDO SE É OU NÃO UM NÚMERO PRIMO
n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m')
        tot += 1
    else:
        print('\033[31m')
    print(c)
print(f'O número {n} foi divisível {tot} vezes')
if tot == 2:
    print('Portanto, este número É PRIMO')
else:
    print('Portanto, este número NÃO É PRIMO')
