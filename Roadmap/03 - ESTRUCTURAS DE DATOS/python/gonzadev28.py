"""* EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación."""

#Listas
mi_lista: list = [1, 7, 34, 76, 98, 9] #"list" es para definir el tipo de variable(lista)
print(mi_lista)

mi_lista.insert(0, 2) #En la posicion 0 inserta el valor de "2"
mi_lista.append(10) #Insercion de valor "10" en la lista
mi_lista.remove(76) #Elimina el valor de "76" de la lista
del mi_lista[5] #Elimina elemento de la lista en la posicion[5]
mi_lista[2] = 35 #Actualiza el elemento de la posicion[2] ("34" a "35")
mi_lista.sort() #Ordenacion de la lista de menor a mayor
print(mi_lista)

#Tuplas
mi_tupla: tuple = ("Aprendo", "Python", "Youtube", "Mouredev") #"tuple" es para definir el tipo de variable(tupla)
print(mi_tupla)

print(mi_tupla[1]) #Acceso en la posicion [1] de la tupla ("Python")
mi_tupla = tuple(sorted(mi_tupla)) #Ordena la tupla por orden alfabetico
print(mi_tupla)

#Sets
mi_set: set = {"Java", "Python", "C#", "Cobol", "C#"} #"set" es para definir el tipo de variable(sets)
print(mi_set) #El set no admite datos repetidos("C#")

mi_set.add("Ruby") #Insercion de "Ruby" en el set
mi_set.remove("Java") #Eliminacion de "Java" en el set
print(mi_set)

#Diccionario
mi_diccionario: dict = { #"dict" es para definir el tipo de variable(diccionario)
    "Nombre": "Gonzalo",
    "Lenguaje": "Python",
    "Github": "gonzadev28",
    "Edad": 30
}
print(mi_diccionario)

mi_diccionario["Ocupacion"] = "Estudiante" #Insercion del campo "Ocupacion: Estudiante" al diccionario
del mi_diccionario["Edad"] #Eliminacion del campo "Edad" al diccionario
mi_diccionario["Lenguaje"] = "JS" #Actualizacion del campo "Lenguaje" ("Python" a "JS")
print(mi_diccionario["Nombre"]) #Acceso a campo "Nombre"
print(mi_diccionario)

"""DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa."""

def mi_agenda():
    agenda: dict = {}
    while True:
        print("==========================================")
        print("Selecciona una de las siguientes opciones:")
        print("==========================================")
        print("1 - Buscar contacto")
        print("2 - Ingresar contacto")
        print("3 - Actualizar contacto")
        print("4 - Eliminar contacto")
        print("5 - Salir\n")
        
        opcion = input("Ingrese una de las opciones: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del contacto a buscar: ")
                if nombre in agenda:
                    print("El numero de telefono es: ", agenda[nombre])
                else:
                    print("Contacto no existe")
            case "2":
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el telefono del contacto: ")
                if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 9:
                    agenda[nombre] = telefono
                else:
                    print("Telefono debe ser menor de 10 digitos")
            case "3":
                nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
                if nombre in agenda:
                    telefono = input("Ingrese el telefono del contacto: ")
                    if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 9:
                        agenda[nombre] = telefono
                    else:
                        print("Telefono debe ser menor de 10 digitos")
                else:
                    print("Contacto no existe")
            case "4":
                nombre = input("Ingrese nombre del contacto que desea eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                else:
                    print("Contacto no existe")
            case "5":
                break
            case _:
                print("Opcion invalida")
            
mi_agenda()