"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# Loop infinito
while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    new_cpf = cpf[:-2]  # Elimina os dois últimos digitos do CPF
    revers = 10  # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:   # Primeiro índice vai de 0 a 9,
            index -= 9  # São os 9 primeiros digitos do CPF

        total += int(new_cpf[index]) * revers  # Valor total da multiplicação

        revers -= 1  # Decrementa o contador reverso
        if revers < 2:
            revers = 11
            digit = 11 - (total % 11)

            if digit > 9:
                digit = 0
            total = 0
            new_cpf += str(digit)  # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequency = new_cpf == str(new_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == new_cpf and not sequency:
        print('Válido')
    else:
        print('Inválido')
