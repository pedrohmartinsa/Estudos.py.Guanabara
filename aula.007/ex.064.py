
count = 0
soma = 0
i = 0
while i < 1:
    n = int(input('Digite um número: '))
    count += 1
    soma += n
    if n == 999:
        print(f'Você digitou {count} números, e a soma entre eles é igual a {soma - 999}')
        print('FIM.')
        i += 1