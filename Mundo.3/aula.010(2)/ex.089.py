grupo = []
dados = []

while True:
    dados.append(input('Nome: ').strip())
    dados.append(float(input('Nota 1: ').strip()))
    dados.append(float(input('Nota 2: ').strip()))
    dados.append((dados[1] + dados[2]) / 2)
    grupo.append(dados[:])
    dados.clear()

    resposta = ' '
    while resposta not in 'SsNn':
        resposta = input('Quer continuar? ').upper().strip()
        print()
    if resposta in 'Nn':
        break

i = 0
for aluno in grupo:
    i += 1
    print(f'{i}- Nome: {aluno[0]}; Media: {aluno[3]}')
print()
while True:
    pergunta_notas = int(input('Digite o número do aluno que deseja ver a nota: [999 para sair]'))
    if pergunta_notas == 999:
        print('FIM.')
        break
    else:
        print(f'{grupo[pergunta_notas-1][0]}: {grupo[pergunta_notas-1][1]} e {grupo[pergunta_notas-1][2]}')
