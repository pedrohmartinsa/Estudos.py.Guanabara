#Alistamento
nome = input('Olá, bem vindo ao programa de alistamento, como posso te chamar? ')
ano = int(input(f'{nome}, em que ano você nasceu? '))

if 2024 - ano < 18:
    print(f'{nome}, ainda não chegou seu momento de se alistar, espere {tempo} anos.')
elif 2024 - ano >= 18:
    print(f'{nome}, está no momento de se alistar.')
else:
    print(f'{nome}, já passou do prazo de alistamento, passou {tempo} anos para se alistar, sinto muito.')
