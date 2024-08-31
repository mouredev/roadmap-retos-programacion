# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24
#import
from queue import Queue
import numpy as np
import sys
from colorama import Fore, Back



## Ejercicio
""" 
*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 """
### EJEMPLOS DE CREACIÓN DE ESTRUCTURAS DE DATOS ###
 
### LISTAS ###
# Las listas son una estructura de datos usada para guardar variables. Permiten variables de distintos tipos de datos, mutables 
# y se pueden ordenar, se pueden repetir elementos, se pueden modificar, se pueden añadir y quitar elementos. 
#Creación
lista = [1,2,3,4,5]
lista2 = ["hola", "que", "tal"]

#Insercción 
lista.append(6)
lista2.append("estas")

#Borrado
lista.remove(2)
lista2.remove("que")

#Actualización
lista[0] = 0
lista2[0] = "adios"

#Ordenación
print(lista)

#ordena de mayor a menor
lista.sort(reverse=True)
print(lista)

#Ordena  alfabeticamente
print(lista2)
lista2.sort()  
print(lista2)

### TUPLAS ###
#Las tuplas son una estructura de datos usada para guardar variables. Permiten variables de distintos tipos de datos, inmutables 
# y no se pueden ordenar, no se pueden repetir elementos, no se pueden modificar, no se pueden añadir y quitar elementos.

#Creación
tupla = (1,2,3,4,5)
tupla2 = ("hola", "que", "tal")

#Insercción
#No se puede insertar

#Borrado
#No se puede borrar

#Actualización
#No se puede actualizar

#Ordenación
#No se puede ordenar

### DICCIONARIOS ###
#Los diccionarios son una estructura de datos usada para guardar variables. Permiten variables de distintos tipos de datos, 
# mutables y se pueden ordenar, no se pueden repetir elementos, se pueden modificar, se pueden añadir y quitar elementos.

#Creación
diccionario = {
    "uno":1, 
    "dos":2, 
    "tres":3, 
    "cuatro":4, 
    "cinco":5}

diccionario2 = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "edad" : 18,
    "telefono" : 123456789
}

#Insercción
diccionario["seis"] = 6

diccionario2["direccion"] = "calle falsa 123"

#Borrado
diccionario.pop("uno")
diccionario2.pop("edad")

#Actualización
diccionario["dos"] = 22
diccionario2["nombre"] = "Pedro"

#Ordenación
#No se puede ordenar
print(diccionario)
print(diccionario2)

### SETS ###
#Los sets son una estructura de datos usada para guardar variables. Permiten variables de distintos tipos de datos, mutables 
# y se pueden ordenar, no se pueden repetir elementos, se pueden modificar, se pueden añadir y quitar elementos.
#Creación
set = {1,2,3,4,5, 2, 3, 4, 5}
print(set)

#Insercción
set.add(6)
set.add(2)
print(set)

#Borrado
set.remove(2)

#Actualización
#No se puede actualizar

#Ordenación
#No se puede ordenar

### COLAS ###
#Las colas son una estructura de datos usada para guardar variables. Permiten variables de distintos tipos de datos, mutables 
# y se pueden ordenar, no se pueden repetir elementos, se pueden modificar, se pueden añadir y quitar elementos.
#Las cosas sirven para guardar datos en orden FIFO (First In First Out), es decir, el primero que entra es el primero que sale.

#Creación
print("### COLAS ###")
cola = Queue()

#Insercción
cola.put(1)
cola.put(2)
cola.put(3)

iterator = cola.queue

for elemento in iterator:
    print(elemento)

cola.get()

for elemento in iterator:
    print(elemento)
#Borrado
cola.get()

#Actualización
#No se puede actualizar

#Ordenación
#No se puede ordenar

### PILAS ###
#Las pilas son una estructura de datos usada para guardar variables. Permiten variables de distintos tipos de datos, mutables 
# y se pueden ordenar, no se pueden repetir elementos, se pueden modificar, se pueden añadir y quitar elementos.

#Las pilas sirven para guardar datos en orden LIFO (Last In First Out), es decir, el último que entra es el primero que sale.

#Creación

pila = []

#Insercción
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

#Borrado
pila.pop()

#Visualización
print(pila)

#Actualización
pila[0] = 0

print(pila)

#Ordenación
pila.sort(reverse=True)
print(pila)

### Arreglos (mediante NumPy) ###
#Los arreglos son una estructura de datos usada para guardar variables. Permiten variables de distintos tipos de datos, mutables
# y se pueden ordenar, no se pueden repetir elementos, se pueden modificar, se pueden añadir y quitar elementos.
#Los arreglos sirven para guardar datos numéricos multidimensionales en arrays.

### Arreglo de una dimensión ###
#Creación
array_1 = np.array([1,2,5,4,3])

#Insercción
array_1 = np.append(array_1, 6)

#Borrado
array_1 = np.delete(array_1, 0)

#Actualización
array_1[0] = 0

#Ordenación
array_1.sort()

print(f"Arreglo de una dimensión: {array_1}")

### Arreglo de dos dimensiones ###
array_2 = np.array([[5,4,3,2,1], [11,7,8,9,10]])

#Insercción
array_2 = np.append(array_2, [[6,12,13,14,15]], axis=0)

#Actualización
array_2[0][0] = 0

#Ordenación
array_2.sort()

print(f"Arreglo de dos dimensiones: {array_2}")

#Borrado
array_2 = np.delete(array_2, 0, axis=0)

print(f"Arreglo de dos dimensiones: {array_2}")

### Existen arreglos de N dimensiones, por eso no los voy a representar todos ###
#Funcionan de manera similar a los anteriores

input("Pulsa enter para continuar y entrar a la agenda...")
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""


### AGENDA DE CONTACTOS ### 
### Función para colorear los prints con Colorama ###
def titulo(texto):
    print(Fore.CYAN + Back.WHITE + texto)
    print()
    
def texto(texto):
    print(Fore.WHITE + Back.BLACK + texto)
    
def error(texto):
    print(Fore.WHITE + Back.RED + texto)
    
def tabla(texto):
    print(Fore.WHITE + Back.CYAN + texto)

def validacion(texto):
    print(Fore.WHITE + Back.GREEN + texto)

def esperar(mensaje="Pulsa enter para continuar..."):
    texto(mensaje)
    input()
    


#TODO: Pasar inputs a try catch 
#TODO: Meter colores/formato a la agenda. 
class agenda:
    def __init__(self):
        self.agenda_nombres = {}
        self.agenda_telefonos = {}

    def comprobar_telefono(self, telefono):
        if(isinstance(telefono, int) and telefono>99999999 and telefono<1000000000):  #Comprueba si el telefono es un telefono entre 100000000 y 999999999
            if telefono in self.agenda_telefonos: 
                return False
            else:
                return True
        else:
            return None
    
    def comprobar_nombre(self, nombre):
        if(isinstance(nombre, str) and len(nombre)>1): #Comprueba si el nombre es un string y el tamaño es mayor a 1. 
            if nombre in self.agenda_nombres:
                return False
            else:
                return True
        else:
            return None
    
    def insertar_contacto(self, nombre, telefono):
        if self.comprobar_telefono(telefono) and self.comprobar_nombre(nombre):
            self.agenda_nombres[nombre] = telefono
            self.agenda_telefonos[telefono] = nombre
            return True 
        else:
            return False
              
    def buscar_contacto_nombre(self,nombre):
        if nombre in self.agenda_nombres:
            return self.agenda_nombres[nombre]
        else:
            return None
        
    def buscar_contacto_telefono(self,telefono):
        if telefono in self.agenda_telefonos:
            return self.agenda_telefonos[telefono]
        else:
            return None
        
    def actualizar_contacto_nuevo_telefono(self, nombre, nuevo_telefono):
        if nombre in self.agenda_nombres:
            #La comprobación ahora es negada, porque ya existen en la agenda por tanto, si devuelve false,
            #es que no existen en la agenda y además tienen el formato valido sino devolveria None
            if not self.comprobar_nombre(nombre) and (isinstance(nuevo_telefono, int) and nuevo_telefono>99999999 and nuevo_telefono<1000000000):
                self.eliminar_contacto_nombre(nombre)
                self.agenda_nombres[nombre] = nuevo_telefono
                self.agenda_telefonos[nuevo_telefono] = nombre
            else:
                return "El contacto no se ha podido actualizar"
        else:
            return None
        
    def actualizar_contacto_nuevo_nombre(self,nuevo_nombre, telefono):
        if telefono in self.agenda_telefonos:
            #La comprobación ahora es negada, porque ya existen en la agenda por tanto, si devuelve false,
            #es que no existen en la agenda y además tienen el formato valido sino devolveria None
            if not self.comprobar_telefono(telefono) and (isinstance(nuevo_nombre, str) and len(nuevo_nombre)>1):
                self.eliminar_contacto_telefono(telefono)
                self.agenda_nombres[nuevo_nombre] = telefono
                self.agenda_telefonos[telefono] = nuevo_nombre
            else:
                return "El contacto no se ha podido actualizar"
        else:
            return None
        
    def eliminar_contacto_nombre(self,nombre):
        if nombre in self.agenda_nombres:    
            telefono = self.agenda_nombres[nombre]
            del self.agenda_telefonos[telefono]
            del self.agenda_nombres[nombre]
        else:
            return None
        
    def eliminar_contacto_telefono(self,telefono):
        if telefono in self.agenda_telefonos:
            nombre = self.agenda_telefonos[telefono]
            del self.agenda_telefonos[telefono]
            del self.agenda_nombres[nombre]
        else:
            return None

    def clear_screen(self):
        sys.stdout.write("\033[2J\033[1;1H") #Limpia la pantalla

    def print_menu(self):
        self.clear_screen()
        titulo("** Agenda de contactos **")
        texto("0. (M)ostrar agenda")
        texto("1. (I)nsertar contacto")
        texto("2. (B)uscar contacto")
        texto("3. (A)ctualizar contacto")
        texto("4. (E)liminar contacto")
        texto("5. (S)alir")

    def get_option(self):
        while True:
            option = input("Introduce la opción que deseas: ")
            option = option.strip()
            if option in ["0", "1", "2", "3", "4", "5", "M", "m", "I", "i", "B", "b", "A", "a", "E", "e", "S", "s"]:
                return option
            else:
                error("Opción no válida.")
                esperar()
                break
                
    def add_contact(self):
        self.clear_screen()
        titulo("1. (I)nsertar contacto")
        nombre = input("Introduce el nombre del contacto: ")
        while True:
            telefono = input("Introduce el número de teléfono del contacto: ")
            if telefono.isdigit():
                telefono = int(telefono)
                break
            else:
                error("El número de teléfono no es válido.")
        if (self.insertar_contacto(nombre, telefono)):
            mensaje = "El contacto con el nombre " + nombre + " y teléfono " + str(telefono) + " ha sido insertado correctamente."
            validacion(mensaje)
        else:
            error("El contacto no se ha podido insertar.")
        
        esperar()

    def search_contact(self):
        self.clear_screen()
        titulo("2. (B)uscar contacto")
        try:
            contacto_a_buscar = input("Introduce el nombre o el teléfono del contacto que deseas buscar: ")
            if contacto_a_buscar.isdigit():
                contacto_a_buscar = int(contacto_a_buscar)
            else: 
                contacto_a_buscar = str(contacto_a_buscar)
        except ValueError:    
            error("El contacto introducido no es un número.")
            
        if(isinstance(contacto_a_buscar, int)):
            resultado = self.buscar_contacto_telefono(contacto_a_buscar)
            if resultado is None: 
                error("No se ha encontrado el contacto")
            else:
                validacion("El contacto con el teléfono " + str(contacto_a_buscar) + " es " + resultado)
        elif(isinstance(contacto_a_buscar, str)):
            resultado = self.buscar_contacto_nombre(contacto_a_buscar)
            if resultado is None: 
                error("No se ha encontrado el contacto")
            else:
                validacion("El contacto con el nombre " + contacto_a_buscar + " es " + str(resultado))
        esperar()
        
    def update_contact(self):
        self.clear_screen()
        titulo("3. (A)ctualizar contacto")
        texto("Para actualizar un contacto, puedes:")
        texto("1. Introducir un nombre existente y un número de teléfono nuevo.")
        texto("2. Introducir un número de teléfono existente y un nombre nuevo.")
        texto("El programa se encargará de actualizar el contacto automáticamente.")
        while True: 
            try:
                nombre = input("Introduce el nombre del contacto: ")
                break
            except ValueError:
                error("El nombre introducido no es válido.")
            
        while True:
            try:
                telefono = int(input("Introduce el número de teléfono del contacto: "))
                break
            except ValueError:
                error("El número de teléfono introducido no es válido.")
                  
        if nombre in self.agenda_nombres:
            self.actualizar_contacto_nuevo_telefono(nombre, telefono)
            validacion("El contacto con el nombre " + nombre + " ha sido actualizado correctamente.")
        elif telefono in self.agenda_telefonos:
            self.actualizar_contacto_nuevo_nombre(nombre, telefono)
            validacion("El contacto con el teléfono " + str(telefono) + " ha sido actualizado correctamente.")
        else:
            error("El contacto con el nombre " + nombre + " y telefono " + str(telefono) + "no se encuentra en la agenda.")
        esperar()

    def delete_contact(self):
        self.clear_screen()
        titulo("4. (E)liminar contacto")
        contacto_a_eliminar = input("Introduce el nombre o el número del contacto que deseas eliminar: ")
        if contacto_a_eliminar.isdigit():
            contacto_a_eliminar = int(contacto_a_eliminar)
        else: 
            contacto_a_eliminar = str(contacto_a_eliminar)
            
        if contacto_a_eliminar in self.agenda_nombres: 
            self.eliminar_contacto_nombre(contacto_a_eliminar)
        elif contacto_a_eliminar in self.agenda_telefonos: 
            self.eliminar_contacto_telefono(contacto_a_eliminar)
        else:
            error("No se ha encontrado el contacto")
        esperar()
        
    def mostrar_agenda(self):
        self.clear_screen()
        titulo("0. (M)ostrar agenda")
        texto("Nombre\t\tTeléfono")
        for nombre, telefono in self.agenda_nombres.items():
            tabla(nombre + "\t\t" + str(telefono))
        esperar()
        
    def ejecutor(self):

        while True:
            self.print_menu()
            option = self.get_option()
            if option == "0" or option == "M" or option == "m":               #0. (M)ostrar agenda
                self.mostrar_agenda()
            if option == "1" or option == "I" or option == "i":               #1. (I)nsertar contacto
                self.add_contact()
            elif option == "2" or option == "B" or option == "b":             #2. (B)uscar contacto
                self.search_contact()
            elif option == "3" or option == "A" or option == "a":             #3. (A)ctualizar contacto
                self.update_contact()
            elif option == "4" or option == "E" or option == "e":             #4. (E)liminar contacto
                self.delete_contact()
            elif option == "5" or option == "S" or option == "s":             #5. (S)alir
                break

if __name__ == "__main__":
    agenda = agenda()
    agenda.insertar_contacto("Uno", 611111111)
    agenda.insertar_contacto("Dos", 611111112)
    agenda.insertar_contacto("Tres", 611111113)
    agenda.insertar_contacto("Cuatro", 611111114)
    agenda.insertar_contacto("Cinco", 611111115)
    agenda.insertar_contacto("Seis", 611111116)
    agenda.insertar_contacto("Siete", 611111117)

    agenda.ejecutor()
    

