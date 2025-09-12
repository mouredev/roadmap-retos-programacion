#Estructuras de Datos

"""
Son formas de organizar y almacenar información para que podamos trabajar con ella de manera eficiente.
Son como cajas o contenedores que nos permiten guardar datos, acceder a ellos, modificarlos o recorrerlos según lo que necesitemos
"""

"""Ejemplos de Estructuras de Datos"""

#Listas(list)

"""Es una estructura de datos que permite almacenar una colección de elementos ordenados y modificables. Pueden contener distintos tipos de datos"""

from test.support import MAX_Py_ssize_t


my_list = ["mango", "wilson", "benito", "toby"]
print(my_list)

"""
🔧 Útiles cuando necesitas acceder por posición, agregar o eliminar elementos que se pueden modificar de esta manera.
"""
my_list.append("lachiquita")  # Agregar un elemento al final de la lista (insercion o append)
print(my_list)
my_list.remove("lachiquita")  # Eliminar un elemento específico de la lista (eliminar o remove)
print(my_list)
print(my_list[2])  # Acceder a un elemento por su posición (indexado o indexing)
my_list[2] = "benito2" #actualizacion por indexing
print(my_list)
my_list.sort()  # asi python Ordena la lista alfabéticamente (lo hace de esta manera por defecto, es posible cambiar el comportamiento del orden) (ordenar o sort)
print(my_list)

#Tuplas(tuple)
"""
es una estructura de datos similar a las listas, pero con la diferencia de que son inmutables (no se pueden modificar una vez creadas). Se definen utilizando paréntesis () en lugar de corchetes [].

Ejemplo de tupla:
"""
mi_tupla: tuple = ("mango", "wilson", "benito", "toby", "4")
print(mi_tupla)

"""
🔧 Útiles cuando necesitas almacenar un conjunto de elementos que no deben cambiar a lo largo del tiempo. (por ejemplo, datos personales, coordenadas geográficas)
"""
print(mi_tupla[1])  #(acceso) Acceder a un elemento por su posición (indexado o indexing) son las unicas que se podran realizar
#mi_tupla[1] = "benito2"  # Esto generará un error porque las tuplas son inmutables
print(mi_tupla.count("benito"))  # Contar cuántas veces aparece un elemento en la tupla (count)
mi_tupla = tuple(sorted(mi_tupla))  #(ordenacion) Ordenar los elementos de la tupla (sorted) #esto devuelve una lista ordenada, no modifica la tupla original
print(type(mi_tupla))  # Verificar el tipo de dato haya terminado en tuple (type)



#Conjuntos(set)
"""
Es una estructura de datos que permite almacenar una colección de elementos únicos y no ordenados. Se definen utilizando llaves {}.
buenas estructuras para guardar, recorrer muchos datos, pero no para buscar datos (los datos se hashean) toda la logica de estas mismas usa hashing/hash para que sea mas facil de localizar
esto evita duplicados (una coleccion de elementos unicos)

Ejemplo de conjunto:
"""
my_set: set = {"mango", "wilson", "benito", "toby", "4"}
print(my_set)

"""
🔧 Útiles cuando necesitas almacenar elementos únicos y no te importa el orden. (por ejemplo, etiquetas, categorías)
"""
my_set.add("lachiquita")  # Agregar un elemento al conjunto (insercion o add)
print(my_set)
my_set.remove("lachiquita")  # Eliminar un elemento específico del conjunto (eliminar o remove)
print(my_set)
print("benito" in my_set)  # Verificar si un elemento está en el conjunto (membership)
my_set = set(sorted(my_set))
print(my_set)  #(ordenacion) Ordenar los elementos del conjunto (sorted) #esto devuelve una lista ordenada, pero no modifica el conjunto original debido al set
print(type(my_set))  # Verificar el tipo de dato haya terminado en set (type)

#Diccionarios(dict)
"""
Es una estructura de datos que permite almacenar pares de clave-valor. Se definen utilizando llaves {} y dos puntos : para separar las claves de los valores.

Ejemplo de diccionario:
"""
mi_diccionario: dict = {
    "nombre": "mango",
    "edad": 5,
    
}
print(mi_diccionario)

"""
🔧 Útiles cuando necesitas asociar valores únicos (claves) con información adicional (valores). (por ejemplo, información de contacto, configuraciones)
"""
mi_diccionario["color"] = "amarillo"  # Agregar un nuevo par clave-valor (insercion o add)
print(mi_diccionario["color"])  # Acceder a un valor por su clave (acceso o indexing)
mi_diccionario["edad"] = 6  # Actualizar un valor por su clave (actualización)
print(mi_diccionario)
del mi_diccionario["color"]  # Eliminar un par clave-valor (eliminacion o del)
print(mi_diccionario)
mi_diccionario = dict(sorted(mi_diccionario.items()))  #(ordenacion) Ordenar los elementos del diccionario por clave (sorted)
print(type(mi_diccionario))  # Verificar el tipo de dato haya terminado en dict (type)

#XTRA
"""
 Crea una agenda de contactos por terminal.
 Debes implementar funcionalidades de búsqueda, inserción, actualización
 y eliminación de contactos.
 Cada contacto debe tener un nombre y un número de teléfono.
El programa solicita en primer lugar cuál es la operación que se quiere realizar,
y a continuación los datos necesarios para llevarla a cabo.
El programa no puede dejar introducir números de teléfono no numéricos y con más
de 11 dígitos (o el número de dígitos que quieras).
También se debe proponer una operación de finalización del programa.
"""


def my_agenda():
    agenda = {}

    while True:
        print("Seleccione una operación:")
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Seleciona una opcion ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"Teléfono de {nombre}: {agenda[nombre]}")
            else:
                print("Contacto no encontrado.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del nuevo contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            if not telefono.isdigit():
                print("El número debe contener solo dígitos.")
            elif len(telefono) != 10:
                print("El número debe tener exactamente 10 dígitos.")
            elif nombre in agenda:
                print("Ya existe un contacto con ese nombre.")
            else:
                agenda[nombre] = telefono
                print("Contacto agregado correctamente.")


        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            if nombre in agenda:
                nuevo_nombre = input("Ingrese el nuevo nombre del contacto: ")
                telefono = input("Ingrese el nuevo número de teléfono: ")
                if not telefono.isdigit():
                    print("El número debe contener solo dígitos.")
                elif len(telefono) != 10:
                    print("El número debe tener exactamente 10 dígitos.")
                else:
                    agenda[nuevo_nombre] = telefono
                    if nuevo_nombre != nombre:
                        del agenda[nombre]
            else:
                print("Contacto no encontrado.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")

        elif opcion == "5":
            print("Saliendo de la agenda.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

    return agenda

my_agenda()