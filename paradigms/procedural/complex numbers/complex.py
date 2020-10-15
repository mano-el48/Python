from collections import namedtuple

Complex = namedtuple("Complex", "real imaginary")


def parse_complex_number_to_string(number: Complex):
    return str(number.real) + " + " + str(number.imaginary) + "i"


def sum_complex_numbers(number1: Complex, number2: Complex):
    a = number1.real
    b = number1.imaginary
    c = number2.real
    d = number2.imaginary

    real = a + c
    imaginary = b + d

    return Complex(real, imaginary)


def subtract_complex_numbers(number1: Complex, number2: Complex):
    a = number1.real
    b = number1.imaginary
    c = number2.real
    d = number2.imaginary

    real = a - c
    imaginary = b - d
    

    return Complex(real, imaginary)


def multiply_complex_numbers(number1: Complex, number2: Complex):
    a = number1.real
    b = number1.imaginary
    c = number2.real
    d = number2.imaginary

    real = ((a * c) - (b * d))
    imaginary = ((b * c) + (a * d))
    
    return Complex(real, imaginary)


def divide_complex_numbers(number1: Complex, number2: Complex):
    a = number1.real
    b = number1.imaginary
    c = number2.real
    d = number2.imaginary

    real = ((a * c) + (b * d)) / ((c ** 2) + (d ** 2))
    imaginary = ((b * c) - (a * d)) / ((c ** 2) + (d ** 2))

    return Complex(real, imaginary)

    # Usando Dicionario

    # def create_complex_number(a: float, b: float):
#     return {
#         'real': a,
#         'imaginary': b
#     }


# def parse_complex_number_to_string(number):
#     return str(number['real']) + " + " + str(number['imaginary']) + "i"


# def sum_complex_numbers(number1, number2):
#     a = number1['real']
#     b = number1['imaginary']
#     c = number2['real']
#     d = number2['imaginary']

#     return {
#         'real': a + c,
#         'imaginary': b + d
#     }


# def subtract_complex_numbers(number1, number2):
#     a = number1['real']
#     b = number1['imaginary']
#     c = number2['real']
#     d = number2['imaginary']

#     return {
#         'real': a - c,
#         'imaginary': b - d
#     }


# def multiply_complex_numbers(number1, number2):
#     a = number1['real']
#     b = number1['imaginary']
#     c = number2['real']
#     d = number2['imaginary']

#     return {
#         'real': ((a * c) - (b * d)),
#         'imaginary': ((b * c) + (a * d))
#     }


# def divide_complex_numbers(number1, number2):
#     a = number1['real']
#     b = number1['imaginary']
#     c = number2['real']
#     d = number2['imaginary']

#     return {
#         'real': ((a * c) + (b * d)) / ((c ** 2) + (d ** 2)),
#         'imaginary': ((b * c) - (a * d)) / ((c ** 2) + (d ** 2))
#     }