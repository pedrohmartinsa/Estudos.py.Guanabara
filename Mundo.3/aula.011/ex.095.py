dados_jogador = {}
grupo = []
gols = []
soma_total_gols = 0
while True:

    print('-'*25)
    dados_jogador['nome'] = input('Nome do Jogador: ').strip()
    dados_jogador['num_partidas'] = int(input(f'Quantas partidas {dados_jogador['nome']} jogou?'))

    for c in range(0, dados_jogador['num_partidas']):
        gol = int(input(f'Quantos gols na partida {c+1}? '))
        gols.append(gol)
        soma_total_gols += gol

    dados_jogador['gols'] = gols[:]
    dados_jogador['total'] = soma_total_gols
    grupo.append(dados_jogador.copy())
    dados_jogador.clear()
    gols.clear()
    soma_total_gols = 0
    r = ' '
    while r not in 'SsNn':
        r = input('Deseja continuar ? [S/N]').upper().strip()
    if r in 'Nn':
        break
print(grupo)

print('-=' * 30)
print('cod ', end='')
for i in dados_jogador.keys():
    print(f'{i:>15}')
print('_'*40)
for k, v in enumerate(grupo):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('_'*40)
while True:
    cod = int(input('Mostrar dados de qual jogador ? [cód]'))
    if cod == 999:
        break
    if cod > len(grupo) - 1 or cod < 0:
        print('Código inexistente, digite um válido.')
        continue

    print(f'LEVANTAMENTO DO JOGADOR {grupo[cod]}')
