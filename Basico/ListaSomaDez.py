n = int(input('Digite o valor de n: '))

vet = [n]
s = 0

for i in range(0, n):
    vet.append(int(input('Digite os números: ')))
    s += vet[i]
print('Soma = {}'.format(s))