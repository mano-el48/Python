#dir(p) - exibe todos os metodos da classe

class pilha:
  def __init__(self):
    self.dados = []
    
  def __str__(self):
    #metodo str devolve em forma de str o objeto dados q é uma lista, os metodos padrões funcionam pra classe
    return str(self.dados)
  
  def __repr__(self):
    #repete o str ou aplica str no objeto
    return str(self)
  
  def __len__(self):
    return len(self.dados)
  
  def pop(self):
    #remove o ultimo elemento e devolve o valor
    if self.dados:
      return self.dados.pop()
    else:
      raise IndexError('Remoção de pilha vazia!')
  
  def push(self, v):
    #dovolve none por padrão
    self.dados.append(v)
  
  def read(self):
    #vazia - False - erro de execução, c dados - True
    if self.dados:
      return self.dados[-1]
    else:
      raise IndexError('Leitura de pilha vazia!')
  
#p = pilha()
#p.push(5)
#print(p.read())
#print(p.pop())
#len(p)


p = pilha()
p.push(4)
p.push(7)
p.push(2)
print(p)
p.pop()
print(p)
p.pop()
print(p)
p.pop()
print(p)


class fila(pilha):
  def pop(self):
  #remove o primeiro elemento e devolve o valor
    if self.dados:
      return self.dados.pop(0)
    else:
      raise IndexError('Remoção de pilha vazia!')
  
  def read(self):
    #vazia - False - erro de execução, c dados - True
    if self.dados:
      return self.dados[0]
    else:
      raise IndexError('Leitura de pilha vazia!')
  
p = fila()
p.push(4)
p.push(7)
p.push(2)
print(p)
p.pop()
print(p)
p.pop()
print(p)
p.pop()
print(p)