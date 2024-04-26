#FATORIAL
from math import factorial
n = int(input('Digite um número: '))
a = n
while a > 0:
    print(f'{n}! =', end='')
    print(f'{a}x', end='')
    a -= 1

