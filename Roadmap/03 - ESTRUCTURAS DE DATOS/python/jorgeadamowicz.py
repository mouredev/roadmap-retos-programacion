## Listas

my_full_pets_list = ["lara", "bruno", "vicente", "chiqui", "olivia","shelly", "emmy"]
print(my_full_pets_list)

## Insercióin: agregar un elemento a la lista (metodo Iserción append)
my_full_pets_list.append("isa")
my_new_pets_list= my_full_pets_list

#(metodo Inserción insert)
#my_full_pets_list.insert (1,"Isa")# insertará el nombre de mi nueva mascota en la posición "1"
print(my_new_pets_list)

## Borrado: borra elementos de la lista (metodo remove)
my_new_pets_list.remove ("lara")
my_new_pets_list.remove ("bruno")
my_new_pets_list.remove ("vicente")
my_new_pets_list.remove ("shelly")
#aquí se podría utilizar un bucle para iterar y eliminar todos los valores de una vez:
my_dead_pets_list = ("lara","bruno","vicente","shelly")
for element in my_dead_pets_list:
    if element in my_new_pets_list:
        my_new_pets_list.remove(element)
my_current_pets = my_new_pets_list
print(my_current_pets)

## Actualización: asignamos un nuevo valor a la posicion establecida
print(my_current_pets[2])
my_current_pets[2] = ("emma")
print(my_current_pets)

## Ordenamiento: permite ordenar los elementos
my_current_pets.sort()
print(my_current_pets)

### Tuplas ###

my_pesonal_data= ("jorge", "adamowicz", "51", "chorch")
print(my_pesonal_data)
print(type(my_pesonal_data))
"""
# Las tuplas son inmutables o que significa que no se pueden cambiar una vez creadas. 
Esto incluye la inserción, eliminación o modificación de los elementos dentro de una tupla.
"""
# Acceso: 
print(my_pesonal_data[2]) #imprime el dato correspondiente a la posición "2"
print(my_pesonal_data.count("jorge")) #contará cuntas veces apararece en dato del parametro
print(my_pesonal_data.index("chorch")) #indicará la posición del parametro asignado. 

### Sets ###

My_sports_set = {"motocross", "surf", "snowboard"}
print(My_sports_set)

# Inserción:

My_sports_set.add("mtb")
print(My_sports_set)

#Borrado: 

My_sports_set.remove("motocross")
print(My_sports_set)

### Diccionarios ###
My_personal_data_dict ={
    "nombre": "jorge",
    "apellido": "adamowicz",
    "edad": "51",
    "alias": "chorch"
    }
print(My_personal_data_dict)

#Inserción:
My_personal_data_dict ["deportes"] = "mtb", "motocross", "surf", "snowboard"
print(My_personal_data_dict)

#Borrado:
del My_personal_data_dict["alias"]
print(My_personal_data_dict)

#Actualización: 
My_personal_data_dict["nombre"]= "George"

print(My_personal_data_dict["nombre"]) # Acceso:

#### Extra ####

"""
la declaración "match" aun no la conocia pero siguiendo un poco el video pude entender su
implementación en este ejercicio... que me costó bastante resolver. voy a intentar hacerlo
utilizando en control de flujo de (if, elif, else), pero mas tarde, todavia me sale humo
de la cabeza! saludos y una vez mas gracias!
"""

def my_contact_list():
    telephone_book = {}

    while True:
        print("")
        print("1. Buscar un contacto")
        print("2. Insertar un contacto")
        print("3. Actualizar un contacto")
        print("4. Eliminar un contacto")
        print("5. salir de la agenda")

        option = input("\n selecciona una opción: ")

        match option:
            case "1":
                name = input("\n Ingresa el nombre de contacto: ")
                if name in telephone_book:
                    print(f"\n el numero de {name} es: {telephone_book[name]}.")
                else: 
                    print(f"\n el nombre {name} no está en la agenda")
                
            case "2":
                name = input("\n Ingresa el nombre de contacto: ")
                number = input("\n Ingresa el numero de telefono: ")
                if number.isdigit() and len(number) <=11 :# verifica si el numero es valido
                    telephone_book [name]= number #asigna el valor numero a la key nombre
                else:
                    print("ingresa un número telefónico válido")
            case "3":
                name = input("\n Ingresa el nombre de contacto que quieres actualizar: ")
                if name in telephone_book:
                    number = input("\n Ingresa el numero de telefono: ")
                    if number.isdigit() and len(number) <=11 :
                        telephone_book [name]= number
                    else:
                        print("ingresa un número telefónico válido")                
                else:
                    print(f"\n el nombre {name} no está en la agenda")

            case "4":
                name = input("\n Ingresa el nombre de contacto que quieres eliminar: ")
                if name in telephone_book:
                    del telephone_book[name]
                else:
                    print(f"\n el nombre {name} no está en la agenda")
            case "5":
                print("has salido de la agenda")
                break
            case _:
                print("Escribe una opción válida entre 1 y 5")
 
my_contact_list()