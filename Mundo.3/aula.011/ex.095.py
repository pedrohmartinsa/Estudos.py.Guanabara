dados_jogador = {}
gols = []
lista_jogadores = []
lista_gols = []

while True:
    dados_jogador['nome'] = input('Nome: ')
    dados_jogador['num_partidas'] = int(input(f'Quantas partidas {dados_jogador['nome']} jogou?'))
    for c in range(0, dados_jogador['num_partidas']):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))

    lista_jogadores.append(dados_jogador.copy())
    lista_gols.append(gols[:])
    dados_jogador.clear()
    gols.clear()

    r = ' '
    while r not in 'SsNn':
        r = input(f'Deseja continuar? [S/N]').upper()
    if r in 'Nn':
        break

print(lista_jogadores)
