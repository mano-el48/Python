
def montanteJurosSimples(capitalInicial, taxaDEJuros, tempoDeAplicacao): 
    return format(
        (capitalInicial + (capitalInicial * (taxaDEJuros/100)* tempoDeAplicacao)),
        '.2f')


def montanteJurosCompostos(capitalInicial, taxaDEJuros, tempoDeAplicacao): 
    return format(
        (capitalInicial * ((1 + (taxaDEJuros/100))** tempoDeAplicacao)),
        '.2f')

#100, 10 e 2
capitalInicial = float (input ('Digite o valor do Capital Inicial: '))
taxaDEJuros = float (input ('Digite o valor da taxa de juros: '))
tempoDeAplicacao = float (input ('Digite a quantidade de tempo de aplicação: '))
print('Digite o regime de juros: ')
regime = input('1 para Juros Simples e 2 para Juros Compostos ')

if regime == 1:
    print(montanteJurosSimples("Montante Juros Simples = R$" +capitalInicial, taxaDEJuros, tempoDeAplicacao))
else:
    print(montanteJurosCompostos("Montante Juros Compostos = R$" +capitalInicial, taxaDEJuros, tempoDeAplicacao))