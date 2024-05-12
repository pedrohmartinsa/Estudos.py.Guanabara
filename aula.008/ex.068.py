from time import sleep
from random import uniform #para escolher um número aleatorimanete

count = 0

while True:
    comp = int(uniform(0, 10))
    print()

    print('[P] para par ou [I] para ímpar.')

    paridade = str(input('Jogador, você quer ser par ou ímpar ?')).strip().upper()
    print()

    while paridade not in 'IiPp':
        print('Paridade inválida, digite novamente...')
        print()
        sleep(1.5)
        print('[P] para par ou [I] para ímpar.')
        paridade = str(input('Jogador, você quer ser par ou ímpar ?')).strip().upper()
        print()

        if paridade in 'Ii':
            print('O computador é par.')
            print()
            break

        elif paridade in 'Pp':
            print('O computador é ímpar.')
            print()
            break



    j1 = int(input('Escolha um número (de 0 a 10):'))
    print()
    soma = comp + j1
    if paridade in 'Ii' and (j1 + comp) % 2 == 1:
        count += 1
        print(f'O computador escolheu {comp} e você escolheu {j1}, a soma deu {soma}.')
        print('Você venceu!')

    elif paridade in 'Pp' and (j1 + comp) % 2 == 0:
        count += 1
        print(f'O computador escolheu {comp} e você escolheu {j1}, a soma deu {soma}')
        print('Você venceu!')

    else:
        print(f'O computador escolheu {comp} e você escolheu {j1}, a soma deu {soma}')
        print(f'Você perdeu depois de {count} vitórias.')
        break
