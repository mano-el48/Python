def get_day(day):
    days = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return days.get(day, '** Inválido **')

for day in range(1, 9):
    print(f'{day}: {get_day(day)}')
