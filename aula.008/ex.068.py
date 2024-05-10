from time import sleep
from random import uniform
print('[P] para par ou [I] para ímpar.')
paridade = str(input('Jogador 1, você quer ser par ou ímpar ?')).strip().upper()

if paridade in 'Ii':
    print('Jogador 2, você é par.')
else:
    print('Jogador 2, você é ímpar.')

comp = int(uniform(0, 10))

j1 = int(input('Escolha um número (de 0 a 10):'))

if comp % 2 == 0 and j1 % 2 == 1:
    
