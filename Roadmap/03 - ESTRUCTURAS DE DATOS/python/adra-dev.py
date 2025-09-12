"""
EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas
por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y 
ordenación.

DIFICULTAD EXTRA (opcional):
- Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, 
actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se 
quiere realizar, y a continuación los datos necesarios para llevarla 
a cabo.
- El programa no puede dejar introducir números de teléfono no 
númericos y con más de 11 dígitos. (o el número de dígitos que 
quieras)
- También se debe proponer una operación de finalización del 
programa.

by adra-dev.
"""

"""
Estructuras de Datos:
    Una estructura de datos es una forma de organizar, gestionar, y
    almacenar conjutos de datos para acceder a ellos y manipularlos
    de manera eficiente, de acuerdo con el problema que estamos 
    resolviendo. El término técnico es Tipo de Dato Abstracto (TDA),
    pues representan tipos de datos más complejos que, además de 
    almacenar valores determinados en una organización concreta de 
    los mismos, proporcionan operaciones con fines específicos.
"""

"""
Listas:
    Las listas son secuencias ordenadas de objetos o valores de 
    cualquier tipo.
"""


# Creación
lista = [] # lista vacía
lista = list() # lista vacía
lista = [1] # lista con un único elemento
lista = [3, 4] # lista con dos elementos
lista = [3, 5.6, 'coche'] # lista con tres elementos de distinto tipo
lista = list(range(5)) # lista con los valores del 0 al 4

print(lista)

# Inserción de elementos

lista[len(lista):] = [9] # Añade el elemento al final de la lista.
print(lista)

lista.append(10) # Añade el elemento al final de la lista.
print(lista)

lista.extend(range(4)) # Añade, al final de la lista, todos los elementos del iterable
print(lista)


lista.insert(2,6) # Inserta un nuevo elemento en la lista en la posición indicada por el primer argumento
print(lista)

# Actualización

lista[2] = 2 # Actualiza un valor en especifico, en base a su índice
print(lista)


lista[8:11] = [8, 9, 10, 11] # Actualiza los valores dentro de un rango de índices
print(lista)

# Ordenación

lista.sort() # modifica la lista ordenando sus elementos, si tenemos elementos de distinto tipo no comparables arroja un error
print(lista)

lista.sort(reverse=True) # ordena de manera inversa
print(lista)

# Borrado

del lista[10] # Elimina el elemente en base al indice indicado como argumento
print(lista)

lista.remove(9) # Elimina de la lista el primer (y solo el primer) elemento  con el valor indicado
print(lista)

lista.pop(8) # Elimina el elemento que ocupa la posicion indicada y devuelve su valor.
print(lista)

lista.clear() # vacia la lista, elimina todos sus elementos
print(lista)

lista = [] # vacia la lista, elimina todos sus elementos
print(lista)

del lista[:]  # vacia la lista, elimina todos sus elementos
print(lista)


"""
Pilas:
    Una estructura de tipo pila es una lista en la que los elementos
    se añaden al final y se sacan del final; es decir, extraemos 
    siempre el elemento añadido más recientemente. A este tipo de 
    estructuras támbien se les denomina stack o LIFO (Last In, First
    Out).
"""

# Este codigo simula la accion de deshacer

# inicializamos la pila
acciones = [] 

# guardamos las acciones del usuario
acciones.append("escribir: 'h'")
acciones.append("escribir: 'o'")
acciones.append("escribir: 'y'")
acciones.append("negrita: 'hoy'")

# mostramos el contenido
print(acciones)

# deshacemos el ultimo cambio y ponemos en cursiva
print("sacamos:", acciones.pop())
acciones.append("cursiva: 'hoy'")

# mostramos estado final de la pila
print(acciones)


"""
Colas:
    Una cola es una lista en la que los elementos llegan por un lado 
    y salen por otro. Támbien se les denomina FIFO (First In, First
    Out), pues el primero elemento en llegar es el primero en salir.
"""

# Este codigo simula una cola de clientes en el supermercado

from collections import deque

# Iniciamos la cola
cola = deque()

# llegan 5 clientes a la cola 
for i in range(5):
    cliente = 'cliente ' + str(i+1)
    print('Llega', cliente)
    cola.append(cliente)
    print('Cola:', cola)


# salen todos los clientes de la cola 
while len(cola) > 0:
    print('Sale', cola.popleft())
    print('Qedan:', cola)


"""
Tuplas:
    Una tupla es un tipo de dato compuesto por varios valores en un 
    orden determinado. similares a las listas, las tuplas son, en 
    cambio, <<inmutables>>. podemos accedera  sus elementos, pero no
    cambiar sus valores ni modificar el numero de elementos de la 
    misma.
"""


# Creación
tupla = () # tupla vacía
tupla = tuple() # tupla vacía
singleton = 3.1415,  # tupla con un único elemento
tupla = (3, 4) # tupla con dos elementos
tupla = (singleton, 3, 5.6, 'coche') # tupla anidada con diferentes elementos
tupla = tuple(range(5)) # tupla con los valores del 0 al 4


# Inserción de elementos

datos = ('Antonio', 'Gutiérrez', 36, '+34 555 343 232')
print(datos)


datos = ('Antonio', 'Gutiérrez', 46, '+34 555 343 232') # El valor no puede modificarse es necesario crear una nueva tupla
print(datos)

singleton += tupla # Se pueden añadir tuplas a tuplas
print(singleton)

# Borrado

del singleton


"""
Conjuntos:
    Un conjunto es unico y no puede almacenar dos elementos iguales.
    Además, los elementos no guardan orden alguno, por tanto, un 
    conjunto no es una secuencia. Esto impide indexar sus elementos o
    acceder a ellos mediante una posición. Si es posible reocrrer el 
    conjunto iterando sobre su contenido, pero no se garantiza orden 
    alguno.
"""

# Creacion
letras = set('abracadabra')
print(letras)

# Borrado 
del letras


"""
Diccionarios:
    En programación, existe una estructura de datos con varias 
    denominaciónes posibles: <<arreglo asociativo>>, <<memoria 
    asociativa>>, <<tabla hash>> o, sencillamente <<diccionario>>.
    
    Los diccionarios de Python están implementados como tablas hash
    de crecimiento dinámico y búsqueda abierta pseudoaleatoria ante
    colisiones.
"""

# Creación

precio_kilo = {} # diccionario vacío

precio_kilo = dict() # diccionario vacío

precio_kilo = {'pera': 2.34, 'tomate': 1.98, 'manzana': 2.50} # usando llaves {}

precio_kilo = dict(pera= 2.34, tomate= 1.98, manzana= 2.50) # usando llaves lla función dict()

precio_kilo = dict(zip(['pera', 'tomate', 'manzana'], [2.3, 1.98, 2.5])) # pares de tuplas

precio_kilo = dict([('pera', 2.34), ('tomate', 1.98), ('manzana', 2.50)]) # usando llaves {}

# Inserción

precio_kilo['uva'] = 3.2
print(precio_kilo)

# actualizacion


precio_kilo.update(pera= 4.20, tomate= 2.98)
print(precio_kilo)

precio_kilo['uva'] = 5.5
print(precio_kilo)

# Eliminación


precio_kilo.pop('tomate')
print(precio_kilo)

del precio_kilo['uva'] 
print(precio_kilo)

precio_kilo.clear()
print(precio_kilo)


"""
Extra
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:48:59 2024

Crea una agenda de contactos por terminal
"""
__author__ = "adra-dev"
__copyright__ = "roadmap-retps-programacion"
__credits__ = "adra-dev"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "alfaroar98@gmail.com"
__status__ = "Development"



campos = ('nombre', 'apellidos', 'email', 'telefono')

contactos = []


def input_contact():
    
    contacto = {}

    for campo in campos:
        
        if campo == 'telefono':
            valor = input(campo + ': ')
            
            if len(valor) > 0 and len(valor) < 12:
                contacto[campo] = valor
                contactos.append(contacto)
            else: return print('Numero no valido')

        valor = input(campo + ': ')
        
        if len(valor) > 0:
            contacto[campo] = valor

    contactos.append(contacto)

    return print(f"El contacto {contacto} ha sido agregado")


def delete_contact():

    nombre = input("Ingresa el nombre: ")
    telefono = input("Ingresa el telefono: ")

    for contacto in contactos:
        if nombre and telefono in contacto.values():
            index = contactos.index(contacto)
            del contactos[index]
            
        else:
            return print("Contacto no encontrado.")
    return print("Contacto eliminado: ", contacto)
    

def search_contact():

    nombre = input("Ingresa el nombre: ")
    telefono = input("Ingresa el telefono: ")

    for contacto in contactos:
        if nombre and telefono in contacto.values():
           return print(
            f"""El Contacto {nombre} con el telefono {telefono}
            si esta en la lista de contactos.""")
        else:
            return print("Contacto no encontrado.")


def update_contact():

    nombre = input("Ingresa el nombre: ")
    telefono = input("Ingresa el telefono: ")
    
    for contacto in contactos:
        if nombre and telefono in contacto.values():
                index = contactos.index(contacto)
                
                print("Introduce los valores a actualizar.")
                
                for campo in campos:
                    valor = input(campo + ': ')
        
                    if len(valor) > 0 and len(valor) <= 12:
                        contacto[campo] = valor
                
                del contactos[index]
                contactos.insert(index, contacto)

    return print(f"El contacto {nombre} ha sido Actualizado")
            


continuar = 's'

while continuar in ('s', 'S'):

    

    estados = ['Introducir', 'Eliminar', 'Buscar', 'Actualizar']

    print('Bienvenido a la agenda python, estas son tus opciones')
    print('------')

    for estado in estados:
        print(estado)
    print('------')

    estado = input('Que operacion quieres realizar?:').capitalize()
    print('------')

    if estado == 'Introducir':
        input_contact()
        print('------')

    elif estado == 'Buscar':
        search_contact()
        print('------')

    elif estado == 'Actualizar':
        update_contact()
        print('------')

    elif estado == 'Eliminar':
        delete_contact()
        print('------')

    else:
        print('Opcion no valida')
        print('------')

    continuar = input('Quieres continuar? s\n:')


for contacto in contactos:

    for k,v in contacto.items():
        print(k + ': ' +v)     
        #mostramos esto para facilitar la lectura 
        print('------')