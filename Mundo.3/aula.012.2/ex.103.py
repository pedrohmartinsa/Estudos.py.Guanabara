def token():
    '''
    Program with intention of register name and goals number of a soccer player
    name: zone of put the name
    goals: zone of put the goals number
    '''
    name = input('Nome: ')
    if name == '':
        name = '<desconhecido>'
    goals = input('Quantidade de gols: ')
    if goals == '':
        goals = 0
    print(f'O jogador {name} fez {goals} gol(s) no campeonato.')


token()
