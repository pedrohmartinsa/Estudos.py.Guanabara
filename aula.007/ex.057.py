#SEXO
a = 1
while a == 'F' or 'M':
    a = input('Qual seu genênero[F/M]?').upper().strip()
    if a not in 'FM':
        print('Errado, digite novamente.')
    else:
        print('Legal.')
