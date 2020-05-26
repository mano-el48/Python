from functools import reduce

#8.7, 6.8, 7.7, 7.7, 9.2, 5.3, 8.0
notas = []
n = int(input('Digite a quantidade de notas: '))

print('Digite as Notas: ')
for nota in range(n):
    notas.append ( float(input()) )

def calcularMediaTurma(notas) :
    total = 0
    for index in range(n):
        total += notas[index]
    return total/len(notas)

media = calcularMediaTurma(notas)

print(f'Media da Turma = {media:.2f}')