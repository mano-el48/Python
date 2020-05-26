from functools import reduce

#8.7, 6.8, 7.7, 7.7, 9.2, 5.3, 8.0
notas = []
n = int(input('Digite a quantidade de notas: '))

print('Digite as Notas: ')
for nota in range(n):
    notas.append ( float(input()) )

somar = lambda a, b: a + b
dividir = lambda a, b: a/b

media = dividir(
    reduce(somar, notas),
    len(notas)
    )

print(f'Media da Turma = {media:.2f}')