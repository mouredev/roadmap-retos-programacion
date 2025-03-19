import os

nombre_archivo = "NeosV.txt"

with open(nombre_archivo, "w") as file:
     file.write("Andres\n")
     file.write("22\n")
     file.write("Python\n")
     
     
with open(nombre_archivo, "r") as file:
     print(file.read())


os.remove(nombre_archivo)     

nombre_tienda = "Negocio.txt"

open(nombre_tienda, "a")
while True:
          
          
          print("1. Añadir Producto")
          print("2. Consultar Producto")
          print("3. Actualizar Producto")
          print("4. Borrar Producto")
          print("5. Calcular Venta Total")
          print("6. Calcular Venta por Producto")
          print("7. Mostrar Productos")
          print("8. Salir")
          
          
          accion = input("Por favor ingrese la accion que desea realizar: ")


          if accion == "1":
              
              nombre = input("Ingresa el Nombre del producto: ")
              cantidad = input("Ingresa la cantidad del producto: ")
              precio = input("Ingresa el precio unitario: ")

              with open(nombre_tienda, "a") as file:
                   file.write(f"{nombre}, {cantidad}, {precio}\n")
               
          elif accion == "2":
                             
              nombre = input("Ingresa el Nombre del producto: ")
              with open(nombre_tienda, "r") as file:
                   for line in file.readlines():
                        if line.split(", ")[0] == nombre:
                             print(line)
                             break
                           
          elif accion == "3":
              nombre = input("Ingresa el Nombre del producto: ")
              cantidad = input("Ingresa la cantidad del producto: ")
              precio = input("Ingresa el precio unitario: ")

              with open(nombre_tienda, "r") as file:
                   lineas = file.readlines()
              with open(nombre_tienda, "w") as file:
                   for line in lineas:
                    if line.split(", ")[0] == nombre:
                       file.write(f"{nombre}, {cantidad}, {precio}\n")
                    else:
                         file.write(line)      
          elif accion == "4":
              nombre = input("Ingresa el Nombre del producto: ")
              

              with open(nombre_tienda, "r") as file:
                   lineas = file.readlines()
              with open(nombre_tienda, "w") as file:
                   for line in lineas:
                    if line.split(", ")[0] != nombre:
                       file.write(file)
          elif accion == "5":
               total = 0
               with open(nombre_tienda, "r") as file:
                  for line in file.readlines():
                      componentes = line.split(", ")
                      cantidad = int(componentes[1])
                      precio = float(componentes [2])
                      total += cantidad * precio
               print(total)              
          elif accion == "6":
                 nombre = input("Ingresa el Nombre del producto: ")
                 total = 0
                 with open(nombre_tienda, "r") as file:
                   for line in file.readlines():
                      componentes = line.split(", ")
                      if componentes[0] == nombre:
                       cantidad = int(componentes[1])
                       precio = float(componentes [2])
                       total += cantidad * precio
                       break
                 print(total)  

          elif accion == "7":
               with open(nombre_tienda, "r") as file:
                   print(file.read())
               
          elif accion == "8":
            
               os.remove(nombre_tienda)          
               break  
          else:
               print("Selecciona una de las opciones disponibles")     
               

                


