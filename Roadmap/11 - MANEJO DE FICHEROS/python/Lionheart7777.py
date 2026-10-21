
 

"""Ejercicio
"""
"""
file_name = "Lionheart7777.txt"

with open(file_name,"w") as filx : # para escribir
    filx.write("Rick\n")
    filx.write("57\n")
    filx.write("Python")
    
with open(file_name,"r") as filx : # para leer
    print(filx.read())

os.remove(file_name)"""


"""
EXTRA
"""
import os
file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lionheart7777_shop.txt")

with open(file_name, "a"):
    pass

while True :
    print("1. Añadir Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Producto")
    print("4. Borrar Producto")
    print("5. Mostrar Producto")
    print("6. Calcular Venta Total")
    print("7. Calcular Venta Por Producto")
    print("8. Salir")
    
    option = input("Selecciona una opción :")
    
    if option == "1" :
        name = input ("Nombre : ")
        quantity = input ("Cantidad : ")
        price = input ("Precio : ")
        with open(file_name,"a") as filx: # para escribir
            filx.write(f"{name}, {quantity}, {price}\n")
            
    elif option == "2" :
        name = input("Nombre : ")
        with open(file_name, "r") as filx :
           for line in filx.readlines():
               if line.split(", ")[0] == name :
                   print(line)
                   break
                 
    elif option == "3" :
        name = input("Nombre :")
        quantity = input("Cantidad :")
        price = input("Precio :")
        with open(file_name,"r") as filx :
            lines = filx.readlines()
        with open(file_name,"w") as filx :
            for line in lines :
                if line.split(", ")[0] == name :
                    filx.write(f"{name}, {quantity}, {price}\n")
                else:
                    filx.write(line)
            
    elif option == "4" :
        name = input("Nombre :")
        with open(file_name,"r") as filx :
            lines = filx.readlines()
        with open(file_name,"w") as filx :
            for line in lines :
                if line.split(", ")[0] != name :
                    filx.write(line)
                    
    
    elif option == "5" :
        with open(file_name,"r") as filx :
            print(filx.read())
                
    elif option == "6" :
        total = 0
        with open(file_name,"r") as filx :  
            for line in filx.readlines():
                components =line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    
    elif option == "7" :
        name = input("Nombre :")
        subtotal = 0
        encontrado = False
        with open(file_name,"r") as filx :
            for line in filx.readlines():
                components =line.strip().split(", ")
                if components[0] == name :
                    quantity = int(components[1])
                    price = float(components[2])
                    subtotal += quantity * price
                    encontrado = True
                    break
        if encontrado:        
            print(subtotal)
        else:
            print("Producto no encontrado")       
                        
    elif option == "8" :
        os.remove(file_name)
        break
    
    else:
        print("Selecciona una de las opciones disponibles")