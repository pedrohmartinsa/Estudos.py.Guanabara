count = 0

while True:
    if count == 10:
        count = 0
    n = int(input('Digite um número para ver sua tabuada: '))

    while count != 10:
        count += 1
        tabuada = n * count
        print(f'{count} x {n} = {tabuada}')
    if n * -1 == +n:
        break
print('FIM.')





