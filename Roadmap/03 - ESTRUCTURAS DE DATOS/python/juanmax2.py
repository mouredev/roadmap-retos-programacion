"""
Estructuras de datos
"""
# Lista
my_list = ["Juanma", "Maria", "David", "Adri"]
print(my_list)
print(type(my_list))
# Añadir nuevo dato al final de la lista
my_list.append("Carlos")
print(my_list)

# Borrar dato de la lista
my_list.remove("Adri")
print(my_list)

# Actualizar un dato en la lista
my_list[2] = "Adri"
print(my_list)

# Ordenar la lista
my_list.sort() # Por defecto lo hace de forma alfabetica o ascendente
print(my_list)

# Tuplas
# Las tuplas son inmutables con lo cual solo se puede acceder a ella
# para ver sus datos
my_tupla = ("Juanma", "juanmax2", "32")
print(my_tupla)
print(type(my_tupla))
# Ordenar una tupla
my_tupla = tuple(sorted(my_tupla))
# Hay que especificar tuple para hacer el sorted porque sino
# devolveria una lista
print(my_tupla)

# Sets (conjuntos)
# Son estructuras desordenadas y no se puede acceder por indice
# No albergan datos iguales entre si ("Juanma", "Juanma")
my_set = {"Juanma", "juanmax2", "32"}
print(my_set)
print(type(my_set))
# Añadir datos
my_set.add("batman")
print(my_set)

# Eliminar datos
my_set.remove("32") # Sin indice, con el valor
print(my_set)

# El set no se puede ordenar porque por defecto no hay indices

# Diccionario

my_dict = {
    "nombre" : "Juanma",
    "edad" : 32,
    "profesion" : "estudiante"
    }
print(my_dict)
print(type(my_dict))

# Insertar datos
# Hay que acceder por la clave
my_dict["email"] = "juanma@gmail.com"
print(my_dict)

# Actualizar datos
my_dict["edad"] = 33
print(my_dict)

# Borrar datos
del my_dict["email"]
print(my_dict)

# Ordenar
my_dict = dict(sorted(my_dict.items()))
print(my_dict)

"""
Ejercicio opcional
* Crea una agenda de contactos por terminal.
Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
Cada contacto debe tener un nombre y un número de teléfono.
El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
los datos necesarios para llevarla a cabo.
El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
(o el número de dígitos que quieras)
También se debe proponer una operación de finalización del programa.
"""
my_agenda = {}

def menu_opciones():
    """Esta función se encarga de mostrar el menu de opciones por pantalla"""
    print("Bienvenido usuario!")
    print("-------------------")
    print("-------------------")
    print(
        """
        1 - Añadir contacto.
        2 - Buscar contacto.
        3 - Eliminación de contacto.
        4 - Actualización de contacto.
        5 - Mostrar lista de contactos.
        6 - Salir del programa.
        """
        )
    print("-------------------")
    print("-------------------")
    
def recibir_opcion():
    """Esta funcion se encarga de recibir la opcion que queremos y retornarla"""
    num = int(input("Por favor seleccione una opción: "))
    return num

def validar_numero(nombre):
    """Esta funcion se encarga de recibir un nombre y validar si el numero de telefono que
    introducimos es correcto, devuelve el dato a nuestra agenda"""
    
    numero = input("Introduce el número de telefono: ")
    if numero.isdigit() and len(numero) > 0 and len(numero) <= 11:
        my_agenda[nombre] = numero
    else: 
        print("Numero no valido")
        
def buscar_contacto():
    """Esta función se encarga de buscar un contacto en nuestra agenda"""
    
    nombre = input("Introduce el nombre de la persona: ")
    if nombre in my_agenda:
        print(f"El contacto {nombre} tiene el número {my_agenda[nombre]}")       
    else:
        print(f"El contacto {nombre} no encontrado")
        
def añadir_contacto():
    """Esta función se encarga de añadir contactos a nuestra agenda"""
    
    nombre = input("Introduce el nombre del contacto: ")
    validar_numero(nombre)

def eliminar_contacto():
    """Esta función se encarga de eliminar contactos existentes en nuestra agenda"""
    
    nombre = input("Introduce el nombre del contacto que quieres eliminar: ")
    if nombre in my_agenda:
        del my_agenda[nombre]
    else:
        print(f"El contacto {nombre} no existe")
    
def actualizar_contacto():
    """Esta función se encarga de actualizar contactos de nuestra agenda"""
    
    nombre = input("Introduce el nombre del contacto a actualizar: ")
    if nombre in my_agenda:
        validar_numero(nombre)
        
def mostrar_contactos():
    """Esta funcón se encarga de mostrar los contactos de nuestra agenda"""
    
    for nombre, numero in my_agenda.items():
        print(f"Nombre : {nombre} Número : {numero} ")
        

def salir_programa():
    """Esta funcón muestra que estamos cerrando el programa"""
    
    print("Cerrando programa...")
    print("Fin de la ejecución")
    return continuar == False



# Caso de uso
continuar = True
while continuar == True:
    menu_opciones()
    opcion = recibir_opcion()
    if opcion == 1:
        añadir_contacto()
    elif opcion == 2:
        buscar_contacto()
    elif opcion == 3:
        eliminar_contacto()
    elif opcion == 4:
        actualizar_contacto()
    elif opcion == 5:
        mostrar_contactos()
    elif opcion == 6:
        salir_programa()
        continuar = False
    else:
        print("No es una opción valida")
        