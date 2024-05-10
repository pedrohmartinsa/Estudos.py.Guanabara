count = soma = i = 0

n = float(input('Digite um número: '))
r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]

menorNumero = n
maiorNumero = n

while i < 1:

    if r in 'Ss':
        count += 1
        soma += n
        n = float(input('Digite um número: '))
        r = input('Quer continuar?[S/N] ').strip().upper()[0]

    if n > maiorNumero:
        maiorNumero = n

    if n < menorNumero:
        menorNumero = n

    if r in 'Nn':
        count += 1
        soma += n
        media = soma / count
        print(f'A média entre esses número é igual a: {media:.2f}')
        print(f'O maior número foi {maiorNumero:.0f} e o menor foi {menorNumero:.0f}.')
        i += 1
