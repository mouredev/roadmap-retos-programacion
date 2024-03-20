#Solo la parte de dificultad extra
eleccion = 0
base = {}
datos = {"Nombre": "","Telefono": ""}

print(eleccion)
while eleccion != 5:
    eleccion = int(input( f"Indique que desa hace: \n1-buscar\n2-insertar\n3-actualizar\n4-eliminar\n5-salir\n" ))
    if eleccion == 1:
       
        name=input ("Indique el nombre que desea consultar:")
        
        print(base)
    elif eleccion == 2:
        
        datos["Nombre"] = input("Indique el nombre:")
        datos["Telefono"] = input("Indique el telefono:")
        nuevo = len(base)+1
        base =  {nuevo : datos}
    
    elif eleccion == 3:
        
        old=input("Indique el nombre que desa moficar:")
        new=input("Indique el nuevo nombre:")
        base.replace(old,new)

    elif eleccion == 4:
        borra = input("Indique el nombre que desa eliminar:")
        base.pop(borra)
    elif eleccion == 5:
        break
    else:
        print("Introduzca solo 1, 2, 3, 4 o 5 segun su eleccion")
        eleccion = input()

print("Gracias por usar nuestro software")
print(base)
