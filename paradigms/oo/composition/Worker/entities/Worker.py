class Worker:
    def __init__(self,
                 name,
                 level,
                 base_salary,
                 department):
        self.__contracts = []
        self.__name = name
        self.__level = level
        self.__base_salary = base_salary
        self.__department = department

    @property
    def name(self):  # get
        return self.__name

    @name.setter  # set
    def name(self, name):
        self.__name = name

    @property
    def level(self):  # get
        return self.__level

    @level.setter  # set
    def level(self, level):
        self.__level = level

    @property
    def base_salary(self):  # get
        return self.__base_salary

    @base_salary.setter  # set
    def base_salary(self, base_salary):
        self.__base_salary = base_salary

    @property
    def department(self):  # get
        return self.__department

    @department.setter  # set
    def department(self, department):
        self.__department = department

    @property
    def contracts(self):  # get
        return self.__contracts

    def add_contract(self, contract):
        self.__contracts.append(contract)

    def remove_contract(self):
        self.__contracts.pop()

    def calculate_income(self, month, year, n) -> float:
        sum = self.__base_salary

        for i in range(n):
            if month == self.__contracts[i].date.month and year == self.__contracts[i].date.year:
                sum += self.__contracts[i].total_value()

        return sum

    def __repr__(self):
        worker_string = ""
        head = "Dados do Funcionario:" + "\n"
        name = f'Nome: {self.__name}' + "\n"
        level = f'Nivel: {self.__level}' + "\n"
        base_salary = f'Salario base: {self.__base_salary}' + "\n"
        department = f'Departamento: {self.__department.name}'
        worker_string = head + name + level + base_salary + department
        return worker_string

    def __str__(self):
        return self.__repr__()