#PROGRESSÃO ARITMÉTICA
from time import sleep
print('='*34)
print('OS 10 PRIMEIROS TERMOS DE UMA P.A.')
print('='*34)
print()
a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual a razão: '))
print()
cont = 0
for c in range(1, 11):
    cont += 1
    an = a1 + (cont - 1) * r
    print(f'o termo {c} da P.A. é: {an}')
    sleep(0.5)
print('FIM.')
