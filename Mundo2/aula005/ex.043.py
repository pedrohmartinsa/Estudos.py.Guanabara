#Índice de massa corpórea (IMC)

peso = float(input('Qual seu peso em Kg? '))
altura = float(input('Qual sua altura em m? '))

imc = peso / (altura ** 2)

print(f'Seu imc é de {imc:.1f}')

if imc < 18.5:
    print('Você esta abaixo do peso.')
elif 18.5 < imc <= 25:
    print('Você esta com o peso ideal.')
elif 25 < imc <= 30:
    print('Você esta com sobrepeso.')
elif 30 < imc <= 40:
    print('Você esta na obesidade.')
else:
    print('Você esta na obesidade mórbida.')
