#Ver se a frase é um palíndromo
frase = input('Digite uma frase: ').upper().split() #deixando tudo em maiúsculo e separando em listas
n = ''.join(frase) #juntando tudo
print(n)
if n == n[::-1]: #comparando a frase normal com  a frase de traz para a frente
    print(f'{n} é um palíndromo.')
else:
    print(f'{n} não é um palíndromo.')
