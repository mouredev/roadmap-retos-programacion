# Estructuras de control

##Listas

this_list=["cuadernos", "lapices", "borrador", "libros"]
print(this_list,type(this_list))

#insercion
this_list.append("tijeras")
print(this_list)

this_list.insert(1, "colores")
print(this_list)

other_list = ["bolso", "regla", "marcadores"]
this_list.extend(other_list)
print(this_list)

#borrado
this_list.remove("bolso")
print(this_list)

this_list.pop()
print(this_list)

this_list.pop(2)
print(this_list)

del this_list[0]
print(this_list)

#actualizacion
this_list.insert(1, "lonchera")
print(this_list)

this_list[2] = "goma"
print(this_list)

this_list[3:5] = ["lapices", "esferos"]
print(this_list)

#orden
this_list.sort()
print(this_list)

number_list = [1,5,7,9,4,2,7,9,4,2]
number_list.sort()
print(number_list)

this_list.sort(reverse=True)
number_list.sort(reverse=True)
print(this_list,number_list)
print("--------------------------------------------------------\n")

##Tuplas

partes_pc = ("CPU", "GPU", "memoria Ram", "Almacenamiento")
print(partes_pc)

#insercion
tupla_list = list(partes_pc)
tupla_list.append("SSD")
partes_pc = tuple(tupla_list)
print(partes_pc)

#actualizacion
tupla_list = list(partes_pc)
tupla_list[2] = "RAM"
partes_pc = tuple(tupla_list)
print(partes_pc)

#borrado
tupla_list = list(partes_pc)
tupla_list.pop()
partes_pc = tuple(tupla_list)
print(partes_pc)

#ordenamiento
tupla_list = list(partes_pc)
tupla_list.sort()
partes_pc = tuple(tupla_list)
print(partes_pc)
print("--------------------------------------------------------\n")

##Sets

fruits = {"Orange", "Banana", "Apple", "Strawberry"}

#insercion
fruits.add("Potato")
print(fruits)

#no se puede ordenar

#borrado
fruits.remove("Strawberry")
print(fruits)

fruits.pop()
print(fruits)
print("--------------------------------------------------------\n")

##Diccionarios
carro = {
    "color":"rojo",
    "modelo":"tesla",
    "año":"2025"
}

print(carro)

#insercion
carro["puertas"] = "4"
print(carro)

#actualizacion
carro.update({"color":"azul"})
print(carro)

#borrado
carro.pop("color")
print(carro)

carro.popitem()
print(carro)

#ordenacion
carro = dict(sorted(carro.items()))
print(carro)
print("--------------------------------------------------------\n")


# Extra
def agenda():
    print("Agenda de contactos")
    contactos = {}

    #agregar contacto
    def agregar_contacto():
        name = input("Ingrese el nombre del nuevo contacto: ")
        phone = input("Ingrese el telefono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            contactos[name] = phone
        else:
            print("Debes introducir un número de teléfono un máximo de 11 dígitos.")


    while True:
        print("""
            Operaciones
            ------------
            1. buscar
            2. agregar
            3. actualizar
            4. eliminar
            5. salir
        """)
        operacion = input("Que operacion desea realizar: ")

        match operacion:
            case "1":
                #buscar contacto
                name = input("ingrese el nombre del contacto: ")
                if name in contactos:
                    print(f"nombre: {name} - telefono: {contactos[name]}")
                else:
                    print("el contacto no exite")
            case "2":
                agregar_contacto()
            case "3":
                #actualizar contacto
                name = input("ingrese el nombre del contacto: ")
                if name in contactos:
                    agregar_contacto()
                else:
                    print("el contacto no exite")
            case "4":
                #eliminar contacto
                name = input("ingrese el nombre del contacto: ")
                if name in contactos:
                    contactos.pop(name)
                else:
                    print("el contacto no exite")
            case "5":
                print("adios")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

agenda()