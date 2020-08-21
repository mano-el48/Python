n = int(input('Digite o numero de linhas: '))
m = int(input('Digite o numero de colunas: '))

print(f'\nDigite os {n*m} elementos da matriz')

matriz = [] # lista vazia
for i in range(n):
    # cria as linhas 
    linha = [] # lista vazia

    for j in range(m):
        linha.append(input())

    # coloque linha na matriz
    matriz.append(linha)

#print(matriz)
print('\n')

# imprimindo
for i in range(n):
    for j in range(m):
        # if i == j:
        #     matriz[i][j] = 0
        
        print(f'{matriz[i][j]} ', end = '')
    print()

