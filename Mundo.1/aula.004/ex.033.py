a = float(input('Digite um número:'))
b = float(input('Digite um número:'))
c = float(input('Digite um número:'))
#verificando qual é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando qual é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'{menor} é o menor número e {maior} é o maior número.')


