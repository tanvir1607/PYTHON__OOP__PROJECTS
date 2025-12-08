class Menu:
    def __init__(self) -> None:
        self.items = [] # a list of item


    def add_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def delete_item(self, item_name):
        item = self.find_item(item_name)
        if item is not None:
            del item

    def view_menu(self):
        print("--------- MENU ---------")
        for item in self.items:
            print(item.name, item.price)
