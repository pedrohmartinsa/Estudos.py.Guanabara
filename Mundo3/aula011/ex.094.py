dados = {}
lista_de_dados = []
mulheres = []
soma = 0
while True:
    dados['nome'] = input('Nome: ').strip()
    dados['sexo'] = input('Sexo [M/F]: ').strip().upper()
    while dados['sexo'] not in 'FfMm':
        print('ERRO! Por favor, digite apenas com M ou F.')
        dados['sexo'] = input('Sexo [M/F]: ').strip().upper()

    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista_de_dados.append(dados.copy())
    dados.clear()

    r = str(input('Deseja continuar?[S/N] '))
    while r not in 'SsNn':
        print('ERRO! Responda apenas com S ou N.')
        r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break

media = soma / len(lista_de_dados)
print('=-'*30)
print(f'- O grupo tem {len(lista_de_dados)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print('- Lista das pessoas que estão acima da média:')

for pessoas in lista_de_dados:
    if pessoas['idade'] >= media:
        for k, v in pessoas.items():
            print(f'  - {k} = {v}; ', end='')
        print()

print('<< ENCERRADO >>')
