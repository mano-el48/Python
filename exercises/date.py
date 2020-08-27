from datetime import datetime


def parse_date(date: str):
    day = int(date.split('/')[0])
    month = int(date.split('/')[1])
    year = int(date.split('/')[2])

    # return  date.strftime('%d/%m/%Y') #passando para string
    return datetime(year, month, day)


date = "09/10/1998"
date = parse_date(date)
print(date)
print(date.day)
print(date.month)
print(date.year)
