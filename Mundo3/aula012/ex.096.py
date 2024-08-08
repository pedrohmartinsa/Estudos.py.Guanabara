def area(x, y):
    a = x * y
    print(f'A área de um terreno {x}x{y} é de {a}m2.')


print(f'{"Controle de Terreno":^30}')
print('-' * 30)
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(lar, comp)
