from functions import read_data
from functions import calculate_average


def main():
    n = int(input("\nDigite o numero de habitantes: "))

    sex = []
    eyes_color = []
    hair_color = []
    ages = []

    print(f'\nDgite os dados de cada um dos {n} habitantes: ')
    read_data(n, sex, eyes_color, hair_color, ages)

    print(
        f'Media das idades dos habitantes de olhos castanhos e cabelos pretos = {calculate_average(n, eyes_color, hair_color, ages)}')
    print("\n")


main()
