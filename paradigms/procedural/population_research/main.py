from functions import read_data
from functions import calculate_average
from functions import determine_older_age
from functions import calculate_quantity
from functions import create_matrix


def main():
    n = int(input("\nDigite o numero de habitantes: "))

    sex = []
    eyes_color = []
    hair_color = []
    ages = []
    matrix = []

    print(f'\nDgite os dados de cada um dos {n} habitantes: ')
    read_data(n, sex, eyes_color, hair_color, ages)

    print("Media das idades dos habitantes de olhos castanhos e cabelos " +
          f'pretos = {calculate_average(n, eyes_color, hair_color, ages)}')

    print(
        f'\nMaior idade entre os habitantes = {determine_older_age(n, ages)}')

    print("\nMulheres, entre 18 e 35 anos, loiras e de olhos azuis = "
          + f'{calculate_quantity(n, sex, eyes_color, hair_color, ages)}')

    print("\n")
    create_matrix(n, ages, matrix)


main()
