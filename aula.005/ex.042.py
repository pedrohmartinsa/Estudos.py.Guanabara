#tipo de triângulo

n1 = float(input('Digite o valor do tamanho do primeiro lado de seu triângulo:'))
n2 = float(input('Digite o segundo:'))
n3 = float(input('Digite o terceiro:'))

if n1 < n2 + n3 and n2 < n1 + n3 or n3 < n1 + n2:
     print('É possível construir um triângulo com os valores escolhidos!')
     if n1 == n2 == n3:
        print('Será um triângulo equilátero.')
     elif n1 == n2 != n3:
        print('Será um triângulo isósceles.')
     else:
         print('Será um triângulo escaleno.')
else:
    print('Não é possível construir um triângulo com os valores escolhidos')

