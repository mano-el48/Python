from complex import Complex
from complex import parse_complex_number_to_string
from complex import sum_complex_numbers
from complex import subtract_complex_numbers
from complex import multiply_complex_numbers
from complex import divide_complex_numbers

a = float(input("\nDigite a parte real do Numero 1: "))
b = float(input("Digite a parte imaginaria do Numero 1: "))

c = float(input("\nDigite a parte real do Numero 2: "))
d = float(input("Digite a parte imaginaria do Numero 2: "))

number1 = Complex(a, b)
print(f'\nNumero 1 = {parse_complex_number_to_string(number1)}')

number2 = Complex(c, d)
print(f'Numero 2 = {parse_complex_number_to_string(number2)}')

result = sum_complex_numbers(number1, number2)
print(f'\nSoma = {parse_complex_number_to_string(result)}')

result = subtract_complex_numbers(number1, number2)
print(f'Subtracao = {parse_complex_number_to_string(result)}')

result = multiply_complex_numbers(number1, number2)
print(f'Multiplicacao = {parse_complex_number_to_string(result)}')

result = divide_complex_numbers(number1, number2)
print(f'Divisao = {parse_complex_number_to_string(result)}')
