#Ver se a frase é um palíndromo
frase = input('Digite uma frase: ').upper().split()
n = ''.join(frase)
print(n)
if n == n[::-1]:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
