from functools import reduce

#8.7, 6.8, 7.7, 7.7, 9.2, 5.3, 8.0
grades = []
n = int(input('Digite a quantidade de notas: '))

print('Digite as Notas: ')
for grade in range(n):
    grades.append ( float(input()) )

def calculate_average(grades) :
    total = 0
    for index in range(n):
        total += grades[index]
    return total / len(grades)

average = calculate_average(grades)
print(f'Media da Turma = {average:.2f}')