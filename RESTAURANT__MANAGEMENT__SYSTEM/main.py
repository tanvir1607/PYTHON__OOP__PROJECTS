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
    while True:
        print(f"Welcome to {rest.name}")
        print("-"*50)
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        print("-"*50)

        choice = int(input("Choice : "))
        print("-"*50)

        if choice == 1: customer_menu()
        elif choice == 2: pass
        elif choice == 3: break


def customer_menu():
    name = input("Name : ")
    customer = Customer(name)
    print("-"*50)
    print(f"hello, {name.upper()}")
    print("-"*50)
    
    while True:
        print("1. Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. View Orders")
        print("5. Bill")
        print("6. Pay")
        print("7. Back")
        print("8. Exit")
        print("-"*50)

        choice = int(input("Choice : "))
        print("-"*50)
        if choice == 1: 
            rest.menu.view_menu()
        
        elif choice == 2:
            while True:
                item_name = input("Item Name : ")
                quantity = int(input("Quantity : "))
                item = menu.find_item(item_name)
                if item: 
                    break
            customer.order.add_order(item, quantity)

        elif choice == 3:
            pass
        
        elif choice == 4: 
            customer.order.view_order()
        
        elif choice == 5:
            pass
        
        elif choice == 6:
            pass
        
        elif choice == 7:
            pass


main_menu()