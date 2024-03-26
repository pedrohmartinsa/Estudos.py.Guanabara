dias = int(input('Quantos dias você ficou com o carro?'))
km = int(input('Quantos Km você andou com o carro?'))
p = (dias * 60) + (km * 0.15)
print(f'O preço a ser pago pelo aluguel do carro é de R${p:.2f}')