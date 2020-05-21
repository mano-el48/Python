n = int(input('Digite o numero de alunos: '))
nomes = []
notas = []
media = 0

for i in range(n):
    nomes.append(input('Informe o nome do aluno: '))
    notas.append(float(input('Informe a nota de ' + nomes[i] + ': ')))
    media = media + notas[i]
media = media / n
print(f'A media da turma é {media:.2f}')

for i in range(n):
    if notas[i] > media:
        print('Parabens', nomes[i])
