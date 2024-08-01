from uteis import moeda

preco = float(input('Digite o valor que deseja ver os detalhes: R$'))
print(f'A metade de {moeda.formatPreco(preco)} é {moeda.metade(preco, sit=False)}')
print(f'O dobro de {moeda.formatPreco(preco)} é {moeda.dobro(preco, sit=True)}')
print(f'Com um aumento de 15% fica {moeda.aumentar(preco, 15, sit=True)}')
print(f'Com um desconto de 20% fica {moeda.diminuir(preco, 20, sit=True)}')
