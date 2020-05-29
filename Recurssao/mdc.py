
def mdc(primeiroNumero, segundoNumero):
    if segundoNumero == 0:
        return primeiroNumero
        
    return mdc(segundoNumero, primeiroNumero % segundoNumero)

primeiroNumero = int(input('Digite o pimeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))
print(mdc(primeiroNumero, segundoNumero))
# mdc(1, 2)
# mdc(2, 3)
# mdc(6, 3)
# mdc(9, 3)

# def mdc(a, b):
#     return a if not b else mdc(b, a % b)

# print(mdc(70, 25)) # 5
