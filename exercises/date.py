from datetime import datetime


date = datetime(1998, 10, 9)
date = date.strftime('%d/%m/%Y')  # passando para string
print(date)

date_str = '09/10/1998'
date = datetime.strptime(date_str, '%d/%m/%Y')
print(date)
day = date.day
print(date.day)
print(date.month)
print(date.year)

date = date.strftime('%d/%m/%Y')  # passando para string
print(date)
