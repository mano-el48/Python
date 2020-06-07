'''
Uma tupla é uma lista imutável que restringe 
a adição, alteração e remoção de elementos

'''
tupla1 = tuple()
print(type(tupla1))
tupla2 = ()
print(type(tupla2))
# tupla3 = ('texto') #str
tupla3 = ('texto', ) #str
print(type(tupla3))
#print(dir(tupla))#funcoes disponiveis

tupla = ('vermelho', 1.1, -2,  'azul', 'azul', 'verde', 'preto')
print(tupla)
print('Vermelho' in tupla) # False
print('vermelho' in tupla) # True
print(tupla[0]) # vermelho
print(tupla[-1]) # preto
print(tupla[0:]) # do primeiro elemento até o ultimo

print(tupla.index('preto')) # 6
print(tupla.count('azul')) # 2
print(f'Tamanho da tupla = {len(tupla)}') # 7