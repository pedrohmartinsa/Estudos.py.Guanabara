#Mudar a base de conversão do número
n1 = int(input('Digite um número inteiro: '))
print()
msg = '''
Qual a base de conversão desejada?

|Comando   |Base

|(1)        |Binário
|(2)        |Octal
|(3)        |Hexadecimal
'''
print(msg)
base = int(input('Sua opção: '))

if base == 1:
    print(f'{n1} em binário é igual á {bin(n1)[2:]}')
elif base == 2:
    print(f'{n1} em octal é igual á {oct(n1)[2:]}')
elif base == 3:
    print(f'{n1} em hexadecimal é igual á {hex(n1)[2:]}')
else:
    print('Opção inválida')
