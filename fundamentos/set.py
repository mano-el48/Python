s = set()
print(type(s))
s = {1}
print(type(s))

#adicioando e removendo elementos
s = set()
s.add(1)# adiocionado
print(s)
s.add(2)
print(s)
s.add(2)
print(s)# não aceita repetições
s.add(3)
print(s)
s.discard(3)# removendo
print(s)
s.add('str')
print(s)
s.add((4, 5, 6))# adicoando uma tupla
print(s)

# operacoes
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print (a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

# pertinencia
print(1 in a) #True
print(5 in a) #False
print(1 not in b) #True
print(5 not in b) #False

c = {1, 2} 
# subconjuto
print(c.issubset(a))
print(c.issubset(b))

# a é "superset" de c
print(a.issuperset(c))#c esta contido em a

# removendo elementos duplicados de uma lista
lista = [1, 2, 2, 3, 4, 5, 5]
print(set(lista))