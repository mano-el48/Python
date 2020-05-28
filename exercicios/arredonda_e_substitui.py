

arredondarESubstir = lambda numero: 'R$' + format(numero, '.2f').replace(".",",")

numero = float(input('Dgigite o valor para ser convertido: '))
print(arredondarESubstir(numero))
#0.30000000000000004
