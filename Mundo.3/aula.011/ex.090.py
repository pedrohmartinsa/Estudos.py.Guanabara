aluno = {'Nome': str(input('Nome: ')), 'Média': float(input(f'Média: '))}
if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7.0:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'{k} do {aluno['Nome']} é {v}')
