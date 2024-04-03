n = int(input('informe um número: '))
'''n = str(n1)
print(f'Analisando o número {n1}, temos:')
print(f'primeiro dígito: {n[0]}')
print(f'segundo dígito: {n[1]}')
print(f'terceiro dígito: {n[2]}')
print(f'quarto dígito: {n[3]}')'''

n1 = n // 1 % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 % 10
print(f'Analisando o número {n}, temos:')
print(f'unidade: {n1}')
print(f'dezena: {n2}')
print(f'centena: {n3}')
print(f'milhar: {n4}')