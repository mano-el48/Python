from complex import Complex
from complex import sum_complex_numbers
from complex import subtract_complex_numbers
from complex import multiply_complex_numbers
from complex import divide_complex_numbers

a = float(input("\nDigite a parte real do Numero 1: "))
b = float(input("Digite a parte imaginaria do Numero 1: "))

c = float(input("\nDigite a parte real do Numero 2: "))
d = float(input("Digite a parte imaginaria do Numero 2: "))

number1 = Complex(a, b)
print(f'\nNumero 1 = {number1}')

number2 = Complex(c, d)
print(f'Numero 2 = {number2}')

result = sum_complex_numbers(number1, number2)
print(f'\nSoma = {result}')

result = subtract_complex_numbers(number1, number2)
print(f'Subtracao = {result}')

result = multiply_complex_numbers(number1, number2)
print(f'Multiplicacao = {result}')

result = divide_complex_numbers(number1, number2)
print(f'Divisao = {result}')
