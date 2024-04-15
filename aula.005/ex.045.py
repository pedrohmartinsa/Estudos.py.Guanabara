#Jokenpô
from random import choice
from time import sleep
escolha = input('Pedra, papel ou tesoura? ').upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
lista = ['Pedra', 'Papel', 'Tesoura']
escolhidoComputador = choice(lista)
print('*'*28)
print(f'O computador jogou {escolhidoComputador}')

if escolha == 'PEDRA' and escolhidoComputador == 'Pedra':
    print('Deu empate, jogue novamente.')
elif escolha == 'PEDRA' and escolhidoComputador == 'Papel':
    print('O computador ganhou.')
elif escolha == 'PEDRA' and escolhidoComputador == 'Tesoura':
    print('Você ganhou.')

elif escolha == 'PAPEL' and escolhidoComputador == 'Papel':
    print('Deu empate, jogue novamente.')
elif escolha == 'PAPEL' and escolhidoComputador == 'Tesoura':
    print('O computador ganhou.')
elif escolha == 'PAPEL' and escolhidoComputador == 'Pedra':
    print('Você ganhou.')

elif escolha == 'TESOURA' and escolhidoComputador == 'Tesoura':
    print('Deu empate, jogue novamente.')
elif escolha == 'TESOURA' and escolhidoComputador == 'Pedra':
    print('O computador ganhou.')
else:
    print('Você ganhou.')
print('*'*28)

