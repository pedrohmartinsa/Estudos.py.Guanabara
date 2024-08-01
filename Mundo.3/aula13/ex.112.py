from utilidadesCeV import moeda, dados
p = dados.leiaDinheiro('Preço desejado: R$')
print(moeda.resumo(p, 35, 70))
