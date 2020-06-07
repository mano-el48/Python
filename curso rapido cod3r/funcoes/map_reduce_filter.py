from functools import reduce

alunos = [
    {'nomes': 'Ana', 'nota': 7.2},
    {'nomes': 'Breno', 'nota': 8.1},
    {'nomes': 'Caludia', 'nota': 8.7},
    {'nomes': 'Pedro', 'nota': 6.4},
    {'nomes': 'Rafael', 'nota': 6.7},
]

obter_aprovados = lambda aluno: aluno['nota'] >= 7
obter_notas = lambda aluno: aluno['nota'] 
somar  = lambda a, b: a + b

alunos_aprovados = list(filter(obter_aprovados, alunos))
print(alunos_aprovados)

notas_alunos_aprovados = list(map(obter_notas, alunos_aprovados))
print(notas_alunos_aprovados)

soma_das_notas = reduce(somar, notas_alunos_aprovados) 
print(soma_das_notas)