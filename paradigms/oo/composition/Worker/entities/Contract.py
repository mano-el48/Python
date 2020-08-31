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


# c1 = Contract("09/10/1998", 15, 5)
# print(c1.date, c1.value_per_hour, c1.hours, c1.total_value())

# c2 = Contract("09/10/1998", 20, 5)
# print(c2.date, c2.value_per_hour, c2.hours, c2.total_value())
