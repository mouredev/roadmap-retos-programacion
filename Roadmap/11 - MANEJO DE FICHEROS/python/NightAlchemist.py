import os

# 1. Crear el archivo con el nombre de usuario de GitHub y la extensión .txt
filename = "NightAlchemist.txt"

# 2. Añadir varias líneas al archivo
content = [
    "Name = Jhoao\n",
    "Age = 37\n",
    "Favorite programming languague = Python\n"
]

# Crear y escribir en el archivo
with open(filename, 'w') as file:
    file.writelines(content)

# 3. Imprimir el contenido del archivo
with open(filename, 'r') as file:
    file_content = file.read()

print(file_content)

# 4. Borrar el archivo
os.remove(filename)  # Eliminar el archivo

# Confirmación de eliminación
file_exists = os.path.exists(filename)
print("The file has been deleted:", not file_exists, "\n")

'''
Extra
'''

filename = "products.txt"

# Instructions for the user
def sales():
    
    while True:
        
        print(
            "What do you want to do?\n\n"
            "1. Add a new product\n"
            "2. Show a product\n"
            "3. Update a product\n"
            "4. Delete a product\n"
            "5. Show all the products\n"
            "6. Calculate total sales\n"
            "7. Calculate sales by product\n"
            "8. Exit\n"
        )

        option = input(str("Pick a number from the options: "))
        
        if option == "1":
            # Option 1: Add a new product
            name = input("Enter the product name: ")
            quantity = input("Enter the quantity sold: ")
            price = input("Enter the price of the product: ")

            try:
                quantity = int(quantity)
                price = float(price)
                
                with open(filename, 'a') as file:
                    file.write(f"{name}, {quantity}, {price}\n")
                print(f"Product '{name}' added successfully!")
            except ValueError:
                print("Invalid input. Please enter valid numbers for quantity and price.")

        elif option == "2":
            # Option 2: Show a product
            search_name = input("Enter the product name to search for: ")
            found = False
            
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.lower().startswith(search_name.lower()):
                            print(line.strip())  # Show the product info
                            found = True
                            break
                if not found:
                    print("Product not found.")
            else:
                print("No information in the file.")

        elif option == "3":
            # Option 3: Update a product
            search_name = input("Enter the product name to update: ")
            found = False
            products = []
            
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        products.append(line.strip())
                
                for i, line in enumerate(products):
                    if line.lower().startswith(search_name.lower()):
                        print(f"Current product info: {line}")
                        new_name = input("Enter new product name (or press Enter to keep current): ")
                        new_quantity = input("Enter new quantity (or press Enter to keep current): ")
                        new_price = input("Enter new price (or press Enter to keep current): ")
                        
                        # Update values if provided, else keep current values
                        if new_name:
                            name = new_name
                        else:
                            name = line.split(",")[0].strip()
                        
                        if new_quantity:
                            quantity = int(new_quantity)
                        else:
                            quantity = int(line.split(",")[1].strip())
                        
                        if new_price:
                            price = float(new_price)
                        else:
                            price = float(line.split(",")[2].strip())
                        
                        # Update the product entry in the list
                        products[i] = f"{name}, {quantity}, {price}"
                        found = True
                        break
                
                if found:
                    with open(filename, 'w') as file:
                        file.write("\n".join(products) + "\n")
                    print(f"Product '{search_name}' updated successfully!")
                else:
                    print("Product not found.")
            else:
                print("No information in the file.")

        elif option == "4":
            # Option 4: Delete a product
            search_name = input("Enter the product name to delete: ")
            found = False
            products = []
            
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        products.append(line.strip())
                
                for i, line in enumerate(products):
                    if line.lower().startswith(search_name.lower()):
                        print(f"Product '{line}' will be deleted.")
                        del products[i]
                        found = True
                        break
                
                if found:
                    with open(filename, 'w') as file:
                        file.write("\n".join(products) + "\n")
                    print(f"Product '{search_name}' deleted successfully!")
                else:
                    print("Product not found.")
            else:
                print("No information in the file.")

        elif option == "5":
            # Option 5: Show all the products
            if os.path.exists(filename):
                try:
                    with open(filename, 'r') as file:
                        content = file.read()
                        if content:
                            print(content)
                        else:
                            print("The file is empty.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("No information in the file.")

        elif option == "6":
            # Option 6: Calculate total sales
            total_sales = 0
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        data = line.strip().split(", ")
                        if len(data) == 3:
                            quantity = int(data[1])
                            price = float(data[2])
                            total_sales += quantity * price
                print(f"Total sales: {total_sales}")
            else:
                print("No information in the file.")

        elif option == "7":
            # Option 7: Calculate sales by product
            product_name = input("Enter the product name to calculate sales: ")
            sales_by_product = 0
            found = False
            
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        data = line.strip().split(", ")
                        if len(data) == 3 and data[0].lower() == product_name.lower():
                            quantity = int(data[1])
                            price = float(data[2])
                            sales_by_product = quantity * price
                            found = True
                            break
                if found:
                    print(f"Total sales for '{product_name}': {sales_by_product}")
                else:
                    print(f"Product '{product_name}' not found.")
            else:
                print("No information in the file.")

        elif option == "8":
            if os.path.exists(filename):
                os.remove(filename)  # Delete the file if it exists
                print("File deleted successfully.")
            return False
        else:
            print("Please select one option")

sales()
