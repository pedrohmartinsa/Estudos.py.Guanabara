#SOMA APENAS DOS NÚMEROS PARES
s = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro:'))
    if n % 2 == 0:
        s += n
    else:
        print()
        print('Número ímpar. Desconsiderado.')
        print()
print()
print(f'A soma dos números pares é {s}')


