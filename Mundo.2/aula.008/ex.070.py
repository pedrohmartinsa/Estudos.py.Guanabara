totalCompra = count = precoBarato = nomeBarato = maisDeMil = soma =  0

print('*' * 28)
print('     LOJA SUPER BARATÃO     ')
print('*' * 28)
while True:
    nome = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$'))
    totalCompra += preco
    soma += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if preco > 1000:
        maisDeMil += 1

    if soma == 1:
        precoBarato = preco
        nomeBarato = nome

    if soma > 1:
        if preco < precoBarato:
            precoBarato = preco
            nomeBarato = nome

    if continuar in 'Nn':
        break
print('*' * 28)
print('     FIM DO PROGRAMA     ')
print('*' * 28)
print(f'O total da compra foi R${totalCompra:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${precoBarato:.2f}')

