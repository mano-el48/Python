

arredondarESubstir = lambda numero: f'R${str(round(numero, 2)).replace(".",",")}'

numero = float(input('Dgigite o valor para ser convertido: '))
print(arredondarESubstir(numero))
#0.30000000000000004
