class Shop:
    def __init__(self, storage):
        self.storage = storage

    def check_availability(self, item):
        if item in self.storage:
            return {item: self.storage[item]}
        else:
            return {}


class Client:
    def __init__(self, name):
        self.name = name
        self.order_list = {}
        self.total = 0

    def create_order(self, item, quantity, shop):
        available = shop.check_availability(item)
        if available:
            if item not in self.order_list:
                self.order_list[item] = quantity
            else:
                self.order_list[item] += quantity

            self.total += available[item] * quantity

    def print_order(self):
        order_list = f'{self.name}\n'
        for o, p in self.order_list.items():
            order_list += f'-- {o} - {p}\n'
        return order_list

    def get_bill(self):
        return self.total


def fill_storage():
    stock = {}
    count = int(input())
    for f in range(count):
        item, price = input().split('-')
        price = float(price)
        stock[item] = price
    return stock


andrey = Shop(fill_storage())
clients = {}

line = input()
while line != 'end of clients':
    client, order = line.split('-')
    client = Client(client)
    i, q = order.split(',')
    q = int(q)
    if andrey.check_availability(i):
        if client.name not in clients:
            client.create_order(i, q, andrey)
            clients[client.name]=client
        else:
            clients[client.name].create_order(i, q, andrey)
    line = input()

total = 0
for n, c in sorted(clients.items(), key=lambda x: x[0]):
    total += c.get_bill()
    print(f'{c.print_order()}Bill: {c.get_bill():.2f}')
print(f'Total bill: {total:.2f}')
