'''from random import choice
lista = [0, 1, 2, 3, 4, 5]
n = int(input('Chute o número sorteado entre 0 e 5: '))
choice(lista)
if n == choice(lista):
    print('Parábens, você acertou o número sorteado!')
else:
    print('Poxa, você errou o número sorteado...')
print(f'O número sorteado foi {choice(lista)}'''

from random import randint #faz o computador "pensar"
from time import sleep
lista = randint(0, 5)
n = int(input('Chute o número sorteado entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if n == lista:
    print('Parábens, você acertou o número sorteado!')
else:
    print('Poxa, você errou o número sorteado...')
print(f'O número sorteado foi {lista}')