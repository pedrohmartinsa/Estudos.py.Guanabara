# somando e contando números usando True e break ignorando o 999
count = soma = 0
while True:
    n = int(input('Digite um número [999 para sair]:'))
    if n == 999:
        break
    count += 1
    soma += n
print(f'A soma dos {count} valores é {soma}.')
