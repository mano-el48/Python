from datetime import datetime


date = datetime(1998, 10, 9)
date = date.strftime('%d/%m/%Y')  # passando para string
print(date)

date = datetime.strptime('09/10/1998', '%d/%m/%Y')
print(date)
print(date.day)
print(date.month)
print(date.year)
