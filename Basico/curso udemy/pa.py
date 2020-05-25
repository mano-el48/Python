
print()
primeiroTermo = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
a1 = primeiroTermo
print('{:.0f}'.format(primeiroTermo))

"""'
range(valor_incial, valor_anterior_ao_valor_final
"""
for termo in range(0, 9):
    a1 = a1 + razao
    print('{:.0f}'.format(a1))