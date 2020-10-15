# from dataclasses import dataclass
# @dataclass

class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        real_part = str(self.real)
        imaginary_part = str(self.imaginary)

        return real_part + " + " + imaginary_part + "i"

    def __str__(self):
        return self.__repr__()


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