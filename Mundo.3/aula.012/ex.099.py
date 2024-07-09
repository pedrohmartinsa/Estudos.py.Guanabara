from time import sleep
def maior(* num):
    print('=~'*30)
    print('Analisando os números...')
    sleep(1)
    cont = maior = 0
    for valor in num:
        cont += 1
        if valor == num[0]:
            maior = valor
        if valor > maior:
            maior = valor
    print(f'{cont} números registrados: {num}')
    print(f'{maior} é o maior deles.')
    print('=~' * 30)




