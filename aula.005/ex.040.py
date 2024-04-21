#Aprovação de aluno

n1 = float(input('Digite sua nota do primeiro semestre: '))
n2 = float(input('Agora, digite a do segundo: '))

nota = (n1 + n2) / 2

if (n1 + n2) / 2 < 5.0:
    print(f'Você foi reprovado. Com uma média de: {nota:.1f}')
elif (n1 + n2) / 2 > 5.0 and (n1 + n2) / 2 < 6.9:
    print(f'Você esta de recuperação. Com uma média de: {nota:.1f}')
else:
    print(f'Você foi aprovado. Com uma média de: {nota:.1f}')
