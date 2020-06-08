
lista = [1, 2, 3]
type(lista)
#dir(lista)

lista.append(3)
print(lista) # [1, 2, 3, 3]
print(f'tamanh da lista = {len(lista)}') # 4

lista[2] = 4
print(lista) # [1, 2, 3, 4]

lista.insert(0, -1)
print(lista) # [-1, 1, 2, 4, 3]

print(lista[4]) # 3
print(lista[-1]) # 3

lista = [1, 5, 'Ana', 'Bia']
lista.remove('Bia')
print(lista)# [1, 5, 'Ana']
print(lista.index('Ana')) # 2
lista.reverse()
print(lista) #['Ana', 5, 1]
print(lista.index('Ana')) # 0

# lista = [1, 5, 'Rebeca', 'Leo', 3.1415]
print(1 in lista) # True
print('Rebeca' in lista) #False
print('Pedro' not in lista) #True


lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[0:2]) # ['Ana', 'Lia']
print(lista[0:3]) # ['Ana', 'Lia', 'Rui']
print(lista[1:]) # ['Lia', 'Rui', 'Paulo', 'Dani']
print(lista[0:-1]) # ['Ana', 'Lia', 'Rui', 'Paulo']
print(lista[0:]) #['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[:]) #['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[::2]) #
print(lista[::-1]) # ['Dani', 'Paulo', 'Rui', 'Lia', 'Ana']
del lista[2]
print(lista) # ['Ana', 'Lia', 'Paulo', 'Dani']
del lista[1:]
print(lista) # ['Ana']