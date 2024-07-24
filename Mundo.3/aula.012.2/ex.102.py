def factorial(num=1, show=False):
    """
    Program with intention of calculated the factorial
    num: parameter where going the number to be calculated
    show: parameter where going show or not the calculation
    return: return the finish product
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c

    if show == True:
        for c in range(num, 1, -1):
            print(f'{c}', end=' x ')
        print(f'1 = {f}')

    else:
        return f


print(factorial(6, True))
