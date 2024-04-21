#Alistamento
from datetime import date
atual = date.today().year
nome = input('Olá, bem vindo ao programa de alistamento, como posso te chamar? ')
print()
ano = int(input(f'{nome}, em que ano você nasceu? '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
print()

if idade == 18:
    print('Você deve se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não pode se alistar, falta(m) {saldo} ano(s) para poder')
    tempo = atual + saldo
    print(f'Seu alistamento será em {tempo}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado há {saldo} ano(s)')
    tempo = atual - saldo
    print(f'Seu alistamento foi em {tempo}')
