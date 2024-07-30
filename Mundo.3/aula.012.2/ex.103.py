def token(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
    '''
    Program with intention of register name and goals number of a soccer player
    name: zone of put the name
    goals: zone of put the goals number
    '''


name = input('Nome: ')
goals = input('Quantidade de gols: ')
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name.strip() == '':
    token(gol=0)
else:
    token(name, goals)




