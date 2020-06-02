
tupla1 = tuple()
print(type(tupla1))
tupla2 = ()
print(type(tupla2))
#print(dir(tupla))#funcoes disponiveis

tupla = ('vemelho', 'azul', 'azul', 'verde', 'preto')
print(tupla[0])
print(tupla[-1])
print(tupla[0:])#do primeiro elemento até o ultimo

print(tupla.index('preto'))
print(tupla.count('azul'))
print(len(tupla))