from time import sleep
def main():
    contador_sem_input()
    contador_com_input()
def contador_sem_input():
    print('DE 1 A 10:')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.5)
    print()
    print('=~' * 30)
    print('DE 10 A 1:')
    for c in range(10, 0, -1):
        print(c, end=' ')
        sleep(0.5)
    print()
    print('=~' * 30)


def contador_com_input():
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo == 0:
        passo = 1

    # crescente
    if inicio < fim:
        if passo < 0:
            passo = -passo
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.5)
        print('=~'*30)
    #decrescente
    else:
        if passo > 0:
            passo = -passo
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
            sleep(0.5)
        print()
        print('=~' * 30)
        print('FIM.')

main()
