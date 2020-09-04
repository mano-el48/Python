import math


def read_data(n: int,
              sex: list,
              eyes_color: list,
              hair_color: list,
              ages: list):

    for i in range(n):
        print("Digite o sexo M(Masculino) ou F(Feminino): ")
        sex.append(input())

        print("\nDigite a cor dos olhos A(Azuis) ou C(Castanhos): ")
        eyes_color.append(input())

        print(
            "\nDigite a cor dos cabelos L(Loiros),P(Pretos) ou C(Castanhos): ")
        hair_color.append(input())

        print("\nDigite a idade: ")
        ages.append(int(input()))

        print("\n")


def calculate_average(n: int,
                      eyes_color: list,
                      hair_color: list,
                      ages: list) -> float:
    average = 0
    summation = 0
    peopleWithBrownEyesAndDarkHair = 0

    for i in range(n):
        if eyes_color[i] == 'C' and hair_color[i] == 'P':
            summation += ages[i]
            peopleWithBrownEyesAndDarkHair += 1

        if peopleWithBrownEyesAndDarkHair > 0:
            average = summation / peopleWithBrownEyesAndDarkHair
            average = math.trunc(average)

            return average

        else:
            return 0
