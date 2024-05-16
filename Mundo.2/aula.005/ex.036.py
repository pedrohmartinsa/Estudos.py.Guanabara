#Aprovar empréstimo bancário de uma casa

nome = input('Olá, como posso lhe chamar? ')
valor = float(input(f'{nome}, qual o valor da casa desejada? R$'))
salario = float(input(f'{nome}, quanto você recebe de salário? R$'))
tempo = float(input('Em quanto tempo (em anos) planeja quitar a casa? '))

prest = valor / (tempo * 12)

if prest > salario * 0.3:
    print(f'Sinto muito {nome}, não será possível financiar.')
else:
    print(f'Muito bem, você terá que pagar R${prest:.2f} pelo financioamento por {tempo} anos.')
