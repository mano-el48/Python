def calcularFatorialDe(numero):
     if numero == 0 or numero == 1:
         return 1
     else:
         return numero * calcularFatorialDe(numero-1)

numero = int(input("Digite o valor: "))
print(calcularFatorialDe(numero))

