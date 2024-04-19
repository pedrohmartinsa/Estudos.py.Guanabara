frase = str(input('Escreva uma frase: ')).lower().strip()
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A primeira letra "a" apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra "a" apareceu na posição {}'.format(frase.rfind('a')+1))