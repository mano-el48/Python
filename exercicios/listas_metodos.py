
#  index: 0  1  2  3  4  5
lista1 = [0, 1, 2, 3, 4, 5]
# index: -6 -5 -4 -3 -2 -1

#ultimo elemento
print(lista1[-1])

lista1.append(6)#inserir elemento no final
print(lista1)

lista1.pop()#remover elemento no final
print(lista1)

lista2 = [7, 8, 9]
lista1 += lista2 #concatenando as listas
print(lista1)

print(max(lista1))
print(min(lista1))

lista1.clear()
print(lista1)