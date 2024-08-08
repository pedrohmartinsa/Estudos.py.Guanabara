matriz = [[], [], []]

for l in range(0, 3):
    for v in range(0, 3):
        matriz[l].append((int(input(f'Digite um valor para [{l},{v}]: '))))

print('-='*30)
for l in range(0, 3):
    for v in range(0, 3):
        print(f'[{matriz[l][v]:^5}]', end='')
    print()
