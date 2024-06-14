from time import sleep
from random import randint

numAleatoriosUm1a60 = []

print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)

numero_sorteios = int(input('Quantos jogos deseja que sejam sorteados? '))

for c in range(0, numero_sorteios):
    while len(numAleatoriosUm1a60) < 6:
        num = randint(0, 60)
        if num in numAleatoriosUm1a60:
            continue
        else:
            numAleatoriosUm1a60.append(num)
    numAleatoriosUm1a60.sort()
    print(f'sorteio {c + 1}: {numAleatoriosUm1a60}')
    sleep(0.5)
    numAleatoriosUm1a60.clear()
print('FIM.')
