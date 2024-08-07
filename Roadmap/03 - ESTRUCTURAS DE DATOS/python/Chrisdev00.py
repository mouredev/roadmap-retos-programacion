"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
"""


#  ------------------------------------- Estructuras de datos------------------------------------------------

"""
                             ########## Listas ##########

Almacenan una colección ordenada y mutable de elementos.
"""

lst = list()
lista = [1, 2, 3, 4, 5]
print(lista)

# Inserción
lista.append(6)
print(lista)

# Borrado
lista.remove(3)
print(lista)

# Actualización
lista[1] = 10
print(lista)

# Ordenación
lista.sort()
print(lista)


"""
                              ######### Tuplas ##########

Similar a las listas, pero inmutable.
Las tuplas son inmutables, por lo que no admiten inserción, borrado ni actualización. 
Pero Puedes ordenar una tupla convirtiéndola a lista primero.
"""

empty_tuple = tuple()
tupla = (1, 2, 3, 4, 5)
print(tupla)

tupla = (1, 2, 5, 4, 3)

# Conversión a lista y ordenación
lista_tupla = list(tupla)
lista_tupla.sort()
tupla_ordenada = tuple(lista_tupla)
print(tupla_ordenada)

"""
                            ######## Diccionarios #########

Almacenan pares clave-valor. Los diccionarios no tienen un orden específico.
"""

empty_dict = dict()
diccionario = {'a': 1, 'b': 2, 'c': 3}
print(diccionario['a'])

# Inserción
diccionario['d'] = 4
print(diccionario)

# Borrado
del diccionario['b']
print(diccionario)

# Actualización
diccionario['a'] = 10
print(diccionario)

"""
                           ###### Conjuntos #######

Almacenan elementos únicos sin un orden específico. Los conjuntos no tienen un orden específico.
"""

st = set()
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
print(conjunto)

conjunto = {1, 2, 3, 4, 5}

# Inserción
conjunto.add(6)
print(conjunto)

# Borrado
conjunto.remove(3)
print(conjunto)

"""
                        #### Cadenas de Texto ####

Almacenan texto. Las cadenas de texto son inmutables, por lo que no admiten inserción, 
borrado ni actualización. Puedes ordenar una cadena convirtiéndola a lista primero.
"""

cadena = "Hola, mundo!"
print(cadena)

# Conversión a lista y ordenación
lista_cadena = list(cadena)
lista_cadena.sort()
cadena_ordenada = ''.join(lista_cadena)
print(cadena_ordenada)


"""
                ###### Estructuras de control - if-else: #######

Permite tomar decisiones basadas en condiciones.
"""

x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")



"""
                         ####### Bucles-for: #######
    
Itera sobre una secuencia (por ejemplo, una lista o tupla).
"""

for i in range(5):
    print(i)


"""
                      ######## Bucles - while: ########
    
Ejecuta un bloque de código mientras una condición sea verdadera.
"""

contador = 0
while contador < 5:
    print(contador)
    contador += 1

"""
                        ####### Funciones ########
    
Bloques de código reutilizables.
"""
    
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)

"""
                              ####### Clases y Objetos #######

Permiten la programación orientada a objetos.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Alice", 25)
print(persona1.nombre)


class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Alice', 'Jhons', 28, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)




"""
                     -------------Dificultad Extra-------------
"""

# Funcion para añadir

def insertar (diccionario):

    name = input("Ingrese su nombre: ")
    phoneNumber = input("Ingrese su numero de telefono: ")
    
    if phoneNumber.isdigit() and len(phoneNumber) > 0 and len(phoneNumber) <= 8:

        diccionario[name] = phoneNumber
        print(f"Se ha insertado correctamente sus datos: {name}: {phoneNumber}")
        print(f"Agenda actualizada: {diccionario}")
    else:
        print("!Error debes introducir un numero de telefono un maximo de 8 digitos")



# Funcion para buscar 
        
def busqueda (diccionario):

    while True:
        option = input("¿Desea hacer una busqueda por nombre (n) o por numero de telefono (t)? ").lower()

        if option == "n":

            clave_nombre = input("Ingrese el nombre a buscar: ")
            if clave_nombre in diccionario:
                nombre_encontrado = diccionario[clave_nombre]
                print(f"El nombre fue encontrado: '{clave_nombre}': {nombre_encontrado} ")
                break
            else:
                print(f"No se encontro el nombre '{clave_nombre}' en la agenda")
                break

        elif option == "t":

            clave_telefono = input("Ingrese el numero de telefono: ")
            claves_encontradas = [clave for clave, valor in diccionario.items() if valor == clave_telefono]
            if claves_encontradas:
                print(f"Numero de telefono encontrado: '{clave_telefono}': {claves_encontradas}")
                break
            else:
                print(f"No se encontro el numero de telefono '{clave_telefono}'.")
                break
        else:
            print("Opcion no valida. Por favor, seleccione 'N' o 'T'.")


# Funcion actualizar
            
def upgrade (diccionario):

    while True:
        option = input("Desea actualizar el nombre (N) o numero de telefono (T): ").lower()

        if option == "n":
            nombre_actualizar = input("Ingrese el nombre a actualizar: ")
            
            if nombre_actualizar in diccionario:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                diccionario[nuevo_nombre] = diccionario.pop(nombre_actualizar)
                print(f"Agenda actualizada: {diccionario}")
                break
            else:
                print(f"No se encontro el nombre '{nombre_actualizar}'. No se puede actualizar")

        elif option == "t":
            telf_actualizar = input("Ingrese el numero a actualizar: ")
            claves_encontradas = [clave for clave, valor in diccionario.items() if valor == telf_actualizar]

            if claves_encontradas:
                clave_encon = claves_encontradas[0]
                nuevo_num = input(f"Ingrese el nuevo numero de telefono para {clave_encon}: ")
                diccionario[clave_encon] = nuevo_num

                print(f"Agenda actualizada: {diccionario}")
                break
            else:
                print(f"No se encontro el numero '{telf_actualizar}' en el diccionario no se puede actualizar.")
                break
        else:
            print("Opcion no valida seleccione 'N' o 'T'.")      



# Funcion borrar
            
def delete (diccionario):

    elimi_nombre = input("Ingrese el contacto que desea eliminar: ")
    if elimi_nombre in diccionario:
        del diccionario[elimi_nombre]
    print(f"Agenda actualizada: {diccionario}")




# Funcion principal de la agenda telefonica
    
def agenda_tel():

    agenda = {}
    
    while True:

        print("")
        print("1. Insertar Contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opcion: ")

        match option:
            case "1":
                insertar(agenda)
            case "2":
                busqueda(agenda)
            case "3":
                upgrade(agenda)
            case "4":
                delete(agenda)
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5.")

agenda_tel()    
