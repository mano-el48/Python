class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = []

    def add_addres(self, city, state):
        self.address.append(Addres(city, state))

    def address_list(self):
        for addres in self.address:
            print(addres.city, addres.state)

    def __del__(self):
        print(f'{self.name} FOI DELETADO')


class Addres:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city}/{self.state} FOI DELETADO')

client1 = Client('Rogério', 32)
client1.add_addres("Belo Horizonte", "MG")
print(client1.name, client1.age)
client1.address_list()
del client1
print()

client2 = Client('Maria', 55)
client2.add_addres("Salvador", "BA")
client2.add_addres("Rio de Janeiro", "RJ")
print(client2.name, client2.age)
client2.address_list()
del client2
print()

client3 = Client('Jorge', 32)
client3.add_addres("São Paulo", "SP")
print(client3.name, client3.age)
client3.address_list()
del client3
print()
