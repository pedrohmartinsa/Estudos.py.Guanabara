#SEQUENCIA DE FIBONACCI

n = int(input('Escolha a quantidade de termos: '))
t1 = 0
t2 = 1
i = 3
t3 = 0
print(f'{t1} - {t2}', end='')
while i <= n:
    t3 = t2 + t1
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    i += 1
print(' - FIM.', end='')
