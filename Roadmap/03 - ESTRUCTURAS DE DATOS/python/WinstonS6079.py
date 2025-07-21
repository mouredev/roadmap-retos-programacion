'''
Estructuras de Datos
'''

list = [1, 2, 3, 4, 5] # La lista es una colección ordenada y mutable de elementos.
list.append(6)  # Añadir un elemento al final de la lista
print("Lista después de añadir un elemento:", list)
list.remove(3)  # Eliminar un elemento de la lista
print("Lista después de eliminar un elemento:", list)

print("Primer elemento de la lista:", list[0])  # Acceso al primer elemento
print("Último elemento de la lista:", list[-1])  # Acceso al último elemento
list[0] = 10  # Actualizar el primer elemento
print("Lista después de actualizar el primer elemento:", list)
list.sort()  # Ordenar la lista en orden ascendente
print("Lista después de ordenar:", list)
print("Sublista de los primeros tres elementos:", list[:3])  # Acceso a una sublista
print("Sublista de los últimos dos elementos:", list[-2:])  # Acceso a una sublista desde el final
print("Lista de elementos del índice 1 al 3:", list[1:4])


tuple = (1, 2, 3, 4, 5) # La tupla es una colección ordenada e inmutable de elementos.
# Inserción y eliminación en una tupla no es posible, ya que son inmutables.
# Sin embargo, se puede crear una nueva tupla a partir de una existente.
#Acceso a elementos en una tupla
print("Primer elemento de la tupla:", tuple[0])  # Acceso al primer elemento
print("Último elemento de la tupla:", tuple[-1])  # Acceso al último elemento
tuple_nueva = tuple + (6,)  # Crear una nueva tupla añadiendo un elemento
print("Tupla después de añadir un elemento:", tuple_nueva) # Tupla original no se modifica


set = {1, 2, 3, 4, 5} # El conjunto es una colección desordenada de elementos únicos.
print("Conjunto:", set)  # Imprimir el conjunto
set.add(6)  # Añadir un elemento al conjunto
print("Conjunto después de añadir un elemento:", set)
set.remove(2)  # Eliminar un elemento del conjunto
print("Conjunto después de eliminar un elemento:", set)
set.update([7, 8])  # Añadir múltiples elementos al conjunto
#Los conjuntos no permiten elementos duplicados, por lo que si se intenta añadir un elemento ya existente, no se producirá ningún cambio.
#Los conjuntos no se pueden ordenar, por lo que no se pueden acceder a los elementos por índice.
print("Conjunto después de añadir múltiples elementos:", set)
print("¿El número 3 está en el conjunto?", 3 in set)  # Comprobar si un elemento está en el conjunto


my_dict = {"a": 1, "b": 2, "c": 3}  # Diccionario con pares clave-valor
print("Valor asociado a la clave 'a':", my_dict["a"])  # Acceso al valor de una clave
my_dict["d"] = 4  # Añadir un nuevo par clave-valor
print("Diccionario después de añadir un nuevo par:", my_dict) # Diccionario original no se modifica
my_dict["a"] = 10  # Actualizar el valor de una clave existente
print("Diccionario después de actualizar un valor:", my_dict)
del my_dict["b"]  # Eliminar un par clave-valor
print("Diccionario después de eliminar un par:", my_dict)
sorted(my_dict.items())  # Ordenar los elementos del diccionario por clave
print("Elementos del diccionario ordenados por clave:", sorted(my_dict.items()))
print(type(my_dict))  

cadena = "Hola, mundo!" # La cadena es una secuencia de caracteres.

# Imprimir estructuras de datos
print("Lista:", list)
print("Tupla:", tuple)
print("Diccionario:", my_dict)
print("Conjunto:", set)
print("Cadena:", cadena)

"""
Extra
"""

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Ingrese el número de teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
            print("Contacto agregado/actualizado correctamente.")
        else: 
            print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 1 y 11 caracteres.")

    while True:

        print("\nAgenda de Contactos")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contactos")
        print("5. Ver contactos")
        print("6. Salir")

        option = input("\nSeleccione una opción: ")
    
        match option:
            case "1":
                name = input("\nIngrese el nombre del contacto a buscar: ")
                if name in agenda:
                    print("Contacto encontrado:")
                    print("Nombre:", name)
                    print("Teléfono:", agenda[name])
                else:
                    print("Contacto no encontrado.")      
            case "2":
                name = input("Ingrese el nombre del contacto a agregar: ")
                insert_contact()
            case "3":
                name = input("Ingrese el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
            case "4":
                name = input("Ingrese el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print("Contacto eliminado.")
                else:
                    print("Contacto no encontrado.")
            case "5":
                print("Contactos en la agenda:")
                for name, phone in agenda.items():
                    print("Nombre:", name, "| Teléfono:", phone)
            case "6":
                print("Saliendo de la agenda...")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 6.")
my_agenda()