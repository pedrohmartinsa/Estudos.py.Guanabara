palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

#para analisar cada palavra da tupla
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    #para analisar cada letra das palavras
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
