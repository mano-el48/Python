
def mdc(primeiroNumero, segundoNumero):
    # not segundoNumero -> segundoNumero == 0 pois 0 = False
    return primeiroNumero if not segundoNumero else mdc(segundoNumero, primeiroNumero % segundoNumero)

primeiroNumero = int(input('Digite o pimeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))
print(mdc(primeiroNumero, segundoNumero))

# def mdc(primeiroNumero, segundoNumero):
#     if segundoNumero == 0:
#         return primeiroNumero
        
#     return mdc(segundoNumero, primeiroNumero % segundoNumero)
