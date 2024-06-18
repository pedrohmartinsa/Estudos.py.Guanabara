from random import randint
from time import sleep
from operator import itemgetter
num = {}
rank = []
for c in range(1, 5):
    num[f'Jogador {c}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in num.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
print('Ranking dos jogadores:')
rank = sorted(num.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1}º colocado: {v[0]} com {v[1]}')
    sleep(0.5)
