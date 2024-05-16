from datetime import date #para analisar a data atual
ano = int(input('Que ano você quer analisar? Digite 0 caso queira analisar o ano em que esta:'))
if ano == 0:
    ano = date.today().year #para analisar a data atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')