""""
ESTRUCTURAS DE DATOS
"""
# LISTAS 

my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.append(6) # inserción al final de la lista
print(my_list)
my_list.remove(3) # eliminación de un elemento
print(my_list)
print(my_list[2]) # acceso a un elemento por su índice
my_list[1] = 10 # modificación de un elemento
print(my_list)

list2 = ["python", "java", "c++"]
list2.sort()
print(list2) # ordena la lista alfabéticamente

# TUPLAS
my_tuple = ("carro", "moto", "bicicleta", "45")
print(my_tuple[1])
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # ordena la tupla | sorted es una función que devuelve una lista ordenada
print(my_tuple)  # muestra la tupla ordenada
print(type(my_tuple))  # muestra el tipo de dato

# SETS
set1 = {"carro", "moto", "bicicleta", "45"}
print(set1)
set1.add("camioneta")  # agrega un elemento al set
print(set1)
set1.remove("carro")  # elimina un elemento del set
print(set1)
set1 = set(sorted(set1))  # ordena el set | el set no se puede ordenar 
print(set1)  
print(type(set1))  # muestra el tipo de dato

# DICCIONARIOS

my_dict = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
my_dict["pais"] = "España"  # inserción de un nuevo par clave-valor
print(my_dict)  
print(my_dict["nombre"])  # acceso a un valor por su clave
my_dict["edad"] = 31  # modificación de un valor
print(my_dict)
del my_dict["ciudad"]  # eliminación de un par clave-valor
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # ordena el diccionario por sus claves | dict es una función que crea un diccionario
print(my_dict)  # muestra el diccionario ordenado
print(type(my_dict))  # muestra el tipo de dato

""""
ESTRAS
"""
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
# los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
# (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.
 
def main(): 
    agenda = {}

    while True:
        print("\nAgenda de Contactos")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_contacto(agenda)
        elif opcion == "2":
            insertar_contacto(agenda)
        elif opcion == "3":
            actualizar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
    else:
        print("Contacto no encontrado.")

def insertar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono (11 dígitos máximo): ")

    if validar_telefono(telefono):
        agenda[nombre] = telefono
        print(f"Contacto {nombre} insertado con éxito.")
    else:
        print("Número de teléfono no válido. Debe ser numérico y tener un máximo de 11 dígitos.")
def actualizar_contacto(agenda):    
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    if nombre in agenda:
        telefono = input("Ingrese el nuevo número de teléfono (11 dígitos máximo): ")
        if validar_telefono(telefono):
            agenda[nombre] = telefono
            print(f"Contacto {nombre} actualizado con éxito.")
        else:
            print("Número de teléfono no válido. Debe ser numérico y tener un máximo de 11 dígitos.")
    else:
        print("Contacto no encontrado.")        
def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print("Contacto no encontrado.")

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) <= 11
if __name__ == "__main__":
    main()
    


