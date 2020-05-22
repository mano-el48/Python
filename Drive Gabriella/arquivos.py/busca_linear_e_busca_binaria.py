# Função que faz a busca linear em um array não ordenado
def busca_linear(array, valor):
  for i in range(len(array)):
    if array[i]==valor:
      return i
  return None
    
array = [2,17,80,3,202]
valor = 5
busca_linear(array, valor)

# Função que faz a busca linear em um array ordenado
def busca_linear_ordenado(array, valor):
  for i in range(len(array)):
    if array[i]==valor:
      return i
    elif array[i] > valor:
      break
  return None

array = [2,3,17,80,202]
valor = 17
print(busca_linear_ordenado(array, valor))