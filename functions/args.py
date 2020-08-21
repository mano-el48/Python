def sum(*numbers):
    total = 0
    for n in numbers:
        total += n

    return total


def result(**kwargs):
    status = 'aprovadx' if kwargs['nota'] >= 6 else 'reprovadx'
    return f'{kwargs["nome"]} foi {status}'
