def notes(* num, sit=False):
    '''
    => Function to review many student's notes and situation
    :param num: one or more notes of students (accepts several)
    :param sit: optional value, show the student's academic situations
    :return: return a dictionary with much information of student
    '''
    dictNotes = {'total': len(num)}
    bigger = smaller = num[0]
    soma = 0
    for n in num:
        soma += n
        if n > bigger:
            bigger = n
        if n < smaller:
            smaller = n
    dictNotes['maior'] = bigger
    dictNotes['menor'] = smaller
    dictNotes['média'] = soma / len(num)
    if sit:
        if dictNotes['média'] < 4:
            dictNotes['Situação'] = 'Reprovado.'
        if dictNotes['média'] < 6:
            dictNotes['Situação'] = 'Recuperação.'
        if dictNotes['média'] > 6:
            dictNotes['Situação'] = 'Aprovado.'
        if dictNotes['média'] > 8:
            dictNotes['Situação'] = 'Aprovado com excelência.'
    return dictNotes


print(notes(3.2, 9, 5, 7.5, 6.4, sit=True))
