from random import randint
from time import sleep
print('TENTE ACERTAR O NÚMERO SORTEADO')
print()
lista = randint(0, 10)
numeroSorteado = 1
cont = 0
while lista != numeroSorteado:
    numeroSorteado = int(input('Digite um número entre 0 e 10:'))
    if numeroSorteado != lista:
        print('Errou, tente novamente.')
        print()
        cont += 1
    else:
        print(f'Parábens você acertou depois de {cont} tentativas.')
print('Fim.')
