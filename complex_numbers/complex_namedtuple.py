from collections import namedtuple

Complex = namedtuple("Complex", "real imaginary")


def parse_complex_number_to_string(number: Complex):
    return str(number.real) + " + " + str(number.imaginary) + "i"


number1 = Complex(1.0, 2.0)
# print(parse_complex_number_to_string(number1))
print(number1)
