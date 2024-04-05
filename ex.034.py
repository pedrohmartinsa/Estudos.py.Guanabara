sala = float(input('Digite seu salário:R$'))
au1 = sala + (0.1 * sala)
au2 = sala + (0.15 * sala)

if sala >= 1250:
    print('Você recebeu um aumento de 10%, passará a receber R${}'.format(au1))
else:
    print('Você recebeu um aumento de 15%, passará a receber R${}'.format(au2))