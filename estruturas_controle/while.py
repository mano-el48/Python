total = 0
quantity = 0
value = 0

while value != -1:
     value = float(input('Digite -1 para encerrar: '))
     if value != -1:
         quantity += 1
         total += value

print(f'Media dos valores digitados = {total / quantity}')

