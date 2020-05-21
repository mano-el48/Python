"""'
Faça um programa que calcule a soma entre todos o números ímpares
que são múltiplos de 3 e que se encontram no intervalo de 1 à 20.
"""
soma = 0
cont = 0
for a in range(1, 20, 2):
    if a % 3 == 0:
        soma += + a
        cont += + 1
print('Soma:', soma)
print('Quantidade:', cont)
