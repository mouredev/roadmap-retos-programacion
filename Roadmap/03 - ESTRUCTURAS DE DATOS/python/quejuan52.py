'''EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 '''

# listas 

listasNombres = ['Juan','Carlos','Ricardo','Maria']
listasNumeros = [2,5,6,9,0]
listaMix = [2,5,'f','r']
print (listasNombres)
print (listasNumeros)
print (listaMix)
# tuplas 

tuplaFrutas = ('Manzana','Uva','Naranja','Mandarina')
tuplaNumeros = (2,4,6,8)
print(tuplaFrutas)
print(tuplaNumeros)

# set 

conjuntoPlanetas = {'marte','venus','jupiter'}
print(conjuntoPlanetas)

# diccionarios 

diccionario = {'IDE':'integrate Development Enviroment','OOP': 'Object oriented programming'}

# Operaciones de inserción, borrado, actualización y ordenación

# listas

listasNombres.append('Ricardo') # para agregar un elemento a nuestra lista 
listasNombres.insert(2,'Cesar') #agregando un elemento en una posicion indicada
listasNombres.remove('Maria')  # estoy eliminando un elemento de la lista 
listasNombres.pop()  # elimina el ultimo elemento que se agrego en la lista
listasNombres.clear() # para limpiar todos los elementos de la lista 
listasNombres.sort() # ordena la lista

# tuplas
'''las tuplas no se pueden modificar o eliminar como las listas son tipos inmutables'''

# Diccionarios

diccionario ['PK'] = 'Primary key'#estamos agragando una nueva llave a nuestro diccionario
diccionario.pop('OOP') # para eliminar un elemento de nuestro diccionario 
diccionario ['IDE'] = 'valor nuevo'# modifica el valor de la llave de nuestro diccionario 

# Set

conjuntoPlanetas.add('Tierra') # agregando un elemento a nuestro conjunto
conjuntoPlanetas.remove('Tierra') # para eliminar un elemento del diccionario 
conjuntoPlanetas.discard('jupiter') # para eliminar un elemento del diccionario 
del conjuntoPlanetas # borrado por completo 

'''DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.'''

class AgendaContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        if not telefono.isdigit() or len(telefono) > 11:
            print("Número de teléfono no válido.")
            return
        self.contactos[nombre] = telefono
        print(f"Contacto {nombre} agregado correctamente.")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"Nombre: {nombre}, Teléfono: {self.contactos[nombre]}")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def actualizar_contacto(self, nombre, telefono):
        if nombre in self.contactos:
            if not telefono.isdigit() or len(telefono) > 11:
                print("Número de teléfono no válido.")
                return
            self.contactos[nombre] = telefono
            print(f"Contacto {nombre} actualizado correctamente.")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado correctamente.")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def mostrar_contactos(self):
        print("Lista de contactos:")
        for nombre, telefono in self.contactos.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")


agenda = AgendaContactos()

while True:
    print("\nSeleccione una operación:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar contactos")
    print("6. Salir")

    opcion = input("Ingrese el número de la operación: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda.agregar_contacto(nombre, telefono)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)

    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a actualizar: ")
        telefono = input("Ingrese el nuevo número de teléfono: ")
        agenda.actualizar_contacto(nombre, telefono)

    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        agenda.eliminar_contacto(nombre)

    elif opcion == "5":
        agenda.mostrar_contactos()

    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

