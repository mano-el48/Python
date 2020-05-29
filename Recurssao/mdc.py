
mdc = lambda numero1, numero2: numero1 if not numero2 else mdc(numero2, numero1 % numero2)

numero1 = int(input('Digite o pimeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
print(mdc(numero1, numero2))

# def mdc(numero1, numero2):
#     if numero2 == 0:
#         return numero1
        
#     return mdc(numero2, numero1 % numero2)
