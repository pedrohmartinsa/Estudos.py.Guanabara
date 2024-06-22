from datetime import date

dados = {}

dados['nome'] = input('Nome: ')

dados['idade'] = date.today().year - (int(input('Ano de nascimento: ')))

dados['cpts'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['cpts'] != 0:
    dados['contratacao'] = int(input('Ano de contratação:'))
    dados['salario'] = float(input(f'Salário:'))
    dados['aposentadoria'] = (dados['idade'] - (date.today().year - dados['contratacao'])) + 35
print()
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
