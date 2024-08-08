from time import sleep
from random import randint

num_aleatorios_de_1_a_60 = []

print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)

numero_sorteios = int(input('Quantos jogos deseja que sejam sorteados? '))

for c in range(0, numero_sorteios):
    while len(num_aleatorios_de_1_a_60) < 6:
        num = randint(0, 60)
        if num not in num_aleatorios_de_1_a_60:
             num_aleatorios_de_1_a_60.append(num)
    num_aleatorios_de_1_a_60.sort()
    print(f'sorteio {c + 1}: {num_aleatorios_de_1_a_60}')
    sleep(0.5)
    num_aleatorios_de_1_a_60.clear()
print('FIM.')
