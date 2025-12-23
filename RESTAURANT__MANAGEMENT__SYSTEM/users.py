from order import Order

class Customer():
    def __init__(self, name):
        self.name = name
        self.order = Order()
        self.bill = 0


class Admin():
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        self.username = name.lower() + "@july"
        self.password = name.lower() + phone[-3:]
        














