#Ver se a frase é um palíndromo
frase = input('Digite uma frase: ').upper().strip(' ')

if frase == frase[::-1]:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
