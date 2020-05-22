'''


'''
class TreeNand:
  def __init__(self,niveis,folhas):
    elem_corretos = [0,1]
    self.niveis = niveis
    self.folhas = folhas
    self.arvore = self.cria_arvore()
    #erros
    for elementos in folhas:
      if elementos not in elem_corretos:
        raise ValueError('Valor da folha inválido!')
    if len(folhas) > 2**(niveis-1):
      raise IndexError('Número de folhas maior que o possível!')
    elif len(folhas) < 2**(niveis-1):
      raise IndexError('Número de folhas menor que o possível!')   
  
  def evaluate_simple(self):
     #nivel = 1 retorna a arvore
    elem = self.arvore[0][0]
    if self.niveis == 1:
      return elem
    else:
      #pega as folhas e divide em dois
      lt = self.arvore[0][:int(len(self.arvore[0])/2)]
      left = TreeNand(self.niveis-1,lt)
      rt = self.arvore[0][int(len(self.arvore[0])/2):]
      right = TreeNand(self.niveis-1,rt)
      #print(f"tamanho - {len(right.arvore)}")
      if len(right.arvore) == 1:
        valor = self.opernand(left.arvore,right.arvore)
        arv_aux = [left, valor, right]
        #print(left.arvore,right.arvore,valor)
        return arv_aux
      else:
        #divide de novo
        left.evaluate_simple()
        right.evaluate_simple()
    
  def opernand(self,left, right):
    if left == right:
      if left == [1]:
        return 0
      else:
        return 1
    else:
      return 1
  
  def evaluate_complex(self):
    elem = self.arvore[0][0]
    if self.niveis == 1:
      return elem
    else:
      lt = self.arvore[0][:int(len(self.arvore[0])/2)]
      left = TreeNand(self.niveis-1,lt)
      rt = self.arvore[0][int(len(self.arvore[0])/2):]
      right = TreeNand(self.niveis-1,rt)
      # recursividade a esquerda    
      if left.evaluate_complex() == '0':
        return '1'
      else:
        # recursividade a direita
        if right.evaluate_complex() == '0':
          return '1'
        else:
          return '0'
    
  def cria_arvore(self):
    ## preenche arvore das folhas com None nas raizes vazias
    arvore = []
    nivel = []
    if len(self.folhas) == 1:
      arvore.append(self.folhas)
    else:
      arvore.append(self.folhas)
      n = self.folhas
  #percorre o nivel
      for j in range(2,self.niveis+1):
  #percorre os elementos dois a dois
        for i in range(0,len(n)-1,2):
   #cria os elementos
          nivel.append(None)
          n = nivel
        arvore.append(nivel)
        nivel = []
    return arvore


  def __str__(self):
    treeStr = str("  ")
    for i in range(self.niveis-1,-1,-1):
      treeStr += "  "*(len(self.folhas)//5*i) + str(self.arvore[i]) +"\n"
    return treeStr

  def __repr__(self):
    return str(self)
