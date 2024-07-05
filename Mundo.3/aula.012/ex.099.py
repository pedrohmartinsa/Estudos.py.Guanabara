def maior(* num):
    print('Analisando os números...')
    cont = maior = 0
    for valor in num:
        cont += 1
        if valor == num[0]:
            maior = valor
        if valor > maior:
            maior = valor
    