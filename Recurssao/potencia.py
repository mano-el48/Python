
def potencia(numero, expoente):
    if expoente == 0:
        return 1
    elif expoente == 1:
        return numero
    else:
        return numero * potencia(numero, expoente-1)

numero = int(input("Digite o primeiro numero: "))
expoente = int(input("Digite o segundo numero: "))
print(potencia(numero, expoente))