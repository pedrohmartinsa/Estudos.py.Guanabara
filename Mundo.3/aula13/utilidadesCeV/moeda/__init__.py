def metade(preco=0, sit=False):
    met = preco / 2
    if sit:
        return f'R${met:.2f}'.replace('.', ',')
    else:
        return met


def dobro(preco=0, sit=False):
    dob = 2 * preco
    if sit:
        return f'R${dob:.2f}'.replace('.', ',')
    else:
        return dob


def aumentar(preco, porcentagem, sit=False):
    aumento = preco + (preco * (porcentagem/100))
    if sit:
        return f'R${aumento:.2f}'.replace('.', ',')
    else:
        return aumento


def diminuir(preco, porcentagem, sit=False):
    diminui = preco - (preco * (porcentagem/100))
    if sit:
        return f'R${diminui:.2f}'.replace('.', ',')
    else:
        return diminui


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
