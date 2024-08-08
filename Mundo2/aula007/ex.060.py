#FATORIAL
n = int(input('Digite um número para ver seu fatorial: '))
n1 = n
a = n - 1
while a > 0:
    #print(n)
    #print(a)
    n *= a
    a -= 1
print(f'{n1}! = {n}')

