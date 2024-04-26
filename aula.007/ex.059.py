#MENU DE OPÇÕES
from time import sleep
msg = '''
[1] ==> SOMAR
[2] ==> MULTIPLICAR
[3] ==> MAIOR
[4] ==> NOVOS NÚMEROS
[5] ==> SAIR DO PROGRAMA 
'''
comando = 1
while comando != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo: '))
    print()
    print(msg)
    comando = int(input('Comando:'))
    print()
    #SOMAR
    if comando == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual á {soma}.')
        print()
    #Multiplicar
    elif comando == 2:
        mult = n1 * n2
        print(f'{n1} x {n2} é igual á {mult}.')
        print()
    #Maior
    elif comando == 3:
        if n1 > n2:
            print(f'{n1} é maior do que {n2}')
            print()
        if n2 > n1:
            print(f'{n2} é maior do que {n1}')
            print()
    #Novos números
    elif comando == 4:
        print('Voltando...')
        sleep(2)
    #Sair do programa
    elif comando == 5:
        print('Fim do programa, obrigado por usa-lo.')
        print()
    else:
        print('Comando inválido, faça novamente.')
        print()
