galera = []
dados = []
pesadosNome = []
levesNome = []
pesadosPeso = []
levesPeso = []


while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    galera.append(dados[:])
    dados.clear()

    r = str(input('Deseja continuar?[S/N] '))
    while r not in 'SsNn':
        r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break


print(f'Foram cadastradas {len(galera)} pessoas.')
for p in galera:
    if p[1] >= 70:
        pesadosNome.append(p[0])
        pesadosPeso.append(p[1])
    elif p[1] <= 70:
        levesNome.append(p[0])
        levesPeso.append(p[1])

print(f'O maior peso foi de {pesadosPeso}. Peso de {pesadosNome}')
print(f'O menor peso foi de {levesPeso}. Peso de {levesNome}')
