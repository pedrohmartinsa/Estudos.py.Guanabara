def notes(* num, sit=False):
    """
    => Function to review many student's notes and situation
    :param num: one or more notes of students (accepts several)
    :param sit: optional value, show the student's academic situations
    :return: return a dictionary with much information of student
    """
    dictNotes = {}
    dictNotes['total'] = len(num)
    dictNotes['maior'] = max(num)
    dictNotes['menor'] = min(num)
    dictNotes['média'] = sum(num) / len(num)
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


print(notes(5.5, 2.5, 1.5,  sit=True))
