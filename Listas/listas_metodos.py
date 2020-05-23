
lista1 = [0, 1 , 2, 3, 4, 5]

print(lista1[-1])#ultimo elemento

lista1.append(6)#inserir elemento no final
print(lista1)

lista1.pop()#remover elemento no final
print(lista1)

lista2 = [7, 8, 9]
lista1 += lista2 #concatenando as listas
print(lista1)

print(max(lista1))
print(min(lista1))