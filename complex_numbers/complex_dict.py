def createComplexNumber(a: float, b: float):
    return {
        'real': a,
        'imaginary': b
    }

def parseComplexNumberToString(number) {
    return number.real.toFixed(2) + " + " + number.imaginary.toFixed(2) + "i"
}

def sumComplexNumbers(number1, number2) {
    a = number1.real, b = number1.imaginary
    c = number2.real, d = number2.imaginary

    return {
        real: a + c,
        imaginary: b + d
    }
}

def subtractComplexNumbers(number1, number2) {
    let a = number1.real, b = number1.imaginary
    let c = number2.real, d = number2.imaginary

    return {
        real: a - c,
        imaginary: b - d
    }
}

def multiplyComplexNumbers(number1, number2) {
    let a = number1.real, b = number1.imaginary
    let c = number2.real, d = number2.imaginary

    return {
        real: ((a * c) - (b * d)),
        imaginary: ((b * c) + (a * d))
    }
}

def divideComplexNumbers(number1, number2) {
    let a = number1.real, b = number1.imaginary
    let c = number2.real, d = number2.imaginary

    return {
        real: ((a * c) + (b * d)) / ((c ** 2) + (d ** 2)),
        imaginary: ((b * c) - (a * d)) / ((c ** 2) + (d ** 2))
    }
}
