import math


def read_data(n, gender, eyes_color, hair_color, ages):

    for i in range(n):
        print("Digite o genero M(Masculino), F(Feminino) ou Outro: ")
        gender.append(input())

        print("\nDigite a cor dos olhos A(Azuis) ou C(Castanhos): ")
        eyes_color.append(input())

        print(
            "\nDigite a cor dos cabelos L(Loiros),P(Pretos) ou C(Castanhos): ")
        hair_color.append(input())

        print("\nDigite a idade: ")
        ages.append(int(input()))

        print("\n")


def calculate_average(n, eyes_color, hair_color, ages):
    average = 0
    summation = 0
    peopleWithBrownEyesAndDarkHair = 0

    for i in range(n):
        if eyes_color[i] == 'C' and hair_color[i] == 'P':
            summation += ages[i]
            peopleWithBrownEyesAndDarkHair += 1

    if peopleWithBrownEyesAndDarkHair > 0:
        average = summation / peopleWithBrownEyesAndDarkHair
        return math.trunc(average)
    else:
        return 0


def determine_older_age(n, ages):
    older_age = ages[0]

    for i in range(n):
        if ages[i] > older_age:
            olderAge = ages[i]

    return olderAge


def calculate_quantity(n, gender, eyes_color, hair_color, ages):

    blondWomenBetween18And35WithBlueEyes = 0

    for i in range(n):
        if gender[i] == 'F' and ages[i] >= 18 and ages[i] <= 35 and eyes_color[i] == 'A' and hair_color[i] == 'L':
            blondWomenBetween18And35WithBlueEyes += 1

    return blondWomenBetween18And35WithBlueEyes


def create_matrix(n, ages, matrix):
    for i in range(n):
        # cria as linhas
        line = []  # lista vazia

        for j in range(n):
            if i == j:
                line.append(ages[i])
            else:
                line.append(0)

        # coloque linha na matriz
        matrix.append(line)

    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j]}  ', end='')
        print()
