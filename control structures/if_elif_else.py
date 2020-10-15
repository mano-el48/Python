
def validate_grade(value):
    grade = float(value)

    if grade > 10:
        return 'Nota inválida'
    elif grade >= 9.1:
        return 'A'
    elif grade >= 8.1:
        return 'A-'
    elif grade >= 7.1:
        return 'B'
    elif grade >= 6.1:
        return 'B-'
    elif grade >= 5.1:
        return 'C'
    elif grade >= 4.1:
        return 'C-'
    elif grade >= 3.1:
        return 'D'
    elif grade >= 2.1:
        return 'D-'
    elif grade >= 1.1:
        return 'E'
    elif grade >= 0:
        return 'E-'
    else:
        return 'Nota inválida'


while True:
    grade = input('Nota do aluno: ')
    result = validate_grade(grade)
    print(result)
