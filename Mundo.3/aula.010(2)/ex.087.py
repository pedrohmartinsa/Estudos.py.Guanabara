matriz = []
colunaZero = []
colunaUm = []
colunaDois = []
for c in range(0, 3):
    colunaZero.append(int(input(f'Digite um valor para [0,{c}]:')))
matriz.append(colunaZero)
for c in range(0, 3):
    colunaUm.append(int(input(f'Digite um valor para [1,{c}]:')))
matriz.append(colunaUm)
for c in range(0, 3):
    colunaDois.append(int(input(f'Digite um valor para [2,{c}]:')))
matriz.append(colunaDois)
print('-='*30)
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
print('-='*30)
pares = 0
for v in matriz:
    for valor in v:
        if valor % 2 == 0:
            pares += valor
print(f'A soma dos números pares é: {pares}.')
print(f'A soma dos valores da última coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
maiorValor = 0
for valores in matriz[1]:
    if valores > maiorValor:
        maiorValor = valores
print(f'O maior valor é da segunda linha é {maiorValor}.')
