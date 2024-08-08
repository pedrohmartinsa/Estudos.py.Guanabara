#TABUADA ATUALIZADA (aqui usei um contador)
from time import sleep
n = int(input('Digite um número inteiro para ver sua tabuada: '))
s = 0
for c in range(0, 10):
    s += 1
    tabuada = n * s
    print(tabuada)
    sleep(0.5)
print('FIM')
