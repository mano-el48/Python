
print('Os falsos.........')
print(not not 0)
print(not not None)#parecido com 'null'
print(not not '')
print(not not [])
print(not not ())#tuple
print(not not {})#dicionario
print(not not set())

print('------------------')

print('Os verdadeiros....')
print(not not 1)
print(not not -1)
print(not not 2)
print(not not 3)
print(not not int)
print(not not float)
print(not not str)