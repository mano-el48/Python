temperaturaAtual = float(input('Digite o valor da temperatura: '))
escalaAtual = str(input('Digite a escala da temperatura atual: '))
escalaConvertida = str(input('Digite a unidade da escala para a qual deseja converter: '))

# Celsius para Fahrenheit
if escalaAtual == 'C' and escalaConvertida == 'F':
    temperaturaConvertida = (temperaturaAtual * (9.0 / 5.0)) + 32.0
    print(f'A temperratura {temperaturaAtual:.2f}{escalaAtual} corresponde à {temperaturaConvertida:.2f}{escalaConvertida}')

# Celsius para Kelvin
if escalaAtual == 'C' and escalaConvertida == 'K':
    temperaturaConvertida = temperaturaAtual + 273.15
    print(f'A temperratura {temperaturaAtual:.2f}{escalaAtual} corresponde à {temperaturaConvertida:.2f}{escalaConvertida}')

# Fahrenheit para Celsius
if escalaAtual == 'F' and escalaConvertida == 'C':
    temperaturaConvertida = (temperaturaAtual - 32.0) * (5.0 / 9.0)
    print(f'A temperratura {temperaturaAtual:.2f}{escalaAtual} corresponde à {temperaturaConvertida:.2f}{escalaConvertida}')

# Fahrenheit para Kelvin
if escalaAtual == 'F' and escalaConvertida == 'K':
    temperaturaConvertida = ((temperaturaAtual - 32.0) * (5.0 / 9.0)) + 273.15
    print(f'A temperratura {temperaturaAtual:.2f}{escalaAtual} corresponde à {temperaturaConvertida:.2f}{escalaConvertida}')

# Kelvin para Celsius
if escalaAtual == 'K' and escalaConvertida == 'C':
    temperaturaConvertida = temperaturaAtual - 273.15
    print(f'A temperratura {temperaturaAtual:.2f}{escalaAtual} corresponde à {temperaturaConvertida:.2f}{escalaConvertida}')


# Kelvin para Fahrenheit
if escalaAtual == 'K' and escalaConvertida == 'F':
    temperaturaConvertida = ((temperaturaAtual - 273.15) * (9.0 / 5.0)) + 32
    print(f'A temperratura {temperaturaAtual:.2f}{escalaAtual} corresponde à {temperaturaConvertida:.2f}{escalaConvertida}')
