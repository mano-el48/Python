n = int(input('Digite o valor de n: '))

vetor = [n]
soma = 0

for index in range(0, n):
    vetor.append(int(input('Digite os números: ')))
    soma += vetor[index]
print(f'Soma = {soma}')