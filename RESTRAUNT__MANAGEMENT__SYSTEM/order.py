class Order:
    def __init__(self) -> None:
        self.cart = {} # item : quantity

    def add_order(self, item, quantity):
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity

    def view_order(self):
        for item, quantity in self.cart.items():
            print(item.name, quantity)