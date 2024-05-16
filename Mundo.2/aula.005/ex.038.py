#mostrando qual valor é maior

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print(f'{n1} é maior.')
elif n2 > n1:
    print(f'{n2} é maior.')
else:
    print(f'{n1} e {n2} são iguais.')
