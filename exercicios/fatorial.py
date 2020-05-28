def fatorial(numero):
     if numero == 0 or numero == 1:
         return 1
     else:
         return numero * fatorial(numero-1)

numero = int(input("Digite o valor: "))
print(fatorial(numero))

