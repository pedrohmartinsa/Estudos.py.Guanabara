count = 0
soma = 0
i = 0
n = float(input('Digite um número: '))
r = input('Quer continuar?[S/N] ').strip().upper()[0]
while i < 1:
    menorNumero = n
    maiorNumero = n
    count += 1
    soma += n
    if n < menorNumero:
        menorNumero = n
    if n > maiorNumero:
        maiorNumero = n
    if r in 'Ss':
        n = float(input('Digite um número: '))
        r = input('Quer continuar?[S/N] ').strip().upper()[0]
    if r in 'Nn':
        media = soma / count
        print(f'A média entre esses número é igual a: {media:.2f}')
        print(f'O maior número foi {maiorNumero} e o menor foi {menorNumero}')
        i += 1


