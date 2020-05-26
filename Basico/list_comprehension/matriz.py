n = int(input('Digite o numero de linhas: '))
m = int(input('Digite o numero de colunas: '))

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(int(input(f'Digite o valor de [{i+1}, {j+1}]:')))
    matriz.append(linha)

#imprimir em formato de matriz
for i in range(n):
    print(matriz[i])
    