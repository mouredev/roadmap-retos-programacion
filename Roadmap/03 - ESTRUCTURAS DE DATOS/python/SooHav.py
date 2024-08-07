#03 ESTRUCTURAS DE DATOS

#Estructuras nativas soportadas por Python
#Operaciones: inserción, borrado, actualización y ordenación.

"""
Listas en Python 
Propiedades: mutables, dinámicas, ordenadas, indexadas, 
pueden ser anidadas y contener varios tipos de datos
"""
lista = list()
lista = ["Sofi", 2024, "SooHav", "Python"]

print(lista[2]) #SooHav
print(lista[-1]) #Python

#Inserción
lista.append(1)
print(lista) #["Sofi", 2024, "SooHav", "Python", 1]

lista.extend([6.5, 7])
print(lista) #["Sofi", 2024, "SooHav", "Python", 1, 6.5, 7]

lista.insert(4, "Junior")
print(lista) # ["Sofi", 2024, "SooHav", "Python", "Junior", 1, 6.5, 7]

#Borrado
del lista[6] 
print(lista)# 6.5

lista.remove(7)
print(lista) # 7

lista.pop()
print(lista) # 1

#Actualización
lista[0] = "Sofia"
print(lista)

lista_num =[1, 10, 20, 4, 8, 2]
lista_num[1:3] = [9, 3]
print(lista_num)

#Ordenación
lista.reverse()
print(lista) # ['Junior', 'Python', 'SooHav', 2024, 'Sofia']

lista_num =[1, 9, 3, 4, 8, 2]
lista_num.sort()
print(lista_num) #[1, 2, 3, 4, 8, 9]

lista_num.sort(reverse=True)
print(lista_num) #[9, 8, 4, 3, 2, 1

print(lista.index("Python")) # 1

"""
Set en Python 
Propiedades: inmutables, desordenadas,no admite 
duplicados y puede contener varios tipos de datos
"""
mi_set = set()
mi_set = {"Sofi", 2024, "SooHav", "Python"}

#Inserción
mi_set.add(1)
print(mi_set) #{1, 2024, 'Python', 'SooHav', 'Sofi'}

#Borrado
mi_set.remove(1)
print(mi_set) #{"Sofi", 2024, "SooHav", "Python"}

mi_set.discard(2024)
print(mi_set) #{"Sofi", "SooHav", "Python"}

mi_set.pop()
print(mi_set) #{"Sofi", "Python"} elimina elemento aleatorio

mi_set.clear()
print(mi_set) #set()

#Actualización
mi_set2 = {"Sofi", 2024, "SooHav", "Python"}
mi_set.update(mi_set2) #unión con otro conjunto
print(mi_set)

"""
Tuplas en Python 
Propiedades: inmutables, rapidas, ordenadas, indexadas, 
pueden ser anidadas y pueden contener varios tipos de datos
"""
mi_tupla = tuple()
mi_tupla = ("Sofi", 2024, "SooHav", "Python")

#Metodos varios, ya que al ser inmutables no se pueden aplicar 
#metodos de inserción, borrado o actualización 

mi_tupla = ("Sofi", 2024, "SooHav", "Python")
print(mi_tupla.count("Sofi")) #1
print(mi_tupla.index("Sofi")) #0

mi_tupla2 = (1, 2, 5, 0)
print(sorted(mi_tupla2)) #sorted no soporta tipos mixtos de datos

"""
Dicconarios en Python 
Colección de elementos, donde cada uno tiene una llave "key" y un valor "value".
Propiedades: dinámicos, indexados, anidados 
"""

mi_diccionario = dict()
mi_diccionario  = {"nombre":"Sofia", "año": 2024, "alias": "SooHav", "lenguaje": "Python"}

for key in mi_diccionario:
    print(key)

for key, item in mi_diccionario.items():
    print(key, item)

it = mi_diccionario.items()
print(it)

k = mi_diccionario.keys()
print(k)

print(list(mi_diccionario.values()))

#Inserción y actualización
mi_diccionario.update({'año': 2023, 'nombre': "Soo"}) #{'nombre': 'Soo', 'año': 2023, 'alias': 'SooHav', 'lenguaje': 'Python'}
print (mi_diccionario)

mi_diccionario['nombre'] = "Sofi" 
print (mi_diccionario)

#Borrado
valor_eliminado= mi_diccionario.pop('nombre')
print(valor_eliminado)

par_eliminado = mi_diccionario.popitem() #el último item
print(par_eliminado)

del mi_diccionario['alias']
print (mi_diccionario)

mi_diccionario.clear() #borra todos los items
print (mi_diccionario)

#Ordenación
#las claves se mantienen en el orden en que fueron insertadas pero se pueden
#usar funciones de orden y devuelve una lista
mi_diccionario = {'nombre': 'Soo', 'año': 2023, 'alias': 'SooHav', 'lenguaje': 'Python'}

claves_ordenadas = sorted(mi_diccionario.keys()) #como lista
print (claves_ordenadas)

items_ordenados = sorted(mi_diccionario.items()) #como lista
print (items_ordenados)

#DIFICULTAD EXTRA: Crea una agenda de contactos por terminal

""" 
- Debes implementar funcionalidades de búsqueda, inserción, actualización 
y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar, 
 y a continuación los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más
 de 11 dígitos (o el número de dígitos que quieras).
 - También se debe proponer una operación de finalización del programa.
 """

class Contacto:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
  
    def mostrar_contactos(self):
        print(f"Datos de {self.nombre} {self.apellido}: {self.telefono}")

    def buscar_contacto(self,contactos):
      if (self.nombre, self.apellido) in contactos:
          contacto = contactos[self.nombre, self.apellido]
          print(f"Datos de {contacto.nombre} {contacto.apellido}: {contacto.telefono}")
      else:
          print(f"{self.nombre} {self.apellido} no se encuentra en la agenda.")

    def agregar_a_agenda(self, contactos):
        if len(self.telefono) <= 12:
            contactos[(self.nombre, self.apellido)] = self
            print(f"{self.nombre} {self.apellido} fue agregado a la agenda.")
        else:
            print("Error: El número de teléfono debe tener hasta 12 caracteres.")

    def actualizar_en_agenda(self, contactos, nuevo_telefono):
        if (self.nombre, self.apellido) in contactos:
            if len(nuevo_telefono) <= 12:
                contactos[(self.nombre, self.apellido)].telefono = nuevo_telefono
                print(f"Teléfono de {self.nombre} {self.apellido} actualizado.")
            else:
                print("Error: El número de teléfono debe tener hasta 12 caracteres.")
        else:
            print(f"{self.nombre} {self.apellido} no se encuentra en la agenda. No se puede actualizar.")

    def eliminar_de_agenda(self, contactos):
        if (self.nombre, self.apellido) in contactos:
            del contactos[(self.nombre, self.apellido)]
            print(f"{self.nombre} {self.apellido} se eliminó de la agenda.")
        else:
            print(f"{self.nombre} {self.apellido} no se encuentra en la agenda. No se puede eliminar.")

#diccionario vacio para agenda de contactos
contactos = dict() 

#Bucle para trabajar por consola
while True:
    opcion = input(
        "Seleccione una opción numérica:\n"
        "1. Agenda completa\n"
        "2. Buscar un contacto\n"
        "3. Agregar un contacto\n"
        "4. Actualizar un contacto\n"
        "5. Eliminar contacto\n"
        "6. Salir: "
    )

    if opcion == "1":
        for contacto_clave, contacto_valor in contactos.items():
            contacto_valor.mostrar_contactos()
    elif opcion == "2":
        nombre, apellido = input("Ingrese el nombre y apellido a buscar: ").split() #divide el string en nombre y apellido 
        contacto = Contacto(nombre, apellido, "")  # teléfono vacío para buscar contacto
        contacto.buscar_contacto(contactos)
    elif opcion == "3":
        nombre, apellido, telefono = input("Ingrese el nombre, apellido, y teléfono a agendar (separados por espacio): ").split()
        nuevo_contacto = Contacto(nombre, apellido, telefono)
        nuevo_contacto.agregar_a_agenda(contactos)
    elif opcion == "4":
        nombre, apellido, telefono = input("Ingrese el nombre, apellido, y nuevo teléfono a actualizar (separados por espacio): ").split()
        contacto_actualizar = Contacto(nombre, apellido, telefono)
        contacto_actualizar.actualizar_en_agenda(contactos, telefono)
    elif opcion == "5":
        nombre, apellido = input("Ingrese el nombre y apellido a eliminar: ").split()
        contacto_eliminar = Contacto(nombre, apellido, "")  
        contacto_eliminar.eliminar_de_agenda(contactos)
    elif opcion == "6":
        print("Saliendo del programa. ¡Vuelve pronto!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
