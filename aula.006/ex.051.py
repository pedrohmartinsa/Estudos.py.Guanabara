#PROGRESSÃO ARITMÉTICA
from time import sleep
a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual a razão: '))
n = 0
for c in range(0, 10):
    n = n + 1
    an = a1 + (n - 1) * r
    print({an})
    sleep(0.5)
print('FIM')
