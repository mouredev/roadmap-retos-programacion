# 11 Files
import os

filename = "ggilperez.txt"

# If no path given, it uses __file__ path
with open(filename, "w") as file:
    file.write("Name: Guillermo\n")
    file.writelines("Age: 31\n")
    file.writelines("Favourite language: Python\n")

with open(filename, "r") as file:
    print(file.read())

os.remove(filename)
if not os.path.exists(filename):
    print("File removed successfully")


# Extra

def store_logistic():
    filename = "inventory.txt"

    # Create empty file
    open(filename, 'a').close()

    def show_menu():
        print("1. Insert product")
        print("2. Search product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Show products")
        print("6. Profit all products")
        print("7. Profit product")
        print("8. Exit")

    def insert_product():
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")

        row = f"{name}, {quantity}, {price}\n"

        with open(filename, "a") as file:
            file.write(row)

    def search_product():
        name_to_search = input("Name: ")

        with open(filename, "r") as file:
            for row in file:
                row = row.strip()  # Remove \n
                name, quantity, price = row.split(", ")
                if name == name_to_search:
                    print(f"Product: {name}")
                    print(f"Quantity: {quantity} ud")
                    print(f"Price: ${price}")
                    return

        print("Product not found")

    def update_product():
        name_to_search = input("Name: ")

        with open(filename, "r") as file:
            data = file.readlines()

        # Search
        found = False
        for i, row in enumerate(data):
            row = row.strip()  # Remove \n
            name, quantity, price = row.split(", ")
            if name == name_to_search:
                found = True
                new_quantity = input("New quantity: ")
                new_price = input("New price: ")

                row = f"{name}, {new_quantity}, {new_price}\n"

                data[i] = row
                break

        if not found:
            # Don't update file if product not found
            print("Product not found")
            return

        with open(filename, "w") as file:
            file.write("".join(data))

    def delete_product():
        name_to_search = input("Name: ")

        with open(filename, "r") as file:
            data = file.readlines()

        # Search
        found = False
        for i, row in enumerate(data):
            row = row.strip()  # Remove \n
            name, quantity, price = row.split(", ")
            if name == name_to_search:
                found = True
                data.pop(i)
                break

        if not found:
            # Don't update file if product not found
            print("Product not found")
            return

        with open(filename, "w") as file:
            file.write("".join(data))

    def show_products():
        with open(filename, "r") as file:
            print(file.read())

    def profit_all_products():
        total = 0
        with open(filename, "r") as file:
            for row in file:
                row = row.strip()
                name, quantity, price = row.split(", ")
                quantity = int(quantity)
                price = float(price)
                total += quantity * price
        print(total)

    def profit_product():
        name_to_search = input("Name: ")
        total = 0
        with open(filename, "r") as file:
            for row in file:
                row = row.strip()
                name, quantity, price = row.split(", ")
                if name == name_to_search:
                    quantity = int(quantity)
                    price = float(price)
                    total += quantity * price
                    break

        print(total)

    def exit_program():
        os.remove(filename)
        print("Ending program")

    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            insert_product()
        elif option == "2":
            search_product()
        elif option == "3":
            update_product()
        elif option == "4":
            delete_product()
        elif option == "5":
            show_products()
        elif option == "6":
            profit_all_products()
        elif option == "7":
            profit_product()
        elif option == "8":
            exit_program()
            return


store_logistic()
