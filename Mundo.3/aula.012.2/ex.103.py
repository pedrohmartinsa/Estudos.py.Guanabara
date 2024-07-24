def token():
    name = input('Nome: ')
    if name == '':
        name = '<desconhecido>'
    gols = input('Quantidade de gols: ')
    if gols == '':
        gols = 0
    print(f'O jogador {name} fez {gols} gol(s) no campeonato.')


token()
