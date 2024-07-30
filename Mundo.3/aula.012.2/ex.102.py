def factorial(num=1, show=False):
    '''
    Program with intention of calculated the factorial
    num: parameter where going the number to be calculated
    show: (optional) parameter where going show or not the calculation
    return: return the finish product
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c

    if show:
        for c in range(num, 0, -1):
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')

    return f


print(factorial(5))
help(factorial())
