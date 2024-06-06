#11 - FICHERO

import os

file_name = 'sperezsa.txt'

with open(file_name, 'w') as f:
    f.write('Sergio\n')
    f.write('44\n')
    f.write('Python\n')
    
with open(file_name, 'r') as f: 
    lineas = f.read()
    print(lineas)  

os.remove(file_name)


"""
Extra
"""

file_name = 'ventas.txt'

while True:
    sel = input("Opciones: \n" \
                "1. Añadir venta \n" \
                "2. Consultar venta \n" \
                "3. Actualizar venta \n" \
                "4. Borrar venta \n" \
                "5. Mostrar ventas \n" \
                "6. Cálculo venta total \n" \
                "7. Cálculo venta por producto \n" \
                "8. Salir \n" \
                "-> Opción: ")
    
    if sel == '1':
        prod = input("Producto: ")
        cant = input("Cantidad: ")
        prec = input("Precio: ")
        with open(file_name, 'a') as f:
            f.write(f"{prod}, {cant}, {prec}\n")
    elif sel == '2':
        prod = input("Producto: ")      
        with open(file_name, 'r') as f:
            for line in f.readlines():
                if line.split(", ")[0] == prod:
                    print(line)
                    break
    elif sel == '3':
        prod = input("Producto: ")
        cant = input("Cantidad: ")
        prec = input("Precio: ")   
        with open(file_name, 'r') as f:
            lines = f.readlines()
        with open(file_name, 'w') as f:
            for line in lines:
                if line.split(", ")[0] == prod:
                    f.write(f"{prod}, {cant}, {prec}\n")
                else:
                    f.write(line)
    elif sel == '4': 
        prod = input("Producto: ")      
        with open(file_name, 'r') as f: 
            lines = f.readlines()
        with open(file_name, 'w') as f:
           for line in lines:
               if line.split(", ")[0] == prod:
                   f.write("")
               else:
                   f.write(line)
    elif sel == '5': 
        with open(file_name, 'r') as f: 
            print(f.read())
    elif sel == '6': 
        v_total = 0
        with open(file_name, 'r') as f: 
            lines = f.readlines()
            for line in lines:
                v_total += int(line.split(", ")[1]) * int(line.split(", ")[2])
        print(f"Ventas totales: {v_total}")        
    elif sel == '7': 
        v_producto = {}
        with open(file_name, 'r') as f: 
            lines = f.readlines()
            for line in lines:
                print()
                if line.split(", ")[0] in v_producto.keys(): 
                    v_producto[line.split(", ")[0]] += int(line.split(", ")[1]) * int(line.split(", ")[2])
                else:
                    v_producto[line.split(", ")[0]] = int(line.split(", ")[1]) * int(line.split(", ")[2])
        print(f"Ventas por producto: {v_producto}")   
    elif sel == '8': 
        print("Salir!")
        os.remove(file_name)
        break
    else: 
        print("Opción no válida. Selecciona otra opción.")
        
        
        
