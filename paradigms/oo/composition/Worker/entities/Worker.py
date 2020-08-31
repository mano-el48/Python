
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
