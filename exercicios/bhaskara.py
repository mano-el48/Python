import math

def bhaskara(a, b, c):
    resultados = []
    delta = delta = (b** 2) - (4 * a * c)
    
    if delta < 0:
    
        return "Delta é negativo, a equação nao possui raizes reais"

    elif delta == 0:
        x1 = (-b + math.sqrt(delta))/(2*a)

        resultados.append(x1) 

        return f'x = {resultados[0]}'

    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
    
        resultados.append(x1)
        resultados.append(x2)
        
        return f'x1 = {resultados[0]} e x1 = {resultados[1]}'

a, b, c = [float(valores) for valores in input('Dgite os valores de a, b e c: ').split()]
print(bhaskara(a, b, c))
# bhaskara(-3, 4, -2)
# bhaskara(1, 1, -6)
# print(bhaskara(1, -10, 25)
