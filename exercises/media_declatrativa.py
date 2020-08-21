from functools import reduce

#8.7, 6.8, 7.7, 7.7, 9.2, 5.3, 8.0
grades = []
grades = []
n = int(input('Digite a quantidade de notas: '))

print('Digite as Notas: ')
for grade in range(n):
    grades.append ( float(input()) )

sum = lambda a, b: a + b
divide = lambda a, b: a / b

average = divide(
    reduce(sum, grades),
    len(grades)
    )

print(f'Media da Turma = {average:.2f}')