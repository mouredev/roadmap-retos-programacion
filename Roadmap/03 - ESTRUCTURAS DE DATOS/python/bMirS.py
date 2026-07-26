"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

"""
#LISTAS
my_list=["Maria", "Camila", "Jorge", "Ivan", 5]
#AGREGAR ELEMETOS 
my_list.append(35) #Inserción
print(my_list)
my_list.remove("Maria") #Eliminar
print(my_list)
print(my_list[-1])
print(my_list[-5])
my_list[-5]="Sofia"#Actualizacion

#TUPLAS 
#NO se puede insertar, modificar, borrar
my_tuple=("Anastacia", "Blanca Nieves", "Aurora")
print(type(my_tuple))

#SETS
#No estan ordenados, no se pueden repetir datos
my_set={"Esperanza", "Amaranta", "35"}
print(type(my_set))
my_set.add("Tortillas")
my_set.remove("35")

#DICCIONARIOS
my_dict=dict()
my_dict={ 
    "Nombre":"Sofia",
    "Apellido": "Camaron",
    "Edad": "34"
    }


#inserción
my_dict["email"]="sfcamaron@gmail.com"
print(my_dict)
#Actualización
my_dict["Edad"]="45"
print(my_dict)
#Eliminación
del my_dict["email"]


""""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */"""

def my_agenda():

    agenda = {}

    def insert_contact(contacto):
        phone = input("Introduce el telÃ©fono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[contacto] = phone
        else:
            print(
                "Debes introducir un numero de telefono con maximo 11 digitos .")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opc=input("Ingresa la opción: ")
        match opc:
            case "1":
                contactoBus=input("Ingresa el nombre de tu contacto: ")
                if contactoBus in  agenda:
                    print(f"El contacto esta en la agenda su numero de telefono es  {agenda[contactoBus]}")
                else:
                    print(f"El contacto {contactoBus}no esta en la agenda")
            case "2":
                contacto=input("Ingresa el nombre de tu contacto: ")
                insert_contact(contacto)
            case "3":
                nombreActualizar=input(" Ingresa el nombre del contacto a actualizar: ")
                if agenda[nombreActualizar] in agenda:
                    insert_contact(nombreActualizar)
                else:
                    print("El contacto no esta en la agenda")  
            case "4":
                contactoEliminar=input(" Ingrese el nombre del contacto a eliminar: ")
                if contactoEliminar in agenda:
                    del agenda[contactoEliminar] 
                else :
                    print("El contacto no existe")
            case "5":
                print("Saliendo de la agenda ")
                break
            case _:
                print(" Escribe una opción valida ")
my_agenda()
                