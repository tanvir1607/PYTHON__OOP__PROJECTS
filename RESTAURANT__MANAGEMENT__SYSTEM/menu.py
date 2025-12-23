class Menu:
    def __init__(self) -> None:
        self.items = [] # a list of item objects

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower(): return item
        return None
    
    def delete_item(self, item_name):
        item = self.find_item(item_name)
        if item: del item

    def view_menu(self):
        print("-" * 43)
        print(f"| {'No':<3} | {'Item':<20} | {'Price':>10} |")
        print("-" * 43)
        for i, item in enumerate(self.items):
            print(f"| {i:<3} | {item.name:<20} | {item.price:>7} Tk.|")
        print("-" * 43)

