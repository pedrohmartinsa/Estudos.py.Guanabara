from random import choice
lista = [0, 1, 2, 3, 4, 5]
n = int(input('Chute o número sorteado entre 0 e 5: '))
choice(lista)
if n == choice(lista):
    print('Parábens, você acertou o número sorteado!')
else:
    print('Poxa, você errou o número sorteado...')
print('O número sorteado era {}'.format(choice(lista)))