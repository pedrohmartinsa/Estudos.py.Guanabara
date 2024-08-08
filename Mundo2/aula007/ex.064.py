count = soma = i = 0
n = int(input('Digite um número [999 para parar]: '))
while i < 1:
    count += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: ')) #para ignorar o 999 na soma e no count
    if n == 999:
        print(f'Você digitou {count} números e a soma entre eles é igual a {soma}.')
        print('FIM.')
        i += 1
