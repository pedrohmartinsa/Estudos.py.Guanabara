#Dizer se ja completou a maioridade
from datetime import date
atual = date.today().year
maiorIdade = 0
menorIdade = 0
for c in range(1, 8):
    ano = int(input('Em que ano você nasceu? '))
    idade = atual - ano
    if idade < 18:
        print('Você ainda não completou maior idade')
        menorIdade += 1
        print()
    else:
        print('Você ja completou maior idade')
        maiorIdade += 1
        print()
print(f'Ao todo, {maiorIdade} já completaram a maior idade e {menorIdade} ainda não completaram.')