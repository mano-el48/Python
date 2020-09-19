from ctypes import Structure, c_float


class Complex(Structure):
    def __init__(self):
        self.real = 0.0
        self.imaginary = 0.0

    _fields_ = [('real', c_float),
                ('imaginary', c_float)]

    def __repr__(self):
        real_part = str(self.real)
        imaginary_part = str(self.imaginary)

        return real_part + " + " + imaginary_part + "i"

    def __str__(self):
        return self.__repr__()


def create_complex_number(a, b):
    number = Complex()
    number.real = a
    number.imaginary = b

    return number


print(create_complex_number(1.0, 2.0))

# number1 = Complex()
# number1.real = 1.00
# number1.imaginary = 2.00

# print(number1)

# number2 = Complex()
# print(number2)
