from math import sqrt, pow

co = float(input('Qual o valor do cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
h = sqrt(co**2 + ca**2 )
print(f'a hipotenusa do triângulo é igual á {h}')
