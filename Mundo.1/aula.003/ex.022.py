nome = str(input('Digite seu nome inteiro:')).strip()
print('analisando seu nome...')
print('seu nome em maiúsculo é: {}'.format(nome.upper()))
print('seu nome em minúsculo é: {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome)- nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))



