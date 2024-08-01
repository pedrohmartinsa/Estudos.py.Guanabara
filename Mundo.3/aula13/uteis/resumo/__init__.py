def formatPreco(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco, juros, desconto):
    dobro = 2 * preco
    metade = preco / 2
    aumento = preco + (preco * (juros/100))
    reducao = preco - (preco * (desconto/100))

    tabela = '''
    --------------------------------
            RESUMO DE VALOR
    --------------------------------
    '''
    msg = f'''Preço analisado:{formatPreco(preco):>20}
    Dobro do preço:{formatPreco(dobro):>20}
    Metade do Preço:{formatPreco(metade):>20}
    {juros}% de aumento:{formatPreco(aumento):>20}
    {desconto}% de redução:{formatPreco(reducao):>20}
    '''
    return tabela + msg



