from time import sleep
print('*' * 34)
print('OS 10 PRIMEIROS TERMOS DE UMA P.A')
print('*' * 34)

a1 = int(input('Qual o primeiro termo ?'))
r = int(input('Qual a razão?'))
print()

count = 0

while count < 10:
    count += 1
    an = a1 + (count - 1) * r
    print(f'O {count}° termo da P.A é {an}')
    sleep(0.5)
print()

i = 1
print('DIGITE [0] PARA SAIR')
n = int(input('Quer mais quantos termos? '))
while i > 0:
    while n > 0:
        count += 1
        an = a1 + (count - 1) * r
        n -= 1
        print(f'O {count}° termo da P.A é {an}')
        sleep(0.5)

    print('DIGITE [0] PARA SAIR')
    n1 = int(input('Quer mais quantos termos? '))

    if n1 == 0:
        i -= 1
        print('FIM!')
    else:
        n = n1



'''if n == 0:
    print()
    print('FIM!')
    break
while n != 0:
    count += 1
    n -= 1
    an = a1 + (count - 1) * r
    print(f'O {count}° termo da P.A é {an}')'''


