#Categoria de natação

ano = float(input('Digite o ano em que nasceu para ver sua categoria: '))

if 2024 - ano <= 9:
    print('Você esta na categoria mirim.')

elif 2024 - ano > 9 and 2024 - ano <= 14:
    print('Você esta na categoria infantil.')

elif 2024 - ano > 14 and 2024 - ano <= 19:
    print('Você esta na categoria junior.')

elif 2024 - ano > 19 and 2024 - ano <= 20:
    print('Você esta na categoria sênior.')

else:
    print('Você esta na categoria master')
