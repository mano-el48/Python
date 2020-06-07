total = 0
qtde = 0
valor = 0

while valor != -1:
     valor = float(input('Digite -1 para encerrar: '))
     if valor != -1:
         qtde += 1
         total += valor

print(f'Media dos valores digitados = {total / qtde}')

