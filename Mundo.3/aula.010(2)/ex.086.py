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