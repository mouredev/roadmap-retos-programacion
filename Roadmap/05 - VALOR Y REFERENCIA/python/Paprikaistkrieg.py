# Valor y Referencia

"""
En Python, los tipos de datos se dividen en dos categorías principales: tipos mutables e inmutables.

Los tipos mutables son aquellos que pueden ser modificados después de su creación. Ejemplos de tipos mutables en Python son las listas y los diccionarios.

Por otro lado, los tipos inmutables son aquellos que no pueden ser modificados una vez que han sido creados. Ejemplos de tipos inmutables en Python son las tuplas y las cadenas de texto.


Es importante entender la diferencia entre estos dos tipos de datos, ya que afecta cómo se manejan en la memoria y cómo se comportan en diferentes situaciones.

Cuando se asigna un valor a una variable, Python maneja la asignación de diferentes maneras dependiendo de si el valor es mutable o inmutable.

# Para los tipos inmutables, como las tuplas y las cadenas de texto, cuando se asigna un valor a una variable, Python crea una nueva copia del valor en la memoria. Esto significa que si se modifica la variable original, la copia no se verá afectada.
#Por ejemplo:
#Asignación de una cadena de texto (tipo inmutable)
"""
original_string = "Hola" # String es inmutable
copied_string = original_string #Asignación por valor (se crea una copia)

#ejemplos de inmutable o paso por valor


my_int_a = 10
my_int_b = my_int_a  # Asignación por valor (se crea una copia)
my_int_a = 30  # Modificación de my_int_a
print(my_int_a)  # Imprime 30 (valor modificado)
print(my_int_b)  # Imprime 10 (valor original)

my_int_a = 10
my_int_b = my_int_a
print(id(my_int_a))  # ID de 10
print(id(my_int_b))  # Mismo ID ➜ misma referencia al valor 10

my_int_a = 30
print(id(my_int_a))  # Nuevo ID ➜ nueva referencia al valor 30
print(id(my_int_b))  # ID de 10 (sin cambios)




#ejemplo de mutable o paso por referencia

"""
En Python, los tipos mutables como list, dict, set y objetos personalizados se pasan por referencia. Esto significa que cuando los usas como argumentos en una función, 
no se copia el valor, sino que se pasa una referencia al mismo objeto en memoria. 
Por lo tanto, si lo modificas dentro de la función, también se modifica fuera
"""

my_list_a = [1, 2, 3]
my_list_b = my_list_a  # Asignación por referencia (misma lista en memoria)
my_list_b.append(4)  # Modificación de my_list_b
print(my_list_a)  # Imprime [1, 2, 3, 4] (lista modificada)
print(my_list_b)  # Imprime [1, 2, 3, 4] (lista también modificada)


# funciones de datos inmutables o paso por valor


def modificar_texto(texto): #aqui definimos la funcion, texto es un parametro, modificar_texto es el nombre de la funcion
    texto = texto.upper()  # Convierte a mayúsculas (solo dentro de la función, no afecta la variable original)
    print("Dentro de la función:", texto)  #imprime el texto modificado dentro de la funcion

mensaje = "hola mundo" # Variable original
modificar_texto(mensaje) # Llamada a la función con la variable original
print("Fuera de la función:", mensaje) #imprime la variable original fuera de la funcion 


mensaje = "hola mundo" # Variable original (aqui es donde se asigna el valor a la variable y este es inmutable)
print("ID fuera:", id(mensaje)) #imprime el id de la variable original
modificar_texto(mensaje) # Llamada a la función con la variable original

def modificar_texto(texto): #aqui definimos la funcion, texto es un parametro, modificar_texto es el nombre de la funcion
    print("ID dentro:", id(texto)) #imprime el id del parametro texto (aqui se puede ver que es igual al id de la variable original, ya que se pasa por valor)
    texto = texto.upper() # Convierte a mayúsculas (solo dentro de la función, no afecta la variable original)
    print("ID modificado:", id(texto)) #imprime el id del texto modificado (aqui se puede ver que es diferente al id del parametro texto, ya que se creo una nueva copia en memoria debido al cambio en el valor)

print(modificar_texto(mensaje)) # Llamada a la función con la variable original

#funciones de datos mutables o paso por referencia

def modificar_lista(lista): #aqui definimos la funcion, lista es un parametro, modificar_lista es el nombre de la funcion
    lista.append(4)  # Agrega un elemento a la lista (esto afecta la variable original)
    print("Dentro de la función:", lista) #imprime la lista modificada dentro de la funcion
mi_lista = [1, 2, 3] # Variable original
modificar_lista(mi_lista) # Llamada a la función con la variable original
print("Fuera de la función:", mi_lista) #imprime la variable original fuera de la funcion (aqui se puede ver que si se modifico la variable original, ya que es mutable)
print("ID fuera:", id(mi_lista)) #imprime el id de la variable original
modificar_lista(mi_lista) # Llamada a la función con la variable original
def modificar_lista(lista): #aqui definimos la funcion, lista es un parametro, modificar_lista es el nombre de la funcion
    print("ID dentro:", id(lista)) #imprime el id del parametro lista (aqui se puede ver que es igual al id de la variable original, ya que se pasa por referencia)
    lista.append(4)  # Agrega un elemento a la lista (esto afecta la variable original)
    print("ID modificado:", id(lista)) #imprime el id de la lista modificada (aqui se puede ver que es igual al id del parametro lista, ya que no se creo una nueva copia en memoria debido a que no hubo un cambio en el valor)
#Asignación de una lista (tipo mutable)
original_list = [1, 2, 3] # List es mutable
copied_list = original_list #Asignación por referencia (se crea una referencia al mismo objeto
# en memoria, no una copia).

#mecanismos de copia
#Para crear una copia de un objeto mutable en lugar de una referencia, puedes usar los siguientes métodos:
import copy
# Usando el método copy() de la lista
copied_list_1 = original_list.copy()
# Usando el módulo copy para una copia superficial
copied_list_2 = copy.copy(original_list)
# Usando el módulo copy para una copia profunda (útil para listas anidadas)
copied_list_3 = copy.deepcopy(original_list)
# Usando la función list() para crear una nueva lista
copied_list_4 = list(original_list)
# Usando slicing para crear una nueva lista
copied_list_5 = original_list[:]
# Usando la función list() para crear una nueva lista
copied_list_6 = list(original_list)
print("Original List ID:", id(original_list))# Todos los IDs de las copias serán diferentes al ID de la lista original
print("Copied List 1 ID:", id(copied_list_1))
print("Copied List 2 ID:", id(copied_list_2))
print("Copied List 3 ID:", id(copied_list_3))# Todos los IDs de las copias serán diferentes al ID de la lista original
print("Copied List 4 ID:", id(copied_list_4))
print("Copied List 5 ID:", id(copied_list_5))
print("Copied List 6 ID:", id(copied_list_6))# Todos los IDs de las copias serán diferentes al ID de la lista original

print("Original List:", original_list) #imprime la lista original
print("Copied List 1:", copied_list_1) #imprime la copia de la lista
print("Copied List 2:", copied_list_2) #imprime la copia de la lista
print("Copied List 3:", copied_list_3) #imprime la copia de la lista
print("Copied List 4:", copied_list_4) #imprime la copia de la lista            
print("Copied List 5:", copied_list_5) #imprime la copia de la lista
print("Copied List 6:", copied_list_6) #imprime la copia de la lista
# Todos los valores de las copias serán iguales al valor de la lista original

#como romper la referencia en una variable mutable
#Para romper la referencia en una variable mutable y crear una nueva copia, puedes reasignar la variable a una nueva instancia del objeto mutable.
# Por ejemplo, si tienes una lista y quieres romper la referencia, puedes hacer lo siguiente:
mi_lista = [1, 2, 3]
nueva_lista = mi_lista[:]  # Crea una nueva lista usando slicing
nueva_lista.append(4)
print("Lista original:", mi_lista)
print("Nueva lista:", nueva_lista)
#Salida:
#Lista original: [1, 2, 3]
#Nueva lista: [1, 2, 3, 4]
#En este ejemplo, al usar slicing (mi_lista[:]), se crea una nueva lista que es una copia de mi_lista.
# Luego, al modificar nueva_lista, la lista original mi_lista no se ve afectada.
#Otra forma de romper la referencia es usando el método copy() o el módulo copy como se mostró anteriormente.
# Usando el método copy()
mi_lista = [1, 2, 3]
nueva_lista = mi_lista.copy()  # Crea una nueva lista usando el método copy()
nueva_lista.append(4)
print("Lista original:", mi_lista)
print("Nueva lista:", nueva_lista)

# Usando el módulo copy para una copia superficial
import copy
mi_lista = [1, 2, 3]
nueva_lista = copy.copy(mi_lista)  # Crea una nueva lista usando copy.copy
nueva_lista.append(4)
print("Lista original:", mi_lista)
print("Nueva lista:", nueva_lista)
# Usando el módulo copy para una copia profunda (útil para listas anidadas)

#Xtra: 

xtra1 = "hola"
xtra2 = "mundo"
xtra3 =  [1, 2, 3]
xtra4 = [4, 5, 6]

def xtra_funcion(xtra, xtra_):
    return xtra_, xtra
nuevo1, nuevo2 = xtra_funcion(xtra1, xtra2)
print("Variables originales:", xtra1, xtra2)
print("Nuevas variables:", nuevo1, nuevo2)
print(id(xtra1), id(nuevo2)) #mismo id
print(id(xtra2), id(nuevo1)) #mismo id

def xtra_funcion2(xtra5, xtra6):
    return xtra6.copy(), xtra5.copy()
nuevo3, nuevo4 = xtra_funcion2(xtra3, xtra4)
print("Variables originales:", xtra3, xtra4)
print("Nuevas variables:", nuevo3, nuevo4)
print(id(xtra3), id(nuevo3)) #diferente id
print(id(xtra4), id(nuevo4)) #diferente id