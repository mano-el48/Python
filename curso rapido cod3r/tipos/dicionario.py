
pessoa = {}
print(type(pessoa))
#print(dir(dict))#funcoes disponiveis
pessoa = {'nome': 'Manoel', 'idade': 21, 'curso': ['CCO']}
print(len(pessoa)) #3
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['curso'])

pessoa['idade'] = 18
print(pessoa)
pessoa['curso'].append('Engenharia de Software') #adiocionar
print(pessoa)
pessoa.pop('idade')#remover idade
print(pessoa)
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)
pessoa.clear() #zerar
print(pessoa)
