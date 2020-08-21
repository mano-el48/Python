
fatorial = lambda numero: 1 if not numero else numero * fatorial(numero-1)

numero = int(input("Digite o valor: "))
print(fatorial(numero))

# def fatorial(numero):
#      if numero == 0:
#          return 1
#      else:
#          return numero * fatorial(numero-1)
