from collections import namedtuple

Complex = namedtuple("Complex", "real imaginary")


def parse_complex_number_to_string(number: Complex):
    return str(number.real) + " + " + str(number.imaginary) + "i"


number1 = Complex(1.0, 2.0)
# print(parse_complex_number_to_string(number1))
print(number1)

# from ctypes import Structure, c_float


# class Complex(Structure):
#     def __init__(self):
#         self.real = 0.0
#         self.imaginary = 0.0

#     _fields_ = [('real', c_float),
#                 ('imaginary', c_float)]

#     def __repr__(self):
#         real_part = str(self.real)
#         imaginary_part = str(self.imaginary)

#         return real_part + " + " + imaginary_part + "i"

#     def __str__(self):
#         return self.__repr__()
