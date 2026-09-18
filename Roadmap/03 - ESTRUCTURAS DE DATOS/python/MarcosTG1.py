"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

### Listas

mi_lista = ["Marcos", "Tudela", "Hernández"]

mi_lista.append(1) # Inserción

print(mi_lista)

mi_lista.remove(1)

print(mi_lista) # Borrado

mi_lista[2] = "Ramón" # Actualización

print(mi_lista)

# Por defecto ordena alfabéticamente para listas de strings

mi_lista.sort(reverse=False) # Ordenación

print(mi_lista)

### Tuplas

mi_tupla: tuple = ("plantas", "abono", "5", "aloe vera")

print(mi_tupla.index("5")) # Búsqueda

print(mi_tupla[2]) # Acceso

print(type(tuple(sorted(mi_tupla)))) # Ordenación

### Sets

mi_set: set = {"plantas", "abono", "5", "aloe vera"}

mi_set.add("palmera")
mi_set.add("limonero") # Inserción ; los sets son estructuras desordenadas
mi_set.add("limonero")

print(mi_set) 

mi_set.discard("plantas") # Eliminación

print(set(sorted(mi_set))) # No se puede ordenar

# valor_clave = mi_set[2] No es posible acceder de esta forma a los sets

## Dicts

mi_diccionario: dict = {"1": "canelones", 22: "macarrones", 3: "paella", "persona": "Marcos"}

print(mi_diccionario.get(22)) # Acceso por clave
nombre = mi_diccionario["persona"] # Acceso por clave
print(nombre)

mi_diccionario.pop(22) # Borrado
del mi_diccionario[3]

mi_diccionario["apellido"] = "tudela" # Inserción
mi_diccionario["apellido"] = "guerra" # Actualización


print(dict(sorted(mi_diccionario.items())))

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

def my_agenda():

    agenda: dict = {}
    is_on = True

    def insertar_contacto():
        print("\nIntroduce el teléfono")
        telefono = input()
        if telefono.isdigit() and len(telefono) < 10 and len(telefono) > 8:
            agenda[nombre] = telefono
        else:
            print("Número de teléfono no válido")

    
    while is_on:

        print("")
        print("Introduce 1 para búsqueda")
        print("Introduce 2 para inserción")
        print("Introduce 3 para actualización")
        print("Introduce 4 para eliminación")
        print("Introduce 5 para acabé")

        opcion = int(input("\nElige una opción: "))
        match opcion:
            case 1:
                print("\nIntroduce el nombre del contacto a buscar")
                nombre = str(input())
                print(f"\nEl número de {nombre} es {agenda[nombre]}")

            case 2:
                print("\nIntroduce el nombre del contacto")
                nombre = str(input())
                insertar_contacto()
                
            case 3:
                print("\nIntroduce el nombre del contacto para actualizar")
                nombre = str(input())
                insertar_contacto()
            case 4:
                 print("\nIntroduce el nombre del contacto para eliminar")
                 nombre = str(input())
                 agenda.pop(nombre)
            case 5:
                is_on = False
            case _:
                print("Opción no válida")
        
    return agenda

agenda = my_agenda()
print(agenda.items())
    

"""
Primer intento de resolución, lucha productiva.
"""
def solicitar_operacion():
    decision = (int(input("¿Qué operación deseas realizar? \n 1:inserción, 2:actualización, 3:eliminación, 4:búsqueda, 5: acabé ")))
    return decision

def add_contacto(agenda: dict):
    nombre = (str(input("Dime el nombre del contacto a añadir: ")))
    numero = (int(input("Dime el número de teléfono de dicho contacto: ")))
    if numero > 99999999999:
        print("Número no válido")
    agenda[numero] = nombre

    return agenda

def actualizar_contacto(agenda: dict):
    numero = int(input("Introduce el número del contacto a actualizar: "))
    nombre_nuevo = str(input("A qué nuevo nombre pertenece este número: "))
    if numero > 99999999999:
        print("Número no válido")
    agenda[numero] = nombre_nuevo
    return agenda

def eliminar_contacto(agenda: dict):
    contacto = int(input("Número de teléfono del contacto a eliminar: "))
    agenda.pop(contacto)

    return agenda

def buscar_contacto(agenda: dict):
    return

mi_agenda = {}
decision = 0

while decision != 5:
    decision = solicitar_operacion()

    if decision == 1:
        mi_agenda = add_contacto(mi_agenda)
    elif decision == 2:
        mi_agenda = actualizar_contacto(mi_agenda)
    elif decision == 3:
        mi_agenda = eliminar_contacto(mi_agenda)
    elif decision == 4:
        mi_agenda = buscar_contacto(mi_agenda)
    else:
        print("Introduce una opción válida \n")


print(mi_agenda.items())
