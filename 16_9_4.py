class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'{self.name} {self.surname}, {self.city}'
client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Олег", "Петров", "Казань", 150)
client_3 = Client("Ирина", "Иванова", "Тюмень", 250)

clients = [client_1, client_2, client_3]
for client in clients:
    if isinstance(client, Client):
        print(client.__str__())
    else:
        print('')
