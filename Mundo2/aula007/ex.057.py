#SEXO
a = input('Qual seu genênero[F/M]?').upper().strip()[0]
while a not in 'FfMm':
    a = input('Dado inválido, por favor, digite seu sexo [F/M]:').upper().strip()[0]
print(f'Sexo {a} registrado com sucesso.')
