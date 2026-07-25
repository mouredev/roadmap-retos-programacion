"""
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""
# Listas
lista = [1, 2, 3, 4, 5]  # Creación de una lista, sus valores pueden modificarse y puede contener cualquier tipo de dato
print(lista)  # Imprime la lista completa

# Tuplas
tupla = (1, 2, 3, 4, 5) # Creación de una tupla, sus valores no pueden modificarse y puede contener cualquier tipo de dato
print(tupla)  # Imprime la tupla completa

# Diccionarios
diccionario = {
    "nombre": "Pedro", 
    "edad": 19, 
    "nacionalidad": "Argentino"} 
# Creación de un diccionario, sus valores pueden modificarse y se accede a ellos mediante claves
print(diccionario)  # Imprime el diccionario completo
print(diccionario["nombre"])  # Imprime el valor asociado a la clave "nombre"
print(diccionario["edad"])  # Imprime el valor asociado a la clave "edad"
print(diccionario["nacionalidad"])  # Imprime el valor asociado a la clave "nacionalidad"

# Conjuntos
conjunto = {1, 2, 3, 4, 5} # Creación de un conjunto, sus valores pueden modificarse pero no se pueden repetir y puede contener cualquier tipo de dato, es lo mismo que una lista pero sin orden y sin elementos repetidos
print(conjunto)  # Imprime el conjunto completo

# Operaciones de inserción, borrado, actualización y ordenación
# Inserción y actualización, ya que en Python no existe una operación de inserción específica para los diccionarios, se utiliza la asignación para insertar o actualizar un valor asociado a una clave

lista.append(6)  # Inserta el número 6 al final de la lista
print(lista)  # Imprime la lista después de la inserción

diccionario["profesion"] = "Programador"  # Inserta una nueva clave "profesion" con el valor "Programador" en el diccionario
print(diccionario)  # Imprime el diccionario después de la inserción

diccionario["edad"] = 20 # Actualiza el valor de la clave "edad" a 20 en el diccionario
print(diccionario) # Imprime el diccionario después de la actualización

conjunto.add(6) # Inserta el número 6 en el conjunto
print(conjunto) # Imprime el conjunto después de la inserción

# Borrado
lista.remove(3)  # Elimina el número 3 de la lista, si no existe genera un error
print(lista)  # Imprime la lista después del borrado

del diccionario["edad"]  # Elimina la clave "edad" y su valor del diccionario
print(diccionario)  # Imprime el diccionario después del borrado

conjunto.remove(3) # Elimina el número 3 del conjunto, si no existe genera un error
print(conjunto) # Imprime el conjunto después del borrado

# Ordenación
lista = [5, 2, 9, 1, 3]  # Creación de una lista desordenada
print("Lista origninal:", lista)  # Imprime la lista original antes de la ordenación
lista.sort()  # Ordena la lista de menor a mayor
print(lista)  # Imprime la lista después de la ordenación

lista.sort(reverse=True)  # Ordena la lista de mayor a menor, el parámetro reverse=True indica que se debe ordenar en orden inverso
print(lista)  # Imprime la lista después de la ordenación

lista.sort(key=lambda x: x % 2)  # Ordena la lista colocando primero los números pares y luego los impares, el parámetro key=lambda x: x % 2 indica que se debe ordenar según el resultado de la función lambda, que devuelve 0 para los números pares y 1 para los números impares
print(lista)  # Imprime la lista después de la ordenación

#lambda es una función anónima, es decir, una función sin nombre que se define en una sola línea de código, se utiliza para crear funciones pequeñas y simples que se pueden pasar como argumentos a otras funciones, como en este caso a la función sort() para indicar el criterio de ordenación. Parece complicado pero es muy útil para evitar tener que definir una función completa solo para un criterio de ordenación específico.

lista.sort(key=lambda x: x % 2, reverse=True)  # Ordena la lista colocando primero los números impares y luego los pares, el parámetro key=lambda x: x % 2 indica que se debe ordenar según el resultado de la función lambda, que devuelve 0 para los números pares y 1 para los números impares, el parámetro reverse=True indica que se debe ordenar en orden inverso
print(lista)  # Imprime la lista después de la ordenación

# Ordenación de un diccionario por sus claves
diccionario = {"b": 2, "a": 1, "c": 3}  # Creación de un diccionario desordenado
print("Diccionario original:", diccionario)  # Imprime el diccionario original antes de la ordenación
diccionario_ordenado = dict(sorted(diccionario.items())) # Ordena el diccionario por sus claves, el método sorted() devuelve una lista de tuplas ordenada por las claves, luego se convierte de nuevo a un diccionario con la función dict()
#sorted() es una función que ordena cualquier iterable, como listas, tuplas o diccionarios, y devuelve una nueva lista ordenada. En este caso, se utiliza para ordenar las tuplas devueltas por el método items() del diccionario, que contiene las claves y valores del diccionario. Al ordenar estas tuplas, se ordena el diccionario por sus claves.
#dict() es una función que convierte una lista de tuplas en un diccionario, donde cada tupla debe contener exactamente dos elementos, el primero se convierte en la clave y el segundo en el valor del diccionario. En este caso, se utiliza para convertir la lista de tuplas ordenada por las claves de nuevo a un diccionario.
print(diccionario_ordenado)  # Imprime el diccionario después de la ordenación por claves

# Ordenación de un diccionario por sus valores
diccionario_ordenado_por_valores = dict(sorted(diccionario.items(), key=lambda item: item [1])) # Ordena el diccionario por sus valores, el parámetro key=lambda item: item[1] indica que se debe ordenar según el segundo elemento de cada tupla, que corresponde al valor del diccionario, si fuera item[0] se ordenaría por las claves, haciendo lo mismo que en el ejemplo anterior
print(diccionario_ordenado_por_valores)  # Imprime el diccionario después de la ordenación por valores

"""
DIFICULTAD EXTRA (opcional):
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
agenda = {}  # Creación de un diccionario vacío para almacenar los contactos

def mostrar_menu():
    print("1. Agregar contacto nuevo")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    if not telefono.isdigit() or len(telefono) > 11: # Verifica que el número de teléfono sea numérico  y no tenga más de 11 dígitos
        print("Número de teléfono no válido. Debe ser numérico y tener como máximo 11 dígitos.")
        return
    if nombre in agenda:
        print(f"Contacto '{nombre}' ya existe en la agenda. Use la opción de actualización para modificarlo.")
        return
    if telefono in agenda.values():
        print(f"El número de teléfono '{telefono}' ya está asociado a otro contacto en la agenda. Use la opción de actualización para modificarlo.") 
        return
    else:
        agenda[nombre] = telefono # Agrega la clave nombre con el valor telefono al diccionario agenda
        print(f"Contacto '{nombre}' agregado exitosamente.")
    input("Presione Enter para continuar...") # Pausa el programa para que el usuario pueda leer el mensaje antes de volver al menú

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda: # Verifica que el nombre introducido existe en el diccionario agenda
        print(f"El número de teléfono de '{nombre}' es: {agenda[nombre]}") # Imprime el número de teléfono asociado a la clave nombre
    else:
        print(f"Contacto '{nombre}' no se ha encontrado en la agenda.")
    input("Presione Enter para continuar...") # Pausa el programa para que el usuario pueda leer el mensaje antes de volver al menú

def actualizar_contacto():
    print("1. Actualizar nombre del contacto")
    print("2. Actualizar número de teléfono del contacto")
    opcion = input("Seleccione la opción: ")
    if opcion == "1":
        nombre_actual = input("Ingrese el nombre actual del contacto: ")
        if nombre_actual in agenda: # Verifica que el nombre actual existe en el diccionario agenda
            nuevo_nombre = input("Ingrese el nuevo nombre del contacto: ")
            agenda[nuevo_nombre] = agenda.pop(nombre_actual) # Reemplaza el nombre actual con el nuevo nombre, utilizando el método pop() para eliminar la clave nombre_actual y obtener su valor, que se asigna a la nueva clave nuevo_nombre
            print(f"Nombre del contacto actualizado de '{nombre_actual}' a '{nuevo_nombre}'.")
        else: 
            print(f"Contacto '{nombre_actual}' no se ha encontrado en la agenda.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in agenda:
            nuevo_telefono = input("Ingrese el nuevo número de telefono del contacto: ")
            if not nuevo_telefono.isdigit() or len(nuevo_telefono) > 11: # Verifica que sea un digito numero y no sobrepase los 11 dígitos
                print("Número de teléfono no válido. Debe ser numérico y tener como máximo 11 dígitos.")
                input("Presione Enter para continuar...") # Pausa el programa para que el usuario pueda leer el mensaje antes de volver al menú
                return
            if nuevo_telefono in agenda.values():
                print(f"El número de teléfono '{nuevo_telefono}' ya está asociado a otro contacto en la agenda.") 
                input("Presione Enter para continuar...") # Pausa el programa para que el usuario pueda leer el mensaje antes de volver al menú
                return
            else:
                agenda[nombre] = nuevo_telefono # Actualiza el numero asociado al nombre del contacto
                print(f"Número de teléfono del contacto '{nombre}' actualizado exitosamente.")
        else:
            print(f"Contacto '{nombre}' no se ha encontrado en la agenda.")
    else:
        print("Opción no válida.")
    input("Presione Enter para continuar...") # Pausa el programa para que el usuario pueda leer el mensaje antes de volver al menú
        
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda: # Verifica que el nombre introducido existe en el diccionario agenda
        del agenda[nombre] # Elimina la clave nombre y su valor asociado del diccionario agenda
        print(f"Contacto '{nombre}' eliminado exitosamente.")
    else:
        print(f"Contacto '{nombre}' no se ha encontrado en la agenda.")
    input("Presione Enter para continuar...") # Pausa el programa para que el usuario pueda leer el mensaje antes de volver al menú
    
def mostrar_contactos():
    if agenda:
        print("Contactos en la agenda:")
        for nombre, telefono in agenda.items(): # Itera sobre las claves y valores del diccionario agenda utilizando el método items()
            print(f"Nombre: {nombre}, Teléfono: {telefono}") # Imprime el nombre y el número de teléfono de cada contacto
    else:
        print("La agenda está vacía.")
    
    input("Presione Enter para continuar...") # Pausa el programa para que el usuario pueda leer el mensaje antes de volver al menú

while True:
    mostrar_menu() # Muestra el menú de opciones al usuario
    opcion = input("Seleccione una opción: ") # Solicita al usuario que seleccione una opción del menú
    if opcion == "1":
        agregar_contacto() # Llama a la función para agregar un nuevo contacto
    elif opcion == "2":
        buscar_contacto() # Llama a la función para buscar un contacto por su nombre
    elif opcion == "3":
        actualizar_contacto() # Llama a la función para actualizar el nombre o el número de teléfono de un contacto existente
    elif opcion == "4":
        eliminar_contacto() # Llama a la función para eliminar un contacto por su nombre
    elif opcion == "5":
        mostrar_contactos() # Llama a la función para mostrar todos los contactos en la agenda
    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!") # Imprime un mensaje de despedida antes de salir del programa
        break # Termina el bucle y finaliza el programa
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
        
