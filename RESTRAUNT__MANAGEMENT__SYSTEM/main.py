from users import Customer, Admin
from restaurant import Restaurant
from menu import Menu
from item import Item
from order import Order

# Create a Menu
menu = Menu()
menu.add_item(Item("Water", 20))
menu.add_item(Item("Borhani", 40))
menu.add_item(Item("Jali Kabab", 30))
menu.add_item(Item("Tehari", 120))
menu.add_item(Item("Beef Khichuri", 120))
menu.add_item(Item("Bashmati Kacchi", 180))
menu.add_item(Item("Chinigura Kacchi", 180))


# Create Restaurant
rest = Restaurant("July Cafe", menu)



def main_menu():
    print(f"Welcome to {rest.name}")
    print("-"*50)
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    print("-"*50)


def customer_menu():
    print("1. Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Paybill")
    print("5. ")
    print("6. ")
    print("7. ")

main_menu()