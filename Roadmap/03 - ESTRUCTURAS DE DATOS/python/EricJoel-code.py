# Estructuras de Datos

# Listas: Colección ordenada y mutable de elementos

mi_lista = ["Python","Java","C++","C#" ]
print(mi_lista)

#Insertar un elemento en una lista
mi_lista.append("Go")
print(mi_lista)

#Eliminar un elemento de una lista
mi_lista.remove("Java")
print(mi_lista)

#Acceder a un elemento de una lista
print(mi_lista[1])

#Actualizar un elemento de una lista
mi_lista[2] = "C"
print(mi_lista)

#Ordenar una lista
mi_lista.sort()
print(mi_lista)

# Tuplas: Colección ordenada e inmutable de elementos

mi_tupla = ("Eric","Joel", "22", "Python") 
print(mi_tupla)

#Acceder a un elemento de una tupla
print(mi_tupla[0])

#Ordenar una tupla (convertir a lista y luego ordenar)
mi_tupla = tuple(sorted(mi_tupla))  
print(mi_tupla)

# Sets: Colección no ordenada y mutable de elementos únicos
mi_set = {"Python", "Java", "C++", "C#" }
print(mi_set)

#Agregar un elemento a un set
mi_set.add("Go")
mi_set.add("Go")  # No se agregará porque ya existe
print(mi_set)

#Eliminar un elemento de un set
mi_set.remove("Java")
print(mi_set)

#Ordenar un set: se convierte a lista, se ordena y luego se convierte de nuevo a set esto no mantiene el orden ya que los sets son desordenados
mi_set = set(sorted(mi_set))  
print(mi_set)

# Diccionarios: Colección ordenada, mutable de pares clave-valor

mi_diccionario = {
    "nombre": "Eric",
    "apellido": "Cacuango",
    "edad": 22,
    "ciudad": "Otavalo"
}
print(mi_diccionario)

#Acceder a un valor en un diccionario
print(mi_diccionario["nombre"]) # Accede al valor asociado a la clave
print(mi_diccionario.get("edad")) # Otra forma de acceder al valor asociado a la clave

#Insertar un par clave-valor en un diccionario
mi_diccionario["profesion"] = "Programador"
print(mi_diccionario)

#Borrar un par clave-valor en un diccionario
del mi_diccionario["ciudad"]
print(mi_diccionario)

#Actualizar un valor en un diccionario
mi_diccionario["edad"] = 23
print(mi_diccionario)

#Ordenar un diccionario por clave (convierte a lista de tuplas, ordena y luego convierte de nuevo a diccionario)
mi_diccionario = dict(sorted(mi_diccionario.items()))
print(mi_diccionario)  # Muestra una lista de tuplas ordenadas por clave

#Extra

# Crea una agenda de contactos por terminal

contactos = {}


def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el numero de telefono del contacto: ")
    while True:
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) < 12:
            contactos[nombre] = telefono
            print(f"Contacto {nombre} agregado.")
            break
        else:
            print("Número de teléfono no válido. Debe ser numérico y tener menos de 12 dígitos.")
            telefono = input("Ingrese nuevamente el numero de telefono del contacto: ")
    

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f"Contacto encontrado: {nombre} - {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")
        

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")
        
        
def actualizar_contacto():
    nombre = input("Ingrese el nombre del contacto a actualizar: ")
    if nombre in contactos:
        nuevo_telefono = input("Ingrese el nuevo numero de telefono: ")
        while True:
            if nuevo_telefono.isdigit() and len(nuevo_telefono) > 0 and len(nuevo_telefono) < 12:
                contactos[nombre] = nuevo_telefono
                print(f"Contacto {nombre} actualizado.")
                break
            else:
                print("Número de teléfono no válido. Debe ser numérico y tener menos de 12 dígitos.")
                nuevo_telefono = input("Ingrese nuevamente el nuevo numero de telefono: ")
    else:
        print("Contacto no encontrado")
        
        
def mostrar_contactos():
    if contactos:
        print("Contactos en la agenda:")
        for nombre, telefono in contactos.items():
            print(f"{nombre} - {telefono}")
    else:
        print("No hay contactos en la agenda.")

def agenda():
    
    while True:
        print("\n --- Agenda de Contactos ---")
        print("1. Agregar Contacto")
        print("2. Buscar Contacto")
        print("3. Actualizar Contacto")
        print("4. Eliminar Contacto")
        print("5. Mostrar Todos los Contactos")
        print("6. Salir")
        print("----------------------------")
        
        opcion = input("Seleccione una opcion (1-6): ")
        
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            actualizar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            mostrar_contactos()
        elif opcion == '6':
            print("Saliendo de la agenda.")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
            
agenda()

        