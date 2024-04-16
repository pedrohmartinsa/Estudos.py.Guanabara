print('*' * 65)
print('Soma entre os número ímpares que são múltiplos de 3 entre 1 e 500')
print('*' * 65)
s = 0
for c in range(0, 501):
    if c % 3 == 0:
        s += c
    print(s)
print('FIM')


