#LENDO NOME, IDADE E SEXO DE 4 PESSOAS E DIZENDO:
#MÉDIA DE IDADE, NOME DO HOMEM MAIS VELHO E QUANTAS MULHERES TEM MENOS DE 20 ANOS
soma = 0
cont = 0
maiorIdadeHomem = 0
nomeVelho = ''
contFem = 0
for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo(M/F): ').upper().strip()
    print()
    #media
    soma += idade
    cont += 1
    #homens
    if c == 1 and sexo in 'M':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    #mulheres
    if sexo in 'F' and idade < 20:
        contFem += 1



media = soma / cont
print(f'A média de idade do grupo é {media}.')
print()
print(f'O homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}.')
print()
print(f'Tem se {contFem} mulheres com menos de 20 anos.')
