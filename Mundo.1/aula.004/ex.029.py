velo = int(input('Qual a velocidade que o carro estava em Km?'))
multa = 7 * (velo - 80)
if velo > 80:
    print(f'Você será multado no valor de R${multa:.2f}, mais atenção nas ruas!')
else:
    print('Você não será multado, continue assim!')
print('Tenha um bom dia e dirija com segurança.')