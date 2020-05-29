
def multiplicacao(primeiroNumero, segundoNumero):
    if primeiroNumero == 0 or segundoNumero == 0:
        return 0
    elif segundoNumero == 1:
        return primeiroNumero
    else:
        return primeiroNumero + multiplicacao(primeiroNumero, segundoNumero-1)

primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero: "))
print(multiplicacao(primeiroNumero, segundoNumero))