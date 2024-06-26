dados_jogador = {}
time = []
gols = []
soma_total_gols = 0
while True:

    print('-'*25)
    dados_jogador['nome'] = input('Nome do Jogador: ').strip()
    num_partidas = int(input(f'Quantas partidas {dados_jogador['nome']} jogou?'))

    for c in range(0, num_partidas):
        gol = int(input(f'Quantos gols na partida {c+1}? '))
        gols.append(gol)
        soma_total_gols += gol

    dados_jogador['gols'] = gols[:]
    dados_jogador['total'] = soma_total_gols
    time.append(dados_jogador.copy())
    dados_jogador.clear()
    gols.clear()
    soma_total_gols = 0
    r = ' '
    while r not in 'SsNn':
        r = input('Deseja continuar ? [S/N]').upper().strip()
    if r in 'Nn':
        break
print(time)

print('-=' * 30)
print('cod ', end='')
for i in time:
    for k in i.keys():
        print(f'{k:<15}', end='')
print()
print('_'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_'*40)

while True:
    cod = int(input('Mostrar dados de qual jogador ? [cód]'))
    if cod == 999:
        break
    if cod > len(time) - 1 or cod < 0:
        print('Código inexistente, digite um válido.')
        continue

    print(f' -- LEVANTAMENTO DO JOGADOR {time[cod]['nome']}')

    for c in range(0, len(time[cod]['gols'])):
        print(f'    - No jogo {c+1} fez {time[cod]['gols'][c]} gols.')
print('<<ENCERRADO>>')
