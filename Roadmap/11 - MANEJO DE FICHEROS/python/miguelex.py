import os 

def create_file(file_name: str) -> None:
    with open(file_name, "w") as file:
        print(f"Fichero {file_name} creado")

def add_data(file_name: str, name: str, age: str, language: str) -> None:
    with open(file_name, "a") as file:
        file.write(f"{name}, {age}, {language}\n")
        print(f"Datos guardados en el fichero {file_name}") 
         
        
def read_data(file_name: str) -> None:
    with open(file_name, "r") as file:
        for line in file.readlines():
            print(line)  
            
def erase_file (file_name: str) -> None:
    os.remove(file_name)
    print(f"Fichero {file_name} eliminado")
    
create_file("miguelex.txt")
add_data("miguelex.txt", "Miguelex", "48", "Python")
read_data("miguelex.txt")
erase_file("miguelex.txt")


# Extra 

file_name = "ventas.txt"

open(file_name, "a")

while True: 
    print("Menu")
    print("1. Añadir venta")
    print("2. Consultar ventas de un producto")
    print("3. Consultar ventas totales")
    print("4. Eliminar producto")
    print("5. Calcular ventas totales")
    print("6. Calcular ventas de un producto")
    print("7. Salir")
    
    option = input("Selecciona una opción: ")
    
    match option:
        case "1":
            product = input("Nombre del producto: ")
            units = input("Unidades vendidas: ")
            price = input("Precio unitario: ")
            
            with open(file_name, "a") as file:
                file.write(f"{product}, {units}, {price}\n")
        case "2":
            product = input("Nombre del producto: ")
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == product:
                        print(line)
        case "3":
            with open(file_name, "r") as file:
                for line in file.readlines():
                    print(line)
        case "4":
            product = input("Nombre del producto: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != product:
                        file.write(line)
        case "5":
            with open(file_name, "r") as file:
                total = 0
                for line in file.readlines():
                    total += int(line.split(", ")[1]) * float(line.split(", ")[2])
                print(f"El total de ventas es {total}")
        case "6":
            product = input("Nombre del producto: ")
            with open(file_name, "r") as file:
                total = 0
                for line in file.readlines():
                    if line.split(", ")[0] == product:
                        total += int(line.split(", ")[1]) * float(line.split(", ")[2])
                print(f"El total de ventas de {product} es {total}")
        case "7":
            os.remove(file_name) 
            break
            
    
    