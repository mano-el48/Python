
def montanteJurosSimples(capitalInicial, taxaDEJuros, tempoDeAplicação): 
    return capitalInicial + (capitalInicial * (taxaDEJuros/100)* tempoDeAplicação)


def montanteJurosCompostos(capitalInicial, taxaDEJuros, tempoDeAplicação): 
    return capitalInicial * ((1 + (taxaDEJuros/100))** tempoDeAplicação)

