from uteis import moeda

preco = float(input('Digite o valor que deseja ver os detalhes: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Com um aumento de 15% fica {moeda.aumentar(preco, 15)}')
print(f'Com um desconto de 20% fica {moeda.diminuir(preco, 20)}')
