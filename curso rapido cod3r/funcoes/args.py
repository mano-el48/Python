
def soma(*nuns):
    total = 0
    for n in nuns:
        total += n

    return total


def resultado_final(**kwargs):
    status = 'aprovadx' if kwargs['nota'] >= 6 else 'reprovadx'
    return f'{kwargs["nome"]} foi {status}'
