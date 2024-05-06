from random import randint
from time import sleep
print('TENTE ACERTAR O NÚMERO SORTEADO')
print()
lista = randint(0, 10)
numeroSorteado = 11
cont = 1
while lista != numeroSorteado:
    numeroSorteado = int(input('Digite um número entre 0 e 10:'))
    if numeroSorteado != lista:
        print('Errou, tente novamente.')
        cont += 1
    if numeroSorteado > lista:
        print('Menos...')
        print()
    if numeroSorteado < lista:
        print('Mais...')
        print()
    else:
        print(f'Parábens, você acertou! Depois de {cont} tentativas.')
print('Fim.')
