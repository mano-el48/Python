from entities.Worker_Level import Worker_Level
from entities.Department import Department
from entities.Contract import Contract
from entities.Worker import Worker

print("\nEntre com os dados do funcionario: ")
name = input("Nome: ")
departments_name = input("Departamento: ")
level = input("Nivel JUNIOR,  MID_LEVEL ou SENIOR : ")
base_salary = input("Salario Base: ")

worker = Worker(name,
                Worker_Level[level].value,
                base_salary,
                Department(departments_name))

# print("\n")
# print(worker)
n = int(input("\nQuantos contratos estao associados a este funcionario: "))

for n in range(n):
    print(f'\nDigite os dados do contrato {n+1}')
