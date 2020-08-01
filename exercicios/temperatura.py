present_temperature = float(input('Digite o valor da temperatura: '))
present_scale = str(input('Digite a escala da temperatura atual: '))
converted_scale = str(input('Digite a unidade da escala para a qual deseja converter: '))

# Celsius para Fahrenheit
if present_scale == 'C' and converted_scale == 'F':
    converted_temperature = (present_temperature * (9.0 / 5.0)) + 32.0
    print(f'A temperatura {present_temperature:.2f} {present_scale} corresponde à {converted_temperature:.2f} {converted_scale}')

# Celsius para Kelvin
if present_scale == 'C' and converted_scale == 'K':
    converted_temperature = present_temperature + 273.15
    print(f'A temperatura {present_temperature:.2f} {present_scale} corresponde à {converted_temperature:.2f} {converted_scale}')

# Fahrenheit para Celsius
if present_scale == 'F' and converted_scale == 'C':
    converted_temperature = (present_temperature - 32.0) * (5.0 / 9.0)
    print(f'A temperatura {present_temperature:.2f} {present_scale} corresponde à {converted_temperature:.2f} {converted_scale}')

# Fahrenheit para Kelvin
if present_scale == 'F' and converted_scale == 'K':
    converted_temperature = ((present_temperature - 32.0) * (5.0 / 9.0)) + 273.15
    print(f'A temperatura {present_temperature:.2f} {present_scale} corresponde à {converted_temperature:.2f} {converted_scale}')

# Kelvin para Celsius
if present_scale == 'K' and converted_scale == 'C':
    converted_temperature = present_temperature - 273.15
    print(f'A temperatura {present_temperature:.2f} {present_scale} corresponde à {converted_temperature:.2f}{converted_scale}')


# Kelvin para Fahrenheit
if present_scale == 'K' and converted_scale == 'F':
    converted_temperature = ((present_temperature - 273.15) * (9.0 / 5.0)) + 32
    print(f'A temperatura {present_temperature:.2f} {present_scale} corresponde à {converted_temperature:.2f}{converted_scale}')
