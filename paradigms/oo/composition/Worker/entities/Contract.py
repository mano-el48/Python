class Contract:
    def __init__(self,
                 date,
                 value_per_hour,
                 hours):
        self.__date = date
        self.__value_per_hour = value_per_hour
        self.__hours = hours

    @property
    def date(self):  # get
        return self.__date

    @date.setter  # set
    def date(self, date):
        self.__date = date

    @property
    def value_per_hour(self):  # get
        return self.__value_per_hour

    @value_per_hour.setter  # set
    def value_per_hour(self, value_per_hour):
        self.__value_per_hour = value_per_hour

    @property
    def hours(self):  # get
        return self.__hours

    @hours.setter  # set
    def hours(self, hours):
        self.__hours = hours

    def total_value(self):
        return int(self.__value_per_hour) * int(self.__hours)

    def __repr__(self):
        contract = ""
        date = "\n" + f'Data: {self.__date}' + "\n"
        value_per_hour = f'Valor Por Hora: R${self.__value_per_hour:.2f}' + "\n"
        hours = f'Quantidade de horas trabalhadas: {self.__hours:.2f} h' + "\n"
        contract = date + value_per_hour + hours
        return contract

    def __str__(self):
        return self.__repr__()


# c1 = Contract("09/10/1998", 15, 5)
# c2 = Contract("09/10/1998", 20, 5)
# contracts = []
# contracts.append(c1)
# contracts.append(c2)
# print(contracts)
