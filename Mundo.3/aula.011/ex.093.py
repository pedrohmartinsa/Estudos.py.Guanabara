dados_jogador = {}
gols = []
soma = 0

dados_jogador['nome'] = input('Nome: ').strip()

num_partidas = int(input(f'Quantas partidas {dados_jogador['nome']} jogou? '))

for c in range(0, num_partidas):
    gols.append(int(input(f'   Quantos gols na partida {c+1}: ')))

dados_jogador['gols'] = gols

for i in gols:
    soma += i
dados_jogador['total'] = soma

print('='*30)
for k, v in dados_jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('='*30)
print(f'O jogador {dados_jogador['nome']} jogou {num_partidas} partidas.')

for j, g in enumerate(gols):
    print(f'   => Na partrida {j+1}, fez {g} gols.')
print(f'Foi um total de {soma} gols.')
