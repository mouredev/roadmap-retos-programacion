import os

#Exercise

file_name = "Irenetitor.txt"

with open(file_name, "w") as file:
    file.write("Irene Martin\n" + "I am 33 years old\n" + "My favourite language is Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)


#Extra Exercise
while True:
    print("1. Add product")
    print("2. View product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Show product")
    print("6. Calculate total sales")
    print("7. Calculate sales by product")
    print("8. Exit")

    option = input("Select an option: ")

    if option == "1":
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        with open(file_name, "a") as file:  # use "a" to append instead of overwriting
            file.write(f"{name}, {quantity}, {price}\n")
    elif option == "2":
        name = input("Name: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif option == "3":
        name = input("Name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        name = input("Name: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")[0]
                quantity = int(components[1])
                price = float(components[2])
    elif option == "7":
        pass
    elif option == "8":
        os.remove(file_name)
        print("Exiting program...")
        break  # ⬅️ only break here
    else:
        print("Select one of the available options")

