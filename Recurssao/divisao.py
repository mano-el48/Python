
divisao = lambda numero1, numero2: 0 if numero1 < numero2  else (1 + divisao(numero1-numero2, numero2))

# def divisao(numero1, numero2):
#     if numero1 < numero2:
#         return 0
#     else:
#         return 1 + divisao(numero1-numero2, numero2)

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
print(divisao(numero1, numero2))