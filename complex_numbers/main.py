from dataclasses import dataclass

# Simulando uma Struct
@dataclass
class Complex:
    real: float
    imaginary: float

    def __repr__(self):
        real_part = str(self.real)
        imaginary_part = str(self.imaginary)

        return real_part + " + " + imaginary_part + "i"

    def __str__(self):
        return self.__repr__()


c = Complex(1.0, 2.0)
print(c)
