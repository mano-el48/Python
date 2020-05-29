
def montanteJurosSimples(capitalInicial, taxaDeJuros, tempoDeAplicacao): 
    return format(
        (capitalInicial + (capitalInicial * (taxaDeJuros/100)* tempoDeAplicacao)),
        '.2f')


def montanteJurosCompostos(capitalInicial, taxaDeJuros, tempoDeAplicacao): 
    return format(
        (capitalInicial * ((1 + (taxaDeJuros/100))** tempoDeAplicacao)),
        '.2f')

#100, 10 e 2
capitalInicial = float (input ('Digite o valor do Capital Inicial: '))
taxaDeJuros = float (input ('Digite o valor da Taxa de Juros: '))
tempoDeAplicacao = float (input ('Digite a quantidade de Tempo de Aplicação: '))
print('Escolha o regime de juros: ')
regime = input('1 para Juros Simples e 2 para Juros Compostos: ')

if regime == '1':
    print('R$' + montanteJurosSimples(capitalInicial, taxaDeJuros, tempoDeAplicacao))
else:
    print('R$' + montanteJurosCompostos(capitalInicial, taxaDeJuros, tempoDeAplicacao))
