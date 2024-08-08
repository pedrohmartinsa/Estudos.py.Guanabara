def vote(year):
    from datetime import date
    age = date.today().year - year

    print(f'Com {age} anos: ', end='')

    if age < 16:
        return 'Não vota.'
    if age >= 65 or 16 <= age < 18:
        return 'Voto opcional.'
    if 65 > age >= 18:
        return 'Voto obrigatório.'


print(vote(2000))
