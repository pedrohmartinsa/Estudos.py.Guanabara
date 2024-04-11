#Aprovar empréstimo bancário de uma casa

nome = input('Olá, como posso lhe chamar? ')
valor = float(input(f'{nome}, qual o valor da casa desejada? '))
sala = float(input(f'{nome}, quanto você recebe de salário? '))
tempo = float(input('Em quanto tempo planeja quitar a casa? '))

prest = valor / (tempo * 365)

if prest > sala *  0.3:
    print(f'Sinto muito {nome}, não será possível financiar.')
else:
    print(f'Muito bem, você terá que pagar R${prest:.2f} pelo financioamento por {tempo} anos.')
