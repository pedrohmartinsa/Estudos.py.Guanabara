from random import randint
from time import sleep
numeros = []
def sorteio():
    for c in range(0, 5):
        numeros.append(randint(1, 100))
    print('Números sorteados: ', end='')
    for numero in numeros:
        print(f'{numero}', end=' ')
        sleep(0.5)
    print()


def somaPares():
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'Soma dos números pares: {soma}')


sorteio()
somaPares()
