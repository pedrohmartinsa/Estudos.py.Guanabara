#LENDO O MAIOR E MENOR PESO ENTRE 5 PESSOAS
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa?'))
    if c == 1: #pois se houver apenas 1 peso, ele será o maior e o menor
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso foi de {maior}Kg.')
print(f'O menor peso foi de {menor}Kg.')

