galera = []
dados = []
mai = men = 0

while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))

    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]

    galera.append(dados[:])
    dados.clear()

    r = str(input('Deseja continuar?[S/N] '))
    while r not in 'SsNn':
        r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break

print(f'Foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}. Peso de ', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()
