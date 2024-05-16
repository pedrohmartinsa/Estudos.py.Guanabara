timesBrasileirao = ('Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 'Cruzeiro', 'Atlético-MG', 'Bragantino', 'Palmeiras', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco da Gama', 'Criciúma', 'Juventude', 'Corinthians', 'Fluminense', 'EC Vitória', 'Atlético-GO', 'Cuiabá')

#colocação completa
print('Tabela completa:')

for cont in range(0, len(timesBrasileirao)):
    print(f'{cont + 1}° colocado: {timesBrasileirao[cont]}.')

print()

#5 primeiros
print('Primeiros colocados:')

for cont in range(0, 6):
    print(f'{cont}°: {timesBrasileirao[cont]}')

print()

#últimos 4
print('Últimos colocados:')

print(timesBrasileirao[::-1])

'''for cont in timesBrasileirao[-1:-4]:
    print(f'{cont}°: {timesBrasileirao}')'''

print()

#Ordem alfabética
print('Tabela em ordem alfabética:')

print(sorted(timesBrasileirao))

print()

#Posição do Corinthians
p = timesBrasileirao.index('Corinthians')

print(f'O Corinthians está na {p}° colocação.')
