from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)

print(f'Os números sorteados foram: ', end='')

for i in n:
    print(f'{i} ', end='')

a = sorted(n)
print(f'\nO maior número foi {a[-1]}')
print(f'O menor número foi {a[0]}')
