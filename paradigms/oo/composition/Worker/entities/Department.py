class Department:
    def __init__(self, name):
        self.__name = name  # private

    @property
    def name(self):  # get
        return self.__name

    @name.setter  # set
    def name(self, name):
        self.__name = name


# d = Department("TI")
# print(d.name)

# d.name = "CCo"
# print(d.name)