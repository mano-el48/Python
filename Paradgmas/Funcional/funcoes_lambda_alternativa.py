
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)


def calcularPrecoTotal(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(map(calcularPrecoTotal, compras))

print('Preços totais:', totais)
print('Total geral:', sum(totais))
