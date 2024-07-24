from datetime import date


def vote():
    year = int(input('Ano de nascimento: '))
    age = date.today().year - year

    print(f'Com {age} anos: ', end='')

    if age < 16:
        print('Não vota.')
    if age >= 65 or 16 <= age < 18:
        print('Voto opcional.')
    if 65 > age >= 18:
        print('Voto obrigatório.')


vote()
