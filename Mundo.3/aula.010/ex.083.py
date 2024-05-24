expressao = str(input('Digite a expressão: '))
parentesesAbrindo = []
parentesesFechando = []

for simbolo in expressao:
    if simbolo == '(':
        parentesesAbrindo.append(simbolo)
    if simbolo == ')':
        parentesesFechando.append(simbolo)

if len(parentesesAbrindo) == len(parentesesFechando):
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')
