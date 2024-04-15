#valor a ser pago e condição de pagamento

valor = float(input('Qual o valor a ser pago pelo produto? R$'))
forma = int(input('Qual a forma de pagamento (digite 1 para dinheiro ou cheque e 2 para cartão)? '))

if forma == 1:
    desconto = valor * 0.9
    print(f'Com os 10% de desconto, o valor a ser pago é R${desconto:.2f}')

elif forma == 2:
    parcela = input('Vai querer parcelar? ').upper().split()
    if parcela == 'NÃO':
        desconto = valor * 0.95
        print(f'Com os 5% de desconto, o valor a ser pago é R${desconto:.2f}')
    else:
        qtd = int(input('Gostaria de parcelar em quantas vezes?'))
        if qtd == 2:
            a = valor / 2
            print(f'O valor a ser pago será R${a:.2f} em duas parcelas.')
        else:
            a = valor / qtd + (valor / qtd * 0.2)
            print(f'O valor a ser pago, com 20% de juros e parcelado em {qtd}x ficará R${a:.2f}')
else:
    print('Forma de pagamento inválida, reinicie o programa.')


