dis = float(input('Qual a distância do seu percurso de viagem em Km?'))
ab = 0.5 * dis
ac = 0.45 * dis
if dis <= 200:
    print(f'Como é abaixo de 200Km, o valor a ser pago é: R${ab:.2f}')
else:
    print(f'Como é acima de 200Km, o valor a ser pago é: R${ac:.2f}')