from time import sleep

cont = cont18 = contHomem = contMulher20 = 0

while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Sexo [F/M]:'))
    cont += 1
    while True:
        if sexo in 'FfMm':
            break
        else:
            print('Sexo inválido, digite novamente.')
            sexo = str(input('Sexo [F/M]:')).upper().strip()[0]

    if idade > 18:
        cont18 += 1

    if sexo in 'Mm':
        contHomem += 1

    if sexo in 'Ff' and idade < 20:
        contMulher20 += 1

    sleep(1)
    print()
    print(f'Idade e sexo cadastrados com sucesso.')
    print()
    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    print()

    while True:
        if continuar not in 'SsNn':
            print('Resposta inválida, digite novamente.')
            continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
            print()
        else:
            break


    if continuar in 'Nn':
        print(f'{cont} pessoas cadastradas.')
        print(f'{cont18} pessoas tem mais de 18 anos.')
        print(f'{contHomem} são homens.')
        print(f'{contMulher20} são mulheres e tem menos de 20 anos.')
        break

