#DIZENDO SE É OU NÃO UM NÚMERO PRIMO
n = int(input('Digite um número inteiro: '))
s = 0
for c in range(n , -1):
    s = s - 1
    d = n // (n + s)
    if d == 0:
        print('Número Primo.')
