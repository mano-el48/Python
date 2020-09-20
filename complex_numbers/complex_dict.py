def create_complex_number(a: float, b: float):
    return {
        'real': a,
        'imaginary': b
    }


def parse_complex_number_to_string(number):
    return str(number['real']) + " + " + str(number['imaginary']) + "i"


def sum_complex_numbers(number1, number2):
    a = number1['real']
    b = number1['imaginary']
    c = number2['real']
    d = number2['imaginary']

    return {
        'real': a + c,
        'imaginary': b + d
    }


def subtract_complex_numbers(number1, number2):
    a = number1['real']
    b = number1['imaginary']
    c = number2['real']
    d = number2['imaginary']

    return {
        'real': a - c,
        'imaginary': b - d
    }


def multiply_complex_numbers(number1, number2):
    a = number1['real']
    b = number1['imaginary']
    c = number2['real']
    d = number2['imaginary']

    return {
        'real': ((a * c) - (b * d)),
        'imaginary': ((b * c) + (a * d))
    }


def divide_complex_numbers(number1, number2):
    a = number1['real']
    b = number1['imaginary']
    c = number2['real']
    d = number2['imaginary']

    return {
        'real': ((a * c) + (b * d)) / ((c ** 2) + (d ** 2)),
        'imaginary': ((b * c) - (a * d)) / ((c ** 2) + (d ** 2))
    }


a = float(input("\nDigite a parte real do Numero 1: "))
b = float(input("Digite a parte imaginaria do Numero 1: "))

c = float(input("\nDigite a parte real do Numero 2: "))
d = float(input("Digite a parte imaginaria do Numero 2: "))

number1 = create_complex_number(a, b)
print(f'\nNumero 1 = {parse_complex_number_to_string(number1)}')

number2 = create_complex_number(c, d)
print(f'Numero 2 = {parse_complex_number_to_string(number2)}')

result = sum_complex_numbers(number1, number2)
print(f'\nSoma = {parse_complex_number_to_string(result)}')

result = subtract_complex_numbers(number1, number2)
print(f'Subtracao = {parse_complex_number_to_string(result)}')

result = multiply_complex_numbers(number1, number2)
print(f'Multiplicacao = {parse_complex_number_to_string(result)}')

result = divide_complex_numbers(number1, number2)
print(f'Divisao = {parse_complex_number_to_string(result)}')
