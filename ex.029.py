velo = float(input('Qual a velocidade que o carro estava em Km?'))
multa = 7 * (velo - 80)
if velo > 80:
    print('Você será multado no valor de {}, mais atenção nas ruas!'.format(multa))
else:
    print('Você não será multado, continue assim!')