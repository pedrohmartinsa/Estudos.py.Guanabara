#tabuada infinita até digitar um número negativo
count = 0

while True:
    if count == 10:
        count = 0
    n = int(input('Digite um número para ver sua tabuada: '))

    if n < 0:
        break

    while count != 10:
        count += 1
        tabuada = n * count
        print(f'{count} x {n} = {tabuada}')
print('FIM.')





