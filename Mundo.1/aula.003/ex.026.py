frase = str(input('Digite uma frase:')).strip().lower()
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A letra "a" apareceu sua primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra "a" apareceu por último na posição {}'.format(frase.rfind('a')+1))