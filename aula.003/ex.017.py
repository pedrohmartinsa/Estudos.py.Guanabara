from math import sqrt, pow, hypot

'''co = float(input('Qual o valor do cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
h = sqrt(co**2 + ca**2 )
print(f'a hipotenusa do triângulo é igual á {h:.2f}')'''

co = float(input('Qual o valor do cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
h = hypot(co, ca)
print(f'a hipotenusa do triângulo é igual á {h:.2f}')


