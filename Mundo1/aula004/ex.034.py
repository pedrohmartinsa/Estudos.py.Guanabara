sala = float(input('Digite seu salário:R$'))
au1 = sala + (0.1 * sala)
au2 = sala + (0.15 * sala)

if sala >= 1250:
    print(f'Você recebeu um aumento de 10%, passará a receber R${au1:.2f}')
else:
    print(f'Você recebeu um aumento de 15%, passará a receber R${au2:.2f}')