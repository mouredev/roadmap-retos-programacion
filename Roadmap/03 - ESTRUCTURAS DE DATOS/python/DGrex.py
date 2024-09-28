"""
    EJERCICIO:
    Muestra ejemplos de creación de todas las estructuras soportadas por defecto
    en tu lenguaje.
    Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

# listas

mi_lista = [3,5,10,89,10,45,75,32]

#Agregar un valor a la lista
mi_lista.append(100)
print("Se agrega un valor a la lista\n",mi_lista)

#Insertar un dato en una posicion
mi_lista.insert(0,11)
print("\nInsertar un dato en una posicion\n",mi_lista)

#Actualizar dato de una posicion
mi_lista[1]= 100
print("\nActualizar dato de una posicion\n",mi_lista)

#Elimina el primer valor identico encontrado
mi_lista.remove(100)
print("\nElimina el primer valor identico encontrado\n",mi_lista)

#Eliminar el dato en una posicion
del mi_lista[4]
print("\nEliminar el dato en una posicion\n",mi_lista)

#Ordenar lista
mi_lista.sort()
print("\nOrdenar lista\n",mi_lista)

#Lista invertida
mi_lista.reverse()
print("\nLista invertida\n",mi_lista)

#Limpiar lista
mi_lista.clear()
print("\nLimpiar lista\n",mi_lista)


#Tuplas
"""
Adiferencia de las lista las tuplas tienen valores constantes
es
"""

mi_tupla = ("Nombre", "Segundo nombre", "Apellido", "Apellido", "Segundo apellido")

#Mostrar tupla
print("\nMostrar tupla\n",mi_tupla)

#Mostrar el dato en una posicion
print("\nMostrar dato en una posicion\n",mi_tupla[2])

#Contar valores identicos
print("\nContar valores identicos\n",mi_tupla.count("Apellido"))
mi_tupla.count("Apellido")

#Mostrar posicion de un valor
print("\nMostrar posicion de un valor\n",mi_tupla.index("Nombre"))


#set
"""
Un set no es una estructura ordenada
"""

mi_set = {9,8,7,6,5,4,3,2,1}

#Imprimir el set
print("\nImprimir set\n",mi_set)

#Agregar un valor
mi_set.add(10)
print("\nAgregar un valor\n",mi_set)
"""
En el set no se permite los valoress repetidos
"""

#Comprovar si existe un valor en el set
print("\nComprovar si existe un valor en el set\n",10 in mi_set)

#Eliminar un valor
mi_set.remove(10)
print("\nEliminar un valor\n",mi_set)

#Limpiar set
mi_set.clear()
print("\nLimpiar set\n",mi_set)


#Diccionarios

my_diccionario = {
    "Marca": "Honda",
    "Modelo": "CB1",
    "Año": 2024
}

#Imprimir diccionario
print("\nImprimir diccionario\n",my_diccionario)

#Actualizar el valor de una clave
my_diccionario["Año"]= 2025
print("\nActualizar el valor de una clave\n",my_diccionario)

#Agregar clave y valor
my_diccionario["Color"]= "Celeste"
print("\nAgregar clave y valor\n",my_diccionario)

#Eliminar una clave y un dato
del my_diccionario["Color"]
print("\nEliminar una clave y un dato\n",my_diccionario)


#Encontrar una clave o un valor de la clave en el diccionario
print("\nExiste esta clave?")
print("Modelo" in my_diccionario)

print("\nExiste el valor en la clave?")
print("CB1" in my_diccionario["Modelo"])


"""
    DIFICULTAD EXTRA (opcional):
    Crea una agenda de contactos por terminal.
    Debes implementar funcionalidades de búsqueda, inserción, actualización
    y eliminación de contactos.
    Cada contacto debe tener un nombre y un número de teléfono.
    El programa solicita en primer lugar cuál es la operación que se quiere realizar,
    y a continuación los datos necesarios para llevarla a cabo.
    El programa no puede dejar introducir números de teléfono no númericos y con más
    de 11 dígitos (o el número de dígitos que quieras).
    También se debe proponer una operación de finalización del programa.
"""

import json
contactos = dict()

def actualizar_o_nuevo_numero(nombre):
    condicion = True
    while condicion :
        numero = input("Numero de contacto: ")
        if numero.isdigit() and len(numero) == 10:
            contactos[nombre]= numero
            condicion = False
        else:
            print("Ingrese un numero correcto")

def nuevo_contacto():
    nombre = input("Nombre del contacto: ")
    actualizar_o_nuevo_numero(nombre)
    
def actualizacion_de_contacto():
    condicion = True
    while condicion:
        nombre = input("Nombre del contacto a actualizar: ")
        if nombre in contactos:
            actualizar_o_nuevo_numero(nombre)
            condicion = False
        else:
            print("Este contacto no existe")
   
def opcion_usuario():
    condicion = True
    while condicion:
        opcion = input("Ingrese una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion > 0 and opcion < 7:
                condicion = False
                return opcion
            else:
                print("Fuera de rango")
        else:
            print("La opccion ingresada es incorrecta")

def buscar_contacto():
    condicion = True
    while condicion:
        nombre = input("Nombre del contacto a buscar: ")
        if nombre in contactos:
            print(f"\nNombre: {nombre}\nNumero: {contactos[nombre]}")
            condicion = False
        else:
            print("Este contacto no existe")

def eliminar_contacto():
    condicion = True
    while condicion:
        nombre = input("Nombre del contacto a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]
            condicion = False
            print(f"Contacto {nombre} eliminado")
        else:
            print("Este contacto no existe")

def imprimir_contactos():
     print(json.dumps(contactos, indent=4))

def iniciar_programa():
    condicion = True
    while condicion:
        print(f"\nELIGE UNA OPCION\n"
            "1. Nuevo contacto\n"
            "2. Atualizar contaco\n"
            "3. Buscar contacto\n"
            "4. Eliminar contacto\n"
            "5. Ver contactos\n"
            "6. Salir\n")
        match opcion_usuario():
            case 1:
                nuevo_contacto()
            case 2:
                actualizacion_de_contacto()
            case 3:
                buscar_contacto()
            case 4:
                eliminar_contacto()
            case 5:
                imprimir_contactos()
            case 6:
                condicion = False
                exit()
    

iniciar_programa()
