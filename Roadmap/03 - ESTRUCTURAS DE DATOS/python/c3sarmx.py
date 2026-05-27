"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
"""

# ========== Listas ==========

numeros = [1, 2, 3, 4]
print(numeros)

# == Insercción ==

numeros.append(5)
print(numeros) #* append() → agrega al final

# == Borrado ==

numeros.remove(1)
print(numeros) #* remove() → borra por valor

numeros.pop(0) #* pop() -> Borrado por indice
print(numeros)

# == Actualización ==

numeros[1] = 10 #* Cambiar un valor por índice:
print(numeros)

# == Ordenación ==

numeros.sort() #* sort() -> Ordena la lista
print(numeros)

ordenada = sorted(numeros) #* sorted() -> Devuelve una nueva lista
print(ordenada)

"""
REFUERZO:

Crea una lista llamada edades con estos valores:
[25, 18, 30, 22]

Luego:
Agrega el número 40
Elimina el 18
Cambia el 22 por 23
Ordena la lista
Imprime el resultado final
"""

edades = [25, 18, 30, 22]

edades.append(40)
print(edades)

edades.remove(18)
print(edades)

edades[2] = 23
print(edades)

edades.sort()
print(edades)

# ========== Tuplas ==========

my_tuple = ("Lio", "Gutierrez", "c3sarmx")
print(my_tuple[0]) #* Acceso por indice
my_tuple = tuple(sorted(my_tuple)) #* Ordenación
print(my_tuple) 

# ========== Sets ==========

my_set = {"Lio", "Gutierrez", "c3sarmx"}
print(my_set)
my_set.add("c3sar.mx@gmail.com") #* Insercción
print(my_set)
my_set.remove("Gutierrez") #* Borrado
print(my_set)


#* REFUERZO #*

"""
Crea un set llamado usuarios con:
{"Ana", "Luis", "Ana", "Pedro"}

Imprime el set
Agrega "María"
Elimina "Luis"
Imprime el resultado final
"""

users = {"Ana", "Luis", "Ana", "Pedro"}
print(users)

users.add("María")
users.remove("Luis")

print(users)

# ========== Diccionarios ==========

user = {
    "name": "Lio",
    "user": "c3sarmx",
    "email": "lioo.py@gmail.com",
    "age": 25
}
print(user)

user["alias"] = "lioodev" #* Insercción
print(user)

print(user["name"]) #* Acceso

user["age"] = 24 #* Actualización
print(user)

del user["age"] #* Eliminación
print(user)

user = dict(sorted(user.items())) #* Ordenación
print(user)

#* REFUERZO #*

""" 
Crea un diccionario agenda con:
"Lio" → "5512345678"
"Ana" → "5587654321"

Imprime el teléfono de "Lio"
Actualiza el teléfono de "Ana"
Elimina a "Lio"
Imprime la agenda final
"""

contactos = {
    "Lio": 5512345678,
    "Ana": 5587654321 
}
print(contactos)

print(contactos["Lio"])

contactos["Ana"] = 5561542101

del contactos["Lio"]
print(contactos)


#* EXTRA

print("========== Extra ==========")

"""
* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización
*   y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
*   y a continuación los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no numéricos y con más
*   de 11 dígitos (o el número de dígitos que quieras).
* - También se debe proponer una operación de finalización del programa.
"""

"""
AGENDA DE CONTACTOS (Reto 03 - Dificultad extra)

Requisitos:
- Búsqueda, inserción, actualización y eliminación de contactos
- Cada contacto: nombre + teléfono
- No permitir teléfonos: con caracteres no numéricos, con más de 11 dígitos (puedes ajustar el límite)
- Opción para finalizar el programa
"""

def my_agenda(): # Definimos la agenda
    
    agenda = {}
    # Creamos un bucle 'while'  
    def insert_contact():
        phone = input("Teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
            return True
        else:
            print("El número telefonico es incorrecto.")
            return False

    while True: 

# Mostramos al usuario las opciones disponibles
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

# Definimos una variable 'Opción' para que el usuario ingrese la opción a elegir.
        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El número de telefono de {name} es {agenda[name]}")
                else: 
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Nombre del contacto: ")
                if name in agenda:
                    print(f"El contacto ya existe. Usa la opción 'Actualizar' si deseas modificarlo.")
                else:
                    if insert_contact():
                        print(f"Contacto {name} se guardó exitosamente.")
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    if insert_contact():
                        print(f"Contacto {name} se actualizó exitosamente.")
                else: 
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Itroduce el contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Contacto {name} eliminado correctamente.")
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break # Con ´break' al elegir una de las opciones cerramos el programa.
            case _:
                    print("Opción no valida. Elige una opción del 1 al 5.")

my_agenda()

