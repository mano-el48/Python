from entities.Worker_Level import Worker_Level
from entities.Department import Department
from entities.Contract import Contract
from entities.Worker import Worker
from datetime import datetime

print("\nEntre com os dados do funcionario: ")
name = input("Nome: ")
departments_name = input("Departamento: ")
level = input("Nivel JUNIOR,  MID_LEVEL ou SENIOR : ")
base_salary = int(input("Salario Base: "))

worker = Worker(name,
                Worker_Level[level].value,
                base_salary,
                Department(departments_name))

n = int(input("\nQuantos contratos estao associados a este funcionario: "))

for i in range(n):
    print(f'\nDigite os dados do contrato {i+1}')

    date_str = input("Data no fomato(dd/MM/yyyy): ")
    contract_date = datetime.strptime(date_str, '%d/%m/%Y')

    value_per_hour = input("Valor por hora: ")

    hours = input("Quantidade de Horas trabalhadas: ")

    contract = Contract(contract_date, value_per_hour, hours)
    worker.add_contract(contract)

month_and_year = input(
    "\nDigite o mes e o ano para calcular a renda do funcionario (MM/yyyy): ")

month = int(month_and_year.split("/")[0])
year = int(month_and_year.split("/")[1])

print("\n") 
print(worker)

print(
    f'\nRenda do funcionario em {month}/{year} = R${worker.calculate_income(month, year, n):.2f}')

print(len(worker.contracts))
worker.remove_contract()
print(len(worker.contracts))